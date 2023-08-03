from django.db import models
from tinymce.models import HTMLField
import datetime
import app.mailer


class DonorInformation(models.Model):
    class CommunicationModeEnum(models.TextChoices):
        EMAIL = ('EMAIL', 'Email address')
        PHONE = ('PHONE', 'Phone')
        MAIL = ('MAIL', 'Mail')

    full_name = models.CharField(max_length=50)
    is_individual = models.BooleanField(default=True)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    nationality = models.CharField(max_length=50, )
    preferred_communication_mode = models.CharField(
        choices=CommunicationModeEnum.choices, max_length=10)

    id_document_1_picture = models.ImageField(upload_to='images/donorID/')
    id_document_1_number = models.CharField(max_length=50)
    id_document_1_expiry_date = models.DateField()

    id_document_2_picture = models.ImageField(
        upload_to='images/donorID/', blank=True)
    id_document_2_number = models.CharField(max_length=50, blank=True)
    id_document_2_expiry_date = models.DateField(null=True, blank=True)

    id_document_3_picture = models.ImageField(
        upload_to='images/donorID/', blank=True)
    id_document_3_number = models.CharField(max_length=50, blank=True)
    id_document_3_expiry_date = models.DateField(null=True, blank=True)

    organisation_name = models.CharField(max_length=50)
    hq_address = models.CharField(max_length=100)
    principal_contact_name = models.CharField(max_length=50)

    ABN = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return self.full_name


class RecipientInformation(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    previous_address = models.CharField(max_length=100)
    # familymembers = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    nationality = models.CharField(max_length=50, )

    id_document_1_picture = models.ImageField(upload_to='images/recipientID/')
    id_document_1_number = models.CharField(max_length=50)
    id_document_1_expiry_date = models.DateField()

    id_document_2_picture = models.ImageField(
        upload_to='images/recipientID/', blank=True)
    id_document_2_number = models.CharField(max_length=50, blank=True)
    id_document_2_expiry_date = models.DateField(null=True, blank=True)

    id_document_3_picture = models.ImageField(
        upload_to='images/recipientID/', blank=True)
    id_document_3_number = models.CharField(max_length=50, blank=True)
    id_document_3_expiry_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name


class RecipientFamilyMember(models.Model):
    full_name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    age = models.IntegerField()
    recipient = models.ForeignKey(
        RecipientInformation, on_delete=models.CASCADE)

    id_document_1_picture = models.ImageField(upload_to='images/recipientID/')
    id_document_1_number = models.CharField(max_length=50)
    id_document_1_expiry_date = models.DateField()

    id_document_2_picture = models.ImageField(
        upload_to='images/recipientID/', blank=True)
    id_document_2_number = models.CharField(max_length=50, blank=True)
    id_document_2_expiry_date = models.DateField(null=True, blank=True)

    id_document_3_picture = models.ImageField(
        upload_to='images/recipientID/', blank=True)
    id_document_3_number = models.CharField(max_length=50, blank=True)
    id_document_3_expiry_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    baseline_quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    @property
    def stock_remaining_qty(self):
        items = AidItem.objects.filter(item_category=self)
        stock_remaining = 0
        for item in items:
            stock_remaining += item.stock_remaining_qty
        return stock_remaining
    
    @property
    def stock_remaining(self):
        qty = self.stock_remaining_qty
        label = get_inventory_label(qty, self.baseline_quantity)
        return f"{qty} ({label})"


class AidItem(models.Model):
    item_name = models.CharField(max_length=50)
    item_quantity = models.IntegerField()
    item_unit = models.CharField(max_length=10)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_baseline_quantity = models.IntegerField()

    food_brand_name = models.CharField(max_length=50, blank=True, null=True)
    food_expiry_date = models.DateField(blank=True, null=True)
    main_ingredients = models.TextField(blank=True, null=True)
    allergen_information = models.TextField(blank=True, null=True)

    clothing_size_information = models.CharField(
        max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return self.item_name

    @property
    def stock_remaining_qty(self):
        stock_added = Inventory.objects.filter(
            item=self.pk).aggregate(models.Sum('quantity'))['quantity__sum']
        if stock_added is None:
            stock_added = 0

        stock_distributed_item = RequestItem.objects.filter(
            request__request_fulfilled=True, item=self.pk).aggregate(models.Sum('quantity'))['quantity__sum']
        if stock_distributed_item is None:
            stock_distributed_item = 0

        aid_kit_items = AidKitItem.objects.filter(item=self)
        stock_distributed_kit = 0

        for aid_kit_item in aid_kit_items:
            item_quantity_per_kit = aid_kit_item.quantity
            kit_quantity_requested = RequestKit.objects.filter(
                request__request_fulfilled=True, kit=aid_kit_item.kit).aggregate(models.Sum("quantity"))['quantity__sum']

            if kit_quantity_requested is None:
                kit_quantity_requested = 0
            stock_distributed_kit += item_quantity_per_kit * kit_quantity_requested

        stock_remaining = stock_added - stock_distributed_item - stock_distributed_kit
        return stock_remaining
    
    @property
    def stock_remaining(self):
        qty = self.stock_remaining_qty
        label = get_inventory_label(qty, self.item_baseline_quantity)
        return f"{qty} ({label})"



class AidKit(models.Model):
    kit_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.kit_name


class AidKitItem(models.Model):
    kit = models.ForeignKey(AidKit, on_delete=models.CASCADE)
    item = models.ForeignKey(AidItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class AidItemRequest(models.Model):
    request_id = models.AutoField(primary_key=True)
    recipient = models.ForeignKey(
        RecipientInformation, on_delete=models.CASCADE)
    request_fulfilled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return ('Request #' + str(self.request_id))


class RequestItem(models.Model):
    request = models.ForeignKey(AidItemRequest, on_delete=models.CASCADE)
    item = models.ForeignKey(AidItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class RequestKit(models.Model):
    request = models.ForeignKey(AidItemRequest, on_delete=models.CASCADE)
    kit = models.ForeignKey(AidKit, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Page(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField(blank=True)

    def __str__(self) -> str:
        return self.title


class Donation(models.Model):
    donor = models.ForeignKey(
        DonorInformation, on_delete=models.SET_NULL, null=True)
    date_received = models.DateField()


class Inventory(models.Model):
    class Meta:
        verbose_name_plural = 'inventories'

    item = models.ForeignKey(AidItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    donation = models.ForeignKey(
        Donation, on_delete=models.CASCADE, blank=True)

    def __str__(self) -> str:
        return self.item.item_name


def get_inventory_label(quantity, baseline):
    ratio = quantity / max(baseline, 1)
    if ratio > 1:
        return "Excess"
    if ratio > 0.6:
        return "High"
    if ratio > 30:
        return "Medium"
    return "Low"
