import time

result = time.localtime()

current_year = result.tm_year


class ParsCvdRisk:
    __name = None
    __gender = None
    __year_of_birth = None
    __diabetic = None
    __family_history_CVD = None
    __waist_circumference = None
    __hip_circumference = None
    __smoking = None
    __systolic_blood_pressure = None
    __total_cholesterol = None

    def __init__(self, name, gender, year_of_birth, diabetic, family_history_cvd, waist_circumference,
                 hip_circumference, smoking, systolic_blood_pressure, total_cholesterol):
        self.__name = name
        self.__gender = gender
        self.__year_of_birth = year_of_birth
        self.__diabetic = diabetic
        self.__family_history_cvd = family_history_cvd
        self.__waist_circumference = waist_circumference
        self.__hip_circumference = hip_circumference
        self.__smoking = smoking
        self.__systolic_blood_pressure = systolic_blood_pressure
        self.__total_cholesterol = total_cholesterol

    def set(self, name, gender, year_of_birth, diabetic, family_history_cvd, waist_circumference, hip_circumference,
            smoking, systolic_blood_pressure, total_cholesterol):
        self.__name = name
        self.__gender = gender
        self.__year_of_birth = year_of_birth
        self.__diabetic = diabetic
        self.__family_history_cvd = family_history_cvd
        self.__waist_circumference = waist_circumference
        self.__hip_circumference = hip_circumference
        self.__smoking = smoking
        self.__systolic_blood_pressure = systolic_blood_pressure
        self.__total_cholesterol = total_cholesterol

    def get_name(self):
        return self.__name

    def get_year_of_birth(self):
        return self.__year_of_birth

    def get_gender(self):
        return self.__gender

    def get_diabetic(self):
        return self.__diabetic

    def get_family_history_cvd(self):
        return self.__family_history_cvd

    def get_waist_circumference(self):
        return self.__waist_circumference

    def get_hip_circumference(self):
        return self.__hip_circumference

    def get_smoking(self):
        return self.__smoking

    def get_systolic_blood_pressure(self):
        return self.__systolic_blood_pressure

    def get_total_cholesterol(self):
        return self.__total_cholesterol

    def age(self):
        global current_year
        age = current_year - int(self.get_year_of_birth())
        return age

    def waist_to_hip_ratio(self):
        whr = round(self.get_waist_circumference() / self.get_hip_circumference(), 2)
        return whr

    def whr_category(self):
        if self.waist_to_hip_ratio() > 0.95 and self.get_gender() == 'Male':
            return 'high'
        elif self.waist_to_hip_ratio() > 0.8 and self.get_gender() == 'Female':
            return 'high'
        else:
            return 'low'

    def total_cholesterol_category(self):
        if self.get_total_cholesterol() <= 150:
            return 1
        if 150 < self.get_total_cholesterol() <= 200:
            return 2
        if 200 < self.get_total_cholesterol() <= 250:
            return 3
        if 250 < self.get_total_cholesterol() <= 300:
            return 4
        if self.get_total_cholesterol() > 300:
            return 5

    def cvd_risk_score(self):
        if self.age() < 35:
            return 0
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and\
                (self.get_gender() is 'Female') and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() <= 139:
                    return 1
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() != 5:
                        return 2
                    else:
                        return 3
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    return 1
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 1 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 7
                    else:
                        return 8
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and \
                (self.get_gender() is 'Female') and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 < self.age() < 44:
                if self.get_systolic_blood_pressure() < 120:
                    return 1
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 2:
                        return 2
                    elif self.total_cholesterol_category() is 5:
                        return 4
                    else:
                        return 3
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    else:
                        return 10
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and\
                    (self.get_gender() is 'Female') and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() <= 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and \
                    (self.get_gender() is 'Female') and (self.get_diabetic() is True) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and (self.get_gender() is \
                    'Male') and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    return 1
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    else:
                        return 10
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and (self.get_gender() is\
                    'Male') and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() <= 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 < self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() <= 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 < self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() <= 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 120 < self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and (self.get_gender() is\
                    'Male') and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is False) and (self.get_gender() is\
                    'Male') and (self.get_diabetic() is True) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 19
                    elif self.total_cholesterol_category() is 2:
                        return 23
                    elif self.total_cholesterol_category() is 3:
                        return 26
                    elif self.total_cholesterol_category() is 4:
                        return 29
                    else:
                        return 31
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    return 1
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 7
                    else:
                        return 8
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 4
                    elif self.total_cholesterol_category() is 3:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 2:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 9
                    else:
                        return 10
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 15
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 16
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 13
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 21
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 12
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 15
                    else:
                        return 16
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 21
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 17
                    elif self.total_cholesterol_category() is 2:
                        return 20
                    elif self.total_cholesterol_category() is 3:
                        return 23
                    elif self.total_cholesterol_category() is 4:
                        return 25
                    else:
                        return 27
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is True) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 2:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 14
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 16
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 20
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 20
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 25
                    else:
                        return 27
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 13
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 21
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 20
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 26
                    elif self.total_cholesterol_category() is 3:
                        return 29
                    elif self.total_cholesterol_category() is 4:
                        return 32
                    else:
                        return 34
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is 'Male')\
                    and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 4
                    elif self.total_cholesterol_category() is 3:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is 'Male')\
                    and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    else:
                        return 7
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is 'Male')\
                    and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 14
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 16
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 20
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 20
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 25
                    else:
                        return 27
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 13
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 21
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 20
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 26
                    elif self.total_cholesterol_category() is 3:
                        return 29
                    elif self.total_cholesterol_category() is 4:
                        return 32
                    else:
                        return 34
        elif (self.whr_category() is 'low') and (self.get_family_history_cvd() is True) and (self.get_gender() is 'Male')\
                    and (self.get_diabetic() is True) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 13
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 15
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 21
                    elif self.total_cholesterol_category() is 4:
                        return 23
                    else:
                        return 25
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 14
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 21
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 26
                    elif self.total_cholesterol_category() is 3:
                        return 29
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 34
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 20
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 25
                    else:
                        return 27
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 34
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 28
                    elif self.total_cholesterol_category() is 2:
                        return 33
                    elif self.total_cholesterol_category() is 3:
                        return 37
                    elif self.total_cholesterol_category() is 4:
                        return 40
                    else:
                        return 43
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    return 1
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 1
                    else:
                        return 2
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 14
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is\
                    'Female') and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 8
                    else:
                        return 9
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is 'Female')\
                and (self.get_diabetic() is True) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 4
                    elif self.total_cholesterol_category() is 5:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    else:
                        return 8
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category()is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category()is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 12
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 14
                    elif self.total_cholesterol_category() is 2:
                        return 17
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 19
                    elif self.total_cholesterol_category() is 2:
                        return 23
                    elif self.total_cholesterol_category() is 3:
                        return 26
                    elif self.total_cholesterol_category() is 4:
                        return 28
                    else:
                        return 31
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is 'Male')\
                and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 < self.age() < 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() != 5:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif self.get_systolic_blood_pressure() >= 160:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is "Male") \
                and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 4
                    elif self.total_cholesterol_category() is 3:
                        return 5
                    else:
                        return 6
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 14
                    elif self.total_cholesterol_category() is 2:
                        return 17
                    elif self.total_cholesterol_category() is 3:
                        return 19
                    elif self.total_cholesterol_category() is 4:
                        return 21
                    else:
                        return 23
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is "Male")\
                and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 4
                    elif self.total_cholesterol_category() is 3:
                        return 5
                    else:
                        return 6
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    else:
                        return 8
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 12
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 14
                    elif self.total_cholesterol_category() is 2:
                        return 17
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 19
                    elif self.total_cholesterol_category() is 2:
                        return 23
                    elif self.total_cholesterol_category() is 3:
                        return 26
                    elif self.total_cholesterol_category() is 4:
                        return 28
                    else:
                        return 31
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is False) and (self.get_gender() is \
                    "Male") and (self.get_diabetic() is True) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 16
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    else:
                        return 8
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 12
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 15
                    else:
                        return 17
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 13
                    elif self.total_cholesterol_category() is 2:
                        return 16
                    elif self.total_cholesterol_category() is 3:
                        return 18
                    elif self.total_cholesterol_category() is 4:
                        return 20
                    else:
                        return 22
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 14
                    elif self.total_cholesterol_category() is 2:
                        return 17
                    elif self.total_cholesterol_category() is 3:
                        return 19
                    elif self.total_cholesterol_category() is 4:
                        return 21
                    else:
                        return 23
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 19
                    elif self.total_cholesterol_category() is 2:
                        return 23
                    elif self.total_cholesterol_category() is 3:
                        return 26
                    elif self.total_cholesterol_category() is 4:
                        return 28
                    else:
                        return 30
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 12
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 16
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 19
                    elif self.total_cholesterol_category() is 2:
                        return 23
                    elif self.total_cholesterol_category() is 3:
                        return 25
                    elif self.total_cholesterol_category() is 4:
                        return 28
                    else:
                        return 30
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 25
                    elif self.total_cholesterol_category() is 2:
                        return 29
                    elif self.total_cholesterol_category() is 3:
                        return 33
                    elif self.total_cholesterol_category() is 4:
                        return 36
                    else:
                        return 39
        if (self.whr_category() is 'high') and (self.get_family_history_cvd() is True) and (self.get_gender() is\
                    'Female') and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if 1 <= self.total_cholesterol_category() <= 3:
                        return 2
                    else:
                        return 3
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 4:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() is 4:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 15
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 21
                    elif self.total_cholesterol_category() is 4:
                        return 23
                    else:
                        return 25
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 19
                    else:
                        return 20
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 34
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Female') and (self.get_diabetic() is True) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 33
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 33
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 27
                    elif self.total_cholesterol_category() is 2:
                        return 32
                    elif self.total_cholesterol_category() is 3:
                        return 36
                    elif self.total_cholesterol_category() is 4:
                        return 39
                    else:
                        return 42
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is True) and (self.get_gender() is\
                    'Male') and (self.get_diabetic() is False) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 1
                    else:
                        return 2
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 2
                    elif 2 <= self.total_cholesterol_category() <= 4:
                        return 3
                    else:
                        return 4
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 6
                    elif self.total_cholesterol_category() is 4:
                        return 7
                    else:
                        return 8
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    elif self.total_cholesterol_category() is 4:
                        return 10
                    else:
                        return 11
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 15
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 21
                    elif self.total_cholesterol_category() is 4:
                        return 23
                    else:
                        return 25
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Male') and (self.get_diabetic() is False) and (self.get_smoking() is True):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 2
                    else:
                        return 3
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 4
                    else:
                        return 5
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    elif self.total_cholesterol_category() is 4:
                        return 6
                    else:
                        return 7
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif self.total_cholesterol_category() is 3:
                        return 6
                    else:
                        return 7
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 8
                    elif self.total_cholesterol_category() is 3:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 14
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 11
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 14
                    else:
                        return 15
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 21
                    elif self.total_cholesterol_category() is 4:
                        return 23
                    else:
                        return 25
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 16
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 19
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 21
                    elif self.total_cholesterol_category() is 4:
                        return 23
                    else:
                        return 25
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 20
                    elif self.total_cholesterol_category() is 2:
                        return 24
                    elif self.total_cholesterol_category() is 3:
                        return 27
                    elif self.total_cholesterol_category() is 4:
                        return 30
                    else:
                        return 32
        elif (self.whr_category() is 'high') and (self.get_family_history_cvd() is True) and (self.get_gender() is \
                    'Male') and (self.get_diabetic() is True) and (self.get_smoking() is False):
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if 1 <= self.total_cholesterol_category() <= 2:
                        return 3
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 4
                    else:
                        return 5
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif self.total_cholesterol_category() is 2:
                        return 5
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 6
                    else:
                        return 7
                elif 140 < self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 8
                    else:
                        return 9
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 4
                    elif 2 <= self.total_cholesterol_category() <= 3:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 6
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    elif self.total_cholesterol_category() is 4:
                        return 9
                    else:
                        return 10
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif self.total_cholesterol_category() is 3:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 9
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 12
                    elif self.total_cholesterol_category() is 4:
                        return 13
                    else:
                        return 14
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 18
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 12
                    elif self.total_cholesterol_category() is 2:
                        return 15
                    elif self.total_cholesterol_category() is 3:
                        return 17
                    elif self.total_cholesterol_category() is 4:
                        return 18
                    else:
                        return 20
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 33
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 18
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 33
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 27
                    elif self.total_cholesterol_category() is 2:
                        return 32
                    elif self.total_cholesterol_category() is 3:
                        return 36
                    elif self.total_cholesterol_category() is 4:
                        return 39
                    else:
                        return 42
        elif self.whr_category() is 'high' and self.get_family_history_cvd() is True and self.get_gender() is \
                    'Male' and self.get_diabetic() is True and self.get_smoking() is True:
            if 35 <= self.age() <= 44:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 3
                    elif self.total_cholesterol_category() is 2:
                        return 4
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 5
                    else:
                        return 6
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 7
                    elif 3 <= self.total_cholesterol_category() <= 4:
                        return 8
                    else:
                        return 9
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 12
                    elif self.total_cholesterol_category() is 3:
                        return 13
                    elif self.total_cholesterol_category() is 4:
                        return 15
                    else:
                        return 16
            elif 45 <= self.age() <= 54:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 5
                    elif self.total_cholesterol_category() is 2:
                        return 6
                    elif self.total_cholesterol_category() is 3:
                        return 7
                    elif self.total_cholesterol_category() is 4:
                        return 8
                    else:
                        return 9
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 8
                    elif self.total_cholesterol_category() is 2:
                        return 10
                    elif self.total_cholesterol_category() is 3:
                        return 11
                    elif self.total_cholesterol_category() is 4:
                        return 12
                    else:
                        return 13
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 12
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 14
                    elif self.total_cholesterol_category() is 2:
                        return 17
                    elif self.total_cholesterol_category() is 3:
                        return 19
                    elif self.total_cholesterol_category() is 4:
                        return 21
                    else:
                        return 23
            elif 55 <= self.age() <= 64:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 7
                    elif self.total_cholesterol_category() is 2:
                        return 9
                    elif self.total_cholesterol_category() is 3:
                        return 10
                    elif self.total_cholesterol_category() is 4:
                        return 11
                    else:
                        return 12
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 11
                    elif self.total_cholesterol_category() is 2:
                        return 14
                    elif self.total_cholesterol_category() is 3:
                        return 15
                    elif self.total_cholesterol_category() is 4:
                        return 17
                    else:
                        return 19
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 15
                    elif self.total_cholesterol_category() is 2:
                        return 18
                    elif self.total_cholesterol_category() is 3:
                        return 20
                    elif self.total_cholesterol_category() is 4:
                        return 22
                    else:
                        return 24
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 19
                    elif self.total_cholesterol_category() is 2:
                        return 23
                    elif self.total_cholesterol_category() is 3:
                        return 26
                    elif self.total_cholesterol_category() is 4:
                        return 29
                    else:
                        return 31
            elif 65 <= self.age() <= 74:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 10
                    elif self.total_cholesterol_category() is 2:
                        return 13
                    elif self.total_cholesterol_category() is 3:
                        return 14
                    elif self.total_cholesterol_category() is 4:
                        return 16
                    else:
                        return 17
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 16
                    elif self.total_cholesterol_category() is 2:
                        return 19
                    elif self.total_cholesterol_category() is 3:
                        return 22
                    elif self.total_cholesterol_category() is 4:
                        return 24
                    else:
                        return 26
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 30
                    else:
                        return 33
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 27
                    elif self.total_cholesterol_category() is 2:
                        return 32
                    elif self.total_cholesterol_category() is 3:
                        return 36
                    elif self.total_cholesterol_category() is 4:
                        return 39
                    else:
                        return 42
            elif self.age() >= 75:
                if self.get_systolic_blood_pressure() < 120:
                    if self.total_cholesterol_category() is 1:
                        return 14
                    elif self.total_cholesterol_category() is 2:
                        return 17
                    elif self.total_cholesterol_category() is 3:
                        return 19
                    elif self.total_cholesterol_category() is 4:
                        return 21
                    else:
                        return 23
                elif 120 <= self.get_systolic_blood_pressure() <= 139:
                    if self.total_cholesterol_category() is 1:
                        return 21
                    elif self.total_cholesterol_category() is 2:
                        return 25
                    elif self.total_cholesterol_category() is 3:
                        return 28
                    elif self.total_cholesterol_category() is 4:
                        return 31
                    else:
                        return 33
                elif 140 <= self.get_systolic_blood_pressure() <= 159:
                    if self.total_cholesterol_category() is 1:
                        return 27
                    elif self.total_cholesterol_category() is 2:
                        return 32
                    elif self.total_cholesterol_category() is 3:
                        return 35
                    elif self.total_cholesterol_category() is 4:
                        return 39
                    else:
                        return 42
                elif self.get_systolic_blood_pressure() >= 160:
                    if self.total_cholesterol_category() is 1:
                        return 35
                    elif self.total_cholesterol_category() is 2:
                        return 41
                    elif self.total_cholesterol_category() is 3:
                        return 45
                    elif self.total_cholesterol_category() is 4:
                        return 49
                    else:
                        return 52

    def cvd_risk_stratification(self):
        if self.cvd_risk_score() < 5:
            return 'low risk'
        elif 5 < self.cvd_risk_score() < 7.5:
            return 'borderline risk'
        elif 7.5 < self.cvd_risk_score() < 20:
            return 'high risk'
        else:
            return 'very high risk'

    def __str__(self):
        return f'{self.get_name()} is a {self.age()} year-old {str(self.get_gender()).lower()} patient with 10-year ASCVD risk ' \
            f'of {self.cvd_risk_score()}% which is {self.cvd_risk_stratification()} according to the PARS study ' \
            f'score tables.'

salim = ParsCvdRisk('Salim', 'Male', 1940, True, True, 105 , 100, True, 170, 350)
#print(salim.age())
print(salim)