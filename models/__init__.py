#!/usr/bin/python3
"""This module serves as entry point"""
from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
