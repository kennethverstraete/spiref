
class NHANESReferenceValueCalculator:
    """
    The ReferenceValueCalculator is used for calculating the NHANES III reference values for
    FEV1, FEV6, FVC, PEF and FEF2575.
    """
    @staticmethod
    def calculate_fev1(sex, height, age, race='Cau'):
        if sex == 'male':
            if race == 'Cau':
                if age < 20:
                    bs = [-0.7453, -0.04106, 0.004477, 0.00014098]
                else:
                    bs = [0.5536, -0.01303, -0.000172, 0.00014098]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-0.7048, -0.05711, 0.004316, 0.00013194]
                else:
                    bs = [0.3411, -0.02309, 0, 0.00013194]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-0.8218, -0.04248, 0.004291, 0.00015104]
                else:
                    bs = [0.6306, -0.02928, 0, 0.00015104]
        elif sex == 'female':
            if race == 'Cau':
                if age < 20:
                    bs = [-0.871, 0.06537, 0, 0.00011496]
                else:
                    bs = [0.4333, -0.00361, -0.000194, 0.00011496]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-0.963, 0.05799, 0, 0.00010846]
                else:
                    bs = [0.3433, -0.01283, -9.7E-05, 0.00010846]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-0.9641, 0.06490, 0, 0.00012154]
                else:
                    bs = [0.4529, -0.01178, -0.000113, 0.00012154]
        return bs[0] + bs[1] * age + bs[2] * age ** 2 + bs[3] * height ** 2

    @staticmethod
    def calculate_fev6(sex, height, age, race='Cau'):
        if sex == 'male':
            if race == 'Cau':
                if age < 20:
                    bs = [-0.3119, -0.18612, 0.009717, 0.00018188]
                else:
                    bs = [0.1102, -0.00842, -0.000223, 0.00018188]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-0.5525, -0.14107, 0.007241, 0.00016429]
                else:
                    bs = [-0.0547, -0.02114, 0, 0.00016429]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-0.6646, -0.1127, 0.007306, 0.0001784]
                else:
                    bs = [0.5757, -0.0286, 0, 0.0001784]
        elif sex == 'female':
            if race == 'Cau':
                if age < 20:
                    bs = [-1.1925, 0.06544, 0, 0.00014395]
                else:
                    bs = [-0.1373, 0.01317, -0.000352, 0.00014395]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-0.637, -0.04243, 0.003508, 0.00013497]
                else:
                    bs = [-0.1981, 0.00047, -0.00023, 0.00013497]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-1.241, 0.07625, 0, 0.00014106]
                else:
                    bs = [0.2033, 0.00020, -0.000232, 0.00014106]
        return bs[0] + bs[1] * age + bs[2] * age ** 2 + bs[3] * height ** 2

    @staticmethod
    def calculate_fvc(sex, height, age, race='Cau'):
        if sex == 'male':
            if race == 'Cau':
                if age < 20:
                    bs = [-0.2584, -0.20415, 0.010133, 0.00018642]
                else:
                    bs = [-0.1933, 0.00064, -0.000269, 0.00018642]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-0.4971, -0.15497, 0.007701, 0.00016643]
                else:
                    bs = [-0.1517, -0.01821, 0, 0.00016643]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-0.7571, -0.0952, 0.006619, 0.00017823]
                else:
                    bs = [0.2376, -0.00891, -0.000182, 0.00017823]
        elif sex == 'female':
            if race == 'Cau':
                if age < 20:
                    bs = [-1.2082, 0.05916, 0, 0.00014815]
                else:
                    bs = [-0.356, 0.01870, -0.000382, 0.00014815]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-0.6166, -0.04687, 0.003602, 0.00013606]
                else:
                    bs = [-0.3039, 0.00536, -0.000265, 0.00013606]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-1.2507, 0.07501, 0, 0.00014246]
                else:
                    bs = [0.1210, 0.00307, -0.000237, 0.00014246]
        return bs[0] + bs[1] * age + bs[2] * age ** 2 + bs[3] * height ** 2

    @staticmethod
    def calculate_pef(sex, height, age, race='Cau'):
        if sex == 'male':
            if race == 'Cau':
                if age < 20:
                    bs = [-0.5962, -0.12357, 0.013135, 0.00024962]
                else:
                    bs = [1.0523, 0.08272, -0.001301, 0.00024962]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-0.2684, -0.28016, 0.018202, 0.00027333]
                else:
                    bs = [2.2257, -0.04082, 0, 0.00027333]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-0.9537, -0.19602, 0.014497, 0.00030243]
                else:
                    bs = [0.0870, 0.06580, -0.001195, 0.00030243]
        elif sex == 'female':
            if race == 'Cau':
                if age < 20:
                    bs = [-3.6181, 0.60644, -0.016846, 0.00018623]
                else:
                    bs = [0.9267, 0.06929, -0.001031, 0.00018623]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-1.2398, 0.16375, 0, 0.00019746]
                else:
                    bs = [1.3597, 0.03458, -0.000847, 0.00019746]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-3.2549, 0.47495, -0.013193, 0.00022203]
                else:
                    bs = [0.2401, 0.06174, -0.001023, 0.00022203]
        return bs[0] + bs[1] * age + bs[2] * age ** 2 + bs[3] * height ** 2

    @staticmethod
    def calculate_fef2575(sex, height, age, race='Cau'):
        if sex == 'male':
            if race == 'Cau':
                if age < 20:
                    bs = [-1.0863, 0.13939, 0, 0.00010345]
                else:
                    bs = [2.7006, -0.04995, 0, 0.00010345]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-1.1627, 0.12314, 0, 0.00010461]
                else:
                    bs = [2.1477, -0.04238, 0, 0.00010461]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-1.3592, 0.10529, 0, 0.00014473]
                else:
                    bs = [1.7503, -0.05018, 0, 0.00014473]
        elif sex == 'female':
            if race == 'Cau':
                if age < 20:
                    bs = [-2.5284, 0.52490, -0.015309, 6.982E-05]
                else:
                    bs = [2.3670, -0.01904, -0.0002, 6.982E-05]
            elif race == 'AfrAm':
                if age < 20:
                    bs = [-2.5379, 0.43755, -0.012154, 8.572E-05]
                else:
                    bs = [2.0828, -0.03793, 0, 8.572E-05]
            elif race == 'MexAm':
                if age < 20:
                    bs = [-2.1825, 0.42451, -0.012415, 9.61E-05]
                else:
                    bs = [1.7456, -0.01195, -0.000291, 9.61E-05]
        return bs[0] + bs[1] * age + bs[2] * age ** 2 + bs[3] * height ** 2

    @staticmethod
    def calculate_fev1fev6p(sex, age, race='Cau'):
        if sex == 'male':
            if race == 'Cau':
                bs = [87.34, -0.1382]
            elif race == 'AfrAm':
                bs = [88.841, -0.1305]
            elif race == 'MexAm':
                bs = [89.388, -0.1534]
        elif sex == 'female':
            if race == 'Cau':
                bs = [90.107, -0.1563]
            elif race == 'AfrAm':
                bs = [91.229, -0.1558]
            elif race == 'MexAm':
                bs = [91.664, -0.167]
        return bs[0] + bs[1] * age

    @staticmethod
    def calculate_fev1fvcp(sex, age, race='Cau'):
        if sex == 'male':
            if race == 'Cau':
                bs = [88.066, -0.2066]
            elif race == 'AfrAm':
                bs = [89.239, -0.1828]
            elif race == 'MexAm':
                bs = [90.024, -0.2186]
        elif sex == 'female':
            if race == 'Cau':
                bs = [90.809, -0.2125]
            elif race == 'AfrAm':
                bs = [91.655, -0.2039]
            elif race == 'MexAm':
                bs = [92.36, -0.2248]
        return bs[0] + bs[1] * age
