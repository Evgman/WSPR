def converse_tab():
    import pandas as pd
    import numpy as np

    df1 = pd.read_csv('Temp1.csv', sep=',')
    df2 = pd.read_csv('Temp2.csv', sep=',')

    df3 = df1.append(df2, ignore_index=True)
    df3_sort_time = df3.sort_values('Timestamp')  # Сортировка по столбцу со временем
    # Таблица преобразования для давления (можно добавлять)
    PG_replaceable = ['PG40', 'PG41', 'PG42', 'PG43', 'PG44',
                      'PG45', 'PG46', 'PG47', 'PG48', 'PG49',
                      'PG50', 'PG51', 'PG52', 'PG53', 'PG54',
                      'PG55', 'PG56', 'PG57', 'PG58', 'PG59',
                      'PG60', 'PG61', 'PG62', 'PG63', 'PG64',
                      'PG65', 'PG66', 'PG67', 'PG68', 'PG69',
                      'PG70', 'PG71', 'PG72', 'PG73', 'PG74',
                      'PG75', 'PG76', 'PG77', 'PG78', 'PG79']
    # Значения меняются соответственно на эти(должно быть одинаковое кол-во с верхней таблицей)
    PG_replace = ['740', '741', '742', '743', '744',
                  '745', '746', '747', '748', '749',
                  '750', '751', '752', '753', '754',
                  '755', '756', '757', '758', '759',
                  '760', '761', '762', '763', '764',
                  '765', '766', '767', '768', '769',
                  '770', '771', '772', '773', '774',
                  '775', '776', '777', '788', '779']
    df_after_replace_PG = df3_sort_time.replace(to_replace=PG_replaceable, value=PG_replace)
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

    # Преобразовываем температуры PP и NN
    PP_replaceable = ['PP', 'PP01', 'PP02', 'PP03', 'PP04', 'PP05',
                      'PP06', 'PP07', 'PP08', 'PP09', 'PP10',
                      'PP11', 'PP12', 'PP13', 'PP14', 'PP15',
                      'PP16', 'PP17', 'PP18', 'PP19', 'PP20',
                      'PP21', 'PP22', 'PP23', 'PP24', 'PP25',
                      'PP26', 'PP27', 'PP28', 'PP29', 'PP30',
                      'PP31', 'PP32', 'PP33', 'PP34', 'PP35',
                      'PP36', 'PP37', 'PP38', 'PP39', 'PP40',
                      'PP41', 'PP42', 'PP43', 'PP44', 'PP45',
                      'PP46', 'PP47', 'PP48', 'PP49', 'PP50']
    NN_replaceable = ['NN01', 'NN02', 'NN03', 'NN04', 'NN05',
                      'NN06', 'NN07', 'NN08', 'NN09', 'NN10',
                      'NN11', 'NN12', 'NN13', 'NN14', 'NN15',
                      'NN16', 'NN17', 'NN18', 'NN19', 'NN20',
                      'NN21', 'NN22', 'NN23', 'NN24', 'NN25',
                      'NN26', 'NN27', 'NN28', 'NN29', 'NN30',
                      'NN31', 'NN32', 'NN33', 'NN34', 'NN35',
                      'NN36', 'NN37', 'NN38', 'NN39', 'NN40',
                      'NN41', 'NN42', 'NN43', 'NN44', 'NN45',
                      'NN46', 'NN47', 'NN48', 'NN49', 'NN50']

    PP_replace = ['0', '+1', '+2', '+3', '+4', '+5',
                  '+6', '+7', '+8', '+9', '+10',
                  '+11', '+12', '+13', '+14', '+15',
                  '+16', '+17', '+18', '+19', '+20',
                  '+21', '+22', '+23', '+24', '+25',
                  '+26', '+27', '+28', '+29', '+30',
                  '+31', '+32', '+33', '+34', '+35',
                  '+36', '+37', '+38', '+39', '+40',
                  '+41', '+42', '+43', '+44', '+45',
                  '+46', '+47', '+48', '+49', '+50']
    NN_replace = ['-1', '-2', '-3', '-4', '-5',
                  '-6', '-7', '-8', '-9', '-10',
                  '-11', '-12', '-13', '-14', '-15',
                  '-16', '-17', '-18', '-19', '-20',
                  '-21', '-22', '-23', '-24', '-25',
                  '-26', '-27', '-28', '-29', '-30',
                  '-31', '-32', '-33', '-34', '-35',
                  '-36', '-37', '-38', '-39', '-40',
                  '-41', '-42', '-43', '-44', '-45',
                  '-46', '-47', '-48', '-49', '-50']
    # Преобразовываем Вольты
    df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP = df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2.replace(
        to_replace=PP_replaceable, value=PP_replace)
    df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP_NN = df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP.replace(
        to_replace=NN_replaceable, value=NN_replace)

    # df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP_NN.to_excel('result_modify.xlsx', index=False)
    # df3_sort_time.to_excel('result_original.xlsx', index=False)
    with pd.ExcelWriter('result.xlsx') as writer:
        df_after_replace_PG_Pwr_PP_NN_Pwr1_Pwr2_PP_NN.to_excel(writer, sheet_name='Original', index=False,
                                                               freeze_panes=(1, 1))
        df3_sort_time.to_excel(writer, sheet_name='Original', index=False, freeze_panes=(1, 1), startcol=13)
    print('Файл выгружен')
