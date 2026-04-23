#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:00:09 2026

@author: megancicerello
"""

from ehr_visit import EHRVisit


def test_get_cost():
    visit = EHRVisit(
        1, "John", "Doe", "1980-01-01", 44,
        "J10", "Influenza", "City Hospital",
        "Low", "General", "2024-01-01", 3, 2500.00
    )
    assert visit.get_cost() == 2500.00


def test_patient_name():
    visit = EHRVisit(
        2, "Jane", "Smith", "1975-05-05", 49,
        "E11", "Diabetes", "Metro Clinic",
        "Medium", "Endocrinology", "2024-02-02", 5, 4000.00
    )
    assert visit.get_patient_name() == "Jane Smith"