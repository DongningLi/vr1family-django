#!/bin/bash
gunicorn --bind 0.0.0.0:8000 vr1family.wsgi
