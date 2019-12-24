def converse_tab():
    import pandas as pd
    import numpy as np

    df1 = pd.read_csv('Temp1.csv', sep=',')
    df2 = pd.read_csv('Temp2.csv', sep=',')

    df3 = df1.append(df2, ignore_index=True)
    df3_sort_time = df3.sort_values('Timestamp')  # Сортировка по столбцу со временем
    df3_sort_time['Temp'] = df3_sort_time['Grid']
    df3_sort_time['Press'] = df3_sort_time['Grid']
    df_after_replace_PG = df3_sort_time.replace({'Press': {'PG40': '740', 'PG41': '741', 'PG42': '742',
                                                           'PG43': '743', 'PG44': '744', 'PG45': '745',
                                                           'PG46': '746', 'PG47': '747', 'PG48': '748',
                                                           'PG49': '749', 'PG50': '750', 'PG51': '751',
                                                           'PG52': '752', 'PG53': '753', 'PG54': '754',
                                                           'PG55': '755', 'PG56': '756', 'PG57': '757',
                                                           'PG58': '758', 'PG59': '759', 'PG60': '760',
                                                           'PG61': '761', 'PG62': '762', 'PG63': '763',
                                                           'PG64': '764', 'PG65': '765', 'PG66': '766',
                                                           'PG67': '767', 'PG68': '768', 'PG69': '769',
                                                           'PG70': '770', 'PG71': '771', 'PG72': '772',
                                                           'PG73': '773', 'PG74': '774', 'PG75': '775',
                                                           'PG76': '776', 'PG77': '777', 'PG78': '778',
                                                           'PG79': '779', 'PG80': '780', 'PG81': '781'
                                                           }})
    #  Таблица соответствия для температур (до +50 градусов)
    Pwr1_replaceable = np.arange(0.1, 100.0, 0.1)
    Pwr1_replace = np.around((10 * np.log10(Pwr1_replaceable * 1000)), decimals=1)
    df_after_replace_PG_Pwr1 = df_after_replace_PG.replace(to_replace=Pwr1_replaceable, value=Pwr1_replace)

    # Преобразование PWR = 1000 в Вольты (от 400, чтобы не было пересечений с Pwr1 и az т.к. при пересечении данные
    # затираются
    Pwr2_replaceable = np.arange(400, 1001, 1)
    Pwr2_replace = np.around((np.log10(Pwr2_replaceable * 1000)), decimals=2)

    df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2 = df_after_replace_PG_Pwr1.replace(to_replace=Pwr2_replaceable,
                                                                               value=Pwr2_replace)
    # Преобразовываем Температуры

    df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP_NN = df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2.replace(
        {'Temp': {'PP': '0', 'PP01': '+1', 'PP02': '+2', 'PP03': '+3', 'PP04': '+4', 'PP05': '+5',
                  'PP06': '+6', 'PP07': '+7', 'PP08': '+8', 'PP09': '+9', 'PP10': '+10',
                  'PP11': '+11', 'PP12': '+12', 'PP13': '+13', 'PP14': '+14', 'PP15': '+15',
                  'PP16': '+16', 'PP17': '+17', 'PP18': '+18', 'PP19': '+19', 'PP20': '+20',
                  'PP21': '+21', 'PP22': '+22', 'PP23': '+23', 'PP24': '+24', 'PP25': '+25',
                  'PP26': '+26', 'PP27': '+27', 'PP28': '+28', 'PP29': '+29', 'PP30': '+30',
                  'PP31': '+31', 'PP32': '+32', 'PP33': '+33', 'PP34': '+34', 'PP35': '+35',
                  'PP36': '+36', 'PP37': '+37', 'PP38': '+38', 'PP39': '+39', 'PP40': '+40',
                  'PP41': '+41', 'PP42': '+42', 'PP43': '+43', 'PP44': '+44', 'PP45': '+45',
                  'PP46': '+46', 'PP47': '+47', 'PP48': '+48', 'PP49': '+49', 'PP50': '+50',
                  'NN01': '-1', 'NN02': '-2', 'NN03': '-3', 'NN04': '-4', 'NN05': '-5',
                  'NN06': '-6', 'NN07': '-7', 'NN08': '-8', 'NN09': '-9', 'NN10': '-10',
                  'NN11': '-11', 'NN12': '-12', 'NN13': '-13', 'NN14': '-14', 'NN15': '-15',
                  'NN16': '-16', 'NN17': '-17', 'NN18': '-18', 'NN19': '-19', 'NN20': '-20',
                  'NN21': '-21', 'NN22': '-22', 'NN23': '-23', 'NN24': '-24', 'NN25': '-25',
                  'NN26': '-26', 'NN27': '-27', 'NN28': '-28', 'NN29': '-29', 'NN30': '-30',
                  'NN31': '-31', 'NN32': '-32', 'NN33': '-33', 'NN34': '-34', 'NN35': '-35',
                  'NN36': '-36', 'NN37': '-37', 'NN38': '-38', 'NN39': '-39', 'NN40': '-40',
                  'NN41': '-41', 'NN42': '-42', 'NN43': '-43', 'NN44': '-44', 'NN45': '-45',
                  'NN46': '-46', 'NN47': '-47', 'NN48': '-48', 'NN49': '-49', 'NN50': '-50',
                  }})

    df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP_NN.to_excel('result.xlsx', index=False)


'''
   Выгрузка файла на два лист Excel
    with pd.ExcelWriter('result.xlsx') as writer:
        df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP_NN.to_excel(writer, sheet_name='Original', index=False,
                                                               freeze_panes=(1, 1))
        df3_sort_time.to_excel(writer, sheet_name='Original', index=False, freeze_panes=(1, 1), startcol=13)
'''
