#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:58:48 2026

@author: megancicerello
"""

class EHRVisit:
    """Represents a cleaned EHR patient visit record."""

    def __init__(
        self,
        patient_id,
        first_name,
        last_name,
        date_of_birth,
        age,
        icd10_code,
        diagnosis_name,
        facility,
        risk_level,
        specialty,
        admission_date,
        length_of_stay,
        cost
    ):
        # Public attributes
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.icd10_code = icd10_code
        self.diagnosis_name = diagnosis_name
        self.facility = facility
        self.risk_level = risk_level
        self.specialty = specialty
        self.admission_date = admission_date
        self.length_of_stay = length_of_stay
        self.age = age

        # Private attribute
        self.__cost = cost

    # Public methods
    def get_cost(self):
        return self.__cost

    def get_patient_name(self):
        return f"{self.first_name} {self.last_name}"

    # Private method
    def __cost_flag(self):
        return "High Cost" if self.__cost > 5000 else "Standard Cost"

    def __str__(self):
        return f"{self.get_patient_name()} | {self.icd10_code} | ${self.__cost:.2f}"

    # Magic method
    def __gt__(self, other):
        return self.__cost > other.__cost