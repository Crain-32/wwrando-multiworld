# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'randomizer_window.ui'
#
# Created: Tue Jul 24 16:46:53 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 806)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.seed = QtGui.QLineEdit(self.tab)
        self.seed.setObjectName("seed")
        self.gridLayout.addWidget(self.seed, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.clean_iso_path = QtGui.QLineEdit(self.tab)
        self.clean_iso_path.setObjectName("clean_iso_path")
        self.gridLayout.addWidget(self.clean_iso_path, 0, 1, 1, 1)
        self.output_folder = QtGui.QLineEdit(self.tab)
        self.output_folder.setObjectName("output_folder")
        self.gridLayout.addWidget(self.output_folder, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.clean_iso_path_browse_button = QtGui.QPushButton(self.tab)
        self.clean_iso_path_browse_button.setObjectName("clean_iso_path_browse_button")
        self.gridLayout.addWidget(self.clean_iso_path_browse_button, 0, 2, 1, 1)
        self.output_folder_browse_button = QtGui.QPushButton(self.tab)
        self.output_folder_browse_button.setObjectName("output_folder_browse_button")
        self.gridLayout.addWidget(self.output_folder_browse_button, 1, 2, 1, 1)
        self.generate_seed_button = QtGui.QPushButton(self.tab)
        self.generate_seed_button.setObjectName("generate_seed_button")
        self.gridLayout.addWidget(self.generate_seed_button, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progression_misc = QtGui.QCheckBox(self.groupBox)
        self.progression_misc.setChecked(True)
        self.progression_misc.setObjectName("progression_misc")
        self.gridLayout_2.addWidget(self.progression_misc, 9, 1, 1, 1)
        self.progression_short_sidequests = QtGui.QCheckBox(self.groupBox)
        self.progression_short_sidequests.setObjectName("progression_short_sidequests")
        self.gridLayout_2.addWidget(self.progression_short_sidequests, 2, 0, 1, 1)
        self.progression_platforms_rafts = QtGui.QCheckBox(self.groupBox)
        self.progression_platforms_rafts.setObjectName("progression_platforms_rafts")
        self.gridLayout_2.addWidget(self.progression_platforms_rafts, 5, 0, 1, 1)
        self.progression_big_octos_gunboats = QtGui.QCheckBox(self.groupBox)
        self.progression_big_octos_gunboats.setObjectName("progression_big_octos_gunboats")
        self.gridLayout_2.addWidget(self.progression_big_octos_gunboats, 6, 1, 1, 1)
        self.progression_submarines = QtGui.QCheckBox(self.groupBox)
        self.progression_submarines.setChecked(False)
        self.progression_submarines.setObjectName("progression_submarines")
        self.gridLayout_2.addWidget(self.progression_submarines, 5, 1, 1, 1)
        self.progression_dungeons = QtGui.QCheckBox(self.groupBox)
        self.progression_dungeons.setChecked(True)
        self.progression_dungeons.setObjectName("progression_dungeons")
        self.gridLayout_2.addWidget(self.progression_dungeons, 0, 0, 1, 1)
        self.progression_expensive_purchases = QtGui.QCheckBox(self.groupBox)
        self.progression_expensive_purchases.setChecked(True)
        self.progression_expensive_purchases.setObjectName("progression_expensive_purchases")
        self.gridLayout_2.addWidget(self.progression_expensive_purchases, 9, 0, 1, 1)
        self.progression_eye_reef_chests = QtGui.QCheckBox(self.groupBox)
        self.progression_eye_reef_chests.setObjectName("progression_eye_reef_chests")
        self.gridLayout_2.addWidget(self.progression_eye_reef_chests, 6, 0, 1, 1)
        self.progression_spoils_trading = QtGui.QCheckBox(self.groupBox)
        self.progression_spoils_trading.setObjectName("progression_spoils_trading")
        self.gridLayout_2.addWidget(self.progression_spoils_trading, 3, 0, 1, 1)
        self.progression_minigames = QtGui.QCheckBox(self.groupBox)
        self.progression_minigames.setObjectName("progression_minigames")
        self.gridLayout_2.addWidget(self.progression_minigames, 3, 1, 1, 1)
        self.progression_long_sidequests = QtGui.QCheckBox(self.groupBox)
        self.progression_long_sidequests.setObjectName("progression_long_sidequests")
        self.gridLayout_2.addWidget(self.progression_long_sidequests, 2, 1, 1, 1)
        self.progression_puzzle_secret_caves = QtGui.QCheckBox(self.groupBox)
        self.progression_puzzle_secret_caves.setChecked(True)
        self.progression_puzzle_secret_caves.setObjectName("progression_puzzle_secret_caves")
        self.gridLayout_2.addWidget(self.progression_puzzle_secret_caves, 1, 0, 1, 1)
        self.progression_great_fairies = QtGui.QCheckBox(self.groupBox)
        self.progression_great_fairies.setChecked(True)
        self.progression_great_fairies.setObjectName("progression_great_fairies")
        self.gridLayout_2.addWidget(self.progression_great_fairies, 0, 1, 1, 1)
        self.progression_combat_secret_caves = QtGui.QCheckBox(self.groupBox)
        self.progression_combat_secret_caves.setObjectName("progression_combat_secret_caves")
        self.gridLayout_2.addWidget(self.progression_combat_secret_caves, 1, 1, 1, 1)
        self.progression_triforce_charts = QtGui.QCheckBox(self.groupBox)
        self.progression_triforce_charts.setObjectName("progression_triforce_charts")
        self.gridLayout_2.addWidget(self.progression_triforce_charts, 7, 0, 1, 1)
        self.progression_treasure_charts = QtGui.QCheckBox(self.groupBox)
        self.progression_treasure_charts.setObjectName("progression_treasure_charts")
        self.gridLayout_2.addWidget(self.progression_treasure_charts, 7, 1, 1, 1)
        self.progression_free_gifts = QtGui.QCheckBox(self.groupBox)
        self.progression_free_gifts.setChecked(True)
        self.progression_free_gifts.setObjectName("progression_free_gifts")
        self.gridLayout_2.addWidget(self.progression_free_gifts, 4, 0, 1, 1)
        self.progression_mail = QtGui.QCheckBox(self.groupBox)
        self.progression_mail.setObjectName("progression_mail")
        self.gridLayout_2.addWidget(self.progression_mail, 4, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.keylunacy = QtGui.QCheckBox(self.groupBox_3)
        self.keylunacy.setObjectName("keylunacy")
        self.gridLayout_3.addWidget(self.keylunacy, 0, 0, 1, 1)
        self.randomize_starting_island = QtGui.QCheckBox(self.groupBox_3)
        self.randomize_starting_island.setObjectName("randomize_starting_island")
        self.gridLayout_3.addWidget(self.randomize_starting_island, 1, 1, 1, 1)
        self.randomize_dungeon_entrances = QtGui.QCheckBox(self.groupBox_3)
        self.randomize_dungeon_entrances.setObjectName("randomize_dungeon_entrances")
        self.gridLayout_3.addWidget(self.randomize_dungeon_entrances, 0, 1, 1, 1)
        self.randomize_charts = QtGui.QCheckBox(self.groupBox_3)
        self.randomize_charts.setObjectName("randomize_charts")
        self.gridLayout_3.addWidget(self.randomize_charts, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.reveal_full_sea_chart = QtGui.QCheckBox(self.groupBox_2)
        self.reveal_full_sea_chart.setChecked(True)
        self.reveal_full_sea_chart.setObjectName("reveal_full_sea_chart")
        self.gridLayout_4.addWidget(self.reveal_full_sea_chart, 1, 0, 1, 1)
        self.swift_sail = QtGui.QCheckBox(self.groupBox_2)
        self.swift_sail.setChecked(True)
        self.swift_sail.setObjectName("swift_sail")
        self.gridLayout_4.addWidget(self.swift_sail, 0, 0, 1, 1)
        self.instant_text_boxes = QtGui.QCheckBox(self.groupBox_2)
        self.instant_text_boxes.setChecked(True)
        self.instant_text_boxes.setObjectName("instant_text_boxes")
        self.gridLayout_4.addWidget(self.instant_text_boxes, 0, 1, 1, 1)
        self.add_shortcut_warps_between_dungeons = QtGui.QCheckBox(self.groupBox_2)
        self.add_shortcut_warps_between_dungeons.setObjectName("add_shortcut_warps_between_dungeons")
        self.gridLayout_4.addWidget(self.add_shortcut_warps_between_dungeons, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_for_num_starting_triforce_shards = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_for_num_starting_triforce_shards.sizePolicy().hasHeightForWidth())
        self.label_for_num_starting_triforce_shards.setSizePolicy(sizePolicy)
        self.label_for_num_starting_triforce_shards.setObjectName("label_for_num_starting_triforce_shards")
        self.horizontalLayout_2.addWidget(self.label_for_num_starting_triforce_shards)
        self.num_starting_triforce_shards = QtGui.QComboBox(self.groupBox_2)
        self.num_starting_triforce_shards.setMaximumSize(QtCore.QSize(40, 16777215))
        self.num_starting_triforce_shards.setObjectName("num_starting_triforce_shards")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.num_starting_triforce_shards.addItem("")
        self.horizontalLayout_2.addWidget(self.num_starting_triforce_shards)
        self.widget = QtGui.QWidget(self.groupBox_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_for_custom_player_model = QtGui.QLabel(self.tab_2)
        self.label_for_custom_player_model.setObjectName("label_for_custom_player_model")
        self.horizontalLayout_3.addWidget(self.label_for_custom_player_model)
        self.custom_player_model = QtGui.QComboBox(self.tab_2)
        self.custom_player_model.setObjectName("custom_player_model")
        self.horizontalLayout_3.addWidget(self.custom_player_model)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.player_in_casual_clothes = QtGui.QCheckBox(self.tab_2)
        self.player_in_casual_clothes.setObjectName("player_in_casual_clothes")
        self.gridLayout_5.addWidget(self.player_in_casual_clothes, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_5)
        self.custom_colors_layout = QtGui.QVBoxLayout()
        self.custom_colors_layout.setObjectName("custom_colors_layout")
        self.verticalLayout_3.addLayout(self.custom_colors_layout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.option_description = QtGui.QLabel(self.centralwidget)
        self.option_description.setMinimumSize(QtCore.QSize(0, 32))
        self.option_description.setText("")
        self.option_description.setWordWrap(True)
        self.option_description.setObjectName("option_description")
        self.verticalLayout.addWidget(self.option_description)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.permalink = QtGui.QLineEdit(self.centralwidget)
        self.permalink.setObjectName("permalink")
        self.horizontalLayout_4.addWidget(self.permalink)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.update_checker_label = QtGui.QLabel(self.centralwidget)
        self.update_checker_label.setOpenExternalLinks(True)
        self.update_checker_label.setObjectName("update_checker_label")
        self.verticalLayout.addWidget(self.update_checker_label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.about_button = QtGui.QPushButton(self.centralwidget)
        self.about_button.setObjectName("about_button")
        self.horizontalLayout.addWidget(self.about_button)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.reset_settings_to_default = QtGui.QPushButton(self.centralwidget)
        self.reset_settings_to_default.setMinimumSize(QtCore.QSize(180, 0))
        self.reset_settings_to_default.setObjectName("reset_settings_to_default")
        self.horizontalLayout.addWidget(self.reset_settings_to_default)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.randomize_button = QtGui.QPushButton(self.centralwidget)
        self.randomize_button.setObjectName("randomize_button")
        self.horizontalLayout.addWidget(self.randomize_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.clean_iso_path, self.clean_iso_path_browse_button)
        MainWindow.setTabOrder(self.clean_iso_path_browse_button, self.output_folder)
        MainWindow.setTabOrder(self.output_folder, self.output_folder_browse_button)
        MainWindow.setTabOrder(self.output_folder_browse_button, self.seed)
        MainWindow.setTabOrder(self.seed, self.generate_seed_button)
        MainWindow.setTabOrder(self.generate_seed_button, self.progression_dungeons)
        MainWindow.setTabOrder(self.progression_dungeons, self.progression_great_fairies)
        MainWindow.setTabOrder(self.progression_great_fairies, self.progression_puzzle_secret_caves)
        MainWindow.setTabOrder(self.progression_puzzle_secret_caves, self.progression_combat_secret_caves)
        MainWindow.setTabOrder(self.progression_combat_secret_caves, self.progression_short_sidequests)
        MainWindow.setTabOrder(self.progression_short_sidequests, self.progression_long_sidequests)
        MainWindow.setTabOrder(self.progression_long_sidequests, self.progression_spoils_trading)
        MainWindow.setTabOrder(self.progression_spoils_trading, self.progression_minigames)
        MainWindow.setTabOrder(self.progression_minigames, self.progression_free_gifts)
        MainWindow.setTabOrder(self.progression_free_gifts, self.progression_mail)
        MainWindow.setTabOrder(self.progression_mail, self.progression_platforms_rafts)
        MainWindow.setTabOrder(self.progression_platforms_rafts, self.progression_submarines)
        MainWindow.setTabOrder(self.progression_submarines, self.progression_eye_reef_chests)
        MainWindow.setTabOrder(self.progression_eye_reef_chests, self.progression_big_octos_gunboats)
        MainWindow.setTabOrder(self.progression_big_octos_gunboats, self.progression_triforce_charts)
        MainWindow.setTabOrder(self.progression_triforce_charts, self.progression_treasure_charts)
        MainWindow.setTabOrder(self.progression_treasure_charts, self.progression_expensive_purchases)
        MainWindow.setTabOrder(self.progression_expensive_purchases, self.progression_misc)
        MainWindow.setTabOrder(self.progression_misc, self.keylunacy)
        MainWindow.setTabOrder(self.keylunacy, self.randomize_dungeon_entrances)
        MainWindow.setTabOrder(self.randomize_dungeon_entrances, self.randomize_charts)
        MainWindow.setTabOrder(self.randomize_charts, self.randomize_starting_island)
        MainWindow.setTabOrder(self.randomize_starting_island, self.swift_sail)
        MainWindow.setTabOrder(self.swift_sail, self.instant_text_boxes)
        MainWindow.setTabOrder(self.instant_text_boxes, self.reveal_full_sea_chart)
        MainWindow.setTabOrder(self.reveal_full_sea_chart, self.num_starting_triforce_shards)
        MainWindow.setTabOrder(self.num_starting_triforce_shards, self.add_shortcut_warps_between_dungeons)
        MainWindow.setTabOrder(self.add_shortcut_warps_between_dungeons, self.permalink)
        MainWindow.setTabOrder(self.permalink, self.about_button)
        MainWindow.setTabOrder(self.about_button, self.reset_settings_to_default)
        MainWindow.setTabOrder(self.reset_settings_to_default, self.randomize_button)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Wind Waker Randomizer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Clean WW ISO", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Output Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Seed (optional)", None, QtGui.QApplication.UnicodeUTF8))
        self.clean_iso_path_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.output_folder_browse_button.setText(QtGui.QApplication.translate("MainWindow", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.generate_seed_button.setText(QtGui.QApplication.translate("MainWindow", "New seed", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Where Should Progress Items Appear?", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_misc.setText(QtGui.QApplication.translate("MainWindow", "Miscellaneous", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_short_sidequests.setText(QtGui.QApplication.translate("MainWindow", "Short Sidequests", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_platforms_rafts.setText(QtGui.QApplication.translate("MainWindow", "Lookout Platforms and Rafts", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_big_octos_gunboats.setText(QtGui.QApplication.translate("MainWindow", "Big Octos and Gunboats", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_submarines.setText(QtGui.QApplication.translate("MainWindow", "Submarines", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_dungeons.setText(QtGui.QApplication.translate("MainWindow", "Dungeons", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_expensive_purchases.setText(QtGui.QApplication.translate("MainWindow", "Expensive Purchases", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_eye_reef_chests.setText(QtGui.QApplication.translate("MainWindow", "Eye Reef Chests", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_spoils_trading.setText(QtGui.QApplication.translate("MainWindow", "Spoils Trading", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_minigames.setText(QtGui.QApplication.translate("MainWindow", "Minigames", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_long_sidequests.setText(QtGui.QApplication.translate("MainWindow", "Long Sidequests", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_puzzle_secret_caves.setText(QtGui.QApplication.translate("MainWindow", "Puzzle Secret Caves", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_great_fairies.setText(QtGui.QApplication.translate("MainWindow", "Great Fairies", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_combat_secret_caves.setText(QtGui.QApplication.translate("MainWindow", "Combat Secret Caves", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_triforce_charts.setText(QtGui.QApplication.translate("MainWindow", "Sunken Treasure (From Triforce Charts)", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_treasure_charts.setText(QtGui.QApplication.translate("MainWindow", "Sunken Treasure (From Treasure Charts)", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_free_gifts.setText(QtGui.QApplication.translate("MainWindow", "Free Gifts", None, QtGui.QApplication.UnicodeUTF8))
        self.progression_mail.setText(QtGui.QApplication.translate("MainWindow", "Mail", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Additional Randomization Options", None, QtGui.QApplication.UnicodeUTF8))
        self.keylunacy.setText(QtGui.QApplication.translate("MainWindow", "Key-Lunacy", None, QtGui.QApplication.UnicodeUTF8))
        self.randomize_starting_island.setText(QtGui.QApplication.translate("MainWindow", "Randomize Starting Island", None, QtGui.QApplication.UnicodeUTF8))
        self.randomize_dungeon_entrances.setText(QtGui.QApplication.translate("MainWindow", "Randomize Dungeon Entrances", None, QtGui.QApplication.UnicodeUTF8))
        self.randomize_charts.setText(QtGui.QApplication.translate("MainWindow", "Randomize Charts", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Convenience Tweaks", None, QtGui.QApplication.UnicodeUTF8))
        self.reveal_full_sea_chart.setText(QtGui.QApplication.translate("MainWindow", "Reveal Full Sea Chart", None, QtGui.QApplication.UnicodeUTF8))
        self.swift_sail.setText(QtGui.QApplication.translate("MainWindow", "Swift Sail", None, QtGui.QApplication.UnicodeUTF8))
        self.instant_text_boxes.setText(QtGui.QApplication.translate("MainWindow", "Instant Text Boxes", None, QtGui.QApplication.UnicodeUTF8))
        self.add_shortcut_warps_between_dungeons.setText(QtGui.QApplication.translate("MainWindow", "Add Shortcut Warps Between Dungeons", None, QtGui.QApplication.UnicodeUTF8))
        self.label_for_num_starting_triforce_shards.setText(QtGui.QApplication.translate("MainWindow", "Triforce Shards to Start With:", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(0, QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(1, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(2, QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(3, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(4, QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(5, QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(6, QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(7, QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.num_starting_triforce_shards.setItemText(8, QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Randomizer Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_for_custom_player_model.setText(QtGui.QApplication.translate("MainWindow", "Player Model", None, QtGui.QApplication.UnicodeUTF8))
        self.player_in_casual_clothes.setText(QtGui.QApplication.translate("MainWindow", "Casual Clothes", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Cosmetic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Permalink (copy paste to share your settings):", None, QtGui.QApplication.UnicodeUTF8))
        self.update_checker_label.setText(QtGui.QApplication.translate("MainWindow", "Checking for updates to the randomizer...", None, QtGui.QApplication.UnicodeUTF8))
        self.about_button.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_settings_to_default.setText(QtGui.QApplication.translate("MainWindow", "Reset All Settings to Default", None, QtGui.QApplication.UnicodeUTF8))
        self.randomize_button.setText(QtGui.QApplication.translate("MainWindow", "Randomize", None, QtGui.QApplication.UnicodeUTF8))

