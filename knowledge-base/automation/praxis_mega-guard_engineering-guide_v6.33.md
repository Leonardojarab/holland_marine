# MEGA-GUARD Ship Automation Systems — Engineering Guide

**Document:** PTD_Mega-Guard_Engineering_Guide_Rev6.33  
**Revision:** 6.33 | **Date:** 17-Mar-2023 | **Total Pages:** 284  
**Source:** Praxis Automation Technology B.V.

---

*This document describes the MEGA-GUARD Ship Automation System, covering engineering configuration, installation, and operation of the PAL (Praxis Automation Logic) controller, CAMClient HMI software, alarm management systems, network configuration, and associated modules for marine vessel automation.*

---

> **[Figure]** Title page / cover graphic for the MEGA-GUARD Ship Automation Systems document. Shows the bold text 'MEGA-GUARD' in a grey banner box and below it 'PRODUCT TECHNICAL DESCRIPTION' in large sans-serif font. Background features a faint compass/radar-ring watermark graphic and a red triangular design element in the lower-right corner. Purpose: title/cover image identifying the document series.

MEGA-GUARD Ship Automation System

# 2 ABOUT THIS MANUAL

This manual describes the information to be used for the engineer to set-up a MEGA-GUARD Ship Automation System. This system can be configured according requirements for a specific vessel. These requirements can be configured beforehand during the engineering phase and on board of the vessel using an OWS (Operating Work Station).

The manual is split up in chapters for the configuring different aspects of the system. The chapter “General Channel Setup” describes how I/O points can be configured. Chapter “PAL1131” describes how value processing calculations can be programmed. Chapter “Mimic Setup” describes how user interface via graphical screens (graphical pages or mimics) can be drawn and configured. Chapter “Documentation with DocGen” explains how documentation can be created from the data in the configuration. Finally the chapter “Network Configuration” explains how the different Work Stations can be configured.

# 3 OPERATOR WORK STATION CONFIGURATION

## 3.1 Configuration

An engineer can configure a Mega-Guard Ship Automation System with a pointing device and a normal PC compatible keyboard connected to any Workstation of the system. The system can also be configured "Off-line" on any standard PC running Windows 10 operating system. The Mega-Guard SET-UP information is stored in an MS-ACCESS compatible database and configuration files.

MPC’s are equipped with following disk sizes and disk life span numbers:

Disk (CF) Terabyte before failure Write speed MB/s

## 2 GB 38.4 11

## 4 GB 51.9 11

## 8 GB 69.8 13

## 16 GB 115 15

Disk (SSD) Terabyte before failure Write speed MB/s

## 30GB 312.5 84

## 60GB 312.5 84

## 3.2 Serial port setup (USB to 8 channel NMEA interface)

This paragraph describes COM port layout for Panel PC type 98.6.022.8xx and Marine PC 98.6.001.830.

The serial ports converter USB to 8 channel NMEA interface 98.6.040.804 must be connected to USB port 2 and if a second one is needed this must be connected to USB port 4 as described in following drawings:

> **[Vector Diagram — Page 11]** Page 11 contains a hardware diagram and a reference table for the MEGA-GUARD Marine PC and USB-to-NMEA interface.

Diagram 1: Marine PC Front Panel Hardware Schematic (top). Type: Hardware block/schematic diagram. Shows the front panel of the PANEL PC / ITX-N2900I J1900 W7E-SP1 unit. The panel is depicted as a rectangular enclosure with visible connectors and ports along its front face. A label 'FRONT DISPLAY' points to the display area at the bottom of the panel. The hardware block shows multiple connectors grouped at the top of the unit, consistent with ETH1, ETH2, and USB ports.

Diagram 2: Marine PC 98.6.001.830 Rear/Side Connector Detail. Type: Hardware connector schematic. Shows the Marine PC board layout from the connector side. Ports are labeled from left to right: ETH1, ETH2, USB1~2, USB3~4, 24VDC, FAL, OOS, MCAT, BGPS, PCN. Below the USB groups, two rows of connectors labeled 1, 2 (left group, USB1~2) and 3, 4 (right group, USB3~4) are shown. This corresponds to the 8CH. COM 11-18 and 8CH. COM 19-26 NMEA interface connections.

Diagram 3: USB Port-to-COM Port Mapping Diagram. Type: Connection mapping/wiring diagram. Two groups shown side by side: Left group labeled 'USB1~2' with ports 1 and 2, captioned '8CH. COM 11-18'; Right group labeled 'USB3~4' with ports 3 and 4, captioned '8CH. COM 19-26'. Each USB port connects to 8 serial COM channels via the USB-to-8-channel NMEA interface (part no. 98.6.040.804).

Reference Table: USB Port to Serial COM Mapping. The table maps USB port terminals to serial port designations: USB port 2: Terminals 1A-1B=COM11, 2A-2B=COM12, 3A-3B=COM13, 4A-4B=COM14, 5A-5B=COM15, 6A-6B=COM16, 7A-7B=COM17. USB port 4: Terminals 1A-1B=COM19, 2A-2B=COM20, 3A-3B=COM21, 4A-4B=COM22, 5A-5B=COM23, 6A-6B=COM24, 7A-7B=COM25. This table documents how NMEA serial ports on the Marine PC connect to the USB-to-8-channel NMEA interface module, relevant to MEGA-GUARD OWS/EAS NMEA data acquisition wiring.

Marine PC 98.6.001.830:

> **[Figure]** Hardware diagram showing USB-to-COM port adapter connections. Two USB connectors labeled USB1~2 (left, ports 1 and 2) and USB3~4 (right, ports 3 and 4). Arrow from USB1~2 labeled 8CH. COM 11-18 indicating 8 COM ports (COM11-COM18). Arrow from USB3~4 labeled 8CH. COM 19-26 indicating 8 COM ports (COM19-COM26). Purpose: hardware interface diagram showing how two USB-to-UART adapters (XR21V1414 type) each provide 8 COM ports, giving 16 COM ports total for MEGA-GUARD serial communications.

The NMEA ports on the USB to 8 channel NMEA interface 98.6.040.804 are connected as follows:

| USB port 2 |  | USB port 4 |  |
| --- | --- | --- | --- | |
| Terminals | Serial port | Terminals | Serial port |
| 1A-1B | COM11 | 1A-1B | COM19 |
| 2A-2B | COM12 | 2A-2B | COM20 |
| 3A-3B | COM13 | 3A-3B | COM21 |
| 4A-4B | COM14 | 4A-4B | COM22 |
| 5A-5B | COM15 | 5A-5B | COM23 |
| 6A-6B | COM16 | 6A-6B | COM24 |
| 7A-7B | COM17 | 7A-7B | COM25 |

> **[Figure]** Hardware diagram showing the rear panel interface of a Panel PC model ITX-N29001 J1900 W7E-SP1. The rear connector panel (labeled FRONT DISPLAY with arrow) shows from left to right: ventilation grilles on both sides, a VGA port (DB-15), a serial COM port (DB-9), two RJ45 Ethernet (LAN) ports (ETH1, ETH2), a USB 3.0 port, a USB 2.0 port (HDMI labeled), two USB type ports, and a terminal block connector strip for I/O connections (labeled with multiple terminals including SYS-ON, DVOK, FAL, ITO, MTON, MODE, PWR). This is a technical line drawing showing the hardware interface layout of the MEGA-GUARD Panel PC workstation.

> **[Figure]** Screenshot of Windows Device Manager showing expanded Ports (COM & LPT) tree with 18 XR21V1414 USB UART COM port entries (COM11 through COM26 visible). The hardware listed shows: Communications Port (COM1), Communications Port (COM2), and XR21V1414 USB UART Ch A (COM11), Ch A (COM15), Ch A (COM19), Ch A (COM23), Ch B (COM12), Ch B (COM16), Ch B (COM20), Ch B (COM24), Ch C (COM13), Ch C (COM17), Ch C (COM21), Ch C (COM25), Ch D (COM14), Ch D (COM18), Ch D (COM22), Ch D (COM26). This is a close-up view of just the COM port section of Device Manager showing all USB-UART channels for MEGA-GUARD serial communications.

| 8A-8B | COM18 | 8A-8B | COM26 |
| --- | --- | --- | --- | |

|  |  | If the USB to 8 channel NMEA interface has accidentally been plugged into another |  |
| --- | --- | --- | --- | |
|  |  | USB port then restart the Marine PC or Panel PC while keeping write protection |  |
|  |  | switched on. This will cause the system to reset to factory defaults and assigned |  |
|  |  | COM ports as described in above table. |  |

Serial mouse is disabled on the preconfigured COM ports. When customizing COM ports configuration (re-assigning them to other terminals or using other USB ports) the “Disable Serial Mouse.exe” must be used to prevent the ‘so called’ jumping mouse problem (the mouse moves and clicks on random places caused by Microsoft Windows using the NMEA port as mouse input port.

Usage of “Disable Serial Mouse.exe”:

1. Start “Disable Serial Mouse.exe” from D:\Drivers\USB-NMEA 2. Select changed COM ports or simple use Select All button 3. Press Save to change settings 4. Re-able write filter and restart MPC

In case of usage of 1 USB-NMEA converter the Windows Device Manager displays following COM ports in a correctly configured system:

Device Manager with 1 USB-NMEA: Device Manager with 2 USB-NMEA:

## 3.3 Terminals for Horn Output

To use MarinePC or PanelPC for dimming follow these steps: 1. Connect wires to Horn C and Horn NC terminals (see picture 1 and 2 below) 2. Open Pal, add Analog Input channel (Remote Data, Status) for horn Output 100201. This is a Virtual Channel only available on I/O Server, not on XP. 3. In CamClient press “Ctrl-A” and go to tab page “Clustering/PanelPC”. Set 100201 for “Set Horn Output Channel” (see picture 3 below)

> **[Figure]** Screenshot of Windows Device Manager showing COM port configuration for the MEGA-GUARD server (Server_2). The tree is expanded under Ports (COM & LPT) which is highlighted. Visible entries: Communications Port (COM1), Communications Port (COM2), and multiple XR21V1414 USB UART entries: Ch A (COM11), Ch A (COM15), Ch A (COM19), Ch A (COM23), Ch B (COM12), Ch B (COM16), Ch B (COM20), Ch B (COM24), Ch C (COM13), Ch C (COM17), Ch C (COM21), Ch C (COM25), Ch D (COM14), Ch D (COM18), Ch D (COM22), Ch D (COM26). Other Device Manager categories visible: Computer, Disk drives, Display adapters, Human Interface Devices, IDE ATA/ATAPI controllers, Keyboards, Mice and other pointing devices, Monitors, Network adapters, Other devices, Portable devices, Processors, Sound video and game controllers, System devices, Universal Serial Bus controllers. Purpose: showing USB-to-UART COM port assignments for MEGA-GUARD serial communications hardware.

Picture 1 with step 1:

Picture 2 with step 1:

Picture 3 with step 3:

> **[Figure]** Screenshot of the MEGA-GUARD PAL main configuration tool showing a detailed channel configuration screen. Left tree: Channels with a long list of channel numbers (01000-01041 range visible, 01021 highlighted). Right panel shows channel 10621 / Tag Name: 10221. Description: 1 EYEN / C8M MIF? (partially visible). Type: Analog Input. Sources: Remote Data. Ship: No. 1131 Name field. Process Data section: Eng. Unit Low/High: 170, Eng. Unit Type fields, Disp. Deviat, 5th Conversion: Y=700, X=-0.000, Link Type=No Recalibration Formula. Report: Value, Hi Dev: 0. Retain Value checkbox. Alarm Delay: 0.0 ms. Inhibit: None. Status Texts: On/Off/Cls/StA dropdowns. Final Status: None. Acq Groups: None. Special Value Display Format: None. Purpose: detailed PAL channel configuration for an analog measurement channel with Modbus/remote data source and alarm settings.

## 3.4 Settings for dimming

To use PanelPC for dimming follow these steps: 1. Open PAL; add Analog Input channel 100211 (Remote Data, Status) for “Get Dimming Channel” (This is a Virtual Channel only available on I/O Server, not on XP). 2. Also in PAL; Add Analog Output channel for dimming 100212. Set it to Status and Source from Other Channel 100211. 3. In CamClient press Ctrl-A to set 100211 for “Get Dimming Channel” 4. In CamClient press Ctrl-A to set 100212 for “Set Dimming Channel” 5. Configure PanelPC.ini as in screenshot below

Screenshots and samples for above explanation:

Step 1: Step 2:

> **[Figure]** Screenshot of MEGA-GUARD CAMClient Client Properties dialog, Clustering/Panel PC tab (alternative view). Clustering section: Client Cluster field (empty). Panel PC Configuration section: Set Dimming Channel: 100212, Set Horn Output Channel: 100201. Get Dimming Channel: 100211, Get Horn Output Channel: 0, Get Digital Input 1 Channel: 0, Get Digital Input 2 Channel: 0. Tab row: Joystick Configuration, General Page Permissions, DP Keyboard Configuration, Permissions, Show, Parking, Clustering/Panel PC (active tab label visible as Clustering/Panel PC), Dimming, Miscellaneous. This appears identical to p48_i2 but is a duplicate/same dialog shown in a different context in the documentation.

Step 3, 4: Step 5:

PanelPC.ini

[Settings] OnScreenDisplay=1

UseMegaGuardDim=1 UseVirtualComPort=0 LocalTCPLogging=0 UseInverseDimming=0

## REPORTDIAGNOSTICS=0

[EXT_COMPort] Enable=0

[SERVER_1-Specific] SyncDimmingToGroup=1 SyncLocalDimmingToGroup=0 DimmingGroup=0

> **[Figure]** Screenshot of Windows Control Panel Text Services and Input Languages dialog, General tab, with Russian keyboard highlighted. Installed services: EN English (United States) > Keyboard, RU Russian (Russia) > Keyboard > Russian (highlighted blue/selected), EN English (United Kingdom) > Keyboard. Purpose: Windows keyboard configuration showing the Russian keyboard layout selected within the installed services for MEGA-GUARD server regional settings.

[SERVER_2-Specific] SyncDimmingToGroup=1 SyncLocalDimmingToGroup=0 DimmingGroup=0

[Preset] Day=75 Dusk=50 Dawn=10

## 3.5 Russian Alternate language

For languages with other symbols than the ones available in the default font the Regional settings must be configured. For Russian the Russian keyboard must be selected. This explanation can also be followed for other languages by using that language instead of “Russian”. Follow these steps to do so: 1. Open Windows Control panel, Select “Region & Languages” and select “Keyboards and Languages” tab. 2. Press “Add” and add Russian keyboard. 3. Select font with the required Asian symbols in PAL Jobs & Language branch. 4. Disable and enable (re-able) the C disk write filter and restart Windows. For extra compatibility in displaying Mimics the following setting is required: 1. Open Windows Control panel, Select “Region & Languages”. 2. Select “Administrative” Tab and press “Change System Local” button. 3. Select Russian language In “Region and Language” dialog that appears

> **[Figure]** Screenshot of Windows Control Panel Text Services and Input Languages dialog, General tab. Default input language dropdown: English (United States) - US. Installed services list: EN English (United States) > Keyboard; RU Russian (Russia) > Keyboard (highlighted blue); EN English (United Kingdom) > Keyboard. Add, Remove, Properties, Move Up, Move Down buttons. OK, Cancel, Apply buttons. Purpose: showing Windows keyboard/language configuration for a MEGA-GUARD server with English (US), Russian, and English (UK) keyboard layouts installed.

## 3.6 Asian Alternate language

For Asian Alternative Language a Compact Flash card (with Asian languages included) is required. The PanelPC has this standard. Before being able to enter text with Asian symbols these two steps are required: 1. Select Asian keyboard in Windows Control panel, Region & Languages. (do not forget to re- able the C disk write filter). 2. Select font with the required Asian symbols in PAL Jobs & Language branch (such as SimSung for Chinese).

## 3.7 Alternate language

For languages with other symbols than the ones available in the default font the Regional settings keyboard for that particular language must be configured. Please check previous paragraph with Russian example how to do this. This is possible for any language that is available in the Windows Installation.

> **[Figure]** Screenshot of Windows Control Panel Region and Language dialog, Administrative tab. Sections: Welcome screen and new user accounts - Copy settings button with description. Language for non-Unicode programs section: description text about system locale; Current language for non-Unicode programs: Russian (Russia). Change system locale button. What is system locale link. OK, Cancel, Apply buttons. Purpose: Windows system locale configuration showing Russian as the non-Unicode language, relevant to MEGA-GUARD server setup requirements for language compatibility.

## 3.8 Basic network layout

Mega-Guard System peripherals consist of Operator Work Stations (OWS) that are connected to Control Processors (XP) via Ethernet. The Control Processors are connected to I/O Modules via CanBus. The hardware input and output points are connected to the I/O Modules.

**Figure 1: System Schematic Overview**

> **[Figure — Vector Diagram]** Block diagram showing the MEGA-GUARD system network topology. At the top are up to 24 Operator Work Stations (WS 1, WS 2, ... WS n) connected via Ethernet to two redundant RSTP SWITCH units (Rapid Spanning Tree Protocol switches that make the Ethernet network redundant). Below the switches are up to 99 Control Processors (XP 01, XP 02, ... XP n), each connected downward to a chain of up to 8 I/O Modules (IOM) via CAN bus. At the bottom, up to 25 Local Operator Panels (LOP 01, LOP 02, ... LOP n) are also connected via Ethernet to the work stations. The diagram illustrates the hierarchical, redundant Ethernet loop architecture: OWS ↔ RSTP switches ↔ XP processors ↔ IOMs, with LOPs as additional Ethernet nodes.

*(Figure 1: System Schematic Overview)*

Local Operator Panels (LOP) of the EAS are also connected to the Work Stations via Ethernet. Rapid Spanning Tree Protocol (RSTP) switches are used to make Ethernet redundant. Each XP is connected to the other via a chain of Ethernet cables that form a loop. RSTP is used to find the best route for the information to be transferred to the server which is running on an OWS.

Channel value and status exchange between the processors is transmitted using Multicast UDP messages 10 times per second for up to 112 channels. When using more than 112 channels to be send to other processor the transmission rate will be lower. For example, when up to 224 channels are used the transmission rate will be 5 times per second. This method makes data rate on the network equal at all times.

## 3.9 Windows File Sharing Security

The folder shares that are available for other PC’s to connect to is secured using name and passwords: Read only usage: User name: readonly Password: 0 Full Read/Write usage: User name: readwrite Password: 5255 The MPC Administrator user also has password 5255. These Administrator account is already created. To create the readonly account please follow these steps:

• Go to: Start – Administrative Tools – System Tools – Local Users and Groups • Click on the ‘Users’ folder

• Right click somewhere in the right part of the screen. (drop-down menu will show) • Fill in a user name and password and set the checkboxes “User cannot change password” and “Password never changes”.

See also these screen shots:

## 3.10 Windows XP and Windows 7 connection

To allow to connect to Windows XP and Windows 7 several settings must be changed. These are the steps to change them: 1. Go to 'Control Panel\Network and Internet\Network and Sharing Center' 2. click 'Change advanced sharing settings' 3. Check these settings: ▪ Network Discovery: Turn on (Is default setup) ▪ File and printer sharing: Turn on (Is default setup) ▪ Public folder sharing: Turn on (Is default setup) ▪ Media sharing: Leave as default setup. 4. Correct these settings (Not default setup): ▪ Password protected sharing: Turn off password protected sharing ▪ HomeGroup connections: Set to “Use user accounts and passwords to connect to other computers”

> **[Figure]** Screenshot of Windows New User dialog. Fields: User name: readonly; Full name (empty); Description (empty); Password: bullet (hidden); Confirm password: bullet (hidden). Checkboxes: User must change password at next logon (unchecked, greyed); User cannot change password (checked); Password never expires (checked); Account is disabled (unchecked). Create and Close buttons. Purpose: creating a Windows user account named readonly with a non-expiring password for MEGA-GUARD server access.

> **[Figure]** Screenshot of Windows Computer Management showing Local Users and Groups section. Left tree: System Tools > Local Users and Groups > Users (selected). Right panel shows user list: Administrator (Built-in account for administering...), axonpostgres, axonpostgres (greyed), Bart Long, Guest (Built-in account for guest access t...), HomeGroup... HomeGroupUser$ (Built-in account for homegroupacc...). Right-click context menu visible with options: New User, Refresh, Export List, View (submenu arrow), Arrange Icons (submenu arrow), Line up Icons, Help. Purpose: Windows user account management showing the MEGA-GUARD server user accounts configuration.

For step 4, also see these screen prints:

## 3.11 Network Security

To be compliant with rules MEGA-GUARD network may not be connected to other network unless checked per case. To exchange data with PLC’s or third party devices a network connection must be isolated on network level. The connected network may not use redundancy because this may conflict with the MEGA-GUARD redundancy. The connected network may not be linked to other networks such as internet.

> **[Figure]** Screenshot of a Windows OS network sharing settings dialog (Password Protected Sharing and HomeGroup connections). Shows two radio-button options under 'Password protected sharing' (Turn on / Turn off) and a HomeGroup connections section with options to allow Windows to manage connections or use user accounts and passwords. Highlighted in red borders suggesting these settings are relevant to MEGA-GUARD network configuration requirements.

## 3.12 Connect to Mega-Guard using Ship view

Ship View allows access from other network into the MEGA-GUARD system. This can be the local ship network including Wifi, but it can also be used via internet. It gives the user a variety of options. Here is a list of a few common applications:

• Maintenance usage: Monitoring the vessels performance statistics. • Service usage: Change software, configuration and settings • Retrieval of log files. (Monitor fuel usage etc.) • Fleet management. • Remote troubleshooting by on-shore engineers (saves service trips)

> **[Figure]** System architecture diagram showing remote monitoring connectivity for the MEGA-GUARD system. Three zones are labeled: 'Customer Office' (left), 'Vessel' (center), and 'Praxis or Customer' (right). The vessel zone shows a ship with 'Ship View MPC' hardware connected via Internet (cloud symbol) and satellite links. Customer Office has a 'Ship Owner PC or Tablet'. The right zone shows 'Ship Cloud Server' rack. The diagram illustrates the Internet Ship View remote access topology for ship automation monitoring.

Ship View system can be applied with MEGA-GUARD products such as an AMCS (Alarm Monitoring and Control System). The Ship View system adds functionality to view system information on external computers, tablets, and mobile phones. The two main usages of Ship View are viewing a computer remotely (on-shore office or engineers) and exchange logging data (CSV files).

Check the Manual “PTD_Mega-Guard_Ship_View_R###” for detailed information of setup and usage.

## 3.13 Group Settings for Client / Workstation

### 3.13.1 Open Choose Groups dialog

To change Group settings the login with password is required. To open the dialog press Ctrl G:

### 3.13.2 Choose Groups dialog to change Group Access

With the Choose Groups dialog it is possible to show alarms from specific groups. The alarms from the other groups are not visible on this client station.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient 'Choose Groups' configuration dialog. Left panel lists available alarm groups (numbered 000-024) including: Default-All Groups, AMS DIAGNOSTICS, HCU DIAGNOSTICS, CONTROLLER-COMMISSIONING, TRANSITIONS-COMMISSIONING, STATIC CONVERTER, TANK, AES1, AES2, AMS DIAGNOSTICS 2, ME PS, ME SB, AQM PS, AQM SB, LIGHTS, BATTERIES, BRIDGE EQUIPMENT, CLIMATE, FIR, HCU, PROPULSION GENERATOR 440V, PUMPS, VENTILATION, MISCELLANEOUS, ELECTRICAL. Right panel shows assigned positions with columns for Pos, Group, Title, Demand, Show Alarms, Ack, Horn. Purpose: configuring which alarm groups are shown and how they are handled in the client display.

To enable usage of a group on a specific workstation select the group at the left and press > (right) button to place it in the list at the right. The group will appear at the position that was selected beforehand (so first select an empty spot in the right list). To remove a group select it at the right list and press the < (left) button.

Logging groups via the “demand log” option can be enabled or disabled by selecting the group in the right list and changing the setting at the center. If the setting is “No” the user will not be able to switch on Demand logging. If the setting is “Yes” the user can select Demand Logging via the Group page and channels in that group will be written to the demand log file and to the demand log printer.

Alarms of each group will always be displayed if “Show Alarms” settings at the center of the dialog is set to “Both”. Else it will depend this setting and on the status of the system.

In unattended status alarms in groups with the “Unattended” setting will be displayed. In attended status alarms in groups with the “Attended” setting will be displayed. Via Channel option it is also possible to show the alarms of a specific group depending of the status of a digital channel.

To allow acknowledgement also the above 3 options are possible: 1. Always allow acknowledgement of alarms of this group with “Both” setting 2. Allow acknowledgment of alarms of this group with “Attended” setting in attended status. 3. Allow acknowledgment of alarms of this group with “Unattended” setting in unattended status.

## 3.14 Client Properties

The Ctrl A dialog is available to configure settings for one particular workstation. In the Ctrl A dialog several Tab pages are available, through which many options can be configured. In this chapter each tab will be discussed.

The settings from the Ctrl-A dialog are stored in the clientconfig.mdb database and in configuration files. When Ctrl A (Client configuration) is pressed the following appears on the screen:

After entering a correct name and password a dialog with tab pages appears which are discussed here.

### 3.14.1 Permissions

The permissions tab enables or disables different functionality such as the possibility to reset the General engineer’s alarm, or the possibility to acknowledge an alarm.

With the option "Reset Unattended State with Acknowledge" it is possible to switch to attended state when an alarm is acknowledged. With the option "Accept unattended selection" it is possible to enable this workstation to allow the ECR / ER to go unattended. This option is explained in paragraph 5.14.3.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient 'Client Properties' dialog, Permissions tab. Shows checkboxes for client permissions including: Reset General Engineers Alarm, Reset Unattended State with Acknowledge, Reset Unattended State with Stop Horn, Stop Global Horn 1 (EAS), Stop Global Horn 2, Switch Attended/Unattended state, Acknowledge (with Lock Channel field), Password for Acknowledge with Password Valid Time, Disable Mouse Menu for Acknowledge, Disable Left Mouse click for Acknowledge, Start Editor/Configuration tool (with Lock Channel), Start PAL-Configuration tool (with Lock Channel), Start PAL on Primary Screen, Accept Unattended Selection, Use Pick Actions with single Click, Use Touchscreen. Bottom section 'Call/Select Engineers EAS Page' with Allow Selection, Allow Call, Allow Control, Function and Level dropdowns. Purpose: setting operator access rights in the MEGA-GUARD alarm management client.

|  | [INFO] |  |  | Pressing Acknowledge will not put the system in attended state if no alarm is present. |  |
| --- | --- | --- | --- | --- | --- | |

Stopping the Global Horn 1 will also stop the buzzers on the LOP.

### 3.14.2 Show

The tab page "Show" enables or disables visible options on the client / workstation.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient 'Client Properties' dialog, Show tab. Sections include General (Channel Tooltips, Download status window, Windows Screen Saver, Enable Alarm Popup Message), display options (Display TagName / ChannelNr / TagName and ChannelNr), Group/Mimic page settings (seconds to remember a page, Use/Reset button timeout, Allow Use of Button(s) with full-screen mimics, Enhance Mimic View, Allowed to Enhance to None in Pixels), EAS Mimic File Name extension, Carousel (Refresh time between two mimics in carousel mode), Alarm Page settings (Enable Alarm Page, Enable Alarm Page Based on Report Type, Default Alarm Page options, Lines Alarm Page for Emergency/Alarm/Warning/Caution, Bottom Lines/Nr of Last Alarm Lines). Purpose: configuring the visual presentation behavior of the alarm management client.

With channel tooltip checked a small window will appear when the mouse cursor points at an alarm. In this window the channel number is visible. The Download status window pops up at the left bottom of the screen whenever a download is done. The number of seconds to remember a page sets the time that is between two clicks on the group or mimic buttons, and decides whether the first page or the next page is shown. The first time the button is pressed, the first page is shown. If the button is pressed again within the time limit, the second page is shown.

### 3.14.3 Printing

With the printing tab it is possible to enable printing from a client workstation.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient Client Properties dialog, Printing tab. Tab row shows: Joystick Configuration, General Page Permissions, DP Keyboard Configuration, Permissions, Show, Printing (active), Clustering, Dimming, Miscellaneous. Page Print Settings section: Use printing on this client (checkbox, checked), Print background (Applies for mimics only) (greyed), Use color of new Alarm line (greyed), Use bold of new Alarm line (greyed), with a Color button. Demand Log Settings section: Use demand log on this client (unchecked), Use Printer dropdown (greyed). Clear Printer Buffer Settings (Applies for WinPrint only) section: Use clear alarm printer buffer on this client (unchecked), Use Printer dropdown (greyed). OK and Cancel buttons at bottom. Purpose: configuring print behavior for the CAMClient alarm management workstation.

### 3.14.4 Clustering

In the clustering tab page the client can be joined in a cluster.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient 'Client Properties' dialog, Clustering tab. Shows a single field 'Client Cluster' with the value 'Bridge'. This tab controls which cluster group a client workstation belongs to, used for coordinating alarm acknowledgement and attended/unattended state across multiple bridge workstations.

A cluster is a group of client workstations, LOP (Local Operator Panels) that will stop their horns when stop horn on one of them is pressed.

### 3.14.5 Dimming

In the dimming tab page several settings can be changed to alter the dimming state to your own preferences.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient 'Client Properties' dialog, Dimming tab. Shows Brightness controls with sliders/spinboxes for Red, Green, Blue values across lighting modes: Day, Twilight, Dusk, Night, Dusk Inv., Night Inv. Backlight Sound (On/Off) and Backlight Off checkboxes per mode. Colors section with 'Change system colors' and 'Use alternate color scheme' checkboxes. Reset to Default button, 'Change Dimming on Other Client' and 'Use Mimic Color Table Dimming' checkboxes. Dimming Channel field: 1809. Purpose: configuring display brightness and color settings for different bridge lighting conditions.

By default all colours are dimmed equally. “Change system colors” makes the system also change the Windows colors. For example the grey menus will become darker grey when the system is dimmed. If this option is turned off (unchecked) it will not change the Windows colors, which means that parts of the Client are not dimmed. Another application should dim these colors instead (for bridge integration with other applications). “Use Default Color Schema” can be switched of to use an alternate color scheme. This alternate scheme has an extra dimming option (“Night inverted”).

| [INFO] |  | To switch back to daylight dimming (no dimming) double click on the logo at the right |  |
| --- | --- | --- | --- | |
|  |  | top. To do this the tracker ball can be rolled up and to the right. This can be done even |  |
|  |  | when the display had been dimmed to a level where it became unreadable. |  |

### 3.14.6 Miscellaneous

In the miscellaneous tab the time synchronization with the server can be set-up. If the option is checked the client workstation will have the same time as the server has. In this way time differences between the systems can be ruled out.

> **[Figure]** Screenshot of MEGA-GUARD Configure Icon dialog. Fields: Application: osk.exe (Browse button); Dialog Title: On-Screen Keyboard; Icon File: Icons\osk.ico. Set Defaults For section: two buttons RedNetwork and On-Screen Keyboard (highlighted/active). OK and Cancel buttons. Purpose: configuring a custom icon button in MEGA-GUARD CAMClient that launches the Windows On-Screen Keyboard (osk.exe), used for touchscreen operator workstations.

The local horn sound can be adjusted by selecting a file with the preferred melody. The "Use Operator Keyboard" option is switched on when using an operator keyboard.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient Client Properties dialog, Miscellaneous tab. Tab row: Joystick Configuration, General Page Permissions, DP Keyboard Configuration, Permissions, Show, Parking, Clustering, Dimming, Miscellaneous (active). Time synchronization section: Sync Time with server (checked), Update time of zone on startup (checked), Sync Timezone with server (checked), dropdown for time format. Local Horn section: Play reveille (Play button). Specials section: Quit client allowed (checked, About button), Use Free Configurable Icon Button (Configure Icon button), Use Password On Time Configurable Icon (unchecked), Use Key Assignment Always (unchecked), Change System Menu Font when All Language Active (unchecked). System Shutdown: System Shutdown Channel: 0. Use Interstation: CAMClient Application Number: 1, CAMClient Application Title field. Activate Mimic via Channel: Turn On Status Digital Channel: 0, Mimic Number Analog Channel: 0. Minimum accepted time before next update in ms: 15000. Get CPU Temperature: Avg by Channel. OK button. Purpose: configuring miscellaneous client behavior settings for a MEGA-GUARD CAMClient workstation.

Add on-screen keyboard (OSK) by selection “User Free Configurable Icon Button”. Press Configure Icon button next to it. Press “On- Screen Keyboard” button in the “Set Defaults For” area. Press OK to close each dialog.

In the miscellaneous tab the time synchronization with the server can be set-up. If the option is checked the client workstation will have the same time as the server has. In this way time differences between the systems can be ruled out.

Update time zone on start-up is required for the CF (Compact Flash) MPC. This MPC does not store the time zone changes in registry, and by enabling this option the software will store this instead.

When time zone update is enabled it is important to know if the system starts up with Daylight time saving or Standard. Set “Start TimeZ. ID” to Daylight Time when the system has Summer time, and set it to Standard when the System starts in Winter time. If this option is set wrong, it will cause the system to change the time by 1 hour each time it starts up.

| [INFO] |  | Conclusive: |  |
| --- | --- | --- | --- | |
|  |  | Winter: Setup “Start TimeZ ID” to “Standard time” |  |
|  |  | Summer: Setup “Start TimeZ ID” to “Daylight time” |  |

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient Configuration of Functions for a Top Button dialog. Fields: Top Button Number (empty text field). Function dropdown showing expanded list of options: None (currently selected), Group Page, Mimic Page, Group Overview Page, Mimic Overview Page, Alarm Page, Channel Page, Skip Page, Inhibitor Page, Active Inhibitor Page, Diagnostic Page, Macro. Right side table with columns Nr and Function, showing row 1 with entry 00. Add and Delete buttons at top. Navigation arrows (up/down) at left side of table. OK and Cancel buttons. Purpose: configuring what function is triggered by a specific top button (programmable hardware button) on the MEGA-GUARD operator panel.

## 3.15 Button configuration

The top buttons can be configured with the Ctrl-B key on the QWERTY keyboard.

> **[Figure]** Screenshot of MEGA-GUARD CAMClient Configure Buttons dialog. Two-column layout with 12 button entries. Left column (Name/value pairs): Row 1: Name=Overview AMS, Knope1; Row 2: Name=PMS, Knope2; Rows 3-6: Name=(empty), Knope3-Knope6. Right column: Rows 7-13: Name=(empty), Knope8-Knope13. Each row has a Config button. OK and Cancel buttons at bottom. Purpose: configuring the labeled function buttons on a MEGA-GUARD operator panel, mapping button names (like Overview AMS and PMS) to hardware knop/button positions.

The text on the button can be altered to show the meaning of the assigned functionality. After pressing the Config button the following dialog will appear:

In this dialog several options can be assigned to the button. Pressing the top button more than once, or using Page down will start the next function in the list.

## 3.16 Mimic configuration

To enable if a mimic will be shown on this workstation the following dialog is available.

To get this dialog Ctrl-M is pressed. The mimics on the left side are all the graphics available on the system. The mimics at the right side are the mimics that can be shown on the client workstation. Per mimic it is possible to "Allow Control" or not. If control is allowed objects on the mimic can be selected so the status of that object can be changed. For instance a valve can be opened or closed.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient 'Choose Mimics' configuration dialog. Left panel lists available mimic pages (001-021) including: Virtual Channel Trending, Alarms, XYPlot Test, Moving Objects, Button Test, Move Test, BarGraph Test, Slider Test, CAPABILITY PLOT, TRACKING, DIAGRAM, MAP, Memory Trend Test, IMTECH 0000 MAIN MENU, IMTECH 4210 BILGE SYSTEM, AUXILIARY ENGINE, Big Trend, BMS Trending, Cargo Bargraph, Conning 01, CONNING. Right panel shows assigned positions with Pos, Title, Ctrl, Le, Channel columns. Navigation arrows in center. Purpose: configuring which graphical pages/mimics are accessible in the CAMClient.

## 3.17 Key assignment

Key assignment (key macros) can be added or changes with the key assignment dialog.

From the moment a key assignment is made the client workstation will carry out the task assigned to that key. To assign a key the following must be done: 1. Select the correct 'Class' at left top of the dialog. 2. Select the desired function in the list box at the left. 3. Press the desired key edit box in middle, at the top of the dialog. 4. Press the assign button. Depending on the function extra parameter input will be asked here. 5. Press OK.

> **[Figure]** Screenshot of the MEGA-GUARD CAMClient 'Key Assignment' dialog. Fields: Class (System), Function list (Operator Action, Switch Application, System Information - 'Operator Action' selected), Press key field (S), Parameter section (Action dropdown, NONE dropdown), Assign/Remove buttons. Key Assignments list shows 'S - System Information' and 'W - Key Assign Dialog'. Status bar: 'CAMClient buttons functions are assigned'. Purpose: assigning keyboard shortcuts to operator actions in the alarm management client.

From this moment on "S" will make the System Information dialog appear (Ctrl-S) will also still work.

[INFO] If keys that are used in the client workstation are used in the key assignment dialog, then the assigned functionality will be executed, and the default functionality will not be executed. For example: if Ctrl-B is assigned to switch to another application, the Button assignment dialog will not appear anymore.

## 3.18 System startup up splash screen

During startup of the system CamClient will display the company logo by default. It is possible to modify this by placing a bitmap file named “Splash.bmp” in the Logo folder. The file must be 800 pixels wide and 357 pixels height. The bottom 62 pixels of this bitmap will be used to show startup progress. For this reason only the top 295 pixels can be used to display a picture.

# 4 PAL CHANNEL SETUP

Several set-up levels are available (refer to paragraph 7.4 Level system security, page 156) each with their own password. The engineer set-up level is level 0. By entering the appropriate username and password, the set-up is entered with the corresponding level. When F12 (SET-UP) is pressed the following appears on the screen:

If the User Name and Password is correct the system will show the User Name and privilege level on the Status Bar on the bottom of the screen. Example below indicates the reaction of the system when a wrong password is supplied. After 3 seconds the system will display the default page (usually ALARM PAGE). The SET-UP key must be pressed anew:

> **[Figure]** Screenshot of MEGA-GUARD CAMClient Login dialog. Fields: User Name (empty text field), Password (empty text field). Buttons: Accept, Cancel. Title: Login. Purpose: MEGA-GUARD CAMClient operator login dialog for authentication before accessing the alarm management system.

The default username is an empty string and the default password is '0' for the engineer level (level'0'). In this document the engineer level (level '0') is described. You can enter set-up when the correct password is entered (default '0'). The system will clear the screen and the following is displayed (operator levels allow restricted set-up): When the SET-UP program is closed the system will return to the default page (usually ALARM PAGE). In case of bad input the system will show an error message.

## 4.1 General Setup Information

In the next image the PAL is displayed:

The following general rules apply to such a configuration page. The easiest way to maneuver between the different items and fields on the screen is by using a pointing device like a Trackball or a mouse, however setup can be performed by using the following keys on a QWERTY keyboard.

> **[Figure]** Screenshot of the PAL [Main Server] - Programmers Application Language 6.0.0.1 main window. Left panel shows a tree view with top-level folders: Channels, Extended Alarm System, Graphics Pages, Groups, Hour Counters, Job and Language, Passwords, Printers, Remote Data, Special, Status Texts, System Parameters. Right panel is empty/grey. Menu bar: File, Edit, View, Special, Help. Status bar: 'For Help, press F1'. Purpose: shows the PAL software configuration tool main interface used for MEGA-GUARD system engineering.

|  | [INFO] |  |  | Setup can only be performed by the use of an QWERTY keyboard |  |
| --- | --- | --- | --- | --- | --- | |

The items: • Switching between the Tree Area and the Set-up area can be done by sing the key F6 on the QWERTY keyboard or by a left click on the area with the pointing device. • Selecting pull down menus from the Menubar can be done by pressing the Alt key together with the letter key which is underline in the menu bar. Or by a single left click on the menu item. To move the focus back to either the Tree Area or the Set- up area press the TAB key on the keyboard or left click on the area. • Selecting the items from the Button Toolbar can only be performed with the pointing device, by a left click on the button. Of course all items of the Button Toolbar can also be selected via the pull down menus from the Menubar.

### 4.1.1 The Tree Area

> **[Figure]** Screenshot of the MEGA-GUARD PAL configuration tool showing the Channels tree expanded to reveal a fieldbus Ethernet FB-ETH_FB(IO) processor with Proc-01 containing XP-010(Ctrl Proc) node with sub-folders: Channels, Conversion Tables, and 010-Channel Layout. Below Proc-01 is Proc-02 with a Diagnostics sub-folder. Below the Channels section are: Extended Alarm System with General Settings and Diagnostics sub-folders; Graphics Pages folder containing Pick Actions (highlighted/selected, blue) and 01-Mimic; Groups; Hour Counters; Job and Language; Passwords; Printers with Printer-01 sub-item; Remote Data; Special; Status Texts; System Parameters. Purpose: PAL main configuration tree showing the Graphics Pages Pick Actions section selected for configuring button/shortcut actions in the MEGA-GUARD operator interface.

• In the Tree Area you can select the different maps by using the arrow keys or by a single click from the pointing device. If a map is closed it is shown as follows and if a map has a symbol on the left, it indicates that there are setup items within this map, which are not shown at this moment. If a map is open it is shown in the following way if such a map has a symbol on the left it, the setup items are shown in the tree. • To open the map you can double left click on it with the pointing device or with a single left click on the symbol. If the map has no symbol you can not open this map. Opening a map from the keyboard can be done by pressing the + sign when the map is selected. • To close map you can double left click on the open map symbol or by a single left click on the symbol. Closing a map from the keyboard can be done by pressing the - sign when the map is selected. • Adding setup items to a map (when applicable) can be done by a right click with the

pointing device or by pressing the context menu key on the keyboard when the map is selected. With this action a context menu will appear and you can select insert to add a setup item. • Selecting the item and pressing the Delete key on the keyboard will delete setup items in a map.

### 4.1.2 The SETUP Area

Field

Checkbox Group of fields

• The set-up area is a form with several fields to define the set-up of the system. To go to the next field or group of fields use the 'TAB' key. To go to the previous field with use the 'Shift'+TAB' key. Within a group of fields you can use the arrow keys to go from one field to another field in that group. With 'Enter' you go to the next field and validate (modified) data. • The checkbox can be changed by a single left click with the pointing device or by pressing the SPACE-Bar on the keyboard. • Enter a new value by just typing from the keyboard. • (Use 'Esc' at any time to restore a field to its former value, i.e. the value before selecting the field.) • For each form context sensitive help will be available. • Fields, which can be modified, are shown in white. Fields, which cannot be modified, are grayed out and will be bypassed.

> **[Figure]** Screenshot of the MEGA-GUARD PAL configuration tool showing a Tank Table (conversion table) editor. Name field: Tank Table 1023. Checkbox: Use Engineering Unit for X Values (unchecked). Left table with columns X and Y showing calibration data points: (0.0, 12.5), (22.5, 13.1), (44.0, 21.1), (67.6, 29.4), (112.6, 47.6), (169.0, 75), (225.2, 100.1), (281.6, 128.3), (394.1, 197.4), (500.0, 250.0), (619.3, 316.0), (732.1, 384.7), (844.7, 458.0), (900.9, 432.0), (950.0, 525.0), (1000.0, 550.0). Y-Value low: 12.5, Y-Value high: 546.4. Right side: scatter/line plot showing the calibration curve (red line through the data points) against a grid, showing a nonlinear tank volume curve. Purpose: MEGA-GUARD tank calibration table defining the relationship between sensor value (X) and actual tank volume (Y) for liquid level measurement.

## 4.2 Channel, Table, Numbering

### 4.2.1 Channel Numbering

All channels have a 5 digit number XPBCC: XP = Processor number (1..99) B = I/O Module number (0..8) CC = Channel number (0..99)

E.g.: the 21st I/O channel on module 4 on processor 3 is 03421, the 2nd channel on module 5 on processor 21 is 21502.

When a channel is required as a set-up parameter: • Enter the full 5-digit number for an absolute reference, i.e. the channel may be located on the same or another module. • For channels the automatic assigned tag name can be entered instead of the channel number.

### 4.2.2 Interface with 1131 application code

#### 4.2.2.1 PAL 1131 channel list

To interface with the 1131 code the PAL 1131 channel list must be configured. In this list a channel is connected to an 1131 variable:

> **[Figure]** Screenshot of the PAL [Main Server] configuration tool showing a channel setup screen. Left tree shows Channels > FB-ETH_FB(IO) > XP_001 > XP-010(CtrlProc) > Channels with items 01000-01041. Right panel shows 'General Settings / Miscellaneous Table / Board Diagnostics / Channel Cross Reference List / 1131 Reference List' tabs. Active tab shows: Cycle Timeout (ms): 100, Check Size button, Use Local Channel Numbering checkbox, Start PAL 1131 button. Channel table shows: Row 1: 01001, ANALOG MEASUREMENT, =>, C001, FINT; Row 2: 01000, ID MODULE STATUS, <=, C000, BOOL. Purpose: PAL channel configuration for an XP I/O processor including 1131 variable mapping.

The 1131 Variables can have names according iec61131-3{ed2.0}. These names must start with a character, may contain numbers and underscores ‘_’, but no spaces or other characters. A lowercase name is different then an uppercase name: C001 is not the same as c001. To prevent making mistakes it is advised to always use uppercase.

#### 4.2.2.2 Functions in 1131

Functions are optional. Once the 1131 editor has started formula’s can be entered directly. Small applications can be made this way. Functions can be used to organize larger applications. Functions must be named according iec61131-3{ed2.0}. Re-using functions to other processors can be done in 2 ways: 1. Copy the function from one XP to the next XP. 2. Put the function in a library. For more information about programming in 1131 please check the official IEC 1131 document: iec61131-3{ed2.0}.

### 4.2.3 Table Numbering

All tables have a 2 digit number CC: CC = table number 15th 2nd E.g.: the table on an XP is 15, the table on an XP is 02.

When a table is required as a set-up parameter: • Enter the number for a reference, i.e. the table will be located on the same module where the set-up resides.

## 5 PAL1131 SET-UP

## 5.1 PAL1131 Overview

> **[Figure]** Screenshot of the PAL1131 IDE main window (empty/new project state). Menu bar: File, Edit, View, Project, Tools, Window, Help. Toolbar with standard icons. Left panel has tabs POU, Resources, Types with empty project tree. Right panel is grey/empty. Title: 'PAL1131'. Purpose: shows the PAL1131 IEC 61131-3 programming environment start screen used to develop control logic for MEGA-GUARD I/O processors.

### 5.1.1 Startup menu tools

PAL1131 starts automatically if Launch PAL1131 is selected during installation. Start menu or desktop icon trigger standard startups.

| [INFO] |  | Nonstandard startups with additional parameters can be executed from directory in |  |
| --- | --- | --- | --- | |
|  |  | which PAL1131 is installed. Otherwise error of loading external modules appears. |  |

The startup displays PAL1131 interface window whose left part will present project tree, middle one program code, and bottom part compiler messages.

### 5.1.2 Menu and toolbar

Menu and toolbar functionality are typical for Windows.

File Menu Edit menu

> **[Figure]** Screenshot showing the PAL1131 menu bar toolbar area with labeled buttons. Menu items: File, Edit, View, Project, Tools, Window, Help. Below the toolbar, a visual icon guide shows buttons with their names: New, Open, Save (row 1); Print preview, Help, Find text (row 2); Build, Start simulator, Print (row 3). Purpose: PAL1131 toolbar/menu reference showing available functions for creating and managing IEC 61131-3 programs.

Some of the items remain inactive until a project is open. Print prints project report and source codes (print preview has not been implemented yet.) Copy and Paste, besides standard text operations, handle items from project tree (POU units, global variables, etc.). Find looks for text written in the toolbar cell.

### 5.1.3 View

Press Alt+0 to get quickly to project tree, Alt+1 to program window, and Alt+2 to message list.

### 5.1.4 Project

The option handles final stages of the project. Build compiles open project or its element. Clear removes intermediate files created automatically during compilation, leaving only two necessary (.xml, .xmc; see Supplements). Simulator and hardware configuration can be run after compilation. Item adds, removes, etc. project elements.

> **[Figure]** Screenshot of PAL1131 Project menu expanded with Item submenu visible. Menu bar: File, Edit, View, Project (active), Tools, Window, Help. Project menu items: Build (F6), Rebuild all (greyed), Clean, Run simulator, Item (highlighted, with right-arrow submenu), Export, Import, Tools, Make copy, Options. Item submenu shows: Add, Remove, Rename, Edit (Ctrl+I), Properties, Unlock (Ctrl+E), Lock (Ctrl+D). Purpose: showing the PAL1131 IDE Project menu structure for managing project items in the MEGA-GUARD IEC 61131-3 programming environment.

Export, Import deal with libraries (.lcp) or external files with ST programs (.cst). Tools edit list of global variables, present compilation report, and open project folder in Windows explorer.

> **[Figure]** Screenshot of PAL1131 View menu expanded with Switch focus submenu. Menu bar: File, Edit, View (active), Project, Tools, Window, Help. View menu items: Toolbar (checked), Status Bar (checked), Switch focus (highlighted, with right-arrow submenu). Switch focus submenu: Project tree (Alt+0), Current edit window (Alt+1), Message list (Alt+2). Background shows START_ project tree with POU, Global variables, Tasks, Libraries folders. Purpose: showing the PAL1131 View > Switch focus keyboard shortcuts for navigating between IDE panels.

> **[Figure]** Screenshot of the PAL1131 Configuration dialog, Projects tab. Compiler options section: General settings with Default Virtual Machine specification file field: E:\Program Files\PAL1131\VM\VM-Univ.xml (with browse button), Optimization level: 1 (spinner), Use single task optimization of global variables (checkbox, checked). Default libraries section: Import selected libraries to new projects checkbox (checked). Library list showing: E:\Program Files\PAL1131\Libraries\IEC 61131-3.lcp. Plus (+) and minus (-) buttons to add/remove libraries. Purpose: PAL1131 default project settings including VM specification and default library imports for new IEC 61131-3 projects.

Contents of the last three options look as follows:

Tools Window Help

Tools configure environment, determine global settings, and run compiler, simulator and configurer standalone for working with external files (.cst, .dcp, .dcp or .xmc). Window arranges interface. Help accesses programming instruction, information materials with function, function blocks, and notes For advanced users. It also indicates whether PAL1131 has been updated.

> **[Figure]** Screenshot of PAL1131 Help menu expanded. Menu bar: (partially visible), Help (active). Help menu items: Programming instruction, Information materials (Ctrl+F1), Function index, Check update, About program... Purpose: showing the PAL1131 IDE Help menu options for accessing programming documentation and software update checking.

### 5.1.5 Environment options

Configuration window with a few tabs is displayed:

#### 5.1.5.1 Projects

Path to a file with Virtual Machine specification (runtime) is provided. Use… option must remain selected (default) for single task VM. Optimization level 1 is normal (ev. see For advanced users).

The tab also indicates which libraries should be automatically imported into new projects. Button [+] adds library from Libraries folder. Button [-] removes selected library.

#### 5.1.5.2 Editing

> **[Figure]** Screenshot of the PAL1131 'Configuration' dialog, Editing tab. ST language editor section: Editor default mode with options (Simple single, Single colorable [selected], Simple double, Double colorable). Checkboxes: Fill new items of the project with default templates (checked), Auto synchronization of item names (checked), Automatically unlock window for editing (checked), Synchronize item names after editing (checked). Purpose: PAL1131 editor preference settings for IEC 61131-3 ST language programming.

Single and Double colorable modes show keywords in different colors. Single (default) provides additional autocomplete help to finish names of variables, functions, etc. (Supplements). Auto synchronization… unifies names of the same elements in different parts of the project.

#### 5.1.5.3 Colors

Scheme of editor colors, text attributes, etc., together with example of colored code, is shown below.

> **[Figure]** Screenshot of PAL1131 'Configuration' dialog, Miscellaneous tab. General section: Number of recently opened files: 16 (spinner). Checkboxes: Clear list, Distinguish active project name for POU (checked), Ask before opening stored report (checked), Replace project VM specification file with default VM specification file (unchecked). Show in the tress: Variable type (checked), Physical address (checked), Logical address (checked), Comment (checked), VM physical address (unchecked). Purpose: miscellaneous PAL1131 IDE preferences.

#### 5.1.5.4 Miscellaneous

Size of Recent files list is determined. Bold characters distinguish active project for selected POU. Ask, or not, before opening the stored report in default browser. Replace Virtual Machine specification file by default (from Projects tab). For a global variable the project tree may show type, addresses and comment.

> **[Figure]** Screenshot of the PAL1131 'Configuration' dialog, Colors tab. Left panel: Editor items list (Build-in type, Comment, Delimiter, Directive, Identifier, Constant, Invalid character, Keyword, Operator). Text attributes: Bold, Italic, Underline checkboxes. Force default parameters: Font, Background. Font color / Background color dropdowns with Default/None checkboxes. Right panel: Code preview showing syntax-highlighted ST code (FUNCTION MyFun:INT, VAR_INPUT, IF Y THEN, MyFun:=MyFun+DINT, Y:=Y XOR BOOL#1, END_FUNCTION, VAR_GLOBAL, vg AT %0001:BOOL). Purpose: configuring syntax highlighting colors in the PAL1131 ST code editor.

#### 5.1.5.5 Compiler

Align addresses avoids overlapping of variables. C++ type comments and nested comments may be accepted.

> **[Figure]** Screenshot of 'CPDev package configuration' dialog, Communications tab. Communication settings: Port COM1, Baud rate 9600, Data bits 8, Stop bits 1, Parity None, Flow control None. SMC controller settings: SMC controller number 1. SMC-I/O modules communication settings: SMC-I/O baud rate 115200, SMC-I/O mode 8N1, Time Out (ms) 500, Silent time 500. OK/Cancel buttons. Purpose: configuring the CPDev communication interface for an SMC controller used with MEGA-GUARD I/O hardware.

### 5.1.6 Global settings

They affect two PAL1131 programs, i.e. compiler and simulator. Selection of Global settings (in Tools) opens PAL1131 package configuration window with three tabs.

#### 5.1.6.1 Communications

PC port for communication with the controller is configured according to Communication settings. If the controller is connected via USB, Windows Device manager determines port number. SMC controller settings define controller number for PC and parameters for communication with distributed I/O modules or other field devices. The 8N1 mode denotes 8 data bits, odd parity (N) and 1 stop bit.

> **[Figure]** Screenshot of PAL1131 Configuration dialog, Compiler tab. Compiler options section: Align addresses of global variables to multiply of their sizes (checked), Align addresses of local variables to multiply of their sizes (checked), Append information data for Fenixle debugger (unchecked/greyed), Ignore bad POUs during compilation (checked), Single-line comments // (from C++) permitted in ST code (not in IEC 61131-3) (unchecked), Nested comments permitted in ST code (checked). Additional columns in compilation report section: Show Modbus addresses in SMC (checked), Show InTouch addresses for SMC (checked). Purpose: configuring PAL1131 compiler options affecting address alignment, comment syntax, and compilation report output.

#### 5.1.6.2 User interface

Interface language of PAL1131 package is chosen

> **[Figure]** Screenshot of CPDev package configuration dialog, Update tab. Fields: Update server: http://js.priezszow.pl/cpdew/cpd_ver.php; Update server user: public; Update server password: *****(hidden). Checkbox: Use proxy for internet connection (unchecked). Proxy settings section (greyed): Proxy server address, Proxy user name, Proxy user password (all empty). Purpose: configuring the CPDev software auto-update server connection settings.

#### 5.1.6.3 Update

The tab determines configuration to check whether new version of PAL1131 has appeared on the update server.

> **[Figure]** Screenshot of 'PAL 1131 package configuration' dialog, User interface tab. Application language section: Current language code 0x0409. Available language list: English, English (0x0409); Polish, Polski (0x0415). Application variables table with columns Name/Value: AppDir E:\Program Files\PAL1131, HpDir ...\Help, LibDir ...\Libraries, ExamplesDir ...\Exampl..., CustomTe... ...\Templa..., TechDocDir ...\Doc, VMsDir ...\VM. New value field with Select/Accept buttons. Purpose: PAL1131 language and path configuration.

| [INFO] |  | Passwords of the update and proxy users are not encoded so should be erased after |  |
| --- | --- | --- | --- | |
|  |  | checking the update. |  |

## 5.2 Example New Project – START_STOP

The objective is to turn a motor on and off. Sample control diagrams are shown below.

### 5.2.1 Example Project diagrams

Function block diagram:

> **[Vector Diagram — Page 46]** Page 46 contains a Function Block Diagram (FBD) and a Ladder Diagram (LD) example, plus a variable address table, demonstrating PAL1131 programming for MEGA-GUARD motor control.

Diagram 1: Function Block Diagram (FBD) - Motor Control. Type: FBD in IEC 61131-3 PAL1131. The FBD shows three input variables feeding into standard logic gates driving a MOTOR output. Inputs: START, STOP, ALARM. Logic: OR gate receives START and ALARM; the OR gate output feeds into an AND gate; STOP connects as second input to the AND gate. Output: AND gate drives MOTOR (output variable). Uses standard IEC 61131-3 FBD notation with signal lines connecting function blocks.

Diagram 2: Ladder Diagram (LD) - Motor Control. Type: LD in IEC 61131-3 PAL1131. The LD represents equivalent logic to the FBD. Structure: Left power rail -> normally open contact START -> normally closed contact STOP (bar/negation above STOP symbol) -> normally open contact ALARM -> output coil MOTOR. MOTOR is energized when START is active AND STOP is not active (negated) AND ALARM is not active.

Variable Address Reference Table: Two-column table associating variable names with IEC 61131-3 addresses: START=0000, STOP=0001, ALARM=0002, MOTOR=0008. START, STOP, ALARM are binary input signals (IOM binary input module, addresses 0000-0002). MOTOR is a binary output at address 0008 via IOM binary output module. The adjacent addresses indicate START, STOP, ALARM will be read in one command for efficiency. Text also notes the START_STOP system can be implemented via RS flip-flop with S connected to START and R connected to STOP.

Ladder diagram:

START, STOP and ALARM inputs are acquired by the controller from binary input module. MOTOR output is sent from the controller to binary output module. The following addresses are assigned to variables.

| START | 0000 |
| --- | --- | |
| STOP | 0001 |
| ALARM | 0002 |

| MOTOR | 0008 |
| --- | --- | |

The adjacent three addresses indicate that START, STOP and ALARM will be read in one command or message. All signals correspond directly to hardware, so they will be declared as global variables.

| [INFO] |  | The START_STOP system can also be implemented by means of RS |  |
| --- | --- | --- | --- | |
|  |  | flip–flop, with START connected to S input and STOP plus ALARM to R. |  |

### 5.2.2 Create a project

First open a new folder, e.g. START_STOP, for all files of the project. Steps executed by PAL1131 are then as follows: 1. Create a new file 2. Give name to the project 3. Declare global variables 4. Enter the program 5. Declare task 6. Compile the program 7. Save the source code in XML file 8. Close the project Entering the program may precede declaration of variables. Closing the project saves all files in the project folder including binary code (.xcp) and data file (.dcp) for

> **[Figure]** Logic diagram showing the START_STOP control logic as function block diagram. Three elements connected: OR gate (inputs: START and MOTOR feedback), AND gate (inputs: from OR gate, inverted STOP, inverted ALARM), output labeled MOTOR. The AND gate output goes to MOTOR. Inputs: START (top-left), STOP (bottom-left, with inversion bubble), ALARM (below STOP, with inversion bubble). MOTOR output also feeds back to the OR gate input. Purpose: functional block diagram illustrating the latching start/stop motor control logic implemented in the PAL1131 START_STOP example program.

simulator and configurer.

> **[Figure]** Screenshot of the MEGA-GUARD PAL mimic editor showing color palette and IO Server panel. Left side: Format Fill dropdown (active), Format Text, Corner Rounding buttons; Color section with Select and Reset to Default options; Fill Style options: Flat, Horizontal Lighting, Vertical Lighting, Radial Lighting; small red/white geometric shape visible. Right side: IO Server panel showing Start/Stop buttons; color table with named system colors: Background (black), Foreground (white), Grid (grey), AlarmRed (red), Comment (green), NoAlarmGreen (green), PanelFace (grey), ButtonFill (blue), ButtonOutline (transparent), SelectedTextBackground (blue), MissingColor (grey), InactivePanelFace (grey), OldAlarm (grey), Red, Green, Blue, Yellow, Magenta, Cyan, Gray, and More colors link. Purpose: showing the MEGA-GUARD PAL mimic editor color configuration system with named system color palette.

#### 5.2.2.1 New file

Use menu: File > New (Ctrl+N) or keys Control + N

Alternatively you can select in the toolbar.

#### 5.2.2.2 Project name

The project is given the name START_STOP entered in Project properties window. In Project tree > Select the project (NoName0) Project properties can be opened in four ways: 1) Right Trackball button / Context menu > Properties :

2) In Menu: Project > Options :

3) In Menu: Project > Item > Properties :

> **[Figure]** Screenshot of 'Project properties' dialog in PAL1131. Fields: Project name: START_STOP, File location: E:\Program Files\PAL1131\Examples\Start_Stop.xml, VM specification: E:\Program Files\PAL1131\VM\VM-Univ.xml. Information section: Project version (unchecked), Project manager (unchecked), Company (unchecked), Created (checked): Wednesday October 08 2008 2:35:57 PM, Compiled (checked): Wednesday October 08 2008 2:38:57 PM, Auto-increment (checked): 1. Purpose: project metadata and file path configuration for a PAL1131 example project 'START_STOP'.

4) Keyboard: Alt + Enter

Enter the name and eventually fill other information cells of Project properties (created and compiled are filled automatically). The name must be correct identifier in ST, so without spaces inside or digits at the beginning (see ST language overview).

> **[Figure]** Screenshot of MEGA-GUARD CAMClient Client Properties dialog, Clustering/Panel PC tab. Clustering section: Client Cluster field (empty). Panel PC Configuration section: Set Dimming Channel: 100212, Set Horn Output Channel: 100201. Get Dimming Channel: 100211, Get Horn Output Channel: 0, Get Digital Input 1 Channel: 0, Get Digital Input 2 Channel: 0. Tab row: Joystick Configuration, General Page Permissions, DP Keyboard Configuration, Permissions, Show, Parking (inactive), Clustering/Panel PC (active), Dimming, Miscellaneous. OK button. Purpose: configuring Panel PC hardware channel assignments for dimming control and horn output in a MEGA-GUARD bridge panel workstation.

After OK the new name appears in the project tree.

The contents of Version, Manager and Company cells will be downloaded to the controller together with the program. By reading it back you can always find out what program is executed.

### 5.2.3 Global variables

Global variables can be used in all programs of the project. Fore ways of declaration are available: 1) Global variable list 2) Add channels to PAL1131 Connection list 3) Individual declaration of each variable 4) VAR_GLOBAL declaration before the program. The first way is most common. Individual declarations are described in the next section. VAR_GLOBAL before program, requires changes of a few options (see For advanced users).

> **[Figure]** Screenshot of 'Global variable list' dialog in PAL1131. Variable parameters: Name (empty), Type (empty dropdown). Attributes: Constant, Retain, Global (greyed), Address (unchecked). Initial value/Comment fields. Add/Remove/Replace buttons. Declared variables table with columns: Name, Type, Attributes, Address (empty). Purpose: PAL1131 global variable declaration interface (empty state, ready for variable creation).

#### 5.2.3.1 Global variable list

Open the list in one of two ways: 1) Select Global variables (project tree) > Context menu > Edit variable list

2) Project > Tools > Global variables In following dialog an empty list is displayed:

• Name and Type The group consists of variables of the same type with adjacent addresses, so START, STOP and ALARM here. Names are entered in Name cell, Type selected from drop–down list or typed in (type first characters, press the arrow ↓ and the editor will match the rest).

> **[Vector Diagram — Page 50]** Page 50 shows PAL1131 software interface screenshots for the variable declaration dialog and global variables window in the PAL1131 IEC 61131-3 development environment.

Diagram 1: PAL1131 Variable Declaration Dialog Screenshot. Type: Software UI screenshot. The dialog contains: Name field (text input for variable name, e.g., START), Type dropdown showing options BOOL (selected), SINT, UINT, INT, DINT, ULINT (note: STRING, USINT, UDINT, UINT and ULINT types listed as 'not implemented yet'), Address field (IEC 61131-3 address with % prefix), Initial Value field, Constant checkbox, Retain checkbox, Comment field, OK and Cancel buttons. Note at top: Setting the Address option is demonstrated; if Address is not selected, variables are located automatically.

Diagram 2: PAL1131 Global Variables Window Screenshot. Type: Software UI screenshot. Shows Global Variables section in the PAL1131 project tree with columns: Name, Type, Address, Initial Value, Constant, Retain, Comment. Sample variables: START (BOOL, %IX0.0), STOP (BOOL, %IX0.1), ALARM (BOOL, %IX0.2), MOTOR (BOOL, %QX0.0). Address begins with %I (input) or %Q (output) per IEC 61131-3 addressing. An 'Add Item > Global variable' menu path is shown. Note on CONSTANT: CONSTANT declares a variable whose value cannot change during program execution and whose last value is kept in memory despite power failure. RETAIN attribute: last value kept in memory during power brake (warm restart). Initial value: applies at cold start. Page 50 illustrates section 5.2.1 workflow steps including saving the project as XML file.

> **[Figure]** Screenshot of PAL1131 Global variable list dialog showing START, STOP, ALARM variable group setup. Variable parameters: Name field: START, STOP, ALARM; Type: BOOL (dropdown). Attributes: Constant (unchecked), Retain (unchecked), Global (checked, greyed), Address (checked): 0000. Initial value (unchecked, empty). Comment (empty). Add, Remove, Replace buttons. Declared variables table with columns Name, Type, Attributes, Address: START (BOOL, global hardware I/O, %0000=>0), STOP (BOOL, global hardware I/O, %0001=>1), ALARM (BOOL, global hardware I/O, %0002=>2). Purpose: PAL1131 global BOOL variable declarations for START, STOP and ALARM signals with hardware I/O address mapping for the START_STOP example project.

|  | [INFO] |  |  | STRING, USINT, UINT, UDINT and ULINT types are not implemented yet. |  |
| --- | --- | --- | --- | --- | --- | |

• Address Selection of Address option automatically fills the cell with first unoccupied address, so 0000 here. For types other than BOOL, the address begins with the sign % and size prefix (ST language overview). If Address is not selected, the variables are located automatically.

| [INFO] |  | Setting the address is optional and demonstrated here for example usage. If your |  |
| --- | --- | --- | --- | |
|  |  | project does not require specific address usage, leave this option empty. |  |

• Constant, retain Attribute CONSTANT declares a variable which does not change during program execution, and RETAIN a variable whose last value is kept in memory despite power failure.

• Initial value If the option is not selected, the variable is set initially to default value (usually zero). For RETAIN variable the initial value applies for cold start only (i.e. after downloading the program). In case of warm restart (power resumed), the last value kept in memory is used. Non RETAIN variables are set to initial values both during cold start and warm restarts.

• Comment Text from the cell is displayed in the project tree and in auto-complete hints (Ctrl+space).

• Add Pressing the button fills the list with declared variables. If the Address option is not selected, text auto appears in the last column.

> **[Vector Diagram — Page 51]** Page 51 shows PAL1131 screenshots demonstrating global variable management and the Programs window for the PAL1131 IEC 61131-3 development environment.

Diagram 1: PAL1131 Global Variables - OK Dialog/Variable Properties. Type: Software UI screenshot. Shows variable properties dialog with fields populated for MOTOR variable (type BOOL, Address 0008). Variables list includes START, STOP, ALARM (type BOOL) and MOTOR (type BOOL).

Diagram 2: PAL1131 Project Tree with Global Variables. Type: Software UI screenshot. Shows PAL1131 project tree left panel with Global Variables node expanded listing declared variables. A context menu shows options for Add Item. After clicking OK the new variable appears in the global variable list. Note: the PAL1131 package provides free address for the first address only. Variables placed before other variables with the same beginning address are shown overlapping in red to indicate address collision.

Diagram 3: PAL1131 Programs Window. Type: Software UI screenshot. Shows the Programs section of the PAL1131 project. Context menu shown with: Add Item > Program. This illustrates section 5.2.4 ('Program') workflow for adding programs to a PAL1131 project. The project tree structure is: Project > Programs > [program name].

Note (information icon): The PAL1131 package provides free address for the first address only (i.e., after the range or group being declared has been specified, the first entry in that range is free). Variables placed before other variables with the same beginning address are shown overlapping in red to indicate address collision. Page 51 corresponds to sections 5.2.2 ('Replace, Remove') and 5.2.4 ('Program').

• OK closes the window. START, STOP and ALARM appear in Global variables section of the project tree.

The variables involve type, physical and logical addresses (or auto) and comment.

• MOTOR variable It could not be declared in the previous group since its address is not adjacent (0008). Select Address and enter 0008 instead of initial 0003.

After Add and OK, MOTOR shows up in the project tree.

#### 5.2.3.2 Replace, Remove

Selecting a variable in the list recreates its name, type and attributes in the upper cells. To make corrections, enter new data and press Replace. Remove deletes selected variable. Selection of a few variables (Shift or Ctrl) recreates only those parameters which are the same. New entry and Replace makes change in all selected variables.

| [INFO] |  | The PAL1131 package provides first free address for the group being declared, but |  |
| --- | --- | --- | --- | |
|  |  | does not check whether the whole group fits into the area before variables placed |  |
|  |  | further down (if any). In case of collision the overlapping variables are shown in red. |  |

### 5.2.4 Program

Name of the program is entered in Program properties window. Program name and preview Select the project > Context menu > Add item > Program

The window can also be opened by: • Select POU > Context menu > Add > Program

Enter program name, here PRG_START_STOP (initial PRG is left to distinguish program from the project). Due to Auto synchronization of project names (Environment options) the name appears simultaneously in the line 001 of the code field.

> **[Figure]** Screenshot of PAL1131 'Program properties' dialog. Fields: Program name: PRG_START_STOP. Program code editor showing IEC 61131-3 ST code: lines 001-006 with PROGRAM PRG_START_STOP, VAR, END_VAR, (blank lines), END_PROGRAM. Purpose: creating a new program POU (Program Organization Unit) named PRG_START_STOP in the PAL1131 development environment.

• OK. The project tree involves PRG_START_STOP in POU section.

• Double click PRG_START_STOP. The program window in edit mode is displayed (Automatically unlock window for editing).

• Enter the code Code of PRG_START_STOP is shown below. VAR_EXTERNAL declarations indicate that the global variables START, STOP, ALARM and MOTOR are used in the program. Body involves single assignment statement with expression corresponding to control diagrams at the beginning.

While entering the code, functionally different elements are shown in different colors and ev. bold. The editor is equipped with a number of useful shortcuts Supplements).

|  | [INFO] |  |  | The code can also be entered in Program properties window. |  |
| --- | --- | --- | --- | --- | --- | |

Preview vs. editing Program and other elements of the project may be inspected in preview mode, protected against modifications. Preview is activated by: Select the program > Project > Item > Lock (Ctrl+D)

Return to edit mode is similar. Project > Item > Unlock (Ctrl+E)

> **[Figure]** Screenshot of PAL1131 main window showing the START_STOP project with STARTSTOP program open. Left tree: START_STOP > POU > STARTSTOP (highlighted), Global variables, Tasks, Libraries. Right editor panel: START_STOP.STARTSTOP :: program (ST) with lines 001-007: PROGRAM STARTSTOP, VAR, (blank), (blank), END_VAR, (blank), END_PROGRAM. Purpose: initial/empty program editor view for the STARTSTOP program in PAL1131.

### 5.2.5 Task

Single task is available in the current version of PAL1131. Name of the task and programs are declared in Task properties window. • Select the project > Context menu > Add item > Task

• Task name and type. Cycle time Fill appropriate cells, i.e. with TSK_START_STOP, Cyclic and 200 ms here. As soon as possible means that the next execution begins immediately after completing previous one (so–called PLC mode).

Select PRG_START_STOP from Available programs and with upper buttons transfer it to Executed programs.

> **[Figure]** Screenshot of PAL1131 'Task properties' dialog. Fields: Task name: TSK_START_STOP. Task type: Single execution / Cyclic (selected) / As soon as possible. Cycle interval: 200, Time unit: ms. Executed programs panel (empty) and Available programs panel (PRG_START_STOP listed). Transfer arrows between panels. Purpose: configuring a cyclic task with 200ms interval for the START_STOP PAL1131 project.

OK, TSK_START_STOP appears in Tasks section of the project tree.

| [INFO] |  | Programs stored in linked libraries (if any) appear in Available |  |
| --- | --- | --- | --- | |
|  |  | programs. A program repeated in Executed programs is executed more often. |  |

### 5.2.6 Save project in XML file

New project must be saved in XML file before compilation. Recall that the START_STOP folder has been opened at the beginning for all files of the project. Current code is saved in Start–Stop.xml file in that folder.

File > Save (Ctrl+S) or

XML extension is provided automatically in Windows XP.

### 5.2.7 Compilation

The program is compiled to universal executable code in binary format for virtual machine (runtime). • Select the project (or any element of it) > Project > Build (F6)

Message window shows compilation results:

Global variables declared without addresses obtain physical addresses seen in the project tree, in parentheses. Logical addresses are still denoted by auto.

#### 5.2.7.1 Error and warnings

Error is indicated by red cross with corresponding description. Double click the description and program code is displayed with cursor in the line with the error (most probably). Errors caused by other reasons than violation of ST syntax are indicated at the beginning (line 0 or -1).

Yellow ”road” sign indicates warnings. For instance; if ALARM were assigned the address 0001 (as STOP) then following warning would appear.

Double click the warning to open Global variable properties individual window for ALARM.

> **[Figure]** Screenshot of PAL1131 'Global variable properties' dialog. Variable parameters: Name: ALARM, Type: BOOL. Attributes: Constant (unchecked), Retain (unchecked), Global (checked/greyed), Address: checked with value %0001. Initial value (unchecked). Comment (empty). IEC 61131-3 declaration preview: 001 VAR_GLOBAL, 002 ALARM AT %0001 : BOOL;, 003 END_VAR. Purpose: defining a global BOOL variable ALARM mapped to hardware address %0001 in PAL1131.

The address must be replaced and accepted.

Group correction of global variable list is also possible (Supplements).

### 5.2.8 Save and close the project

The project is saved both in binary format (.xcp) and semi–compiled form (.dcp) for simulation and hardware configuration. Some intermediate files are also saved. • Select the project > File > Save (Ctrl+S) • File > Close PAL1131 – closing the project window is displayed with Save changes question and information on file location.

The question is asked even if no changes have been made (see For advanced users to remove it).

> **[Figure]** Logic diagram showing IEC 61131-3 TON (Timer On Delay) and TOF (Timer Off Delay) function block symbols and timing diagrams. Left: TON block with BOOL inputs IN, TIME PT; BOOL output Q, TIME ET. Timing diagram shows IN rising edge, then Q rising after PT delay, ET ramp. Right: TOF block with same I/O structure. Timing diagram shows IN going high and Q following, then after IN falls Q remains high for PT duration, ET ramps down. Purpose: IEC 61131-3 standard timer function block reference showing TON and TOF behavior used in PAL1131 MEGA-GUARD programming.

| [INFO] |  | The START_STOP project will be extended in the next section, so it is closed here solely |  |
| --- | --- | --- | --- | |
|  |  | for demonstration. |  |

## 5.3 LIBRARY TIMERS

### 5.3.1 Delayed switching

The START_STOP system will be extended by turning a pump on and off 5 seconds after the motor. The IEC 61131–3 standard defines a set of function blocks including three timers. Two of them will be used here: TON – on–delay TOF – off–delay Input/output symbols, types and time diagrams are shown below.

Let the instances of TON and TOF be declared as ON_DELAY and OFF_DELAY. The former program will be extended by statements implementing cascade connection of the following blocks.

The PUMP signal will be sent to the same binary output module as MOTOR, so its logic address is 0009.

### 5.3.2 Open existing project

File > Open (Ctrl+O) or Find START_STOP folder and open Start_Stop.xml file.

The project tree appears in interface window.

### 5.3.3 IEC_61131 standard library

The timers TON, TOF are stored in PAL1131 IEC_61131 library (linked to the project by Environment options > Projects).

Library content is displayed by unfolding the tree (above) or opening Library properties window. Select IEC_61131 library > Context menu > Properties

|  | [INFO] |  |  | Time of the last compilation of the library is given in Version. |  |
| --- | --- | --- | --- | --- | --- | |

> **[Figure]** Screenshot of PAL1131 'Library properties' dialog. Library information: Library name: IEC_61131, Copyright: Praxis Automation Technology B.V., File location: E:\Program Files\PAL1131\Libraries\IEC 61131-3.lcp. Protection: None/Basic/Extended radio buttons (None selected), Settings button. Menu path: Basic/IEC. Version: 0.2.0.0 dated Wednesday April 08 2009 11:2. Objects in library table: CTD (function block), CTU (function block), CTUD (function block), F_TRIG (function block), R_TRIG (function block), RS (function block), SEMA (function block). Toggle all/Interface buttons. Purpose: shows the IEC 61131 standard function block library used in PAL1131.

Buttons − selects a library (transfers to Libraries folder) − reverses selections of all objects − shows declaration of selected object − reverses selections of function blocks − as above, for programs, functions and global variables respectively.

The button is active only while exporting or importing the library (Project > Export/Import > Library).

Timers TON, TOF Remove selections of other blocks than TON, TOF.

> **[Figure]** Screenshot of PAL1131 code editor showing the STARTSTOP program (ST language). Lines 001-020: PROGRAM STARTSTOP, VAR: ON_DELAY:TON, OFF_DELAY:TOF. END_VAR. VAR_EXTERNAL: START:BOOL (*$READ*), STOP:BOOL (*$READ*), ALARM:BOOL (*$READ*), MOTOR:BOOL, PUMP:BOOL (*$WRITE*). END_VAR. MOTOR:=(START OR MOTOR) AND NOT STOP AND NOT ALARM, ON_DELAY(IN:=MOTOR, PT:=t#5s), OFF_DELAY(IN:=ON_DELAY.Q, PT:=t#5s), PUMP:=OFF_DELAY.Q, END_PROGRAM. Purpose: complete IEC 61131-3 ST program implementing start/stop motor control with on/off delays for pump control.

Compiler links only those objects which are selected.

## 5.4 Extension of START_STOP project

### 5.4.1 Declare and use variable of Type TON and TOF

The PRG_START_STOP program will be extended and variable PUMP declared. Program Double click the program PRG_START_STOP in the project tree. Supplement the code with: – declarations of the instances ON_DELAY, OFF_DELAY – declaration of the use of global variable PUMP – statements corresponding to the cascade connection of the blocks and assignment to

## PUMP.

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing Remote Data (RD) settings. Name: RD16 Simulation. Switch Link On checkbox (checked). Use On Backup checkbox (checked). Filename: Simulation.dll (dropdown). Link device: Remote Data (dropdown, greyed). Comment field (empty). Purpose: configuring a Remote Data source named RD16 Simulation using a simulation DLL for MEGA-GUARD data simulation/testing.

Optional directives (*$READ*), (*$WRITE*) assure ”read–only” and ”write–only” properties of declared variables. Input/output structure of function block can be recalled as tip in the project tree, or in the main window by selecting the block and clicking Enter.

> **[Vector Diagram — Page 61]** Page 61 contains PAL1131 ST (Structured Text) code editor screenshots showing program code with PAL1131 system variable usage and auto-complete features.

Diagram 1: PAL1131 ST Code Editor - Program Code with System Variables. Type: Software UI screenshot showing Structured Text code. Visible code includes function block call using ON_OFF_DELAY: ON_OFF_DELAY(%IN=MOTOR, PT:=T#500ms, Q=>PUMP). The ON_OFF_DELAY function block has inputs: IN (connected to MOTOR variable), PT (preset time T#500ms); output Q connected to PUMP variable.

Diagram 2: PAL1131 Auto-Complete/IntelliSense Dropdown. Type: Software UI screenshot showing autocomplete popup. Lists available identifiers beginning with 'ON': ON_DELAY, ON_FUNCTION_BLOCK, ON_OFF_DELAY, END_FUNCTION_BLOCK. Text notes the two lines 18, 19 in program code can be replaced by single character using Ctrl+JUMP.

Diagram 3: PAL1131 New Global Variable Dialog. Type: Software UI screenshot. Shows 'Add Global Variable' dialog from Context menu > Add Item > Global Variable. Dialog has: Name field (variable name), Type: BOOL, Address field, OK and Cancel buttons.

Also shown: Auto complete section (5.4.1) showing how PAL1131 editor autocompletes variable and function block names. New global variable declaration: Ctrl+Down adds a variable to the list. A note about function compilation, specifically Build > Project > Build (Build selected). Contextual note: illustration of PAL1131 autocomplete (section 5.4.1), individual global variable declaration workflow, and compilation steps. The ON_OFF_DELAY function block is a standard IEC 61131-3 timer block in PAL1131 for MEGA-GUARD controller programs.

| [INFO] |  | The two lines 18, 19 in the program code can be replaced by single |  |
| --- | --- | --- | --- | |
|  |  | one by using internal assignment Q=>PUMP. |  |

#### 5.4.1.1 Auto complete

Name of type, function, variable, etc. may be automatically completed after writing at least one character, but only if the project at current stage has been compiled to acquire the names (Build). Pressing Ctrl + space generates list of names with the same beginning.

New global variable Select Global variables > Context menu > Edit variable list Fill in upper cells and press Add.

Compilation • Select START_STOP project • Project > Build

### 5.4.2 Individual declaration of global variable

The variable PUMP can be also declared individually, what may be more convenient sometimes. Two methods are available: 1) Select START_STOP project > Context menu > Add item > Global variable 2) Select Global variables > Add variable

Upper part of Global variable properties window should be filled in as before, lower part is updated automatically.

> **[Figure]** Screenshot of PAL1131 'Global variable properties' dialog showing PUMP variable. Name: PUMP, Type: BOOL. Attributes: Address checked: 0009. IEC 61131-3 declaration: 001 VAR_GLOBAL, 002 PUMP AT %0009 : BOOL;, 003 END_VAR. Purpose: defining a global BOOL output variable PUMP mapped to hardware address %0009.

Recall that this window is also used to correct overlapping addresses. • After OK the project tree is supplemented with PUMP.

### 5.4.3 Project report

From menu choose: Project > Tools > Report

> **[Figure]** Screenshot of PAL1131 compilation report showing the Variable list after compilation table. Columns: Name (arrow icon), Full name, Address, Size, Type, Modbus. Rows: ALARM (START_STOP.A..., 2, 1, BOOL, 2), MOTOR (START_STOP.M..., 8, 1, BOOL, 8), PUMP (START_STOP.P..., 9, 1, BOOL, 9), START (START_STOP.S..., 0, 1, BOOL, 0 - highlighted blue/selected), STOP (START_STOP.S..., 1, 1, BOOL, 1). Purpose: compilation output table showing the address and Modbus register assignments for the START_STOP example project variables after PAL1131 compilation.

> **[Figure]** Screenshot of PAL1131 project compilation report window titled 'Report from compilation of the project: START_STOP'. Project information section: Project name START_STOP, Disk file location E:\Program Files\PAL1131\Examples\Start_Stop.xml, Imported libraries IEC_61131. Variable list after compilation table: START (Address 0, Size 1, BOOL, Modbus 0), STOP (1, 1, BOOL, 1), ALARM (2, 1, BOOL, 2), MOTOR (8, 1, BOOL, 8), PUMP (9, 1, BOOL, 9). Memory use: Code memory 400, Data memory 60. Controller task list: Task0001 (Cyclic, 200 ms). Refresh/Save to file/Close buttons. Purpose: compilation output showing variable-to-address mapping and memory usage for the START_STOP project.

Full name column involves variable names preceded by project name (also in case of tasks).

#### 5.4.3.1 Sorting

Initial order of variables in the report corresponds to declarations. This may be changed by clicking header of a column what shows the sign of increasing or decreasing sorting. Depending on the column, the sorting may be either alphabetic or numeric. The first one is shown below.

#### 5.4.3.2 HTML report file

Click Save to file in the previous window to save the report in HTML format.

> **[Figure]** Screenshot of CPDev compilation report viewed in Windows Internet Explorer. Report titled 'Report from compilation of the project: START_STOP'. Project information: Project name START_STOP, Disk file location C:\Program Files\CPDev\Praxis\START_STOP\Start_Stop.xml, Imported libraries IEC_61131. Variable list: ALARM (Address 2, BOOL, Modbus SMC 40003, Modbus INTOUCH 40003), MOTOR (8, BOOL, 40009), PUMP (9, BOOL, 40010), START (0, BOOL, 40001), STOP (1, BOOL, 40002). Memory use: Code memory 430, Data memory 60. Purpose: CPDev HTML compilation report showing complete variable mapping including Modbus addresses.

Project save • File > Save (Ctrl+S)

| [INFO] |  | The window indicating the path is not called up now since location of the file has been |  |
| --- | --- | --- | --- | |
|  |  | determined already (previous Save). |  |

## 5.5 PROJECT SIMULATION

The purpose is to check operation of the project before final implementation. Both off–line and on–line tests can be carried out.

### 5.5.1 Run PAL1131Sim simulator

Three ways are available: 1) PAL1131 menu: Project > Run simulator 2) PAL1131 menu: Tools > Simulator 3) Start

2) PAL1131 menu: Tools > Simulator

3) Start menu: PAL1131 > PAL1131Sim

> **[Figure]** Screenshot of PAL1131 Tools menu expanded. Menu bar: PAL1131, File, Edit, View, Project, Tools (active), Window, Help. Tools menu items: Environment options, Global settings, Compiler, Simulator. Background shows START_STOP project tree with POU, Global variables, Tasks, Libraries folders. Purpose: showing the PAL1131 Tools menu for accessing compiler and simulator configuration options.

The first way is used directly after compilation (Project > Build), what creates .dcp file read automatically by Pal1131Sim. The next two ways require opening the .dcp file from PAL1131Sim window.

Open file for simulation

• File > Open DCP file or (PAL1131Sim menu or toolbar, see below)

> **[Figure]** Screenshot of PAL1131 Project menu showing Build option. Menu bar: PAL1131, File, Edit, View, Project (active), Tools, Window, Help. Project menu items visible: Build (F6, at top), Rebuild all (greyed), Clean, Run simulator, Item (submenu arrow). Background shows START_STOP project tree. Purpose: showing the PAL1131 Project > Build command (F6 shortcut) used to compile the IEC 61131-3 project.

| [INFO] |  | If the project has been simulated already and session data saved, the question “Do you |  |
| --- | --- | --- | --- | |
|  |  | want to open saved session as well?” is displayed. |  |

### 5.5.2 Simulator window

The window consists of two parts: – variable tree – view area

> **[Figure]** Screenshot of PAL1131Sim simulator running the Start_Stop project. Left tree: Start_Stop > Global variables (START, STOP, ALARM, MOTOR, PUMP) > Task Task0001 > Program STARTSTOR > ON_DELAY, OFF_DELAY. Global variables dialog box showing: Variable/Value table with START, STOP, ALARM, MOTOR, PUMP (all empty/no values). Status: Ready. Purpose: initial state of the PAL1131 simulator before any values are set, showing the project structure.

The variable tree differs a little from the project tree before. The view area presents initially the list of global variables or collection of individual windows for such variables (also called variable views). Panels for groups of variables or additional lists can also be placed in the view area. Scroll bars provide access to components outside (if any).

### 5.5.3 PAL1131 Simulation menu

File Trace

View Tools Window

Simulation session data can be saved in a file to repeat it later. Trace controls PAL1131Simulation operation, so starts or stops it reads (Supplements) or logs variables, and selects data source, i.e. either Simulator (off–line) or Modbus–SMC (on–line). Window > Arrange places individual windows side–by–side.

### 5.5.4 Simulation Toolbar

> **[Figure]** Screenshot of PAL1131Sim Trace menu expanded with Data source submenu. Menu bar: Trace (active), View, Tools, Window. Trace menu: Start (F5), Stop (Shift+F5), Pause (F6), Cold start (Shift+F5), Read input data (greyed), Log output data (greyed), Data source (highlighted, submenu arrow). Submenu shows: Simulator (checked, blue dot), Modbus-SMC. Background shows global variables panel with Variable/Value columns showing RT, IP, RM, LOR entries. Purpose: PAL1131Sim data source selection menu showing Simulator mode currently active for the simulation session.

> **[Figure]** Screenshot of PAL1131Sim File menu expanded. Menu bar: File (active), Trace, View, Tools, Window, Help. File menu items: Open DCP file... (Ctrl+O), Open session..., Save session (Ctrl+S), Save session as..., Exit (Alt+F4). Purpose: PAL1131 simulator File menu showing options for opening compiled DCP files and managing simulation sessions.

#### 5.5.4.1 Start, stop and pause

• Trace > Start or Simulation begins from initial values of variables (as first start after downloading the program into the controller). View area shows the results.

> **[Figure]** Screenshot of PAL1131Sim simulator running the Start_Stop project with simulation running. Global variables dialog shows values: START (blank), STOP (0), ALARM (0), MOTOR (0), PUMP (0). Status bar shows running time 00:00:03. Purpose: simulator showing the project running with initial zero values after 3 seconds of execution.

Bottom bar indicates simulation progress.

Trace > Stop or This corresponds to power brake in real controller, so last values of RETAIN variables are saved.

Another Trace > Start or Warm restart after power brake is simulated, so RETAIN variables are set to last values and non–RETAINs to initial.

Pause or resume trace Simulation stops and resumes without any change of variable values.

Trace > Cold start or This represents cold start, so simulation begins from initial values of all variables (as first start after downloading).

### 5.5.5 Variable list

Enter value or variable – Select corresponding cell – Click for editing

– Enter new value, press Enter

Values after 5 seconds since 1 has been entered for START are shown below.

> **[Figure]** Screenshot of PAL1131Sim simulator with START=1 set. Global variables dialog shows: START=1, STOP=0 (highlighted blue), ALARM=0, MOTOR=1, PUMP=1. A small MOTOR popup dialog shows Value: 1. Purpose: demonstrating the START_STOP logic result - when START=1 and STOP=0 and ALARM=0, MOTOR and PUMP both become 1.

MOTOR and PUMP are turned on.

Add variable Select variable in the tree, drag it to the list and drop (keeping pressed left key of the mouse). Remove variable Select line > Context menu > Remove

### 5.5.6 Variable views (individual windows)

Add view – Select variable in the tree. – View of the variable can be opened in three ways: 1) Drag–and–drop the variable in view area. 2) Menu: View > Variable view. 3) Context menu: Variable view. Variable view for MOTOR is shown below.

> **[Figure]** Screenshot of PAL1131Sim Global variables dialog showing START_STOP simulation with INPUTS popup. Main Global variables window shows: Variable/Value: START=1, STOP=0, ALARM=0, MOTOR=1, PUMP=1. Overlaid INPUTS popup dialog (small window with blue title bar and X close button) showing empty content (variable input entry for simulation). Purpose: PAL1131 simulator showing the START_STOP variables with an INPUTS overlay dialog for manually entering variable values during simulation.

New values are entered in the same way as in the list.

Close view, Click Additional information on variable

> **[Figure]** Screenshot of PAL1131 Panel properties dialog. Name field: Panel. Panel type section: two radio buttons: Control elements (selected), Variable list. Description text: After creating the panel drag and drop on it variables from the variable tree. OK button. Purpose: creating a new panel in PAL1131Sim with Control elements type for interactive variable manipulation during simulation.

Click to show lower part of the variable view, with type, address and full name.

### 5.5.7 Group panels

Two kinds of group panels are available: – control panels – variable lists. Variable lists look the same as the list of global variables before. Panels with control elements are created as follows: View > Group panel or Panel properties window is displayed.

> **[Figure]** Screenshot of PAL1131Sim variable inspector popup showing PUMP variable details. Title: PUMP (with X close button). Value field (empty). Advanced section (expandable arrow): Type: BOOL; Address: 0009; Full name: START_STOP.PUMP. Purpose: PAL1131 simulator variable detail popup showing the PUMP boolean variable at hardware address 0009, full path START_STOP.PUMP.

Enter name, select Control elements, press OK. Empty panel with the name (INPUTS) appears in the view area.

> **[Figure]** Screenshot of PAL1131Sim 'Options' dialog. Session tab active. Interface section: 'Open global variable views automatically' checkbox (checked). Two radio buttons: 'Use individual variable windows' with 'Limit number of windows to workarea' sub-option, and 'Use variable list' (selected). 'Always open SCP session file while opening DCP (if exists)' checkbox. 'Open variable views in advanced mode' checkbox. OK button. Purpose: PAL1131 simulator interface configuration.

Fill in the panel with appropriate variables by drag–and–drop from the tree. Panel grows automatically. Boolean variables are represented by rectangles, variables of other types by text cells.

Panel in trace mode Colors of rectangles depend on values. Click the rectangle to reverse value.

### 5.5.8 Program options

Selecting Tools > Program options opens the window with four tabs.

> **[Figure]** Screenshot of PAL1131Sim Global variables dialog showing START_STOP simulation results with INPUTS popup. Global variables window: Variable/Value: START=1, STOP=0 (blank), ALARM=0, MOTOR=1, PUMP=1. Separate INPUTS popup window (small, blue title) overlaid showing empty content. Purpose: PAL1131 simulator showing the active simulation state with MOTOR and PUMP=1 when START=1, STOP=0, ALARM=0.

Session The option Open global variable view automatically opens either the list (default) or collection of individual windows. The number of such windows may be limited for large projects. The question “Do you want to open saved session as well?” asked at the beginning is dropped if the option Always open SCP session file … is selected. Open variable views in advanced mode opens lower parts of individual windows.

Input file The tab defines .inp file for simulation controlled automatically (Supplements). Path to the file can be chosen by pressing or entered directly.

> **[Figure]** Screenshot of PAL1131Sim Options dialog, Output file tab. Session, Input file, Output file (active), Data source tabs. Path field (empty, with browse button). Store variable values in output file checkbox (unchecked). Append to existing file checkbox (unchecked). Purpose: configuring the PAL1131 simulator output file settings for logging simulation variable values to a file.

Output file Simulation results may be recorded in .out file (default name as project file name). If the file exists already, its content may be overwritten or appended.

Data source The tab is equivalent to Tracking > Data source in the menu, so it selects either off–line simulation or on–line commissioning (for SMC controller). Communication parameters can be checked by pressing Configure.

> **[Figure]** Timing diagram showing MEGA-GUARD RTC (Real-Time Controller) or ventilation/heating schedule over a 24-hour period. X-axis: time from 1:00 (night) through 6:00, daytime period, to 20:00 (n.) and 23:00. Three signal traces: T (top, continuous sinusoidal-like curve showing temperature or setpoint variation, dashed reference line labeled W above it, with W marking a peak at 6:00), F (middle, square wave pulsing between 6:00 and 20:00 daytime period, shows on/off pattern), P (bottom, narrow square pulse at 6:00 start). Purpose: illustrating a 24-hour time-based control schedule for heating/ventilation with day/night modes in the MEGA-GUARD RTC control system.

## 5.6 Example project RTC Clock

### 5.6.1 Problem description

Temperature in an apartment must be kept at given level SP (Set Point), higher during the day, e.g. 22 C, lower at night, 18 C. Actual temperature PV (Process Variable) is measured by analog input. If SP>PV, heating furnace is turned on by Control Variable CVF (CV Furnace) from binary output, and if SP>PV the furnace is turned off. However, to avoid frequent switching, the furnace can be turned on again only if the temperature PV drops below SP by at least 0.5 C (hysteresis). Circulation pump, controlled by the output CVP (CV Pump), is turned on all time during the day, and at night when the furnace is on and between the hours 23.00 and 1.00, no matter whether the furnace is on or off (the day is understood as the period between 6.00 and 20.00).

• Sample diagrams

T = Temperature, F=Furnace, P=Pump

> **[Figure]** Screenshot of PAL1131Sim Options dialog, Data source tab. Current data source: dropdown showing Simulator (selected, highlighted blue) and Modbus-SMC option visible in dropdown list. Configure button. Purpose: PAL1131 simulator data source selection - choosing between internal simulation or Modbus-SMC hardware connection for variable values during debugging/testing.

• Control system The controller CNT measures the temperature PV and controls the furnace and pump by the outputs CVF, CVP. It also communicates with PC computer, which: – sets the set point SP, – monitors the variables PV, CVF, CVP. Temperatures at the controller side are denoted by SP, PV and at PC side by SP_, PV_ (different formats).

> **[Figure]** Screenshot of PAL1131 'Global variable list' dialog showing multiple declared variables. Variable parameters: Name: SP, Type: INT. Attributes: Retain (checked), Address (checked): W0005. Initial value: 200, Comment: Set Point - PC. Declared variables table: SP (REAL, global hardware I/O), PV (REAL, global hardware I/O), CVF (BOOL, global hardware I/O), CVP (BOOL, global hardware I/O), SP_ (INT, global hardware I/O retain, %W0005, highlighted), PV_ (INT, global hardware I/O). Purpose: PAL1131 global variable list showing PID control variables with hardware I/O address mapping.

### 5.6.2 Analog input

Temperature in the range 0...100°C is measured by a transmitter with voltage output 0...10V. A/D converter converts the voltage to REAL number PV in 0.0…10.0.

Communications

Assume that PC and the controller can exchange data of the types BOOL and INT only. So the temperatures SP_, PV_ at PC side are INT variables. Accuracy 0.1 °C is required, so the range of SP_, PV_ corresponding to 0...100°C, is 0...1000 (SP=SP_/100, PV_=PV · 100). For instance, the set point 20 °C is represented by SP_=200 in PC and by SP=2.0 in the controller.

### 5.6.3 Real Time Clock (RTC) project

Global variables

> **[Figure]** Block diagram / connection diagram showing CPDev SCADA PC connected to MEGA-GUARD hardware. Left: CPDev SCADA PC with W_, Y_, U, O labels. Connected via USB to SMC controller (with W, Y, U, O labels). SMC connects via RS-485 to SM2 module (IN1 (Y) label) and SM4 module (OUT1 (U), OUT2 (O) labels). Arrows showing data flow direction. Purpose: hardware connection topology for CPDev/PAL1131 programming interface to SMC controller and I/O modules.

Note that corresponding pairs of variables can be declared as groups. Set point temperature SP_ received from PC is declared as RETAIN, with initial value

200. So SP_ will be kept in memory despite power failure (warm restart) or communication brake. From SP_=200 (20 ºC) the controller will begin operation after downloading the program (cold start).

Program PRG_RTC program of RTC project is shown below. Comments seen in the project tree are entered during declaration of variables. The task TSK_RTC is executed every 200 ms.

> **[Figure]** Screenshot of PAL1131 main window showing RTC project. Left tree: FB > POU > PRG_RTC > Global variables including SP, PV, CVF, CVP, SP_, PV_, and Tasks. Right panel shows RTC_PRG_RTC.RTC::program (ST) code editor with IEC 61131-3 ST code implementing a PID/RTC controller including CUR_TIME(), GET_TXT(), date comparisons. Purpose: PAL1131 RTC (Real-Time Controller) program source code view.

The directive (*$AUTO*) after VAR_EXTERNAL automatically includes Global variable list into compiled program. Two local variables, C_DATE and C_TIME, are declared. Statements in the lines 11: conversion of INT value received from PC into REAL, followed by adjustment of the range. 13: setting current date–and–time C_DATE to value returned by system function GET_TST() which reads the controller’s RTC clock when the task begins (Get Task Time). Separation of current time C_TIME from C_DATE by DT_TO_TOD() conversion (Day_and_Time To Time_of_Day). 15: determination of the furnace control CVF by comparison of measurement PV and set point SP temperatures, taking into account 0.5 ºC drop after turning the furnace off. 17: determination of the pump control CVP, switched on all time during the day, at night between 23.00 and 1.00 and when the furnace is on. 21: conversion of REAL to INT after adjustment of the range, to be read by PC.

### 5.6.4 Simulation

The window shown below corresponds to 9 a.m. The measured temperature 16 C is lower than the set point 20 C, so the furnace is turned on. Pump is also on (daytime). Individual window for the set point SP (controller side) is shown under the list.

> **[Figure]** Timing diagram showing PAL1131 FB_PULSE function block behavior. Two signal traces: IN (top) and Q (output, bottom). IN goes high, remains high for a long period, then goes low. Q produces a single narrow pulse (1 cycle wide) at the trailing edge of IN (after time T delay). Arrow labeled T shows the delay from IN high to Q pulse. Label: 1cycle indicates pulse width. Purpose: timing diagram illustrating the FB_PULSE function block behavior - generating a one-cycle-wide output pulse after time T following a rising edge on IN.

> **[Figure]** Screenshot of PAL1131Sim simulator running the RTC project. Global variables dialog: SP=2, PV=1.6 (highlighted blue), CVF=1, CVP=1, SP_=200, PV_=160. SP popup dialog shows Value: 2. Status bar shows 00:02:31 running time. Purpose: RTC simulator output showing controller running with setpoint and process value variables.

## 5.7 USER–DEFINED LIBRARY

### 5.7.1 Library as a project

A library with two function blocks will be created: FB_AVERAGE – average of three inputs

FB_PULSE – single pulse after time T since rising edge appeared at the input

Pulse may be generated by the following block diagram:

| [INFO] |  | User library is created as a new project with programs, function blocks, |  |
| --- | --- | --- | --- | |
|  |  | functions and global variables (or only some of them). |  |

> **[Figure]** Screenshot of PAL1131 'Project properties' dialog for START_STOP project. Fields: Project name: START_STOP, File location: E:\Program Files\PAL1131\Examples\Start_Stop.xml, VM specification: E:\Program Files\PAL1131\VM\VM-Univ.xml. Created: Wednesday October 08 2008 2:35:57 PM, Compiled: Wednesday October 08 2008 2:38:57 PM, Auto-increment: 1. Purpose: project properties reference for the START_STOP example project.

### 5.7.2 New project

File > New NoName appears in the project tree. NoName > Context menu > Properties Enter name in Project properties, for instance PROJ_MY_BLOCKS.

New function block POU > Context menu > Add > Function block

> **[Figure]** Logic diagram showing the IEC 61131-3 / PAL1131 function block interconnection for the FB_PULSE function block. Three blocks are shown left to right connected by signal lines: R_TRIG block (inputs: CLK=IN, output: Q), RS block (inputs: S=from R_TRIG.Q, R1=from TON.Q feedback, output: Q1), TON block (inputs: IN=RS.Q1, PT=T, outputs: Q, ET). Input signals: IN (top-left) feeds R_TRIG.CLK; T (bottom-left) feeds TON.PT. Output Q (top-right) comes from TON.Q via a negated (bubble) connection. The feedback from TON.Q loops back to RS.R1. Purpose: schematic diagram of the FB_PULSE function block logic showing rising-edge triggered timed pulse using R_TRIG, RS latch, and TON timer.

> **[Figure]** Screenshot of PAL1131 code editor showing PROJ_MY_BLOCKS.FB_AVERAGE function block (ST language). Lines 001-016: FUNCTION_BLOCK FB_AVERAGE, comment 'Average of three inputs', VAR_INPUT: IN1 REAL (Input 1), IN2 REAL (Input 2), IN3 REAL (Input 3), END_VAR, VAR_OUTPUT: OUT REAL (Average), END_VAR, OUT:=(IN1+IN2+IN3)/3.0;, END_FUNCTION_BLOCK. Purpose: IEC 61131-3 function block implementing 3-input average calculation.

### 5.7.3 FB_AVERAGE

Name Enter FB_AVERAGE. OK inserts the block into project tree.

Code Double click FB_AVERAGE to open editor window. Directive (*$COMMENT*) is particularly useful for user libraries.

> **[Figure]** Screenshot of PAL1131 Function block properties dialog. Function block name field: FB. Function block code editor showing IEC 61131-3 ST code: 001 FUNCTION_BLOCK FB, 002 VAR_INPUT, 003 END_VAR, 004 VAR_OUTPUT, 005 END_VAR, 006 (blank), 007 END_FUNCTION_BLOCK. Purpose: creating a new empty function block named FB in the PAL1131 IEC 61131-3 development environment.

Compilation Project > Build Correct errors, if any. Function instead of a block Since FB_AVERAGE does not store internal state, it may be replaced by a function

Remaining steps are the same.

> **[Figure]** Screenshot of PAL1131 code editor showing PROJ_MY_BLOCKS.FB_PULSE function block (ST language). Lines 001-015: FUNCTION_BLOCK FB_PULSE, comment 'Pulse after time T', VAR_INPUT: IN BOOL (Rising edge input), T TIME (Time T), END_VAR, VAR_OUTPUT: Q BOOL (Output), END_VAR, VAR: TRIG_B:R_TRIG, RS_B:RS, TON_B:TON, END_VAR. Purpose: declaration section of a pulse-after-time function block using R_TRIG, RS and TON blocks.

### 5.7.4 FB_PULSE

Blocks from IEC_61131 library will be used to implement the diagram shown at the beginning. Code – part I Local declarations define block instances.

Input/output names Sometimes you may need to recall declarations of library blocks for input/output names. This can be done in two ways: 1) Select block in the library folder in project tree. Tip with input/output declarations is briefly presented. 2) Select the block and press Ctrl+I to get permanent window with the declarations.

Code – part II While entering the code, auto complete option of PAL1131 editor is available. Ctrl + space opens auto complete list.

Compilation of the project after declarations is needed to build up the list (see Supplements). Enter inserts selected word and closes the list; you may also click the word or click outside. Esc closes the list as well.

Final code of FB_PULSE is shown below.

> **[Figure]** Screenshot of PAL1131 code editor showing the IEC_61131.TON function block source code (ST language). Title bar: IEC_61131.TON :: function block (ST). Lines: 001 FUNCTION_BLOCK TON, 002 VAR_INPUT, 003 IN : BOOL;, 004 PT : TIME;, 005 END_VAR, 006 VAR_OUTPUT, 007 Q : BOOL;, 008 ET : TIME;, 009 END_VAR, 010 ..., 011 END_FUNCTION_BLOCK. Purpose: viewing the source interface declaration of the IEC 61131-3 standard TON (Timer On Delay) function block in the PAL1131 library.

> **[Figure]** Screenshot of PAL1131 Project > Export > Library submenu. Menu: Project (active) expanded, showing Export submenu with Library and Text file options (Library highlighted). Background shows PAL1131 code editor with FB_PULSE function block. Purpose: showing the PAL1131 export workflow to export a project as a library file via Project > Export > Library menu path.

> **[Figure]** Screenshot of PAL1131 code editor showing full PROJ_MY_BLOCKS.FB_PULSE function block implementation (ST language). Lines 001-022: full FB_PULSE with declarations plus body: TRIG_B(CLK:=IN), RS_B(S:=TRIG_B.Q, R1:=Q), TON_B(IN:=RS_B.Q1, PT:=T), Q:=TON_B.Q, END_FUNCTION_BLOCK. Purpose: complete implementation of the FB_PULSE function block showing rising-edge triggered timed pulse logic.

Compilation

| [INFO] |  | You could now write a test program as additional POU unit and run it using simulator. |  |
| --- | --- | --- | --- | |
|  |  | However, it will be more natural from user viewpoint if we first export the project as a |  |
|  |  | library, and test it later in another project. |  |

### 5.7.5 Library export

The project will be exported as semi–compiled library. Project > Export > Library

Project name is temporarily used as library name.

> **[Figure]** Screenshot of PAL1131 'Export project as library' dialog with populated name. Library name: My_blocks, Copyright: Robin Hood. File location: (empty). Protection: None. Version: 0.0.0.0 dated 7 sierpnia 2009 13:00:30. Objects: FB_AVERAGE (function block), FB_PULSE (function block). Purpose: exporting custom function blocks as a named library 'My_blocks'.

Library name Enter proper name, here My_blocks, version number and eventually fill in other cells (menu path is reserved for future use in FBD diagrams).

> **[Figure]** Screenshot of PAL1131 'Export project as library' dialog. Library name: PROJ_MY_BLOCKS. Copyright: (empty). File location: (empty). Protection: None selected. Version: 0.0.0.0 dated 7 sierpnia 2009 12:32:33. Objects in library table: FB_AVERAGE (function block), FB_PULSE (function block). Toggle all/Interface buttons. Purpose: exporting the PROJ_MY_BLOCKS project as a reusable library containing FB_AVERAGE and FB_PULSE function blocks.

Library file location – Click – Select target folder, usually Libraries, enter name of library file with .lcp extension, here My_blocks.lcp, and save.

Filename may be the same as library name (but does not have to)

Objects for export Options on the left side select exported objects (both here). Button Toggle all toggles selected/non–selected, Interface recalls input/output declarations, four buttons below select function blocks, programs, functions, and global variables.

> **[Figure]** Screenshot of PAL1131 Objects in library panel showing IEC 61131 standard library function blocks. Two-column table: Object name / Object type. Entries (all function block type, some checked/unchecked): RS (unchecked), SEMA (unchecked), SR (unchecked), TOF (checked), TON (checked), TP (unchecked). Toggle all and Interface buttons. Purpose: showing the IEC_61131 standard library timer and latch function blocks available in PAL1131, with TOF and TON selected/enabled.

Semi–compilation OK compiles selected objects into semi–compiled from (.lcp extension; Project > Build produces binary code). Warnings on non–imported dependencies are not relevant.

If no error occurs, My_blocks.lcp is saved in Libraries folder.

> **[Figure]** Screenshot of the CPDev Export project as library dialog showing final configuration. Library information: Library name: My_blocks; Copyright: Robin Hood; File location: C:\Program Files\CPDev\Libraries\My_blocks.lcp (with browse button). Purpose: CPDev IDE export dialog for saving custom function blocks (My_blocks library) to the CPDev library format, showing the installed library path differs from PAL1131.

File > Save The original project PROJ_MY_BLOCKS is saved in .xml file, for instance in Proj_My_blocks.xml here.

|  | [INFO] |  |  | Library source code as XML file with original project should be saved for future use. |  |
| --- | --- | --- | --- | --- | --- | |

## 5.8 Testing

Separate project, here Test_My_blocks, is created. The block FB_AVERAGE will be tested by sample input data and FB_PULSE by counting number of pulses with CTU standard counter. Global variable list

> **[Figure]** Screenshot of PAL1131 main window showing Test_My_blocks project with PRG_A program. Left tree: Test_My_blocks > POU > PRG_A, Global variables (A, B, C, D, E, F), Tasks > TASK, Libraries > IEC_61131, My_blocks (FB_AVERAGE, FB_PULSE). Right code editor showing IEC 61131-3 ST program: VAR: AVER FB_AVERAGE, PULSE FB_PULSE, CTU1 CTU, P2C BOOL. Body: AVER(IN1:=A, IN2:=B, IN3:=C, OUT=>D), PULSE(IN:=E, T:=t#1s, Q=>P2C), CTU1(CU:=P2C, R:=FALSE, PV:=100, CV=>F). Purpose: test program using custom library function blocks FB_AVERAGE and FB_PULSE with CTU counter.

A, B, C are inputs and D output of FB_AVERAGE, E input to FB_PULSE, and F output of CTU.

> **[Figure]** Screenshot of PAL1131 'Global variable list' dialog showing variables for a My_blocks test project. Name: F, Type: INT. Declared variables: A (REAL, global, auto), B (REAL, global, auto), C (REAL, global, auto), D (REAL, global, auto), E (BOOL, global, auto), F (INT, global, auto). Purpose: declaring input/output test variables for testing the FB_AVERAGE and FB_PULSE custom function blocks.

The project Test_My_blocks uses two libraries, IEC_61131 and My_blocks. The first one is required by the second as dependent library. FB_PULSE and CTU are connected by local variable P2C.

### 5.8.1 Simulation

> **[Figure]** Screenshot of PAL Fieldbus diagnostics display window. Columns: XPn, XP Status, FRQ, IRQ, Event, Event Max, IEC1131A, IEC1131B, User, Loops, RX Total, RX Errors, RX M Errors, Error%, TX Total. Rows show XP13-XP29, with some NOT Present (red) and others showing communication statistics (RX totals in millions, error percentages near 0.0%). Purpose: diagnostic view of PAL field bus communication statistics showing which XP processors are present/absent and their communication quality metrics.

Compile Test_My_blocks, run PAL1131Sim, enter 1, 2, 3 for A, B, C, and set E five times alternately to 0, 1. The variable list of the simulator looks then as follows:

### 5.8.2 Library extension

It is done by supplementing the library source code (Proj_My_Blocks.xml) with new components. Export of the extended library is repeated by Project > Export > Libraries. Previous content of semi–compiled file (My_blocks.lcp) is replaced by the new one in Libraries.

### 5.8.3 Performance

The Processor should be checked for performance. Besides the PAL1131 task it has many other tasks to do. Via Debug Command console it is possible to see what tasks the processor is working on.

Press Ctrl-D and login. Then type “FBD” to see the following dialog:

> **[Figure]** Screenshot of PAL1131Sim simulator window showing Test_My_blocks project running. Title: PAL1131Sim :: Simulator - Test_My_blocks.dcp. Menu bar: File, Trace, View, Tools, Window, Help. Toolbar with simulation control buttons. Left tree: Test_My_blocks > Glob variables > A, B, C, D, E, F > TaskTASK. Global variables dialog box overlaid showing Variable/Value table: A=1 (implied, blank shown), B=2 (shown), C=3(?), D=2(?), E=0, F=6. Purpose: PAL1131 simulator running the Test_My_blocks project showing the FB_AVERAGE and FB_PULSE function block results with input values.

> **[Vector Diagram — Page 86]** Page 86 contains a reference table summarizing MEGA-GUARD XP (Control Processor) firmware performance metrics viewable in the OWS performance monitor.

Table: XP Firmware Performance Metrics. Type: Technical reference/specification table. Two columns: Column (parameter name) and Description.

Parameters documented:
- FIQ: Fast Interrupt Queue (for Praxis Innovation Development of the firmware)
- IRQ: Interrupt Routine Queue (for Praxis Innovation Development of the firmware)
- Event/Event Max: Percentage Processor Usage of code execution made in PAL1131. The usage is average over one second in which the firmware attempts to run it 10 times.
- PAL1131: Percentage Processor Usage is total of PAL1131 + Channel Range checks of firmware attempts. The usage is average over one second in which the firmware attempts to run this 2 times.
- Loops: Number of cycles the firmware makes per second. Each cycle the basic code is run, and all PAL1131 checks of firmware are performed. If the loop number is lower than 10 it means the processor could not manage to do all its tasks (10 complete loops per second is the target design rate).
- RX Total: Bytes received on Workstation from XP via Ethernet (Windows IServer Ethernet software counts bytes).
- RX Errors: Number of errors because of CRC faults, buffer overflows. Some errors cannot be prevented (e.g., messages transmitted while the XP is restarting).
- Error %: RX Errors as percentage of RX Total. Not applicable if RX Total is zero.
- TX Total: Number of bytes from Workstation transmitted to XP.

This table is from section 5.9 ('Processor Performance'). It defines diagnostics parameters visible in MEGA-GUARD OWS performance monitor. The Loop counter is the key health indicator - below 10 loops/second indicates processor overload.

| Column | Description |
| --- | --- | |
| FIQ | Fast Interrupt Queue (for Praxis Innovation Development of the firmware) |
| IRQ | Interrupt Routine Queue (for Praxis Innovation Development of the firmware) |
| Event/ Event Max | Software Interrupt routines (for Praxis Innovation Development of the firmware) |
| PAL1131R | Percentage Processor Usage of code execution made in PAL1131. The usage is average over one second in which the firmware attempts to run this 10 times. |
| PAL1131G | Percentage Processor Usage of Graphics Update made in PAL1131 Graphical Editor. The usage is average over one second in which the firmware attempts to run this 2 times. |
| User | Percentage Processor Usage is total of PAL1131R + PAL1131G + Channel Range and Alarm checks of firmware averaged over 1 second. |
| Loops | Number of cycles the firmware makes per second. Each cycle basic code is run, such as reading and sending channel data over Ethernet. If the number of loops is lower than 20 it means the processor could not manage to do all its tasks as designed. This can be because of User time is too high. |
| RX Total | Bytes received on Workstation from XP via Ethernet (Windows IOServer Ethernet software counts bytes) |
| RX Errors | Number of errors because of CRC faults, buffer overflows. Also some errors cannot be prevented, for examples messages that are transmitted while the XP is starting up. |
| RX M Errors | Not applicable. |
| Error % | RX Errors over RX Total |
| TX Total | Number of bytes from Workstation transmitted to XP |

## 5.9 1131 ST LANGUAGE OVERVIEW

This overview is for the readers with some experience in high level language programming (C, Pascal, scripts). More on ST can be found in John K. H. and Tiegelkamp M.: IEC 61131–3: Programming Industrial Automation Systems, Springer, 2001, or elsewhere.

### 5.9.1 IEC 61131-3 standard

#### 5.9.1.1 Programming languages

The IEC 61131-3 standard (IEC below) defines five languages for controller programming: – structured text ST – function block diagram FBD – instruction list IL – sequential function chart SFC – ladder diagram LD

ST, a high level language similar to Pascal, is a basis for PAL1131 package.

#### 5.9.1.2 Language components

Common components of the five languages are the following: – data types, e.g. BOOL, INT, REAL – program organization units POU – configuration elements.

#### 5.9.1.3 POU units

Three kinds of POUs are defined in IEC: – programs – functions blocks – functions Whereas a function for the same input data always yields the same output, output of a block may be different, as it depends on actual state of this block. Therefore declaration of block instance to allocate memory for the state must precede usage of the block.

#### 5.9.1.4 Configuration elements

Installation and configuration of programs is supported by: – configuration – tasks – access paths – resources – global variables Configuration is called a project in PAL1131. Tasks and global variables are sufficient for configuration of single controller. Programs belong to tasks.

#### 5.9.1.5 Structure of POUs

Structure of programs, functions and function blocks is the same, i.e.: – POU type and name – declaration of variables and function block instances – program code PROGRAM, FUNCTION BLOCK and FUNCTION keywords define POU type. Global and local variables are declared separately. Block instances are declared together with local variables (within VAR…END_VAR).

#### 5.9.1.6 Identifiers (names)

They begin with a letter or underscore sign _. IEC standard does not make difference between lower and upper case letters, even in keywords. So the following identifiers (names) are the same: 1) START, Start, start (variable), 2) THEN, Then, then, 3) END_VAR, end_var. PAL1131 automatically converts lower case letters into upper case (although the editor still shows them as originally entered).

Identical names in different libraries Names must be unique within a project or library. If the same name, e.g. TON, denotes another block in another library than IEC_61131, declarations of corresponding instances in the program must indicate the library, so: IEC_61131.TON Another_lib.TON

Otherwise multiple name found or Ambiguous... error appears. Actual name preceded by name of the project or library is called full name in PAL1131.

> **[Figure]** Reference table/diagram showing IEC 61131-3 data type hierarchy. Title: ANY. Four columns: ANY_BIT (BOOL, BYTE, WORD, DWORD, LWORD), ANY_NUM subdivided into ANY_INT (INT, UINT, SINT, USINT, DINT, UDINT, LINT, ULINT) and ANY_REAL (REAL, LREAL), ANY_DATE (DATE, TIME_OF_DAY, DATE_AND_TIME), and TIME/STRING/derived types. Purpose: IEC 61131-3 type hierarchy reference table showing all standard data types supported by PAL1131.

#### 5.9.1.7 Data types and variables

• Elementary data types

No. Name Data types Size and range 1 BOOL Boolean 1B (FALSE, TRUE⇔ 0,1) 2 BYTE byte 1B (0 ... 255) 3 WORD word 2B (0 ... 65535) 4 DWORD double word 4B (0 ... 232-1) 5 LWORD long word 8B (0 ... 264-1) 6 SINT short integer 1B (-128 ... 127) 7 INT integer 2B (-32768 ... 32767) 8 DINT double integer 4B (-231 ... 231-1) 9 LINT long integer 8B (-263 ... 263-1) unsigned short 10 USINT integer 1B (0 ... 255) 11 UINT unsigned integer 2B (0 ... 65535) unsigned double 12 UDINT integer 4B (0 ... 232-1) 13 ULINT unsigned long integer 8B (0 ... 264-1) 14 REAL real 4B, IEEE-754 format 15 LREAL long real 8B, IEEE-754 format 4B (-T#24d20h31m23s648ms... T#0s... 16 TIME duration #24d20h31m23s647ms) 17 DATE date 4B (0001-01-01 ... 9999-12-31) 18 TIME_OF_DAY time of day 4B (00:00:00.00... 23:59:59.99) 19 DATE_AND_TIME date and time 8B (connection of DATE and TIME_OF_DAY types)

# 20 STRING character string variable length

|  | [INFO] |  |  | STRING, USINT, UINT, UDINT and ULINT types are not implemented in PAL1131 yet.. |  |
| --- | --- | --- | --- | --- | --- | |

• Universal types Groups of elementary types collected according to applications are called universal.

• Constants (literals)

> **[Vector Diagram — Page 89]** Page 89 covers PAL1131 IEC 61131-3 standard programming language reference including constants, variable types, initial values, and attribute declarations.

Table 1: IEC 61131-3 Data Types and Initial Values. Type: Technical reference table. Lists PAL1131 data types with default initial values: BOOL=FALSE (TRUE_BOOL_INT for non-zero), SINT=0, INT=0, DINT=0, TIME=T#0s, DATE=D#0001-01-01, TIME_OF_DAY=TOD#00:00:00.000, DATE_AND_TIME=DT#0001-01-00:00:00, STRING='' (empty).

Variable Declaration Types documented: VAR_INPUT (inputs), VAR_OUTPUT (outputs), VAR_EXTERNAL (external access to global), VAR_GLOBAL (global variable list), VAR_IN_OUT (bidirectional). AT keyword: used for absolute address assignment (e.g., pump AT %NW0003: WORD).

Constant and Literal Syntax: Non-decimal constants: 2#1111_1111 (binary), 8#377 (octal), 16#FF or 16#ff (hex). Type-qualified literals: DINT#18, T#1d12h35m15s500ms. STRING literal: enclosed in single quotes. Initial value note: RETAIN attribute means variable's last value kept in memory during power brake (warm restart). Non-RETAIN variables reset to initial value at warm restart.

Global Variable Prefix/Size Table. Type: Technical reference table. Prefix | Data types | Size: B=BOOL (1), W=SINT/UINT/INT (2), D=DWORD/DINT/UINT (4), L=TIME/DATE/TIME_OF_DAY/DATE_AND_TIME (8), 0(8)=LWORD/LINT/ULINT/REAL (8). The AT addressing prefix convention for PAL1131: %I=Input, %Q=Output, %M=Memory, %N=Network/IOM address. Page 89 is from section 5.9.1 ('IEC 61131-3 standard').

Examples of constants of the types used most often are given below:

|  | Constant type |  |  | Value |  |
| --- | --- | --- | --- | --- | --- | |
| BOOL |  |  | TRUE, BOOL#1 |  |  |
| INT |  |  | 13, INT#-1 |  |  |
| REAL |  |  | 4.1415, REAL#18, 1.2E-6 |  |  |
| TIME |  |  | T#1m3s250ms |  |  |
| TIME_OF_DAY |  |  | TOD#06:00:00 |  |  |

| [INFO] |  | Single numerical constant without the dot is of type INT, whereas constant |  |
| --- | --- | --- | --- | |
|  |  | with the dot is of type REAL. |  |

Other types than INT, REAL are chosen by putting type name and sign # before the number, e.g. DINT#-13, REAL#1.

Non decimal numbers Format of non decimal number involves: 1) base of numerical system, e.g. 2, 8, 16, etc., 2) sign #, 3) alphanumeric string as value. For instance, 2#11111111, 8#377, 16#FF denote 255 decimal. WORD#16#00FF is another option (leading zeroes are not necessary).

• Initial values Default initial values are in the table:

|  | Data type |  |  | Initial value |  |
| --- | --- | --- | --- | --- | --- | |
| ANY_BIT, ANY_INT |  |  | 0 |  |  |
| ANY_REAL |  |  | 0.0 |  |  |
| TIME |  |  | T#0s |  |  |
| DATE |  |  | D#0001-01-01 |  |  |
| TIME_OF_DAY |  |  | TOD#00:00:00 |  |  |
| DAY_AND_TIME |  |  | DT#0001-01-01-00:00:00 |  |  |
| STRING |  |  | '' (empty) |  |  |

Other initial values are declared by means of assignment sign :=, for instance lamp: BOOL := TRUE; Attributes PAL1131 package supports two attributes of variables:

`RETAIN CONSTANT`

RETAIN declares a retentive variable whose value is kept in memory during power brake (for warm restart). CONSTANT variable cannot be changed. Initial value of retentive variable applies for cold start only, whereas initial value of non–retentive one is also used for warm restart. Declarations of variables IEC standard defines a few kinds of variable declarations:

`VAR VAR_IN_OUT VAR_ACCESS`

> **[Vector Diagram — Page 90]** Page 90 continues PAL1131 variable type and declaration documentation including RETAIN attributes, global variable prefixes, and variable declaration kinds.

Table: Global Variable Data Prefixes and Size. Type: Technical reference table. Address prefix table for global variables in PAL1131: Prefix B=BOOL (1 byte), W=SINT/UINT/INT (2 bytes), D=DWORD/DINT/UINT (4 bytes), L=TIME/DATE/TIME_OF_DAY/DATE_AND_TIME (8 bytes), 0=LWORD/LINT/ULINT/REAL (8 bytes).

Variable Declaration Kinds (four types):
1. VAR_INPUT / VAR_EXTERNAL: external inputs assigned via AT keyword; initial value is 0 or FALSE; used for VAR (local) and VAR_GLOBAL
2. VAR_OUTPUT: declared in program block, accessible to other programs
3. VAR_IN_OUT: bidirectional variables
4. RETAIN: variable value kept in memory during power brake (warm restart); CONSTANT: initial value applies only at cold start; Non-RETAIN variables use initial value 0 at restart

Declarations of variables in VAR section: variable := expression; Statements: IF HAMM_2 THEN B := A; ELSIF A<B THEN B := D; ELSE A := 0; B := D; END_IF. Selections: IF_CASE. Also shown: VAR_INPUT, VAR_EXTERNAL declarations at start/end of program blocks.

Contextual note: Page 90 is from section 5.9.1 of the PAL1131 language reference. Global variable AT keyword assignments follow the format: VAR_VAR_EXTERNAL AT %NW0003: WORD. These memory allocation specifications apply to all IEC 61131-3 language elements (ST, FBD, LD) in MEGA-GUARD XP controller programming.

`VAR_INPUT VAR_EXTERNAL`

`VAR_OUTPUT VAR_GLOBAL`

VAR declares local variables and function block instances. VAR_INPUT, VAR_OUTPUT and VAR_IN_OUT are used in function blocks and functions. VAR_EXTERNAL declares usage of variables defined in Global variable list (or, equivalently, by VAR_GLOBAL; see For advanced users). END_VAR terminates each kind of declaration. Declarations VAR_EXTERNAL are allowed in programs only (not in function blocks or functions). RETAIN attribute may appear in Global variable list (or VAR_GLOBAL), in VAR and VAR_OUTPUT. VAR_ACCESS is not supported by PAL1131. Allocation of global variables Allocation of single variable is determined by AT keyword followed by concatenation of the sign %, size prefix and logical address, e.g.: pump AT %B0009 : BOOL; Global variable list involves Address option instead of AT. Size prefixes are shown in the table.

Prefix Data types Size

|  | Prefix |  |  | Data types |  |  | Size |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | |
| B, X, none |  |  | BOOL, BYTE, SINT, USINT |  |  | 1B |  |  |
| W |  |  | WORD, INT, UINT |  |  | 2B |  |  |
| D |  |  | DWORD, DINT, UDINT, REAL, TIME, DATE, TIME_OF_DAY |  |  | 4B |  |  |
| L |  |  | LWORD, LINT, ULINT, LREAL, DATE_AND_TIME |  |  | 8B |  |  |

Prefixes B, X and leading zeroes of the address may be dropped (as %9 for the pump above). Group declaration

`A, B, C AT %W0000:INT;`

is equivalent to three individual declarations

`A AT %W0000:INT; B AT %W0001:INT; C AT %W0002:INT;`

The keyword AT cannot be used for local variables which are located automatically. Memory addresses Compiler determines number of bytes from size prefix and assigns memory for the variable beginning from the byte with address byte address := logical address * size, (logical address from Global variable list or AT declaration). For instance, declaration counter AT %W0007: INT; means that counter occupies 2 ·7=14th byte (and 15th). So the addresses of first bytes where variables are located have the following properties

> **[Figure]** Reference table showing IEC 61131-3 POU (Program Organization Unit) keyword delimiters. Two-column table: POU / Limiting keywords. Program: PROGRAM ... END_PROGRAM; Function block: FUNCTION_BLOCK ... END_FUNCTION_BLOCK; Function: FUNCTION ... END_FUNCTION. Purpose: PAL1131/IEC 61131-3 reference showing the required keyword delimiters for each type of program organization unit.

| [INFO] |  | Addresses of variables are needed to configure communication with host computer. |  |
| --- | --- | --- | --- | |
|  |  | They are shown in Project report. |  |

If global variable is declared without selecting Address option in Global variable list (or without AT) the compiler locates it automatically filling empty spaces. Text auto appears in the list. If variables are declared in groups, some of the addresses may overlap since the compiler checks whether address for first variable is free, and not the area for the whole group. Warning appears in case of overlapping.

Function block declaration As mentioned before, instances of function blocks are declared locally within VAR ... END_VAR. For instance, if DELAY is going to be an instance of the TON block, it must be declared by:

## DELAY : TON;

### 5.9.2 Programming in ST

#### 5.9.2.1 Programs, function blocks and functions

The following keywords begin and terminate declarations of POU units:

> **[Figure]** Reference table showing IEC 61131-3 variable address prefix alignment rules in PAL1131. Two-column table: Prefix / Byte address. B, X, none: number after prefix (any byte address); W: even number (address must be divisible by 2); D: number divisible by 4; L: number divisible by 8. Purpose: PAL1131 reference showing memory address alignment requirements for different data type prefixes (Bit/Byte, Word, Double-word, Long-word) in IEC 61131-3 variable declarations.

A program may call (invoke) function blocks and functions; function block may call other blocks or functions. Recursive calls are not allowed.

#### 5.9.2.2 ST language statements

They involve assignment, selections, loops, exits, function and function block calls (invocations).

> **[Vector Diagram — Page 92]** Page 92 covers PAL1131 ST (Structured Text) programming control flow constructs: IF/CASE conditional statements and FOR/WHILE/REPEAT loop statements.

Code Examples - ST Language Constructs:

Assignment: variable := expression;

IF statement syntax:
IF A>B THEN
  B := A;
ELSIF A<B THEN
  B := A+2;
ELSE A := 0; B := D;
END_IF
Note: Semicolons not necessary after END_IF, END_VAR and other END tokens.

CASE statement syntax:
CASE A OF
  1: B := WORD_0;
  11, 13, 15: B := A*10;
  ELSE A := B+9999;
END_CASE
Selection variable must be integer type. CASE list values can be constants or sets. If the function selector matches that integer value, execution branches to that CASE.

FOR loop syntax:
FOR i:=0 TO 10 DO
  pump := FALSE;
  alarm := TRUE;
END_FOR
IF control variable increment is other than 1, the BY clause is used: FOR i:=0 TO 10 BY 2 DO.

WHILE loop syntax:
WHILE i>0 DO
  pump := FALSE;
END_WHILE

REPEAT loop syntax:
REPEAT
  B := B+1;
UNTIL i>10
END_REPEAT

EXIT: exits FOR, WHILE or REPEAT loop. RETURN: early exit from function or function block (not from program). Page 92 is from section 5.9.2 ('Statements'). FOR loop counter must be a local variable (not VAR_EXTERNAL or VAR_GLOBAL).

Assignment: variable := expression; Statements is terminated by semicolon ;. Selections: IF, CASE

| IF |  |
| --- | --- | |
| IF A>B THEN B := A; ELSIF A<B THEN A := B; ELSE A := 0; B:= 0; END_IF | Semicolons are not necessary after END_IF, END_VAR and other ENDs. |

| CASE |  |
| --- | --- | |
| CASE A OF 1: B:=1; A:=2; 2..10: A:=A+1; B:=A*1000; 11,13,15..21: A:=A+2; B:=A*10; ELSE A:=1; B:=9999; END_CASE | Selection variable must by of integer type (ANY_INT, BYTE, WORD...). Entries are constant values (or CONSTANT variables) of selector type, otherwise Cannot match primitive function... error appears (in line 0). |

Loops : FOR, WHILE, REPEAT

| FOR | WHILE | REPEAT |
| --- | --- | --- | |
| counter := 0; FOR i:=1 TO 10 DO counter:= counter+i; END_FOR | WHILE st1 OR st2 DO pump := FALSE; alarm := TRUE; END_WHILE | REPEAT B := B+1; UNTIL B>10 END_REPEAT |

If control variable of FOR loop must be increased by other number than 1, then BY… component is included into the statement, as in FOR i:=1 TO 10 BY 2 DO ... END_FOR FOR i:=10 TO 1 BY –1 DO ... END_FOR (BY must be followed by a constant or CONSTANT variable).

Exits : EXIT, RETURN EXIT interrupts FOR, WHILE or REPEAT loop. RETURN provides early exit from a function or function block (before END).

| EXIT | RETURN |
| --- | --- | |
| WHILE i>0 DO | FUNCTION LINE: REAL |

> **[Vector Diagram — Page 93]** Page 93 documents PAL1131 function and function block definitions, plus the standard operator precedence table for IEC 61131-3 Structured Text.

Function Call Syntax: Functions/FBs can be called with named parameter assignments. The output can be transferred directly via '=>' notation, e.g., DELAY(input:=MOTOR, PT:=T#500ms, Q=>PUMP). Standard FBD function block instantiation uses IEC 61131-3 syntax. Example: graph := DELAY(%_input=MOTOR, PT:=T#500ms, Q=>PUMP).

Operator Precedence Table. Type: Reference table with Symbol, Description, and IEC 61131-3 abbreviation columns. In order of highest to lowest priority:
() = parentheses (highest priority)
** = exponentiation (EXP)
- = negation (NEG)
NOT = Boolean negation (NOT)
* = multiplication (MUL)
/ = division (DIV)
MOD = modulo (MOD)
+ = addition (ADD)
- = subtraction (SUB)
<, >, <=, >= = comparison (LT, GT, LE, GE)
=, <> = equality/inequality (EQ, NE)
AND, & = Boolean AND (AND)
XOR = exclusive OR (XOR)
OR = inclusive OR (OR, lowest priority)

Notes: ** after function name indicates functions may accept up to 15 inputs. ANY_BIT (without BOOL) is a valid type for bitwise operations. Additional function RANDOM (not in standard list) returns REAL in range 0.0..1.0. Page 93 is from section 5.9.2 ('Expressions'). These operators govern expression evaluation order in ST programs running on MEGA-GUARD XP controllers.

| l := l+1; IF l>MAX_l THEN EXIT; END_IF i := i-1; END_WHILE | VAR_INPUT a,x,b: REAL; END_VAR LINE:=a*x+b; RETURN; END_FUNCTION |
| --- | --- | |

Function Standard and system functions (next chapter) are called directly. To call user– defined functions corresponding libraries must be imported. Function call statement may look as follows:

`Y := LINE(A1,X1,B1);`

Function block Suppose DELAY denotes instance of the standard timer TON. The following statements invoke DELAY and transfer its outputs: DELAY(IN:=_input, PT:=t#5s); motor := DELAY.Q; bargraph := DELAY.ET; The outputs can also be transferred directly in the call statement by means of the sign =>, i.e.: DELAY(IN:=_input, PT:=t#5s, Q=>motor, ET=>bargraph); Order of inputs and outputs does not matter in the call.

#### 5.9.2.3 ST language operators

Expressions consist of operators and operands. The following table lists operators with priorities in descending order.

|  | Symbol |  |  | Description |  |  | Function |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | |
| ( ) |  |  | parentheses |  |  | – |  |  |
| F(x) |  |  | function evaluation |  |  | F(x) |  |  |
| ** |  |  | exponentiation |  |  | EXPT |  |  |
| - |  |  | arithmetic negation |  |  | NEG |  |  |
| NOT |  |  | Boolean negation |  |  | NOT |  |  |
| * |  |  | multiplication |  |  | MUL |  |  |
| / |  |  | division |  |  | DIV |  |  |
| MOD |  |  | modulo |  |  | MOD |  |  |
| + |  |  | addition |  |  | ADD |  |  |
| - |  |  | subtraction |  |  | SUB |  |  |
| <, >, <=, >= |  |  | comparison |  |  | LT,...,GE |  |  |
| = |  |  | equality |  |  | EQ |  |  |
| <> |  |  | inequality |  |  | NQ |  |  |
| AND, & |  |  | Boolean multiplication |  |  | AND |  |  |
| XOR |  |  | exclusive |  |  | OR XOR |  |  |
| OR |  |  | Boolean sum |  |  | OR |  |  |

> **[Vector Diagram — Page 94]** Page 94 documents PAL1131 standard library functions organized by category, covering arithmetic, numeric, boolean, comparison, and selection functions.

Table: Standard Library Functions by Group. Type: Four-column reference table (Group, Name, Operation, I/O Types).

Arithmetic group: ADD (addition, ANY_NUM), MUL (multiply, ANY_NUM), SUB (subtraction, ANY_NUM), DIV (division, ANY_NUM), MOD (modulo, ANY_NUM), EXPT (exponentiation, ANY_NUM), MOVE (assign/move, ANY).

Numeric group: ABS (absolute value, ANY_NUM), SQRT (square root, ANY_REAL), LN (natural logarithm, ANY_REAL), LOG (log base 10, ANY_REAL), EXP (natural exponential, ANY_REAL), SIN (sine, ANY_REAL), COS (cosine, ANY_REAL), TAN (tangent, ANY_REAL), ASIN (arc sine, ANY_REAL), ACOS (arc cosine, ANY_REAL), ATAN (arc tangent, ANY_REAL).

Bit shift group: SHL (shift left zero-filled, BYTE/WORD), SHR (shift right zero-filled, BYTE/WORD), ROR (right-rotate circular, DWORD), ROL (left-rotate circular, DWORD).

Comparison group: GT (greater than, ANY), GE (greater/equal, ANY), EQ (equal, ANY), LT (less than, ANY), LE (less/equal, ANY), NE (not equal, ANY).

Selection group: SEL (binary selector 2 options, ANY), MAX (maximum, ANY), MIN (minimum, ANY), LIMIT (min/in/max limiter, ANY), MUX* (multiplexer up to 15 inputs, ANY).

Note: * after function name = accepts up to 15 inputs. ANY_BIT (without BOOL) applies. Additional function RANDOM returns REAL in range 0.0..1.0. These functions are accessible in PAL1131 ST/FBD/LD programs on MEGA-GUARD XP controllers.

The operators separated above by the dashed lines have the same priority, so they are executed in the order defined by expression (from left to right). Operators can be replaced by functions given in the table, as in: x1 AND x2 AND(x1,x2)

#### 5.9.2.4 Single–dimensional arrays

| Program part |  |
| --- | --- | |
| VAR T:ARRAY[0..5] OF INT; END_VAR FOR I:=1 TO 5 DO T[I-1]:=T[I]; END_FOR T[5]:=A; S:=0; FOR I:=0 TO 5 DO S:=S+T[I]; END_FOR S:=S/I; | Compiler accepts single–dimensional arrays declared as local variables. The arrays cannot be used as inputs or outputs. Program on the left implements moving average filter for variable A. |

#### 5.9.2.5 Functions

IEC standard defines large set of functions divided into groups. Most of IEC functions are available in PAL1131 (several data types are not supported, e.g. STRING).

Mathematic and logic functions

|  | Group |  |  | Name |  |  | Operation |  |  | I/O types |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | |
| Arithmetic |  |  | ADD* SUB MUL* DIV MOD EXPT |  |  | Add subtract multiply divide modulo exponentiation |  |  | ANY_NUM |  |  |
|  |  |  | NEG |  |  | negation |  |  | SINT, INT, DINT LINT, REAL |  |  |
| Numeric |  |  | ABS SQRT LN LOG EXP SIN COS TAN ASIN |  |  | Absolute value square root natural logarithm logarithm base 10 natural exponential sine cosine tangent arc sine |  |  | REAL, LREAL |  |  |

> **[Vector Diagram — Page 95]** Page 95 documents additional PAL1131 standard library functions (Boolean, type conversion) and single-dimensional array usage in PAL1131.

Table (continuation of page 94): Standard Functions - Boolean and Type Conversion.

Boolean group: AND* (Boolean AND, ANY_BIT), OR* (Boolean OR, ANY_BIT), XOR* (exclusive OR, ANY_BIT), NOT (Boolean NOT, ANY_BIT). * = accepts up to 15 inputs.

Type Conversion group (examples): BOOL_TO_INT, BOOL_TO_REAL, SINT_TO_INT, SINT_TO_DINT, SINT_TO_REAL, INT_TO_SINT, INT_TO_DINT, INT_TO_REAL, DINT_TO_INT, DINT_TO_SINT, DINT_TO_REAL, REAL_TO_INT (rounds to nearest), REAL_TO_DINT, REAL_TO_LREAL, TRUNC (truncates REAL to INT, same as INT_TO_INT with truncation semantics).

Single-Dimensional Arrays in PAL1131. Type: Language reference with code examples. Array declaration syntax: ARRAY[lower..upper] OF data_type. Example:
VAR
  T_ARRAYS_5 OF INT;
  ENG_VAR: ARRAY[1..5] OF INT;
END_VAR
FOR i:=1 TO 5 DO
  ENG_VAR[i] := 0;
END_FOR
S:=S/5.0;

Arrays can be used as inputs or outputs in function blocks. The program example shown implements a moving average filter for variable A. Page 95 is from sections 5.9.2 ('Functions') and 5.9.2.4 ('Single dimensional arrays') of PAL1131 reference. These capabilities apply to all IEC 61131-3 language elements (ST, FBD, LD) in MEGA-GUARD XP controller programs.

|  | ACOS ATAN | arc cosine arc tangent |  |
| --- | --- | --- | --- | |
| Boolean | AND* OR* XOR* NOT | logic product logic sum exclusive OR complement | ANY_BIT |
| Bit shift | SHL SHR ROL ROR | shift left, zero–filled shift right, zero–filled left–rotated, circular right–rotated, circular | BYTE, WORD DWORD, LWORD |
| Comparison | GT GE EQ LT LE NE | greater greater or equal equal less less or equal not equal | ANY |
| Time | ADD SUB | add subtract | TIME |

> **[Figure]** Reference table showing IEC 61131-3 selection function blocks. Title: 'Switches, selectors'. Four rows: ASWI (analog switch: OUT=IN1 for S=FALSE, OUT=IN2 for S=TRUE), BSWI (binary switch), AMEM (analog memory: OUT=IN for TRG=FALSE, OUT=IN(t0) for TRG=TRUE), BMEM (binary memory). Each shows block symbol with I/O types and behavioral descriptions. Purpose: PAL1131 standard function block library reference for switching and memory elements.

Explanations – Star * after function name indicates varying number of arguments (up to 15). – Bit shift functions have two arguments, ANY_BIT (without BOOL) and INT. – Other operations on TIME data can be executed by conversion to REAL or DINT. – Additional function RANDOML (not listed above) returns REAL number in 0.0...1.0 for rectangular probability distribution.

Selection functions All elementary types are allowed (ANY).

MUX may switch up to 15 inputs. Conversions

> **[Vector Diagram — Page 96]** Page 96 documents PAL1131 type conversion functions, real-time clock (RTC) functions, and the complete type conversion table for the PAL1131 environment.

Type Conversion Function Matrix. Type: Technical reference table. Shows full type conversion matrix with input types INT, REAL, DINT, DWORD, WORD, BOOL and output types DINT, INT, REAL, DWORD, WORD, BOOL, BYTE, SINT, UINT, UDINT, STRING. Function names follow pattern TYPE1_TO_TYPE2. Additional conversions: INT_TO_BOOL, INT_TO_BYTE, INT_TO_SINT, INT_TO_UINT, INT_TO_UDINT, REAL_TO_LREAL, TRUNC (truncates REAL to INT). Depending on argument type, SINT_TO_LINT (last listed) converts INT to LINT by repeating MSB.

RTC (Real-Time Clock) Function Table. Type: Function reference table. Columns: Name, Function returns, Result type.
- CUR_TIME: current time (time elapsed since system startup, not wall-clock), returns TIME
- READ_RTC: absolute time from RTC clock, returns DATE_AND_TIME
- GET_TOD: time of day component, returns TIME_OF_DAY
- WRITE_RTC: write to RTC clock, returns BOOL (status of RTC update operation)
- TASK: check box (task clock), returns BOOL

Explanatory text: WRITE_RTC and GET_TOD functions operate on DATE_AND_TIME data including system time, date, days of week. CUR_TIME returns time elapsed since startup. Time interval determined as difference between two CUR_TIME readings. READ_RTC returns status flag of RTC update. Note: RTC functions depend on hardware platform availability on MPC hardware. Page 96 is from sections 5.9.2 ('Conversions') and 5.9.2 ('Real time'). RTC functions used in MEGA-GUARD XP controller programs for time-stamped logging, alarm management, and scheduled operations.

If the following table does not include a particular conversion, two steps are needed with some intermediate type.

|  | Input |  |  | Function name |  |
| --- | --- | --- | --- | --- | --- | |
| INT |  |  | INT_TO_REAL, INT_TO_DINT, INT_TO_BOOL, INT_TO_WORD |  |  |
| REAL |  |  | REAL_TO_INT, REAL_TO_TIME, REAL_TO_LREAL, TRUNC, ROUND |  |  |
| DINT |  |  | DINT_TO_REAL, DINT_TO_TIME, DINT_TO_DWORD, DINT_TO_INT |  |  |
| TIME |  |  | TIME_TO_DINT, TIME_TO_REAL |  |  |
| BYTE |  |  | BYTE_TO_SINT |  |  |
| WORD |  |  | WORD_TO_INT |  |  |
| BOOL |  |  | BOOL_TO_INT |  |  |
| SINT |  |  | SINT_TO_BYTE |  |  |
| LREAL |  |  | LREAL_TO_REAL, TRUNC ROUND |  |  |
| LINT |  |  | LINT_TO_LWORD |  |  |
| DWORD |  |  | DWORD_TO_DINT |  |  |
| LWORD |  |  | LWORD_TO_LINT |  |  |

> **[Figure]** Reference table showing PAL1131 RTC (Real-Time Clock) system functions. Three-column table: Name, Function returns, Result type: CUR_TIME (current system time, TIME), READ_RTC (absolute time read from RTC clock, DT), WRITE_RTC (RTC clock update status, BOOL), GET_TST (absolute time of task start, DT), TASK_CYCLE (task cycle duration, TIME). Purpose: PAL1131 standard library reference for real-time clock and task timing functions used in IEC 61131-3 programs for MEGA-GUARD controllers.

| [INFO] |  | Depending on argument type, TRUNC and ROUND convert either to DINT or LINT. |  |
| --- | --- | --- | --- | |
|  |  | DEPR_INT_TO_DINT (not listed) converts INT to DINT by repeating MSB bit. |  |

Real time PAL1131 package provides: – system time as TIME data – RTC clock read and write – daytime and date components – days of the week. System time and RTC functions are given in the table. CUR_TIME increments system time up to 24 days (a little more), then resets it to „negative” 24 days, and so on. Time interval is determined as the difference between two CUR_TIME readings.

Explanations – READ_RTC, WRITE_RTC and GET_TST functions operate on DATE_AND_TIME data. WRITE_RTC returns status flag of RTC update operation (RTC functions depend on hardware platform).

– Task start time returned by GET_TST is used more often than the time returned by READ_RTC. – TASK_CYCLE returns value set in the project (Task properties window).

Daytime and date components Structure of DATE_AND_TIME data in shown below. Successive bytes denote: CC – hundredth parts of a second, SS – second, NN – minute, HH – hour, DD – day, MM – month, YY+YY – year.

Functions from GET_HUNDSEC to GET_YEAR return INT value. Two types of input arguments are supported.

> **[Figure]** Reference table showing PAL1131 time-related functions. Title: (implied: Time functions). Three-column table with headers Name, Function returns, Argument type: GET_HUNDSEC (hundredths of second, DT/TOD), GET_SECOND (second, DT/TOD), GET_MINUTE (minute, DT/TOD), GET_HOUR (hour, DT/TOD), GET_DAY (day, DT/D), GET_MONTH (month, DT/D), GET_YEAR (year, DT/D), GET_DAYOFWEEK (day of week, DT/D). Purpose: PAL1131 standard library reference table for date/time decomposition functions used in IEC 61131-3 programs.

Status word Bits of status word returned by GET_STATUS_WORD1 denote

### 5.9.3 FUNCTION BLOCK LIBRARIES

PAL1131 package involves two libraries with function blocks, IEC_61131 and Basic_blocks.

#### 5.9.3.1 IEC_61131 library

Symbols of inputs and outputs are as in the IEC standard, so: R – reset input (logic) S – set input

CLK↑ – rising edge at CLK input Q – output of BOOL type Initial values of all inputs are zero.

> **[Figure]** Reference table showing IEC 61131-3 counter function blocks. Title: 'Counters'. Three sections: CTU (up counter: CV=CV+1 for CU rising and CV<PV and R=FALSE; CV=0 for R=TRUE; Q=TRUE for CV=PV), CTD (down counter: CV=CV-1 for CD rising and CV>0 and LD=FALSE; CV=PV for LD=TRUE; Q=TRUE for CV=0), CTUD (up-down counter combining CTU and CTD logic). Each shows block symbol with inputs CU/CD/R/LD/PV and outputs Q/CV. Purpose: IEC 61131-3 counter function block reference.

> **[Figure]** Reference table showing IEC 61131-3 bistable elements. Title: 'Bistable elements'. Sections: RS flip-flop (Q1=NOT R1 AND (Q1(n-1) OR S)), SR flip-flop (Q1=S1 OR (NOT R AND Q1(n-1))), SEMA semaphore (BUSY=TRUE for CLAIM=TRUE, BUSY=FALSE for RELEASE=TRUE and CLAIM=FALSE). Each shows block symbol with BOOL inputs/outputs. Purpose: IEC 61131-3 flip-flop and semaphore function block reference for PAL1131.

> **[Figure]** Reference table showing PAL1131 mathematical function blocks. Title: Mathematic blocks. Two entries: DIVI block (symbol: REAL inputs IN1, IN2, LM; REAL output OUT) - description: DIVI - division with limited divisor, OUT=IN1/IN2, LM=limit of IN2 before 0, If |IN2|<LM then OUT=IN1/(+/-LM); +/- is IN2 sign. SQR block (symbol: REAL inputs IN, LM; REAL output OUT) - description: SQR - square root with linear initial part, OUT=sqrt(IN) for IN>=LM, OUT=IN/sqrt(LM) for IN<LM. Purpose: PAL1131 mathematical library reference showing safe division and square root function blocks.

| [INFO] |  | Recall that READ_RTC, WRITE_RTC and GET_TST functions handle |  |
| --- | --- | --- | --- | |
|  |  | RTC clock in PAL1131 |  |

#### 5.9.3.2 Basic_blocks library

Notation: R – reset input for arithmetic and logic, or to set another value S – selection or switching input, set input for flip–flops IN↑ – rising edge at IN input; edge at t0 is denoted by t0:IN↑ Q – output of BOOL type OUT – output of REAL,TIME or other type. Initial values of all inputs are zero.

> **[Figure]** Reference table showing IEC 61131-3 timer function blocks. Title: 'Timers'. Three sections with timing diagrams: TON (on-delay timer: Q=TRUE after IN has been TRUE for PT duration, ET counts up), TOF (off-delay timer: Q stays TRUE for PT duration after IN goes FALSE), TP (pulse timer: Q=TRUE for exactly PT duration after IN rising edge). Each shows block symbol with BOOL IN, TIME PT inputs and BOOL Q, TIME ET outputs. Purpose: IEC 61131-3 timer function block reference.

> **[Figure]** Reference table showing IEC 61131-3 switch and memory function blocks. Title: 'Switches, selectors'. Shows ASWI, BSWI, AMEM, BMEM function blocks with block symbols, I/O types, and behavioral descriptions. Purpose: PAL1131 selection/memory function block reference (duplicate of p95_i2 content).

> **[Figure]** Reference table showing PAL1131 filter function blocks. Title: Filters. Two entries: FILT block (inputs: REAL IN, TIME T, BOOL R; output: REAL OUT) - FILT lag filter: OUT = 1/(T_s+1) * IN for R=FALSE; OUT = IN for R=TRUE. DIFR block (inputs: REAL IN, TIME T, BOOL R; output: REAL OUT) - DIFR lead filter (differentiation): OUT = T_s/(T_s+1) * IN for R=FALSE; OUT = IN for R=TRUE. Purpose: PAL1131 standard library reference for first-order lag and differentiation filter function blocks used in MEGA-GUARD control programs.

> **[Figure]** Reference table showing IEC 61131-3 flip-flops, pulsers, and special blocks. Title: 'Flip-flops, pulsers'. Sections: DFF (D flip-flop), TFF (T flip-flop), JKFF (JK flip-flop with truth table), RSFF (RS flip-flop with NQ output), SRFF (SR flip-flop with NQ output), DELS (delay by one cycle: Q(n)=IN(n-1)), GENR (alarm generator: oscillates between TRUE/FALSE based on IN1/IN2 frequency inputs), PDUR (pulse duration: OUT=time IN was TRUE). Purpose: extended PAL1131 function block library reference for flip-flops and signal generators.

> **[Figure]** Reference table showing PAL1131 alarm detection function blocks. Title: Alarms blocks. Two entries: APON block (inputs: BOOL R; output: BOOL Q) - Warm restart (after power break). ASTR block (inputs: BOOL R; output: BOOL Q) - Cold start (memory cleared, initial values). Purpose: PAL1131 standard library reference for system startup/restart detection function blocks used to handle power restoration logic in MEGA-GUARD controllers.

| [INFO] |  | ASWI, BSWI and LIMT blocks can be replaced by SEL and LIMIT functions (see earlier). |  |
| --- | --- | --- | --- | |
|  |  | SEL automatically recognizes type of inputs. |  |

#### 5.9.3.3 System blocks

They are ”always available”, so no library is needed. Alarms R – reset input Q – alarm output Alarm condition is indicated by TRUE at the output Q. Setting R to TRUE cancels the alarm.

> **[Figure]** Reference table showing IEC 61131-3 'Others' function blocks. Title: 'Others'. Sections: DEBA (dead-band: OUT=0 for |IN|<DB, OUT=IN+-DB for |IN|>=DB), LIMT (limiter: OUT=IN for MN<IN<MX, OUT=MN for IN<MN, OUT=MX for IN>MX), RAND (random: normal distribution N(IN1,IN2) for S=FALSE, rectangular distribution for S=TRUE). Purpose: PAL1131 signal conditioning function block reference.

Cold start is also initiated when memory test detects data error. Global variables are then set to initial values.

Example Declarations VAR

## STATE:APON; RESET:BOOL; ALARM:BOOL;

`END_VAR;`

Usage

## RESET:=FALSE; STATE(R:=RESET); ALARM:=STATE.Q;

## 5.10 SUPPLEMENTS

### 5.10.1 Correcting variable list

Suppose the Global variable list looks initially as follows:

• Incorrect address New group of two variables, MOTOR and PUMP, is declared, the first one with wrong address 0002. Clicking Add supplements the list with the two variables, however the line MOTOR is shown in red indicating address collision.

> **[Figure]** Screenshot of PAL1131 'Global variable list' dialog showing hardware I/O variables. Declared variables: START (BOOL, global hardware I/O, %0000=>0), STOP (BOOL, global hardware I/O, %0001=>1), ALARM (BOOL, global hardware I/O, %0002=>2). Add/Remove/Replace buttons visible. Purpose: global variable list with hardware address mapping for digital I/O variables in the START_STOP project.

As in the START_STOP project, MOTOR and PUMP should be located at 0008, 0009.

• Group selection Select the lines to be corrected, the second one with Shift or Ctrl. Names of variables, types and addresses appear in the upper cells (cell Type would be empty for different types).

• Corrections Selection of Address option automatically displays first free address for the colliding MOTOR, so 0004 here.

If you pressed Replace now, PUMP would remain at 0003 and MOTOR placed at 0004. However, we want 0008 instead of 0004.

Pressing Replace corrects the variable list accordingly.

Note that five bytes from 0003 to 0007 remain empty.

### 5.10.2 Filling empty areas

Suppose we need another REAL variable called ANALOG. Enter name and type, select Address option. First free address D0001 is then indicated.

Since ANALOG occupies four bytes (REAL), so the address of its first byte is 0001*4=0004. Pressing Add displays the following list

Former empty area is almost full now.

### 5.10.3 Marks

Small rectangles with digits indicating portions of large programs, to improve clarity and navigation, are called marks (or bookmarks). Portion of a code with two marks is shown below.

> **[Vector Diagram — Page 105]** Page 105 documents PAL1131 keyboard shortcuts, compiler message icon meanings, and the message format for error indication in the PAL1131 development environment.

Keyboard Shortcuts Table. Type: Quick reference table. Keyboard shortcuts for PAL1131 editor:
- Ctrl+Up: Scroll line up; Ctrl+Down: Scroll line down
- Ctrl+Home: Jump to first line; Ctrl+End: Jump to last line
- Ctrl+I: Insert line; Ctrl+Delete: Delete line
- Shift+Del: Cut selected; Shift+Ins: Paste from clipboard
- Alt+Bksp: Undo; Ctrl+Y: Redo
- Ctrl+C: Copy selected; Ctrl+V: Paste
- Del: Delete selected
- Ctrl+F: Find; Ctrl+M: Bookmark
- Shift+Ctrl+A: Select all
- Shift+Ctrl+N: Block unindent
- Shift+Ctrl+0..9: Set mark 0-9; Shift+Ctrl+0..9 (second): Go to mark 0-9

Compiler Message Icons Table. Type: Icon legend. Icons in PAL1131 compiler output (Build message window):
- Red circle with X: Error
- Yellow triangle with !: Warning
- Blue circle with i: Information
- Question mark: Question

Message Format: [Icon][filename:line] description. Example: Red X error shown with code reference [FBD_Program:5] and description text. Double-clicking a message in the message window jumps to the corresponding line of code in the editor.

Page 105 is from sections 5.10 ('Shortcuts, hints') and 5.10.4 ('Errors, warnings, hints'). The shortcuts apply to the PAL1131 text (ST/LD/FBD) editor for developing MEGA-GUARD XP controller programs.

The following shortcuts handle marks: • Shift + Ctrl + 0,...,9 – create a mark 0,...,9 at the line indicated by the cursor • Ctrl + 0,...,9 – place cursor at the line with mark 0,...,9

| Shortcuts | Operation |  | Shortcuts | Operation |
| --- | --- | --- | --- | --- | |
| Ctrl+Up | Scroll line up |  | Shift+Ctrl+I | Block indent |
| Ctrl+Down | Scroll line down |  | Shift+Ctrl+U | Block unindent |
| Ctrl+PgUp | Scroll screen up |  | Ctrl+M | Break line |
| Ctrl+PgDown | Scroll screen down |  | Ctrl+H | Insert line |
| Ctrl+Home | Editor top |  | Ctrl+T | Delete word |
| Ctrl+End | Editor end |  | Ctrl+G | Delete line |
| Ins | Toggle insert/enter mode |  | Shift+Ctrl+Y | Delete till end of line |
| Ctrl+Ins | Copy selected part |  | Ctrl+0,...,9 | Go to mark 0,...,9 |
| Shift+Del | Delete selected part |  | Shift+Ctrl+0,...,9 | Set mark 0,...,9 |
| Shift+Ins | Paste from clipboard |  | Shift+Ctrl+N | Select by lines |
| Ctrl+Bksp | Remove last word |  | Shift+Ctrl+C | Select by columns |
| Alt+Bksp | Undo |  | Shift+Ctrl+L | Select full lines |
| Shift+Alt+Bksp | Redo |  | Shift+Ctrl+B | Match brackets |

### 5.10.4 Errors, warnings, hints

Message list Bottom area of interface window may show the following messages:

Icons from left table are used by the compiler. An error interrupts compilation, warning indicates possibility of erroneous code (or another reason, e.g. outdated library). A hint may point out that global variable is hidden by local one with the same name.

Message format: [icon] filename.cst@code_line message text Context menu clears message list or removes some of its components. Right table is reserved for future use in languages supported by .NET (e.g. C#). Code line A .cst file indicated in a message involves program code in ST language created by

> **[Vector Diagram — Page 106]** Page 106 covers PAL1131 error handling, compilation behavior for erroneous objects, project opening with version differences, and autocomplete usage in the PAL1131 IDE.

Diagram 1: PAL1131 Build Message Window Screenshot. Type: Software UI screenshot. Shows PAL1131 Build/Compile message window with error messages displayed. Columns: error icon, line number, code reference [FBD_Program:N], description text. The Build menu is shown with 'Project > Build' option visible.

Text: Omitting Erroneous Objects. The compiler will skip an object (program, function block) if it has errors and compile the rest of the project. Error objects are shown in red in the project tree. Subsequent objects should not depend on erroneous ones for successful compilation.

Text: Project Opening with Different PAL1131 Version. When opening an older project, PAL1131 displays a warning that it was compiled with an older version. The project still opens but some features may behave differently. A note icon appears to flag the version discrepancy.

Text: Autocomplete Details. Double-clicking an error message in the message window opens the code at the associated line. Context menu available by right-clicking in the message list. Autocomplete (Ctrl+JUMP) completes variable and function block names.

Text: Compiling (Build). Project compilation: Select Project > Build. Errors in first compilation prevent second compilation of dependent blocks. Autocomplete list is populated from project > Add Item. Page 106 is from section 5.10.4 ('Errors, warnings, hints') of the Engineering Guide.

Project > Build. Double clicking the message opens POU editor with cursor at erroneous line. Sometimes however, the error may be somewhere else. If the compiler is unable to find erroneous line, it indicates the line with number 0 or -1 (for instance, when task is not declared).

Omitting erroneous objects The compiler operates similarly to a stack. So an error in a component of IF instruction in a function block generates three messages: 1) error in the component, 2) error in IF, 3) error in function block. In addition, if the option Omit erroneous POU objects during compilation has been selected, fourth message warns that the next object is being compiled without completing the previous one. In this next object, even for correct code, an error may be detected due to omitting the earlier code.

Autocomplete Compilation of the project is a condition to display autocomplete list. It is convenient to compile the project after declaration of POUs to include datatype names, standard functions, etc. into the list. Second compilation should follow declaration of variables (clear message list before). Library update While opening an old project a warning may appear with information that library version of the project is different than the one being now used by PAL1131. The library reference will be automatically updated if, while closing the project, you answer Yes to the question Save changes in the project ...

### 5.10.5 Compiler directives

Directives are optional commands for the compiler to simplify coding, determine access to variables, save comments, etc. Format is the same as for standard comments except additional sign $ after initial (*. Four most useful directives are described below.

| Directive | Meaning |
| --- | --- | |
| (*$AUTO*) | Declaration VAR_EXTERNAL (*$AUTO*) END_VAR automatically inserts declarations from Global variable list into the program. |
| (*$READ*) | Variable declared in a program, as e.g. START: BOOL (*$READ*), is considered read only in this program. Other programs may write into it, however. |
| (*$WRITE*) | Variable declared in a program, as e.g. PUMP: BOOL (*$WRITE*), is considered write only in this program. Other programs may read it, however. |
| (*$VMASM*) | Part of a program written in Virtual Machine language. |

Other directives govern internal operations of the compiler. Directives are highlighted by the editor.

### 5.10.6 Simulation session

All data for simulation, i.e. variable list, individual windows and control panels, can be saved in a file to repeat simulation session in future. File > Save session or click Save as window involves default filename with .scp extension.

> **[Figure]** Simulation output table from PAL1131Sim showing variable values over time. Columns: Time, START, STOP, ALARM, MOTOR, PUMP. Rows: Time 200 (0,0,0,0,0), Time 400 (0,0,0,0,0), Time 2000 (1,0,0,1,0), Time 11000 (1,1,0,0,1), Time 16600 (1,1,0,0,0). This shows the START_STOP program simulation: at t=2000ms START=1 causes MOTOR=1; at t=11000ms STOP=1 causes MOTOR=0 but PUMP=1 (off-delay active); at t=16600 PUMP turns off. Purpose: simulation trace output demonstrating the START_STOP IEC 61131-3 program with on-delay and off-delay timer behavior.

Resuming the session File > Open session or click

Session may be also resumed while opening .dcp file (provided that .scp is in the same folder). Answer Yes to the question Do you want to open saved session as well? One of PAL1131Sim Program options enables automatic resuming.

### 5.10.7 Save results

Simulation results may be saved in an .out file by selecting Trace > Log output data. Filename is determined in Program options (Output file tab with and Path). Symbol in the status bar indicates logging. The .out file is a text file with variable values written in successive cycles. Variables from individual windows are logged only. Logging may be stopped by clicking the variable window with right button. A part of Start_Stop.out file is shown below. START is set in 2nd and STOP in 11th second.

Time is given in milliseconds (200 ms task cycle). Columns are separated by Tab. The file can be processed by MS Excel.

Simulation controlled automatically By selecting Trace > Read input data the simulator automatically sets values of variables from .inp file indicated in Program options (Output file tab). It is a text file (prepared earlier) of the same format as .out. Negative time terminates simulation.

### 5.10.8 PAL1131 files

Programs and libraries of PAL1131 package exchange data through files withextensions given in the table. Name of .xml basic file is default name for the others.

| Extension | Content |
| --- | --- | |
| .xml | Basic file of the project |
| .cst | Program code in ST language (text file) |
| .hcp | Project header created during compilation |
| .dcp | Intermediate file for simulator and configurer created during compilation |
| .xcp | Binary code of compiled program for virtual machine VM (runtime) |
| .lcp | Semi–compiled library |
| .scp | Simulation session |
| .inp | Input data for session executed automatically (text file) |
| .out | Session results (text file), e.g. for MS Excel |
| .xmc | Communication parameters (for SMC controller) |
| .html | Project report |
| .htm | Communication report (for SMC: parameters, task table) |

The .cst and .xcp files are created automatically during compilation. Recall that at the beginning it is convenient to create project folder for all files.

## 5.11 SOURCE CODES OF STANDARD BLOCKS

Implementations of IEC 61131–3 standard blocks are presented below, one for each of four groups. They may be of some help while learning ST programming using

## PAL1131.

SR flip–flop

**FUNCTION_BLOCK SR**

`VAR_INPUT`

S1: BOOL; (* set input *) R: BOOL; (* reset input *)

`END_VAR`

`VAR_OUTPUT`

Q1: BOOL; (* output *)

`END_VAR`

## Q1 :=S1 OR (NOT R AND Q1);

`END_FUNCTION_BLOCK`

R_TRIG rising edge detector

**FUNCTION_BLOCK R_TRIG**

`VAR_INPUT`

CLK : BOOL; (* input *)

`END_VAR`

`VAR_OUTPUT`

Q : BOOL; (* output *)

`END_VAR`

VAR CLKp : BOOL := FALSE; (* previous value of CLK input *)

`END_VAR`

Q := CLK AND NOT CLKp; CLKp := CLK;

`END_FUNCTION_BLOCK`

CTU up–counter

**FUNCTION_BLOCK CTU**

`VAR_INPUT`

CU : BOOL; (* up–count input *) R : BOOL; (* counter reset *) PV : INT; (* preset value – upper limit *)

`END_VAR`

`VAR_OUTPUT`

Q : BOOL; (* output set when limit reached *) CV : INT; (* current value *)

`END_VAR`

VAR CUp : BOOL := FALSE; (* previous value of CU input *)

`END_VAR`

IF R THEN (* if R = TRUE *)

`CV := 0;`

ELSE IF (CU AND NOT CUp) THEN (* if rising edge at CU input *)

## IF (CV < PV) THEN

CV := CV + 1; (* increment *)

`END_IF`

`END_IF`

`END_IF`

Q := CV >= PV; (* if CV >= PV, then Q := TRUE *) CUp := CU; (* save CU as previous *)

`END_FUNCTION_BLOCK`

• TP pulse timer (pulse of preset duration)

**FUNCTION_BLOCK TP**

VAR

stime: TIME; (* start time *)

`END_VAR`

`VAR_INPUT`

IN: BOOL; (* input *) PT: TIME; (* preset time *)

`END_VAR`

`VAR_OUTPUT`

Q: BOOL; (* output *) ET: TIME; (* elapsed time *)

`END_VAR`

IF NOT Q THEN (* state 0 or 2: *) IF IN THEN (* if rising edge at IN or waiting for IN=0 *) IF ET = t#0s THEN (*if rising edge at IN *) IF PT > t#0s THEN (* state 1: pulse time count *) stime := CUR_TIME(); (* save start time *) Q := TRUE; (* set the output Q *)

`END_IF`

ELSE (* state 2: wait for IN=0 *) Q := FALSE; (* reset Q *)

`END_IF`

ELSE (* state 0: wait for rising edge at IN *) ET := t#0s; (* reset elapsed time *)

`END_IF`

ELSE (* state 1: pulse time count *) ET := CUR_TIME() - stime; (* elapsed time update *) IF ET >= PT THEN (* if preset value reached *) Q := FALSE; (* reset Q *) ET := PT; (* elapsed := preset *)

`END_IF`

`END_IF`

`END_FUNCTION_BLOCK`

## 5.12 Differences from IEC 31131-3 Standard

1. Local declaration VAR cannot involve modifier AT to locate a variable (local variables are located automatically). 2. Global variable declaration cannot begin with AT. 3. VAR_EXTERNAL is used in programs only (not in function blocks). 4. Access paths declared by VAR_ACCESS are not handled. 5. Identifiers are associated with name spaces (ranges of identifier names). Identifier name must be unique in any space. Each project or imported library is a separate name space. Short names of identifiers in different spaces may be the same. Finding short name is executed as follows: a) Directly in current space, in which the name is called b) In imported space (library), but at the main level only and depending on call type (call with determined type category, call with any type category); name matching in other spaces is also checked. If the same name is found, an error of identifier ambiguity is raised („Ambiguous ...”, „Multiple name found ...”, etc.). If this happens, full name in the form NAMESPACE.IDENTIFIER must be used. Name spaces of the system involves

dollar sign ( $ ), e.g. $DEFAULT, $VMSYS . To get into such space in case of ambiguity, use directive NS (NameSpace) for instance (*$NS $DEFAULT*)ADD(3, 4). 6. Non-decimal numbers are entered as character string with: 1) base of number system (in decimal form), 2) the sign #, 3) alphanumeric string. For instance 5#24 means 14 decimal. So non-computer systems, e.g. base 3, 4 etc., are also supported. 7. Numeric literal may appear in declaration of non-numeric types, e.g. BOOL#1, WORD#16#55AA. Numeric literal without the dot ( . ) is of the type INT, and with the dot of the type REAL. Type of a constant may be implied in some cases. 8. Optional inputs to function blocks are defined by: 1) initial value of the input, 2) and/or directive PAROPT after name of the input. 9. Configuration elements declared by the following keyword constructions are not allowed: CONFIGURATION , RESOURCE ... ON ... , TASK ...(INTERVAL := ..., PRIORITY := ...) , PROGRAM ... WITH ... : ... etc. Tasks are declared by means of directive TASKS. 10. So far, user types declared by TYPE ... END_TYPE are permitted for structures and arrays only. Other types, such as aliases (e.g. USINT, UINT, UDINT), enumeration and subrange are not implemented yet. Elementary data types must be used instead. 11. STRING type is not handled by the compiler (Unknown type error appears). 12. Entry point of CASE instruction (sequence before the colon: ) requires constant or constants. Identifiers declared as constants (or expressions) are not allowed. Compiler does not check, whether ranges of entry points do not overlap, and whether types of entries correspond to the type of CASE control variable. 13. Type of FOR loop is determined by increment constant that follows BY keyword (if used). For negative constant the system checks whether loop control variable is greater or equal to final value; for positive constant it checks whether the variable is less or equal to the final value. Increment constant cannot be 0. 14. Contrary to function blocks, assignments to parameter names are not allowed while calling a function (no matter whether the function is built-in, user-defined, or in-line). For instance, function call may look like X := SEL(BWY, P, 1); , whereas function block call is BSWI1(S:=BWY, IN1 := Pb, IN2 := TRUE); Parameters of function block call may appear in any order (names matter), whereas order of function parameter is fixed (as defined by the programmer). 15. Communication blocks COM_SM x (for SMC controller) are specific examples of function blocks not being called during program execution. The blocks merely reserve memory space for data of communication subsystem. Assignment of outputs directly in the block call is not permitted. Inputs denoted as constants (e.g. slave number) must have the same value in each of corresponding instances.

## 5.13 Example code

This paragraph contains examples to use for reference or learning.

### 5.13.1 Time Example

Following sample code shows how to work with reading clock and time variables and functions:

> **[Figure]** Screenshot of PAL1131 code editor showing TIME_EXAMPLE program (ST language). Lines 001-024: PROGRAM TIME_EXAMPLE, VAR: T1/T2/T3:TIME, C1:FINT, DT1/DT2:DATE_AND_TIME, LATER:BOOL. Code: T1:=CUR_TIME() (GET SYSTEM CLOCK), T2:=T#1h30m30s (SET VARIABLE MANUAL), T3:=T1+T2, C1:=TIME_TO_FINT(T1) (CONVERT TIME TO FINT TO USE ON CHANNEL), DT1:=READ_RTC(), DT2:=DATE_AND_TIME#2016-07-24-12:30:45, LATER:=DT1>DT2, END_PROGRAM. Purpose: example program demonstrating time and date manipulation functions in PAL1131.

## 6 PAGE (MIMIC GRAPHICS)

## 6.1 Introduction

Page is an application that enables modification of Mega-Guard Graphic files (Mimics). This is usually done during project engineering but it can be used via Marine PC at any time to include latest modifications on the vessel. This manual will provide information on how to use GraphicEditor.exe program.

### 6.1.1 Mega-Guard Page hardware & software requirements

> **[Figure]** Screenshot of MEGA-GUARD Editor warning dialog. Title: Editor. Warning icon (yellow triangle with exclamation). Message: Running without Administrator rights. The application appears to be running without Administrator rights. You can use the editor, but communication with the IO Server will probably not work. (This is due to limitations in the IO Server.). To always run the Editor with Administrator rights, try enabling Run as Administrator in the Compatibility tab of the executable file properties. Show this message next time checkbox (checked). OK button. Purpose: MEGA-GUARD PAL editor administrator rights warning dialog that appears when the engineering software is not run as Administrator.

Page requires a 4GB or larger CompactFlash disk or SSD with Windows 7 or 10 Embedded including SP1 (Service Pack 1). The installation vcredist_2015_x86 from Microsoft Visual Studio 2015 should also be installed. The Windows system must include DirectX / Direct2D system.

### 6.1.2 Running Page application

When running Page please note the following.

• Page requires .pat files with graphics / mimics. It does not work with .g (Loox) graphic files from previous release. The graphic files can be placed/found in the Mega-Guard Setup\Mimics folder. Loox editor is still available in this release for backwards compatibility.

### 6.1.3 Administration rights

MEGA-GUARD software requires Administrator rights to work. On your laptop you can start Page without administration rights, but it will show this warning:

This can be discarted with OK. It will not be possible to show live values during testing.

### 6.1.4 Program Window layout and basics for editing

Once the Graphic Edit program has started it shows a left a main drawing area with buttons and properties besides it:

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw (Container editor) main window. Title bar shows 'Container - Untitled*'. Ribbon toolbar with Edit, Create, Font, Format, Corner Rounding, Start/Stop, IO Server sections. Drawing toolbar has Line, Arc, TextBox, Rectangle, Polyline, Panel, Ellipse, Bezier, More. Left Properties panel shows RootElement properties: X/Y 0, Width 1024, Height 768, GridSpacing 20, CoordSysPlacement TopLeft. Right is blank drawing canvas. Purpose: CAMDraw graphic editor for creating MEGA-GUARD HMI mimic screens.

• Pressing a button with an element in the top button bar will start drawing procedure • Pressing Escape will cancel drawing procedure. • Mouse scroll wheel can be used to zoom in and out. • Clicking on an element in the drawing area will select it. • Pressing Delete will remove all selected elements

### 6.1.5 Help during drawing

During drawing a text balloon will be displayed with some help to guide you through the drawing process.

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw container editor with container properties panel showing COMMON, LAYOUT and MISC sections. Canvas shows a selected container element with orange dashed outline and resize handles. Hint tooltips shown: 'Rotate the mouse wheel for zooming...', 'Place new elements from the Elements section...'. Purpose: CAMDraw container element being created with properties.

For example, this hint is displayed when drawing an element:

### 6.1.6 Zooming and panning

To zoom in (enlarge view) the mouse wheel can be used. The zoom action will use the actual mouse position to zoom into. For panning (move the view) the wheel mouse has to be pressed and dragged.

For example, when the mouse is on an element at the left side of the screen this element will remain at the left side while zooming in or out. All other elements will move because of the scaling.

### 6.1.7 The context menu

With a right click on an element in the drawing area a context menu will be displayed. This context menu shows which allows a variety of actions is brought up..

### 6.1.8 Colors

The elements in the Graphic have a color from color table. This color table holds a set of colors for each element for day, night, dusk and dawn. On this manner dimming is handled.

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw 'Color Selection' dialog. Table with columns: Color Name, Predefined (*), Day, Dawn, Dusk, Night. Colors listed: Background, Foreground (selected), Grid, AlarmRed, NoAlarmGreen, PanelFace, ButtonFill, ButtonOutline, Comment, Transparent (Alpha=0 in all modes), SelectedTextBackground, MissingColor (pink/magenta), InactivePanelFace, OldAlarm (yellow). Copy All Colors to Clipboard, Paste Colors from Clipboard, OK, Cancel buttons. Purpose: CAMDraw color theme configuration for different display lighting modes.

## 6.2 Drawing

Pagecan draw a number of elements. Each element has its own properties.

### 6.2.1 Drawing a line

To draw a line do as follows:

1. Press the Line button in the top button bar 2. Click in drawing area to set line start 3. Click in drawing area to set line end 4. Adjust line settings in the properties list at the left

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a Line element selected. Properties panel shows: Width 4, P0 140;140, P0CapStyle Flat, P1 340;140, P1CapStyle Flat, Color Foreground (highlighted black), LineStyle Flat. Canvas shows a horizontal line element with blue endpoint handles. Purpose: CAMDraw line element properties configuration.

|  |  |  | Grid will be applied unless Alt is pressed. |
| --- | --- | --- | --- | |

The properties can be used to change appearance of the line: • Visible will hide the line if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element • Width is thickness of the line in pixels • P0, P1 start and end point of the line • P0CapStyle and P1CapStyle can be Flat for normal line ending or Arrow • P0CapSize and P1CapSize hold number of pixels in size for the Arrow • Color sets the color of the line from the color selection table • LineStyle sets the type of line as a 3D style using shade effect.

### 6.2.2 Drawing a rectangle

To draw a line do as follows:

1. Press the Rectangle button in the top button bar 2. Click in drawing area to set rectangle left top 3. Click in drawing area to set rectangle right bottom 4. Adjust rectangle settings in the properties list at the left

|  |  |  | Mouse scroll wheel can be used to zoom in and out. |
| --- | --- | --- | --- | |

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a Rectangle element selected. Properties: X 100, Y 100, Width 180, Height 140, BorderWidth 3 (highlighted blue), BorderStyle Flat, BorderColor Foreground, FillStyle Solid, FillColor Background, CornerRoundRadius 0. Canvas shows a rectangle with blue selection handles. Purpose: CAMDraw rectangle element properties.

The properties can be used to change appearance of the line: • Visible will hide the rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • BorderWidth sets the rectangle edge line thickness • BorderStyle sets the 3D line type (sunken, raised) • BorderColor sets color via the reference to the Color table • FillStyle sets 3D gradient for filling the rectangle • FillColor sets the color used for the Gradient (with white as second color) • CornerRoundRadius sets the edge corner of the rectangle to be rounded

### 6.2.3 Drawing a Circle or Ellipse

To draw a circle or ellipse do as follows:

1. Press the Ellipse button in the top button bar 2. Click in drawing area to set ellipse center 3. Click in drawing area to set ellipse radius 4. Adjust ellipse settings in the properties list at the left

|  |  |  | Mouse scroll wheel can be used to zoom in and out. |
| --- | --- | --- | --- | |

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with an Ellipse element being created. Properties: Center 160;240, Radius 120;60, AngleStart 0, AngleLength 360, ArcCloseStyle Pie, BorderWidth 1, BorderColor Foreground, FillColor Background, FillStyle Solid. Canvas shows ellipse being drawn with radiusX/Y tooltip. Purpose: CAMDraw ellipse/arc element creation.

The properties can be used to change appearance of the line: • Visible will hide the ellipse if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashing (displaying and hiding twice per second) • Name is text string with user definable name for the element • Center are the coordinates for the left top point • Radius is distance from center to edge, in length and height direction • AngleStart, and AngleLength can be set to make an Arc from the Ellipse • AngleCloseStyle and OutlineClosed can modify an Arc to a Pie with edge lines • BorderWidth sets the line thickness • BorderStyle sets the 3D line type (flat, sunken, raised) • BorderColor sets color via the reference to the Color table • FillColor sets the color for fill color

• FillStyle sets 3D gradient for filling the rectangle

### 6.2.4 Drawing a Circle or Ellipse Arc

To draw an arc do as follows:

1. Press the Arc button in the top button bar 2. Click in drawing area to set arc center 3. Click in drawing area to set arc radius 4. Click in drawing area to set arc start angle 5. Click in drawing area to set arc end angle

6. Select property OutlineClosed and set it to True 7. Adjust ellipse settings in the properties list at the left

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with arc/partial ellipse elements. Properties panel shows Ellipse: Center 480;220, Radius 140;60, AngleStart 0, AngleLength 50, ArcCloseStyle Pie, OutlineClosed True, BorderColor Foreground (highlighted black). Canvas shows two arc segments (partial ellipses). Purpose: CAMDraw arc/partial ellipse element with AngleLength=50 degrees.

|  |  |  | Arcs are same element type as Circle and Ellipse. |
| --- | --- | --- | --- | |

For properties explanation see previous paragraph with Circle and Ellipse.

### 6.2.5 Drawing a Polyline

Polylines are shapes with a flexible number of edges. Each edge can be drawn with different length and angle. To draw a polyline do as follows:

1. Press the Arc button in the top button bar 2. Click in drawing area to set polyline start point 3. Click in drawing area to set next polyline point, repeat this until before last point 4. Double click in drawing area to set last polyline point

5. Select property ClosedOutline and set it to True 6. Adjust polyline settings in the properties list at the left

|  |  |  | Arcs are same element type as Circle and Ellipse. |
| --- | --- | --- | --- | |

The properties can be used to change appearance of the line: • Visible will hide the ellipse if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashing (displaying and hiding twice per second) • Name is text string with user definable name for the element • LineColor sets color via the reference to the Color table • FillColor sets the color for fill color • Width is thickness of the edge line in pixels • ClosedOutline will make draw an edge line between first and last point

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a closed Polyline element. Properties: LineColor Foreground (black highlighted), FillColor PanelFace (grey highlighted), Width 1, ClosedOutline True. Canvas shows a grey filled pentagon/polygon shape with blue selection handles. Purpose: CAMDraw polyline element configured as a closed filled polygon.

### 6.2.6 Drawing a Bezier (not implemented at this time)

Beziers are shapes with a flexible number of rounded edges. Each edge can be drawn with different length and angle. To draw a Bezier do as follows:

1. Press the Bezier button in the top button bar 2. Click in drawing area to set Bezier start point 3. Click in drawing area to set next Bezier point, repeat this until before last point 4. Double click in drawing area to set last polyline point

5. Select property OutlineClosed and set it to True 6. Adjust bezier settings in the properties list at the left

|  |  |  | Beziers are not implemented yet. |
| --- | --- | --- | --- | |

### 6.2.7 Drawing Text

To add text to the graphic use the Text tool as follows:

1. Press the Text button in the top button bar 2. Click in drawing area to set point above left top of the text 3. Click in drawing area to set point above right bottom of the text 4. Click on “(text)” in the text box to enter text 5. Adjust text settings in the properties list at the left

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a TextBox element. Properties: X 100, Y 140, Width 200, Height 100, BorderWidth 1, BorderStyle Flat, BorderColor Foreground (black highlighted), FillStyle HorizontalLighting, FillColor ButtonFill, CornerRoundRadius 0. Canvas shows a grey textbox with 'Example text' label. Purpose: CAMDraw TextBox element configuration.

The properties can be used to change appearance of the text box: • Visible will hide the text and rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • BorderWidth sets the rectangle edge line thickness • BorderStyle sets the 3D line type (sunken, raised) • BorderColor sets color via the reference to the Color table • FillStyle sets 3D gradient for filling the rectangle • FillColor sets the color used for the Gradient (with white as second color) • CornerRoundRadius sets the edge corner of the rectangle to be rounded

### 6.2.8 Drawing a Panel

Panels are collections of objects that can be displayed or hidden together.

1. Press the Panel button in the top button bar 2. Click in drawing area to set left top of the panel 3. Click in drawing area to set point right bottom of the panel 4. Adjust panel settings in the properties list at the left 5. Add other elements to the panel by drawing these inside panel region

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a Panel (Container sub-element) selected. Properties: X 140, Y 110, Width 400, Height 260, GridSpacing 20, BorderWidth 2, BorderStyle Raised, BorderColor PanelFace, FillColor PanelFace. Canvas shows a panel containing an ellipse and rectangle with X/Y arrows. Purpose: CAMDraw Panel container element used to group child elements.

The properties can be used to change appearance of the panel: • Visible will hide the panel if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • Gridspacing allows to use different mouse snap settings as drawing aid • CoordSysPlacement allows for 0,0 point at left top or at center of the panel • ChildrenRotation is angle in degrees for rotate of panel contents • BorderWidth sets the panel edge line thickness • BorderStyle sets the 3D line type (sunken, raised) • BorderColor sets color via the reference to the Color table • FillColor sets the color used for the Gradient (with white as second color) • CornerRoundRadius sets the edge corner of the panel edge to be rounded

### 6.2.9 Drawing an Image

Images are bitmapped stored in external files. These can be of type GIF, PNG, JPG.

1. Press the More and then the Image button in the top button bar 2. Select an image file 3. Click in drawing area to set center of the image 4. Adjust image properties at the left of the window

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with an Image element. Properties: X 364, Y 344, Width 32, Height 32, FilePath calendar-icon.png. Canvas shows the calendar icon (32x32 pixel). Purpose: CAMDraw Image element used to display static icon graphics on mimic screens.

The properties can be used to change appearance of the image: • Visible will hide the image if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashing (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the center point • Width is distance from left to right, Height is distance from top to bottom • FilePath holds relative folder and file name in the Mimics folder

|  | If the image is rescaled but the original size must be restored it is possible to right click on the image and select “Restore Size to 100%” |  |  |  |
| --- | --- | --- | --- | --- | |

| If the image is rescaled but the original size must be restored |
| --- | |
| it is possible to right click on the image and select “Restore |
| Size to 100%” |

### 6.2.10 Drawing a FillBar

FillBar is an indication to show graphically how much the value of a channel is. It does this by coloring a rectangle from one side to the other depending on a value. This can for example be used to display how much of a tank is filled or how much power a thruster is using.

1. Press the More and then the Image button in the top button bar 2. Click in drawing area to set left top of the fill bar 3. Adjust image properties at the left of the window

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a FillBar element. Properties: X 320, Y 330, Width 200, Height 60, FillDirection LeftToRight, RangeLow 0, RangeHigh 100, LimitType LowAndHigh, FirstLimit 25, SecondLimit 75, LimitMarkerSize 10, Value 50, NormalColor NoAlarmGreen (green highlighted), LimitLowColor AlarmRed, LimitHighColor AlarmRed (red highlighted), EmptyColor Background. Canvas shows a horizontal bar gauge in green with red limit markers. Purpose: CAMDraw FillBar element for displaying analog values with alarm limits.

The properties can be used to change appearance of the FillBar: • Visible will hide the image if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashing (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the center point • Width is distance from left to right, Height is distance from top to bottom • FillDirection can be set to left, right, top (up) or bottom (down) • RangeLow holds value where the FillBar begins to fill (lower values will not show) • RangeHigh holds value where the FillBar is filled (higher values will not show) • LimitType can choose between None, Very Low and Low, Low and High, High and Very High, or just Low or just High. This will set what the red marker lines show. • FirstLimit is the value for the first red marker. • SecondLimit is the value for the second red marker. • LimitMarkerSize is the value for the arrow of the red marker

• Value is the most important property of this list, it holds the actual value of the fill bar (how much is colored). • LimitLowColor values below the low limit will be colored according this setting • NormalColor values above the low limit and below the high limit will be colored according this setting • LimitHighColor values above the high limit will be colored according this setting • Empty color is the ‘background’ color to show when the value is below the low range. • BorderColor is the color of the edge • RoundingRadius sets the edge corner round radius • LineWidth sets the edge line width

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a Button element. Properties: X 300, Y 340, Width 160, Height 60, RoundRadius 5, Text 'button text', FillColor ButtonFill, FillStyle HorizontalLighting, OutlineColor ButtonOutline (blue highlighted), TextColor Foreground (black highlighted), HorzAlignment Center, VertAlignment Center, ClickActions (empty). Canvas shows a grey button labeled 'button text'. Purpose: CAMDraw Button element with click action capability.

### 6.2.11 Drawing Button

To add a button to the graphic use the Text tool as follows:

1. Press the More and then the Image button in the top button bar 2. Click in drawing area to set point above left top of the button 3. Keep pressed drawing area to set point above right bottom of the button 4. Click on “(button)” in the button box to enter text 5. Adjust text settings in the properties list at the left

The properties can be used to change appearance of the text box: • Visible will hide the text and rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element

• X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • GridSpacing sets the mouse snap inside the button (unused at this time) • RoundRadius sets the edge corner of the rectangle to be rounded • Text is function description of the button displayed to users • FillColor sets the color used for the Gradient (with white as second color) • FillStyle sets 3D gradient for filling the rectangle • OutlineColor sets color via the reference to the Color table • TextColor sets function description text color via the reference to the Color table • HorzAlignment sets horizontal alignment to left, center or right • VertAlignment sets vertical alignment to top, center or bottom • ClickActions set function of the button (what to do if it is pressed)

> **[Figure]** Screenshot of the MEGA-GUARD PAL mimic editor showing a CheckBox object properties panel. Left panel shows Property/Value/Data Binding table: Visible=True, UserActionsLocked=False, FlashState=Off, Name=(empty), X=390, Y=350, Width=90, Height=70, FillColor=ButtonFill, OutlineColor=ButtonOutline (highlighted/selected blue), Width=3, OutlineStyle=Sunken, Checked=True. Right panel shows the mimic canvas with a blue checkbox element (square with checkmark) selected with resize handles at corners. Background is a grey grid canvas. Purpose: showing the property configuration of a CheckBox graphical element in the MEGA-GUARD PAL mimic/graphics editor.

### 6.2.12 Drawing Check Box

To add a check box to the graphic use the Check Box tool as follows:

1. Press the More and then the Image button in the top button bar 2. Click in drawing area to set center point of the CheckBox 3. Optionally: keep pressed drawing area to set point above right bottom of the button 4. Adjust text settings in the properties list at the left

The properties can be used to change appearance of the text box: • Visible will hide the text and rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom

• FillColor sets the color used for the Gradient (with white as second color) • OutlineColor sets color via the reference to the Color table • Width sets the size of the 3D bevel • OutlineLineStyle set line style of the check box • Checked is true for checked and false for not checked (use with your channel)

### 6.2.13 Drawing a Tab Panel

To add a panel with multiple tabs.

1. Press the More and then the Image button in the top button bar 2. Click in drawing area to set center point of the Tab Panel 3. Adjust text settings in the properties list at the left

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a TabPanel element. Properties: X 300, Y 280, Width 320, Height 240, HeaderVisible True, Font Segoe UI-18.0-B, SelectedPageIndex 0, MinTabSize 5, HeaderSide Top, ActiveTabColor Background, InactiveTabColor InactivePanelFace, LineColor Foreground (black highlighted). Canvas shows a tab panel with 'Page1 Page2 Page3' tabs. Purpose: CAMDraw TabPanel element for creating tabbed interface screens.

The properties can be used to change appearance of the text box: • Visible will hide the text and rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • Gridspacing allows to use different mouse snap settings as drawing aid • HeaderVisible allows to hide or display the Tab selection button at the top • Font sets the text font for the Tab name

• SelectedPageIndex allows to input a number that uniquely identifies a Tab Page • MinTabSize for setting tab size even if text is smaller • HeaderSide defines where tabs are drawn (Right, Left, Top, Bottom) • ActiveTabColor sets the color of the selected Tab Page button at the top • InactiveTabColor sets the color of the other Tab Page buttons at the top • LineColor sets the color used for the edge • TextColor sets the color used for the Tab Page Button Text

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a Frame element. Properties: X 130, Y 130, Width 300, Height 300, Path sample.prax. Canvas shows an oval/ellipse as placeholder for the frame content. Purpose: CAMDraw Frame element used to embed other mimic files as sub-frames.

|  |  | After selecting a Tab by pressing on the button with the Tab name and click inside |  |
| --- | --- | --- | --- | |
|  |  | the drawing region. Then elements can be added to the tab page and properties |  |
|  |  | of the tab page can be set. |  |

### 6.2.14 Inserting a Frame

Frames are rectangle shapes that refer to other graphic files. On this manner graphic files can be re-used so they only have to be drawn once.

To add a frame follow these steps:

1. Press the More and then the Image button in the top button bar 2. Click in drawing area to set center point of the Tab Panel 3. Adjust text settings in the properties list at the left

The properties can be used to change appearance of the text box: • Visible will hide the text and rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a Trending element. Properties: X 160, Y 220, Width 480, Height 160, DurationShown 30, DurationStored 300, LineColor Grid, FillColor Background, VerticalLineInt 5, ShowLegend True, ShowVerticalAxis True, Runs (3 entries). Canvas shows a trend chart with three colored lines with Y-axis range -100 to 100 and time axis. Purpose: CAMDraw Trending element for real-time trend display.

• X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • Path is the relative folder and file name inside the Mimic folder.

To draw a frame simply save a (small) graphic into a separate file. To edit a frame right click on the frame and select “Edit frame #”. The frame name will be given in the menu:

In this example the name of the frame file is “Frame_menu.prax”.

### 6.2.15 Drawing a Trending element

Trending elements show the history of a value in a diagram.

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw editor showing a context menu on a frame element. Menu options: Cut, Copy, Paste, Bring to Front, Send to Back, Restore Size to 100%, Edit Frame_Menu.prax (highlighted blue), Select RootElement, Select Frame. Canvas shows a menu bar with 'Monitoring', 'Diag...' (diagnostics) tabs. Purpose: CAMDraw context menu for editing an embedded frame file showing the 'Edit Frame_Menu.prax' option.

To add a trend follow these steps:

1. Press the More and then the Image button in the top button bar 2. Click in drawing area to set center point of the trend 3. Adjust text settings in the properties list at the left

The properties can be used to change appearance of the trend: • Visible will hide the text and rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashin (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • DurationShown sets the time in seconds displayed • DurationStored sets the time for values to keep in memory • LineColor sets edge line color • FillColor sets edge fill color • VerticalLineInterval number of seconds between vertical grid lines (zero for none) • Padding sets distance between legend descriptions of each value • ShowLedgend True for display legend, False to hide it • LegendFontSize sets font to draw text for each value • ShowVerticalAxes True for display vertical axis, False to hide • VerticalAxisFontSize set size of the description for all vertical axis • Runs set amount of values that are displayed as trend

### 6.2.16 Drawing an alarm list

Alarm list show the list of actual alarms with descriptions and status information

To add an alarm list follow these steps:

1. Press the More and then the Image button in the top button bar 2. Click in drawing area to set center point of the list 3. Adjust text settings in the properties list at the left

The properties can be used to change appearance of the trend: • Visible will hide the text and rectangle if it is set to false • UserActionsLocked can be set to False to enable mouse click on this element • FlashState will show element flashing (displaying and hiding twice per second) • Name is text string with user definable name for the element • X, Y are the coordinates for the left top point • Width is distance from left to right, Height is distance from top to bottom • HeaderVisible True for display header, False to hide • HeaderFillColor background color for header text • HeaderTextColor for header text color • HeaderFont font for header text • FillColor color for alarm list for odd alarm lines • AlternateFillColor color for alarm list for even alarm lines • TextColor Alarm text color for both odd and even lines • ShowTag display alarm tag column • ShowChannel display alarm channel number column • ShowDate display alarm date column • ShowTime display alarm time column • ShowReportType display alarm report grouping • ShowDescription display alarm description column • ShowValue display alarm value column • ShowUnits display alarm engineering units column • ShowLimits display alarm limits column • ShowDT display alarm delay time column • ShowStatus display alarm status column

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with an AlarmList element. Properties: X 96, Y 296, Width 768, Height 128, HeaderVisible True, HeaderFillColor ButtonFill, FillColor Background, AlternateFillColor InactivePanelFace, ShowTag True, ShowDescription True, ShowStatus True (other Show fields set False). Canvas shows an alarm list with headers: Tag, Description, Status. Purpose: CAMDraw AlarmList element for displaying alarm states on mimic screens.

### 6.2.17 Draw Group, Graphics, Diagnostic, Skip, Unavailable, Inhibit lists

This is implemented in similar way as the Alarm List from previous paragraph. Use any of the list options from the List insertion item in the menu:

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw with a WebBrowser element. Properties: Address b.google.com, Flash settings, Width 436, Height 281, X 114, Y 156. Canvas shows a partial view of Google homepage loaded in the browser element. Hint: 'User input disabled in the Editor.' Purpose: CAMDraw WebBrowser element for embedding web content in mimic screens.

From this point onward please follow directions from previous paragraph.

### 6.2.18 Drawing WebBrowser Element

WebBrowser elements can be used to show data from External Sources. This can be a webpage from local webserver, an IP Camera, a PDF file or other information sources as long as they are supported by the Internet Explorer version installed on the MarinePC. For PDF files the Adobe Acrobat Reader has been made available.

To add a Web Browser Element follow these steps: 1. Press the Web Browser

button and Click in drawing area to place it 2. In the properties dialog Select the Common Address option to input the desired web address. This can for example also be a local path to a PDF file 3. Save and open in CamClient to see the working result.

|  |  | If large files are used as PDF file it will decrease loading time of the Mimic. Best is |  |
| --- | --- | --- | --- | |
|  |  | to only add large PDF files in separate Mimics (not a frame in commonly used |  |
|  |  | mimic). |  |

## 6.3 Usage

In this chapter will be discussed how to best draw graphics with the GraphicEditor.

### 6.3.1 Button Bar (menu)

To navigate through the different graphic pages button bars can be used as a menu. Each button makes the system switch to a particular page. Because these buttons will be repeated on most pages it is best to place the buttons into a separate graphic file and to include this file into a full screen graphic as frame.

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw Container editor showing a completed Frame_Menu design with three buttons: 'Monitoring' (selected with orange handles), 'Diagnostics', 'Alarm'. Button properties: Text 'Monitoring', X 22.5, Y 12.5, Width 155, Height 35, RoundRadius 5, OutlineColor ButtonOutline (highlighted blue), ClickActions (one entry). Purpose: CAMDraw design for a navigation menu frame with Monitoring/Diagnostics/Alarm page buttons.

In the above example the buttons are placed horizontal next to each other. It is up to the project designers to reformat this to customer / project requirements.

|  |  |  |  | It is also possible to use a panel to split up a graphic into ‘pages’. Each panel tab |  |
| --- | --- | --- | --- | --- | --- | |
|  |  |  |  | can show graphics parts (elements) that use up the entire screen. |  |

In the Setup/Mimics/Lib folder the sample button bar is stored as Frame_Menu.pat. By storing the frames in a separate folder it is easier to distinguish between re-usable graphic parts of a graphic and full screen graphics. The full screen graphics are stored in the Setup/Mimics folder. Once a frame has been inserted into a graphic this frame file should remain in the same folder (else the system will not be able to display it).

### 6.3.2 Button to pulse a channel

To trigger a switch the button can be used with a pulse. To do this: Draw a button 1. Select Click action and press the + symbol

2. Select “Pulse Channel” from the Click Action selection dialog (left side) 3. Enter Channel Number for channel to pulse 4. Set PulseLength to define the period of time in milliseconds for pulse duration 5. Set PulseTypeHigh if channel signal should be high for period of time and PulseTypeLow if the channel signal should be low for period of time

> **[Figure]** Screenshot of a MEGA-GUARD CAMDraw Alarm mimic screen at runtime. Shows top navigation bar (Monitoring, Diagnostics, Alarm tabs - Alarm highlighted red). Main display shows FAIL boxes labeled 'Fire Alarm', 'EAS 1', 'EAS 2' (all red FAIL), 'Navlight', 'Server_1' (grey/normal), 'Server_2' (red/alarm), 'Switch_1', 'Switch_2', and two I/O module stacks. Alarm list at bottom: Tag 100134 'XP34 (AFAS PANEL) Not Present - Alarm!', Tag 100110 'XP01 - Not Present - Alarm!'. Praxis logo, time 17:06:12, date 8/19/2016. Purpose: MEGA-GUARD runtime alarm screen showing active alarms for fire alarm system, EAS, servers, and XP processors.

### 6.3.3 Diagnostics

Each module has a diagnostic channel that can be visualized graphically. To do this there are pre-configured frames available. Each frame displays the status of one module. For each module a frame has to be added to the diagnostic mimic.

> **[Figure]** Screenshot of MEGA-GUARD CAMDraw button element with ClickActions configured. Button: X 50, Y 290, Width 120, Height 40, Text 'on/off', OutlineColor ButtonOutline. ClickActions: Pulse Channel / Pulse Length 1000 / PulseType PulseTypeHigh. Canvas shows ship control mimic with buttons: 'Ahead on/off', 'Sea Regulation on/off', 'Astern on/off', 'Inland Regulations on/off', 'Navigation on/off', 'NUC on/off', 'RAM on/off', 'Short Towage on/off', 'Anchor on/off'. Purpose: CAMDraw navigation light control panel with pulse output click actions.

### 6.3.4 Draw valve frame example

This paragraph explains how to draw a valve in a frame so that it can be re-used. The methods that are used for this can also be used for other reusable components.

To draw a valve frame do as follows 1. Select File > New from the menu to create a new graphic file.

2. In layout section enter Width=100 and Height=50 for the size of the valve and set GridSpacing=2 to allow detailed drawing. 3. Select Polyline and click at left top, then left bottom, right top, right bottom and double click at left top to complete. 4. Select the Polyline and choose from menu Home > Format Fill > Select > “Background” color 5. Select the Polyline, right click on top of this with mouse and choose Copy. Right click a second time and choose Paste. Click at left top of the drawing area to insert the second polyline. 6. Select the second Polyline and choose from menu Home > Format Fill > Select “AlarmRed” color 7. Keep second Polyline selected and Press Layout > Visible > Bind

> **[Figure]** Screenshot of the MEGA-GUARD PAL Bind Property dialog for a mimic element. Title: Bind Property. Target Object field (empty), Target Property: Visible. Bindings panel (left, labeled only those usable for the property are shown): list includes Channel Limit, Channel 2nd Limit, Channel Alarm, Channel Alarm Not Ack, Channel Current Alarm (deprecated), Channel Lock, Channel Range High, Channel Range Low, Channel SensorFail, Channel Value, EAS Button Status, Fast Tick, Select Condition, Frame Property. Right panel TravelBinding section: ConvertParams: (none); ExportedPropertyName: ALARM (highlighted blue). Bottom: ExportedPropertyName (String) label. OK and Cancel buttons. Purpose: binding a mimic graphical element visibility property to the ALARM exported property name of a channel in the MEGA-GUARD PAL graphics editor.

Property button . The Bind Property dialog appears. 8. Select “Frame Property” and in ExportedPropertyName type “ALARM”. Press OK to close the bind property dialog. 9. Select File > Save to make the frame file. Give name “frame_valve” and press OK. 10. Select File > New from the menu to create a new graphic file. 11. Use Place Frame Element to Insert the “frame_valve” in the new graphic.

> **[Figure]** Screenshot of the MEGA-GUARD PAL mimic editor showing Project > Item menu with Export > Library submenu visible. Menu: Project (active) > Item submenu expanded showing Export > Library option. Background shows PAL1131 code editor with FB_PULSE function block code (FUNCTION_BLOCK FB_PULSE,  Pulse after,  Rising). Purpose: showing the PAL1131/PAL project export workflow for exporting function blocks as a library via Project > Item > Export > Library.

12. Press the Bind Property button in Properties > Exported the ALARM property. 13. Connect Channel Alarm property to a Channel in your project that shows alarm for this valve. 14. Save the graphic and open it in CamClient.

The graphic in CamClient will show a normal when the channel is not in alarm and a red valve when the channel is in alarm. Steps 11 to 13 can be repeated to add multiple valves connected to different channels.

# 7 PAL SETUP

## 7.1 Group Pages

After selecting ‘Groups’ and 1 – Group Description

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing channel Logging settings panel. Logging section: Logging checkbox (checked), Event Logging checkbox (unchecked), Allow Logging Control button (unchecked), Cyclic Storage checkbox (checked), Log OnChange checkbox (unchecked). Sample Rate in (s): 5. Disk storage rate (s): 300. Start/Stop Channel: 0. Log history (days): 100. Maximum usage of disk/memory per day: 2437.9 and 9.9 (two fields). Purpose: configuring trend data logging parameters for a MEGA-GUARD channel including sample rate, disk storage rate, and history retention.

Description Text for description or name of this group Display group To show this group on a Client. Default checked. Rarely unchecked (For example, uncheck for usage in Extended Alarm System).

### 7.1.1 General Settings

Select ‘Groups’ and ‘General Settings’

Maximum number of KB Indicates the size on disk what could be use for logging for all logging files

### 7.1.2 Workstation group Logging

Logging: Possibility to turn on logging for this group Event Logging: Log status changes of channel(s) belonging to this group (Alarm Summary per group) 1 channel per line Allow Logging Control: Is the user allow to turn off logging for this group Cycle Storage: Remove oldest log files Log OnChange: Log Channels and only log a new line when at least one of the channel value(s) is changed (group Can NOT be used for display Trending!). Sample Rate in (s): Time in seconds (default 5)*

> **[Vector Diagram — Page 139]** Page 139 covers MEGA-GUARD OWS data logging configuration, log file locations, SSD storage estimation, and Trend logging group configuration parameters.

Log File Locations (text): Default paths on the OWS Windows computer:
  ALARMLOG = d:\Software\Data\ALARMLOG
  DIAGNOSTICSLOG = d:\Software\Data\DIAGNOSTICSLOG
  HOURCOUNTER = d:\Software\Data\HOURCOUNTER
Note: A 60 GB SSD has approximately 30 GB Flash available for logging.

Table: SSD Storage Estimation for Trend Logging. Type: Technical specification table. Columns: Disk (GB), Terabyte before failure, Write speed MB/s:
  2 GB / 38.8 TB / 11 MB/s
  4 GB / 51.9 TB / 11 MB/s
  8 GB / 69.8 TB / 11 MB/s
  16 GB / 94.6 TB / 11 MB/s
  32 GB / 128 TB / 11 MB/s
  64 GB / ~131 TB / 11 MB/s

Memory Calculation Example: One day = 86400 seconds. At 5-second sample rate: 86400/5 = 17,280 samples/day. 17,280 * 117 bytes/sample = 2,021,760 bytes/day per channel.

Trend Logging Configuration Parameters Table. Type: Configuration parameter reference.
- Trend Replay: checkbox to enable trend replay for this group
- Time Span (hh:mm:ss): time span hours (default 400)
- High Limit: max value on trend graph
- Low Limit: min value on trend graph
- Trend Memory: checkbox to enable trending in Memory
- Min Value: minimum value applied by default
- Sample Rate (ms): (default not shown but referenced)

Page 139 is from section 7.1.4 ('Configure Alarm history, Log and Printing'). Documents OWS data storage configuration for MEGA-GUARD alarm/trend logging including file locations, memory calculation examples, and Trend Group replay configuration in iObserver.

Disk Storage rate (s): Time in seconds to store in memory, after this time the memory will be written to disk. Start/Stop Channel Channel which its value could start/stop logging process Log history (days) Number of days to keep log files Remark: If cycle storage is not checked then after this number of files the logging will be stopped automatically.

* For a list with more than 10 channels the sample rate is 5 or more, if a channel list contains 10 or less channels a sample rate of 1 sec is the minimum.

#### 7.1.2.1 Limitations Workstation group Logging

The CSV group logging it is possible to use a group with 1000 channels and 4x per second logging and simultaneously use a group with 2000 channels and 1x per second logging.

In Trend mimic any channel can be added and this will show this channel value history. In Trend mimic channel data can be exported to CSV file via pressing a button

Maximum usage of disk/memory per day (KB) gives an indication about the maximum ever to be used KB if logging for group is on. Memory requirements for logging

| General header Header per channel Per channel Sample time stamp Number of bytes in file header | 152 Bytes 90 Bytes 8 Bytes 21 Bytes 692 Bytes |
| --- | --- | |

Example: One day (60 seconds * 60 minutes * 24 hours) has 86400 seconds.

86400 / 5 = 17280 (=times taking a sample for all these channels in this group)

(12 channel values * 8 bytes) + 21 bytes (date + time) = 117 17280*117 = 2021760 bytes = 1974 KB = 1.92 MB

90 bytes (header info per channel) * 12 channels + 152 bytes (header general) = 1232

Results in total of (2021760+1232) / 1000 = 2022.9 (disk) (117 * 300 (=nr of samples to disk)) / 1000 = 35.5 (memory)

Example for calculating RAM memory requirements: To write once per hour with 5 seconds per sample: 3600 / 5 = 720 samples. For 12 channels 720 samples require (12 * 8 + 21) * 720 = 49.6 KB

#### 7.1.2.2 MarinePC disk logging (SSD) and path.ini log files location

Check the amount of space available on the MPC before using logging.

> **[Vector Diagram — Page 140]** Page 140 covers MEGA-GUARD OWS alarm acknowledgement sequence configuration and display behavior in the iObserver alarm management interface.

Diagram 1: Alarm Acknowledgement Sequence Table. Type: State transition/configuration table. Shows alarm acknowledge sequences based on settings (1=enabled, 0=disabled). Columns show channel display state in iObserver before and after acknowledgement, and Printer output.

Sequence diagram (settings=1): Alarm-Unacknowledged -> (user acknowledges) -> Alarm-Acknowledged -> (condition clears) -> Normal-Acknowledged. The 'Acknowledged' state remains visible until cleared.

Sequence diagram (settings=0): Alarm-Unacknowledged -> (condition clears) -> Normal-Unacknowledged. No explicit acknowledgement state required.

Diagram 2: OWS Acknowledge Display Example. Type: Configuration sequence reference. When 'Along side' / acknowledge setting = 1: extra alarm state shown on acknowledgement. When setting = 0: simplified flow without extra state.

Text describes: sequence setting controls whether an 'Acknowledged' state is required after alarm returns to Normal. Setting = 1 requires both Acknowledge and Normal-clear steps. Setting = 0 only tracks Alarm and Normal states.

Page 140 is from section 7.1.4 of the Engineering Guide. These settings configure how MEGA-GUARD OWS iObserver displays alarm acknowledgement states, matching IEC/marine class society requirements for unmanned machinery spaces (UMS).

|  | [INFO] |  |  | A 60 GB SSD approximately has 30GB Flash available for system files and logging. |  |
| --- | --- | --- | --- | --- | --- | |

The preferred location of the log files is \: D:\Software\Data

The log file location is configured in this file:

D:\Software\System\path.ini

**[PATH]**

ALARMLOG= d:\Software\Data\ALARMLOG DIAGNOSTICLOG= d:\Software\Data\DIAGNOSTICLOG GROUPLOG= d:\Software\Data\GROUPLog HOURCOUNTER= d:\Software\Data\HOURCOUNTER

Above configuration is recommended for all projects.

### 7.1.3 Workstation Alarm History, Logging and Printing

Alarm display in History view can be configured depending on class requirements. The alarms will be logged and printed same as displayed in Alarm History. These Settings in the IOServer.ini [Settings] section are controlling Alarm logging.

[Settings] …. #Set to 1 for Report print line on acknowledgement while in alarm

`REPORTACKEDALARMS=0`

#Set to 1 for Report print line on status change to normal while unacknowledged

`REPORTBACKTONORMALALARMS=0`

….

When the settings are set to 1, then extra alarm lines are displayed on acknowledgement

| Sequence: | Channel in alarm |  |  |  |
| --- | --- | --- | --- | --- | |
|  | Channel returns to normal |  |  |  |
|  | Alarm -> Normal -> Acknowledge |  | Alarm -> Acknowledge -> Normal |  |
| IOServer.ini -> [Settings] |  |  |  |  |
| REPORTACKEDALARMS=0 REPORTBACKTONORMALALARMS=0 | Alarm - UnAcknowledged Normal - Acknowledged |  | Alarm - UnAcknowledged Normal - Acknowledged |  |
| REPORTACKEDALARMS=1 REPORTBACKTONORMALALARMS=0 | Alarm - UnAcknowledged Normal - Acknowledged |  | Alarm - UnAcknowledged Alarm - Acknowledged Normal - Acknowledged |  |
| REPORTACKEDALARMS=1 REPORTBACKTONORMALALARMS=1 | Alarm - UnAcknowledged Normal - UnAcknowledged Normal - Acknowledged |  | Alarm - UnAcknowledged Alarm - Acknowledged Normal - Acknowledged |  |

| Channel in alarm |
| --- | |
| Channel Acknowledged by user |

> **[Vector Diagram — Page 141]** Page 141 documents OWS alarm history acknowledge sequence (continuation), log file extraction, PAL1131 TFT logging configuration, and workstation log file access rights.

Acknowledge Sequence Continuation Table (from page 140): Shows additional sequence rows:
- %REPORT%ALARMLOG=1: Alarm -> UnAcknowledged -> Normal -> Acknowledged (extra step)
- %REPORT%ALARMLOG=0: Alarm -> UnAcknowledged only (simplified)
Indicates how the OWS logs alarm-to-Normal transitions in the ALARMLOG CSV file.

Text: 'After changing the settings it is OK. You do not need to restart System (iObserver).' Describes live reconfiguration capability of MEGA-GUARD OWS alarm history settings.

Diagram: Alarm Sequence Examples (OWS iObserver alarm window screenshot). Type: Software UI screenshot. Shows two example alarm display sequences in iObserver alarm list view:
Example 1 (settings=1): '%REPORT%ALARMLOG=1  Alarm - UnAcknowledged' followed by '%REPORT%ALARMLOG=1  Normal - Acknowledged'
Example 2 (settings=0): '%REPORT%ALARMLOG=0  Alarm - UnAcknowledged' only.

PAL1131 TFT Logging Configuration Steps (section 7.1.5.5):
1. Start PAL1131 from D:\Software\System\PAL1131 (using the PAL project)
2. Go to Processor with TFT when logging needs to be established
The TFT (display panel on XP processor) logging configuration is transmitted from PAL1131 to the XP processor for on-panel display of MEGA-GUARD system status. Page 141 is from sections 7.1.4 and 7.1.5.5.

| REPORTACKEDALARMS=0 REPORTBACKTONORMALALARMS=1 | Alarm - UnAcknowledged Normal - UnAcknowledged Normal - Acknowledged | Alarm - UnAcknowledged Normal - Acknowledged |
| --- | --- | --- | |

After changing the settings it takes 30 seconds before these are active. You do not need to restart System (IOServer.exe).

### 7.1.4 Workstation Log file extraction rights

Users with Administration role can access Windows System to copy files onto the USB drives. These sensor logs are stored on the MPC flash drive in the folder:

D:\Software\Data

Users with specific roles that allow the extraction of log files is possible via a button in the Mimics without accessing the Windows system. During project Engineering the button will only be available for users with the proper roles (rights). This can be accomplished by using PAL to configure roles for specified groups according user specification.

### 7.1.5 TFT Logging

The 8.4” TFT operator panel of the TCU includes an alarm/status logger with real-time time stamping for maintenance purposes and a periodic data (trend) logger. The logged data is stored in the internal non-volatile flash memory of this operator panel. The logged data can be retrieved via Ethernet using the Firmware Installer tool.

#### 7.1.5.1 Real Time Clock

The data logger real-time clock keeps track of the current time and date for time-stamping the logged data. The (initial) time and date (UTC) are set via the parameter menus in the TCU operator panel. This can be password protected. When the TCS is used in a proprietary “Mega- Guard” Ethernet network (i.e. when integrated with other Mega-Guard equipment such as Alarm and Monitoring System or Dynamic Positioning System) then the data logger real-time clock is automatically synchronized with the Mega-Guard server workstations. The time and date formats are: • Time: HH:MM:SS (HH=hour in 24 hour format, MM=minute, SS=second) • Date: YYYY-MM-DD (DD=day, MM=month, YYYY= year)

#### 7.1.5.2 Alarm/Status Logging

All project alarms and status channels (• see project signal list) are logged on the TCU operator panel.

For every alarm channel the following situations trigger an event to be logged: Digital and analog alarm channels: 1. When the alarm condition changes 2. Where applicable, if the sensor is failed

For every status channel the following situations trigger an event to be logged:

Digital status channel: 1. On Active Only 2. On De-active Only 3. Both

Analog status channel: 1. When the status condition changes 2. Where applicable, if the sensor is failed.

For each alarm or status change that triggers an event, a total event counter value is increased and logged for statistical purposes. The data that is logged (actually: exported) per event: • Date : YYYY-MM-DD • Time : HH:MM:SS • Tag name : unique number to identify the signal (• see project signal list) • Value : analog value or 0/1 for digital status • Unit : Engineering unit e.g. “%”, “degC”, “rpm” • Event trigger : “<a>” for easy filtering of alarm events in the CSV “<s>” for easy filtering of status events in the CSV • Status : status text e.g. “normal”, “alarm”, “high”, “low”, “sensfail”

Additionally there is logged for statistics: • Event count: (+) ####, the counter is reset every 9999 alarm events, after the first reset the prefix shows “+”

Alarm and status events should be logged on change.

#### 7.1.5.3 Periodic Data (trend) Logging

The trends of the signals as indicated in the • project signal list are periodically logged on the TCU operator panel. Data samples that will be logged are:

Digital channel: 1. On Active Only 2. On De-active Only 3. Both

Analog channel: 1. Exceeding a preset deviation since last logged sample

For each of these three events there is also a total sample counter value logged for statistical purposes.

The data that is logged (actually: exported) per signal trend: • Date: YYYY-MM-DD

• Time: HH:MM:SS • Tag name: unique number to identify the signal (• see project signal list) • Value: analog value or 0/1 for digital status • Unit: Engineering unit e.g. “%”, “degC”, “rpm”, “digital” • Event trigger: analog signal deviation setting, digital signal “-/1” or “0/1” or “1/0” • Status: status text e.g. “normal”, “alarm”, “high”, “low”, “sensfail”

> **[Figure]** Graph/chart showing alarm limit configuration with labeled threshold points A1, B1, A2, B2. X-axis shows signal values, Y-axis shows alarm levels. Two curves: blue curve rising from A (at A1/B1) to C (at A2/B2), red curve rising from B to peak then falling. Dashed vertical lines at A2 and B2. Horizontal arrow D showing time interval. Purpose: diagram illustrating alarm hysteresis/rate-of-change limit settings with two alarm level thresholds.

Additionally there is logged for statistics: • Event count: (+) ####, the counter is reset every 9999 alarm events, after the first reset the prefix shows “+”

The frequency and amount of events will be restricted by two setting; a periodic data (trend) logging frequency and minimum event timeout.

The periodic data (trend) logging frequency will set the global frequency of the logging mechanism which is set to 1 second. The minimum event timeout can be configured per channel and will prevent multiple consecutive events in the event log. This prevents an unnecessary amount of data to be written to the event log allowing a longer period of logging.

The images below including the following explanations will explain the functionality.

The image (Rising value event) shows an analog value (Y-axel) which is changing over time (X- axel). At point A, the first event is being logged because the value exceeds the preset deviation (A1). The time and date (A2) are being logged along with the current value. At point B you can see the value is exceeding the preset deviation (B1) again. This time it is not logged until point C, this is because the minimum event timeout (D) has not exceeded yet.

Rising value event.

The image (Rising and dropping value event) shows an analog value (Y-axel) which is changing over time (X-axel). Another situation would be a rising and dropping value within the minimum event timeout (D). At point A, the first event is being logged because the value exceeds the preset deviation (A1). The time and date (A2) are being logged along with the current value. At point B you can see the value is exceeding the preset deviation (B1) again. This time however the value drops again and remains within the preset deviation (B1). At point C, when the

minimum event timeout has exceeded the value is within the preset deviation value (B1) and no new event is being logged.

Rising and dropping value event.

#### 7.1.5.4 Logging Storage

The logging storage has the capacity for storing a total of 6Mb which equals approximately 360 000 event samples when using a maximum of 300 Alarm/Status signals and 300 Trend signals. When the storage limit is reached, the oldest logging data will be deleted (first in, first out). The statistical counters for all logging data however remain active until the logging is reset/restarted.

To safeguard logging information, the system will copy the samples from its working memory (Ram) to its storage memory (Flash) using a 15 minute timer. A copy from Ram to Flash is also triggered when the number of samples in Ram exceeds 64.

For example: Over the period of the first year an average of 980 events can be logged per day before the logger starts deleting the oldest log samples.

Logging data storage can only be reset/restarted via the ZF menus. The logged data can be retrieved via Ethernet using the Firmware Installer tool.

> **[Figure]** Trend/graph diagram used in MEGA-GUARD showing a PID/RTC controller response over time. X-axis spans a time range with markers A2 (left) and B2 (right dashed lines). Y-axis shows signal levels with labeled horizontal dotted lines B1 (upper, blue) and A1 (lower, red). The red curve (input/setpoint) rises from left, while the blue curve (response/output) shows a peak above B1 at point B and settling. Key labeled points: A (on red curve at A2 vertical line, at A1 level), B (peak of blue curve at A2, above B1), C (blue curve descending after B2). Dimension D marks the horizontal time span between A2 and B2 with a double arrow. Horizontal dotted lines in red (A1 level) and blue (B1 level). This appears to be a response curve diagram illustrating alarm level thresholds A1/B1 and their relationship to a process value over time in MEGA-GUARD trending.

No data is logged when the TCU operator panel is switched off.

Details: The 6Mb logging storage is divided into 48 sectors of 128KB. Each sector begins with a header which is 10KB when the maximum number of Alarm/Status and Trend signals is configured. Each sector contains around 7500 events.

#### 7.1.5.5 Export of Logging Data

The logging files are exported in CSV format (comma-separated values). The CSV-files can be transported with the flash drive to any PC and analyzed with e.g. Excel or Calc. Two logging files are created by the Firmware Installer tool; one log file containing all statistical data (since the start of the logging) and one log file containing all chronological logged events.

> **[Vector Diagram — Page 145]** Page 145 documents the MEGA-GUARD OWS statistical and chronologic CSV log file formats, TFT logging configuration details, and Asian language support in iObserver.

Diagram 1: Statistical CSV Log (STAT CSV) Format. Type: Data format/file structure diagram. Header row columns: Date, Time, Tag, Value, Status, Alm-hi, Alm-lo, In Units, De-State, Trend, Total. Example data rows show DD-MM-YY date format, HH:MM:SS time, 10-char tag names, engineering values, status flags, alarm high/low limits, units, deviation state, trend flags. Note: 'Header/alarm row (left column), the last column are explanatory fields which do not appear in the actual logging.'

Diagram 2: Chronologic CSV Log (CHRON CSV) Format. Type: Data format diagram. Header row: Date, Time, Tag, Value, Status. Rows show alarm events in chronological order with timestamps. Used for time-ordered alarm event export.

Text: TFT Logging Configuration (section 7.1.5.5 continued): TFT logging configuration file stored in D:\Software\System\PAL1131 folder. WRITE_RTC and GET_TOD functions return DATE_AND_TIME type. Time interval determined as difference between CUR_TIME readings. The log file ExistingList.bit stores Unicode (Siemens) log format.

Diagram 3: iObserver Alternative Language Dialog. Type: Software UI screenshot. Language configuration dialog showing: Job Message field (title, up to 18 chars), Alt. Job Message field (alternate language, up to 40 chars), 'Use Alt Language' checkbox, Font dropdown (showing Asian font options e.g., MS Gothic for Chinese/Japanese). Note: 'For Asian Alternative language (CJK) is required. Need to configure system to Asian language before entering text in Chinese/Japanese. Choose a font which has the language characters the project will use (such as MS Gothic for Chinese/Japanese).' Page 145 is from sections 7.1.5.2 and 7.1.5.5.

7.1.5.5.1 Statistical log file (STAT.CSV) The statistic log file gives a non-chronologic summary of all alarm and event signals and the totalizer counter value of how many (alarm) events occurrences there have been since the start of the logging. The export format of the statistical CSV file is:

| Date, | Time, | Tag, | Value, | Unit, | Trigger, | Status, | Count, |
| --- | --- | --- | --- | --- | --- | --- | --- | |
| DD-MM-YY (of start-up), | HH:MM:SS (of start-up), | name, | -, | EU, | Value, or <a>, in case of alarm log | Text, | Total event count, |

Header:

Event Rows:

Example:

|  | Date |  |  | Time |  |  | Tag |  | Value |  |  | Unit |  | Trigger |  |  | Status |  |  | Count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | |
|  | 23-05-12 |  |  | 11:03:20 |  |  | PS-4638 |  | - |  |  | degC |  | <a> |  |  | HIGH |  |  | 3 |
|  | 23-05-12 |  |  | 11:03:20 |  |  | PS-4639 |  | - |  |  | degC |  | <a> |  |  | Normal |  |  | 7 |
|  | 23-05-12 |  |  | 11:03:20 |  |  | 09-4034 |  | - |  |  | digital |  | <a> |  |  | ALARM |  |  | 1 |
|  | 23-05-12 |  |  | 11:03:20 |  |  | 07-12569 |  | - |  |  | rpm |  | 50 |  |  | Normal |  |  | +6923 |
|  | 23-05-12 |  |  | 11:03:20 |  |  | 05-3238 |  | - |  |  | digital |  | -/1 |  |  | On |  |  | 367 |

(Header)2 (alarm) (alarm) (alarm)

(trend) (trend)

|  | [INFO] |  | (header/alarm/trend) text in left column are explanatory fields which do not appear in the actual loggin | g |
| --- | --- | --- | --- | --- | |

7.1.5.5.2 Chronologic log file (CHRON.CSV) The chronological log file gives all stored chronologic logged events. The export format of the statistical CSV file is:

| Date, | Time, | Tag, | Value, | Unit, | Trigger, | Status, |
| --- | --- | --- | --- | --- | --- | --- | |
| DD-MM-YY | HH:MM:SS | name, | -, | EU, | Value, or <a>, in case of alarm log | Text, |

Header: Event Rows: (Data at time of event)

| Date | Time | Tag | Value | Unit | Trigger | Status | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | |
| 15-10-13 | 21:01:53 | 07-12569 | 750 | rpm | 50 | Normal | Normal |
| 17-10-13 | 23:15:53 | PS-4638 | 145 | degC | <a> | HIGH | HIGH |
| 17-10-13 | 23:16:15 | PS-4638 | 145 | degC | <a> | SENSFAIL | SENSFAIL |
| 17-10-13 | 23:16:55 | PS-4639 | 130 | degC | <a> | Normal | Normal |
| 12-03-14 | 22:45:29 | 09-4034 | 1 | digital | <a> | ALARM | ALARM |
| 12-03-14 | 23:15:53 | 05-3238 | 1 | digital | -/1 | On | On |

(Header)2 (event) (alarm) (alarm) (alarm) (alarm) (alarm)

|  | [INFO] |  | (header/alarm/trend) text in left column are explanatory fields which do not appear in the actual loggin | g |
| --- | --- | --- | --- | --- | |

#### 7.1.5.6 TFT logging Configuration with PAL

The configuration via PAL. • Open PAL (F12) • Go to Processor with TFT when logging needs to be established.

• Go to tree-item “General Menu”

By clicking on “Page” Column, the following dropdown list is shown

> **[Figure]** Screenshot of PAL system 'Add/Delete Groups' dialog section. Fields: Type dropdown (Group), Sort button, Add button, Group dropdown (empty), Delete button. Empty list area below. Purpose: PAL alarm system group management interface for adding/deleting group assignments.

Choose “Alarm/Status Logging”

> **[Figure]** Screenshot of PAL 6.0.0.7 system showing channel configuration tree. Left tree: Channels > Ethernet-ETH_FB(I/O) > TC1 > Proc-10 through Proc-13 > Menus > General Menu > Parameter-Hide Items, Parameter-Main Menu, Alarm List-1, Alarm/Status Logging-1, Periodic Data Logging-1. Right panel shows a table with pages: Parameter List (PARAMETER LIST), Alarm List (ALARMLIST), Alarm/Status Logging (ALARM/STATUS LOGGING), Periodic Data Logging (PERIODIC DATA LOGGING). Purpose: PAL system General Menu structure configuration showing available page types.

To put comments you could enter text inside the “Description” column.

Go to tree-item “Alarm/Status Logging - 1”

Add a certain group by selection this group at “Group” combo-box after that press button “Add”

It is possible to add multiple groups

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing Add/Delete Groups for trend/event logging. Add/Delete Groups section: Type: Group (dropdown), Sort, Add, Delete buttons; Group dropdown (empty). List showing one entry: 22 - TC1 EVENT LOGGING. Purpose: configuration showing Group 22 (TC1 EVENT LOGGING) added to the trend or event logging configuration in MEGA-GUARD.

Furthermore a grid is shown It shows a list of all “Digital Status Channels” from the inserted groups.

Channel number and its Description are shown for obviousness reasons.

Log Deviation [Digital]

These options can be configured for each digital status channel.

Go to tree-item “Periodic Data Logging – 1”

Add a certain group by selection this group at “Group” combo-box after that press button “Add”

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing TC1 group listings. Text list showing group entries: 10-TC1 PROPULSION ALARMS, 11-TC1 STEERING ALARMS, 12-TC1 THRUSTER/PUMP ALARMS, 13-TC1 LIFTING ALARMS, 14-TC1 OTHER (SYSTEM) ALARMS, 21-TC1 STATUS LOGGING. Purpose: configuration list showing MEGA-GUARD alarm group definitions for TC1 (machinery/technical category 1) covering propulsion, steering, thruster/pump, lifting, system alarms, and status logging groups.

Furthermore a grid is shown It shows a list of all “Channels” from the inserted groups.

• Channel number and its Description are shown for obviousness reasons. • Log Deviation [EU], can be changed for each analog channel. • Min. Event Timeout [sec] can be changed for each channel. (analog or digital channel) • Log Deviation [Digital]

These options can be configured for each digital channel.

The “Min. Event Timeout” and “Log Deviation” of the channels that are configured under tree- item “Periodic Data Logging – 1” & tree-item “Alarm/Status Logging - 1” can also be changed in the Channel configuration window.

> **[Figure]** Screenshot of MEGA-GUARD PAL Remote Data configuration for a Conning system. Table showing 8 entries with columns Nr, Channel, Description, Log Deviation [EU], Min Event Timeout [sec], Log Deviation [Digital]: 1: 13483, FIELD 3/30010-STEERING ORDER, 5, (blank), (blank); 2: 13484, FIELD 4/30011-STEERING FEEDBACK, 5, 1, (blank); 3: 13485, FIELD 5/30012-PROPULSION ORDER, 5, 1, (blank); 4: 13486, FIELD 6/30013-PROPULSION FEEDBACK, 5, 1, (blank); 5: 13487, FIELD 7/30014-PROP LOAD FEEDBACK, 5, 1, (blank); 6: 13488, FIELD 8/30015-THRUSTER MODE, 1, 1, (blank); 7: 13489, FIELD 9/30009-ACTIVE CONTROL POS., 1, 1, (blank); 8: 13490, FIELD 10/30016-ALARM ACTIVE, 5, (blank), On Active Only. Purpose: configuring Modbus remote data logging parameters for conning system channels in MEGA-GUARD, including Modbus register addresses and event logging thresholds.

> **[Figure]** Screenshot of PAL channel configuration form for a Digital Input channel. Channel: 13490, Description: FIELD 10 / 30016 - ALARM ACTIVE. Type: Digital Input, Source: Remote Data. Sensor Fail: None, Norm. Cond.: Open. Report: Status, Retain Value: unchecked. Alarm Delay: 0.0 sec. Status Texts: Off (yellow), On (green), SensFail (red). Area Groups: 22 - TC1 EVENT LOGGING, Min Event Timeout: 5. Purpose: PAL digital input channel configuration for a remote data alarm signal with event logging.

Vice versa, changing the “Min. Event Timeout” and “Log Deviation” in tree-item “Periodic Data Logging – 1” & tree-item “Alarm/Status Logging - 1” will also be reflected in the Channel configuration window.

Configuring date, time and reset functions

When data logging is used without a server, the time and date must be configurable using the menu. When a server is used, the system will receive its time updates from the server.

> **[Figure]** Screenshot of PAL 6.0.0.11 system showing parameter list configuration page '3.3 GENERAL SETTINGS - MAINTENANCE' (438 items). Table: Channel 11497 'SHOW ALL MENUS (MAX 1HOUR)', Level 2-LEVEL_1; 11498 'SET TCU CLOCK DATE', Level 2-LEVEL_1; 11498 'SET TCU CLOCK TIME', Level 2-LEVEL_1; 11499 'RESTART TCU DATALOG', Level 2-LEVEL_1. Purpose: PAL parameter list showing maintenance-level system settings with access level control.

The In the ‘Parameter – Hide Items’ 3 digital input (RD) channels have to be configured under ‘SPEC_FUNC’. These channels are used to control; - Setting the date - Setting the time - Resetting the log memory

> **[Figure]** Screenshot of PAL 6.0.0.11 system showing Password-Hide Items configuration. Right panel shows a table: LEVEL_0: Formula '13094 AND NOT 13095 AND NOT 13096', Comments CONFG; LEVEL_1: Formula 'NOT 13094 AND 13095 AND NOT 13096', PARAM; LEVEL_2: Formula 'NOT 13094 AND NOT 13095 AND 13096', CREW; PASSWORD: Formula '13395 OR 13396 OR 13397 OR 13398', PW STORAGE CHAN; SPEC_FUNC: Formula '13497 OR 13498 OR 13499', SET DATE/TIME/LOG. Purpose: PAL password/access level configuration using channel-based formulas for multi-level user access control.

The same channel numbers should be configured in the Parameter – Submenu, here you can also configure the access level. The menu knows when to trigger a set date, set time or reset log function because they were configured in the ‘SPEC_FUNC’ section.

The ‘Use Master Clock Update’ checkbox should be checked on each TFT to allow other TFTs to receive time updates.

> **[Figure]** Screenshot of PAL system Processor settings showing General Settings tab. Name: Proc. Automatic Tag Creation: <XP><B><CH>. Board Setup: IP Address 192.168.1.13, Port 502, VLAN Mode, Use Order Printer, ComPort Not Connected, Use Local Time, Use Master Clock Update (checked). Retain Internal Time (min): 5. Purpose: PAL processor board setup and general configuration settings.

> **[Vector Diagram — Page 153]** Page 153 documents SSD storage media wear characteristics and Trend logging memory calculations for MEGA-GUARD OWS data storage sizing.

Table: SSD Storage Capacity vs. Terabytes Written Before Failure. Type: Technical specification table. Columns: Disk (GB), Terabyte before failure, Write speed MB/s:
  2 GB / 38.8 TB / 11 MB/s
  4 GB / 51.9 TB / 11 MB/s
  8 GB / 69.8 TB / 11 MB/s
  16 GB / 94.6 TB / 11 MB/s
  32 GB / 128 TB / 11 MB/s
  64 GB / ~131 TB / 11 MB/s

Memory Calculation Examples (text):
One day = 60 * 60 * 24 = 86,400 seconds.
At 5-second sample rate: 86,400/5 = 17,280 samples/day.
17,280 samples * 117 bytes/sample = 2,021,760 bytes/day per channel (~2 MB/day).
For 12 channels: 12 * 8 bytes * 720 samples/hour * 2 = memory usage per hour.
Maximum usage per memory per sample: 300 * 1000 / 3000 = 49 KB.

Note (hand/alert icon): 'A 60 GB SSD approximately has 30GB Flash available for logging.'

Contextual calculation: A 60 GB SSD (~30 GB available for logging) / 2 MB/day per channel = 15,000 days per channel = ~41 years of single-channel trend logging. Page 153 is from section 7.1.6 ('Wear and tear logging'). This calculation assists MEGA-GUARD engineers in sizing OWS SSD data logging media for the number of channels, sample rate, and expected vessel lifetime.

### 7.1.6 Logging wear and tear

Logging will cause runout of the storage media. The Solid State memory uses a wear and tear mechanism so that the whole disk will degrade evenly. In the following table is displayed how much logging can be done before the Compact Flash (CF) or SSD has to be replaced:

Disk (CF) Terabyte before failure Write speed MB/s 11

## 2 GB 38.4

## 4 GB 51.9 11

## 8 GB 69.8 13

## 16 GB 115 15

For example; if you log 10MB per day with a 2GB disk it will work for 38.4TB /10MB = 4 * 10^6 days, => 11 years. (TB has to be multiplied by 1024^4 to convert to bytes and MB has to be multiplied by 1024^2 to convert to bytes).

Disk (SSD) Terabyte before failure Write speed MB/s

## 30 GB 312 84

## 60 GB 624 84

Other SSD disk sizes the Terabyte before failure increases linear to the disk size.

### 7.1.7 Trending

Trend Replay: Check box to turn on possibility to do a trend replay of this group Timespan (hh - mm): Time span hours (default) - Time span minutes (default) High Limit: Max. value which is to be displayed (default) Trend Memory: Check box to turn on possibility to trend in Memory Sample Rate (ms): Sample Rate Memory Trending in ms. Low Limit: Min. value which is to be displayed (default)

The message “Data Log file size too big for trend replay” is displayed when the “maximum usage of disk per day” bigger is than 1.44 MB.

### 7.1.8 Add / Delete Channels

Type Channel, Tagname, Description, Range, All, Empty Line Channel / Tagname / Channel number, Tagname, filter of description, Range starting from a Filter / From To* channel number to another channel number (should be ascending) Channel List List of Channels in this Groups, Remark: a channel should be existing and its source must not “Not Installed” * Depends on the chosen “Type”

Buttons Browse: Add channels from list with available channels Add: After a given channel/tagname/range of channels, add the channel(s) to this group Insert: After a given channel/tagname/range of channels, insert the channel(s) to this group Delete: After a given channel/tagname/ range of channels, delete the channel(s) from this group Sort: Sorting all the channels in this group, on channel number or tag name

| [INFO] |  | Channel value and status exchange between the processors is transmitted using |  |
| --- | --- | --- | --- | |
|  |  | Multicast UDP messages 10 times per second for up to 112 channels. When using more |  |
|  |  | than 112 channels to be send to other processor the transmission rate will be lower. |  |
|  |  | For example, when up to 224 channels are used the transmission rate will be 5 times |  |
|  |  | per second. This method makes data rate on the network equal at all times. |  |

## 7.2 Job and Language

> **[Figure]** Screenshot of the MEGA-GUARD PAL configuration tool, Add/Delete Channels dialog for a trend or hour counter. Type: Channel (dropdown). Browse, Sort, Insert, Add, Delete buttons. Channel list (Items=15) with note: Only the first 12 channels are used for trend memory. Items listed: 108021-(108021) Test Virtual Channel 21 (highlighted blue), 108022-(108022) Test Virtual Channel 22, 108023-(108023) Test Virtual Channel 23 TEST DESCRIPTION, 108024-(108024) Test Virtual Channel 24, 108025-(108025) Test Virtual Channel 25. Purpose: adding channels to a trend group in MEGA-GUARD PAL configuration, showing virtual test channels assigned to a trend recorder.

### 7.2.1 General Settings

After selecting ‘Job and Language’ and ‘General Settings’

> **[Vector Diagram — Page 155]** Page 155 documents iObserver alternative language configuration dialog for Asian character support and Client Tests functionality in the MEGA-GUARD OWS.

Diagram 1: iObserver Job Language Configuration Dialog. Type: Software UI screenshot. Left panel shows project tree with 'Job Message' selected. Dialog fields:
- Job Message: text field (up to 18 characters long)
- Alt. Job Message: alternative language message (up to 40 characters)
- Use Alt Language: checkbox
- Font: dropdown showing available fonts (Arial, MS Gothic for Asian)
- Description: up to 40 characters
Panel label shows: 'Job Message [record] Alt. Job Message'

Note (hand icon): 'For Asian Alternative language (CJK) is required. Is it required to configure the system to Asian language before being able to enter text with the proper address in Chinese/Japanese text. You need to choose a font which has the language characters the project will use (such as MS Gothic for Chinese/Japanese).'

Text: Client Tests (section 7.2.2). Shows 'Client Tests' as a menu item under 'Job and Language'. A table is shown with columns: Language (English), Type (User Defined). The table displays test language entries for both the default English and any user-defined alternative language configuration. The Client Tests feature allows verification that the language configuration is correctly applied in the iObserver client display.

Page 155 is from section 7.2 ('Workstation Log Language'). The OWS iObserver supports dual-language display for alarm messages and channel tags. The Alt Language font must be set before entering non-Latin characters.

Job Message Title display on Client, up to 18 characters long Use Alt. Language If you like to use besides English another language, check this box, now new fields are available, like Alt. Job Message and Alt. Description at a single Group or Channel configuration. Also, see Note below! Alt. Job Message Alt. title display on Client, up to 18 characters long Font Button to choose a font which alt. language texts will use. You need to choose a font which your preferred language supports!

| [INFO] |  | For Asian Alternative Language a Compact Flash card (with Asian languages included) |  |
| --- | --- | --- | --- | |
|  |  | is required. The PanelPC has this standard. Before being able to enter text with Asian |  |
|  |  | symbols these two steps are required: |  |
|  |  | 3. Select Asian keyboard in Windows Control panel, Region & Languages. (do not |  |
|  |  | forget to re-able the C disk write filter). |  |
|  |  | 4. Select font with the required Asian symbols in PAL Jobs & Language branch (such |  |
|  |  | as SimSung for Chinese). |  |

### 7.2.2 Client Texts

Selecting ‘Job and Language’ and ‘Client Texts’ and one of its items:

A table is shown with language text "English" and "User Defined". "User Defined" text can be adapted. These texts are shown inside a Client, when the Client is setup to used Alternative Language.

> **[Vector Diagram — Page 156]** Page 156 documents MEGA-GUARD user role security configuration, role-based access control, and system login in the PAL programming and OWS iObserver environment.

Role-Based Access Control System Description:
- Each role assigned specific user rights for MEGA-GUARD functions
- Roles agreed with customer and configured in PAL (F12 role input dialog)
- Each user assigned a role on login; role controls OWS function access
- Roles can be chosen to make specific mimics accessible only to specific role in which the workstation is associated
- Drawing during mimic design: controls can restrict access per Babel control Role

Example Role List Table. Type: Configuration reference table. Example numbered roles:
1. Administration
2. Engineer
3. Propulsion
4. Power Management
5. (additional customer-specific roles)

Note: 'Depending on vessel type and customer information all possible roles must be input via PAL (F12) Role input dialog.'

User Login Procedure:
1. User enters username
2. User enters password
3. System grants rights based on role assignment
4. VAR PAL F12 input used to assign role globally

Text: 'Via the role list each MEGA-GUARD function will be limited to the role in which the workstation is associated with in the role. Each role is assigned the rights...' Role access restricts control of MEGA-GUARD automation functions to authorized personnel only.

Page 156 is from section 7.3 ('Level system security'). Role-based access control in MEGA-GUARD OWS restricts operator access, ensuring only authorized personnel (engineers vs. watch officers) can modify control setpoints or override alarms.

## 7.3 Role system security

For cyber security certified systems users are assigned a role (function). This role gives them specific rights for controlling equipment and changing parameters. All on board equipment control via Mimics is divided into roles. For example the role “Power Management” will contain generator equipment. Once a user with the role Power Management has logged in this specific equipment control is enabled on the mimic.

During engineering/commissioning a list of roles must be entered into the PAL roles input. Each role is assigned the rights to control specific equipment. For testing specific user names must be entered and assign roles via PAL user input (F12). Via the role list also each role will allow configuration changes to specific Control Processors, Channels on those processors and Groups.

After commissioning the system is in usage the crew can input the crew names using PAL user input (F12). Each user will be prompted to set a password onto first usage.

The equipment control via Mimic has unique Boolean variable for the role. Once the user has logged in the variable will be switched to High value allowing the controls to become accessible.

### 7.3.1 Role setup

During system engineering the roles have to be agreed with customer. The following list is an example of a roles set that can be used for a system.

| # | Role |
| --- | --- | |
| 1 | Administration |
| 2 | Propulsion |
| 3 | Engine Control |
| 4 | Power Management |
| 5 | Ballast Control |

Depending on vessel type and customer information all possible roles must be input via PAL (F12) Role input dialog.

### 7.3.2 Mimics with role accessibility

In mimics each equipment control is engineered to be only accessible for a logged in user with the role in which the equipment is associated. During drawing and mimic design the control parts of the mimic are assigned to the Role each control belongs. In PAGE mimic editor the Roles can be chosen to make controls inside a specific frame accessible only for this workstation. For example Ballast pump control is configured to be accessible via Ballast control Role.

## 7.4 Level system security

In Software versions 6.0.1.15 and older a level system security is available. This is not sufficient for Cyber Security certified systems. With the level system to top level (0) is allowed to do all

(configuration and control). Each level with higher number (1,2,3) is allowed to do less. The level with the highest number may only control simpler equipment. It is not possible to give user rights for different equipment in the same level.

> **[Figure]** Screenshot of PAL [Main Server] - PAL 6.0.0.1 configuration tool showing Hour Counters section selected. Left tree shows: Channels, Extended Alarm System, Graphics Pages, Groups, Hour Counters (highlighted yellow), Job and Language, Passwords, Printers, Remote Data, Special, Status Texts, System Parameters. Right panel: 'No values available for this tree-item'. Purpose: PAL Hour Counters configuration section (empty/no counters defined).

### 7.4.1 Passwords

Press F12 (SET-UP) and the following screen will appear:

Supply the correct username (up to 12 characters, mind you that the input is case sensitive) and password (up to 12 characters, mind you that the input is case sensitive) to enter the set- up. The Mega-Guard System has 3 Levels of Security. Each level giving access to a certain number or all parameters of the system. For each level you can setup a list of (max 32) user with their passwords.

### 7.4.2 Main Screen Privileges

After entering a username and password of level ‘0’ (highest degree of accessibility) the system will clear the screen and the main set-up menu of the selected unit is displayed. (See the Product Technical Description of the Mega-Guard station for details on this procedure). All items in the list below can be selected and configured:

> **[Figure]** Screenshot of MEGA-GUARD CAMClient Login dialog (alternative appearance). Fields: User Name text field (empty, cursor visible), Password text field (empty). Buttons: Accept, Cancel. Title: Login. Purpose: MEGA-GUARD CAMClient user authentication login dialog - identical to p32_i2 but shown in a different chapter context.

Figure 2: Main Setup Screen Privilege Level '0'

Entering a wrong password, will indicate the following popup window on the screen and the system will return to the normal operating mode:

Privilege level '0' gives access to all items.

Privilege level ‘1’ gives you access to the following items: 1. PLUGINS / FIELDBUS / CHANNELS (refer to paragraph 7.4.6.1)

## 2. GROUP PAGES AND TRENDING

## 3. PERIODIC PRINT-OUT

## 4. TIME AND DATE

## 5. JOB AND LANGUAGE/TEXT

## 6. EXTENSION ALARM SYSTEM

## 7. PASSWORD

## 8. SHOW CHANGED CHANNELS

Privilege level ‘2’ gives you access to the following items: 1. PLUGINS / FIELDBUS / CHANNELS (refer to paragraph 7.4.6.2)

## 2. GROUP PAGES AND TRENDING

## 3. PERIODIC PRINT-OUT

## 4. TIME AND DATE

## 5. PASSWORD

## 6. SHOW CHANGED CHANNELS

Privilege level ‘3’ gives you access to the following items: 1. PLUGINS / FIELDBUS / CHANNELS (refer to paragraph 7.4.6.3)

## 2. PASSWORD

## 3. SHOW CHANGED CHANNELS

### 7.4.3 Channels / Average Lay-Out Privileges

#### 7.4.3.1 Privilege Level ‘0’

In the items mentioned in the Main Setup Screen(s), only the Channel Setup has different accessibility to the parameters (in this item) with the different Privilege levels. Below you will find the Channels / Conversion Tables / Stored Pulse Counters for level ‘0’. All items are accessible.

Figure 3: Tree view Level ‘0’

If you have enter the Setup with the Level ‘0’ password and you select the CHANNELS the system will respond for example with the following Setup Screen:

### 7.4.4 Permissions - Fieldbus

After login with passwords the level protection is used. At the Fieldbus it is possible to configure a level of access. Distinguish are levels 0,1,2,3 and M (master level). This field could only be adapted at Administrator level.

### 7.4.5 Permissions – General

After selecting ‘Passwords’ and ‘Permissions - General’

Besides passwords another kind level of protection is introduced. It is possible to configure a level of access. Distinguish are levels 0,1,2,3 and M (master level). This field could only adapted at Administrator level.

### 7.4.6 Permissions – Client

> **[Figure]** Screenshot of MEGA-GUARD PAL Channels tree showing Ethernet fieldbus hierarchy. Tree: Channels > FB-ETH_FB(IO) > Proc-01 > XP-010(Ctrl Proc) > Channels, Conversion Tables, 010-Channel Layout; Proc-02 (expanded); Diagnostics; Virtual. Purpose: PAL channel configuration tree showing the hierarchical structure of a MEGA-GUARD fieldbus Ethernet controller with Proc-01 (main processor with XP-010), Proc-02, diagnostics, and virtual channels.

After selecting ‘Passwords’ and ‘Permissions - Client’

Besides passwords another kind level of protection is introduced. Available are levels 0,1,2,3 and M (master level). The level field can only be adapted at Administrator (master) level.

Figure 4: Channel Setup Screen Level '0'

> **[Figure]** Screenshot of PAL channel configuration for an Analog Input channel. Channel: 01101, Description: ANALOG MEASUREMENT. Type: Analog Input, Source: 4-20mA. Eng Unit Low: 0.0, Eng Unit High: 100.0, Eng Unit Type: DegC. Displ. Deviat: 0.1, Filtersamples: 1. Limit Type: None, Rate Limit: None EU/Scan. Report: Alarm, Nr Dec.: 1. Alarm Delay: 0.0 sec. Status Texts: Normal (yellow), Alarm! (red), SensFail (red). Area Groups: 1-Group 1. Purpose: PAL analog input channel configuration for a 4-20mA temperature sensor.

All Highlighted (Black on White) are accessible.

#### 7.4.6.1 Privilege Level ‘1’

If you enter the Setup with the Level ‘1’ password and you select the system will respond with the following Setup Screen:

> **[Figure]** Screenshot of PAL channel configuration for an Analog Input channel (read-only state). Channel: 01001, Description: ANALOG MEASUREMENT. Type: Analog Input (greyed), Source: 4-20mA (greyed). Eng Unit Low: 0.0, Eng Unit High: 100.0, Eng Unit Type: DegC. Limit Type: None. Report: Alarm. Status Texts: Normal, Alarm! (yellow), Alarm! (red), SensFail (red). Area Groups: 1-Group 1. Purpose: PAL analog input channel configuration in partially read-only/greyed view.

Figure 5: Channel Setup Screen Level ‘1’

Only the highlighted (Black on White) items can be modified, all other fields are not accessible.

#### 7.4.6.2 Privilege Level ‘2’

If you enter the Setup with the Level ‘2’ password and you select the CHANNELS the system will respond with the following Setup Screen:

> **[Figure]** Screenshot of PAL channel configuration showing greyed-out Analog Input. Channel: 01001, Description: ANALOG MEASUREMENT. All fields greyed/disabled: Type Analog Input, Source 4-20mA, engineering ranges, limits. Status Texts: Normal, Alarm!, SensFail. Area Groups: 1-Group 1. Purpose: PAL analog input channel in disabled/greyed state showing non-editable fields.

Figure 6: Channel Setup Screen Level '2'

Only the highlighted (Black on White) items can be modified, all other fields are not accessible.

#### 7.4.6.3 Privilege Level ‘3’

If you enter the Setup with the Level ‘3’ password and you select the CHANNELS the system will respond with the following Setup Screen:

> **[Figure]** Screenshot of PAL channel configuration similar to p162. Channel: 01001, all configuration fields greyed out including Type Analog Input, Source 4-20mA, engineering ranges, limits. Status Texts: Normal, Alarm!, SensFail. Area Groups: 1-Group 1. Purpose: PAL analog input channel in read-only/inactive display state.

Figure 7: Channel Setup Screen Level '3'

Level 3 is read only. All fields are not accessible.

## 7.5 Printers

The system offers several ways to generate printouts of life data on the system printer. One is called periodic log, which will start at a certain time and will be repeated, at predefined time intervals. The other way to create a printout is by activation of the 'Demand log'. The printout will include date and time in the header of the printout and for each channel will be printed the tag name, description, high and low alarm limit(s), actual value and the status. If you select the following item on the tree it will give you the parameters for the setting of the periodic log. Remark: Demand Log is setup inside Client.

### 7.5.1 General

After selecting ‘Printer’ and ‘Printer - xx’

Printer Driver Select lineprint.dll for OKI matrix printer, and winprint.dll for Windows printers. Share Name Network printer share name. Required if printer is placed on a client (network) station. This client must be on during startup of server. Printer Name For example OKI or HP. Take care while inputting this because default init strings will created different depending on printer name Use Alt. Language Select this option to print in alternative language. If this language does On Printer not use the Roman alphabet (for example Russian), a special IC must be placed inside the printer. CodePage Only for alternate language, choose code page matching your language.

> **[Figure]** Screenshot of PAL channel configuration - printer init strings section. 'Use Init Strings on Printer' checkbox (checked). Init Strings table: Header: ESC-sequence string, Normal or Status Line: ESC-sequence string, Alarm Line: similar ESC sequence, Reset: control code sequence. ESC: 27, LF: 10, CR: 13, FF: 12. Defaults button. Purpose: printer initialization string configuration for PAL report printing with control codes.

Init Strings:

Header String will be send to printer before a header is printed to set up font Normal Status Line String will be send to printer before a normal status line is printed to set up font Alarm Line String will be send to printer before an alarm line is printed to set up font Reset reset code of printer

Initializing strings can be adapted, but is not recommended, use default values which will be filled in automatically after setting the printer name.

Remark: An alarm line will be printed when a channel comes in alarm. After the channel alarm is solved a normal or status line will be printed.

### 7.5.2 Printers – Alarm Log

After selecting ‘Printer’ and ‘Printer - xx’, and Alarm Log

Alarm Log Check box to turn on/off alarm log for this printer Add/Sort/Delete Buttons to insert/delete groups which needed to be logged Groups Group of which channels need to be Logged

Remark: For alarm logging normally group 0 (All Channels) is inserted.

### 7.5.3 Printers - Periodic Log

After selecting ‘Printer’ and ‘Printer - xx’, and Periodic Log

Periodic Log Check box to turn on/off periodic log for this printer Add/Sort/Delete Buttons to insert/delete groups which needed to be logged First Log Time After start of system, logging will be start at certain time (in hours:minutes) Log Interval Time After a certain interval (in hours:minutes) Channel for disable / Channel to Enable the Periodic Log Printout (0 if None) enable periodic log Periodic Log Start / Stop Channel to Start / Stop the Periodic Log Printout (0 if None) Channel Note This channel is Available per Group and defined in It’s Group.

> **[Figure]** Screenshot of PAL 'Periodic Log' configuration. Periodic Log checkbox (checked). Group list shows: 255-Hour Counters. Periodic Log section: First log time: 08:30, Log interval time: 06:00, Channel for disable/enable periodic log: 0. Purpose: PAL periodic data logging configuration with 6-hour interval starting at 08:30, logging hour counters group.

Example of a set-up of periodic log parameters

| Periodic printout required?: | Deselect checkbox if no periodic printout is required Select checkbox if periodic printouts are required. If this field is selected to 'Yes' automatically two other parameters can be entered. |
| --- | --- | |
| First log time (hr:min): | Enter the time in hours and minutes when the first periodic log should be printed. |
| Log interval time (hr:min): | Enter the interval time in hours and minutes when the periodic log printout will be repeated after the first log time. |
| Groups to include in the periodic and alarm log: | Insert the groups that should be included in the log printout(s). The maximum number of groups to include is limited to 255 |
| Channel for disable / enable Periodic log | If Channel is Active or channel number = 0, the Periodic Log will be Logged, if the channel is not active the log will be skipped. |

| Periodic Log Start / Stop Channel | If the group Channel is Active or channel number = 0, the Group of the Periodic Log will be printed. |
| --- | --- | |

### 7.5.4 Printers – Order Log

After selecting ‘Printer’ and ‘Printer - xx’, and Order Log

Order Log Check box to turn on/off Order log for this printer Add/Sort/Delete Buttons to insert/delete groups which needed to be logged Groups Group of which channels need to be Logged

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing an Order Log settings panel. Order Log checkbox (checked). Add/Delete Groups section: Type: Group (dropdown), Sort, Add buttons; Group dropdown (empty). List showing: 255 - Hour Counters. Purpose: configuring which groups are included in the MEGA-GUARD order log feature, with Hour Counters group (255) currently added.

## 7.6 Remote Data

Plugins are software modules (DLL's), that are used to establish communication with the connected hardware in- and outputs. Here we use the following link Type: - Remote Data (Indicated in the tree with RDx where x can be 1 to 32) For the configuration of the plugin(s) select the following item on the tree:

Plugins: • Adding a plugin: • Select the Remote Data folder in the tree and click with the right pointing device key or press the context menu key on the keyboard. Select 'Insert' from the context menu and a new plugin will be created. you will be asked

for the definition of the name (max 50 characters) and the link(type) for this plugin. • Deleting a plugin: • Select the specific plugin which should be deleted and press the delete key on the keyboard.

Once the plugin is created the following SET-up Fields Area will be displayed:

• Name: • This field contains the user name of the plugin. This name is also shown in the tree area. • Switch Link ON/OFF • This field indicates whether the communication to/from the hardware is enabled or not. Changing the value can done by clicking on this field or by selecting the item and pressing the Space-bar of the keyboard. • Use On Backup • This field indicates whether the communication to/from the hardware is enabled or not when the IOServer is running as Standby (Not the Active IOServer). Changing the value can done by clicking on this field or by selecting the item and pressing the Space-bar of the keyboard. • Filename: • Select filename of the DLL. • Remote Data: • Select this type whenever this plugin has to establish the communication with third party interface (E.g. ModBus, NMEA etc.) • Comment: • This field contains complementary information for describing the plugin. This field is only used for documentary reason.

> **[Figure]** Screenshot of MEGA-GUARD CAMClient General settings showing I/O server connection parameters. General section: Automatic acknowledge of channels: No (dropdown); Redundant I/O-Server checkbox (checked). Main Server - IP Address: 192.168.1.101; Main Server - Port: 502. Backup Server - IP Address: 192.168.1.102; Backup Server - Port: 502. Purpose: configuring the MEGA-GUARD CAMClient connection to redundant I/O servers via Modbus TCP at IP addresses 192.168.1.101 and 192.168.1.102 on port 502.

### 7.6.1 XP setup

#### 7.6.1.1 General module setup

General settings are located in the tree area just above the processor position table; see the following image of the tree area

It is strongly advised to leave all settings in this page on their default values.

General Setup Input Channels

• General Setup Input Channels: Delay before return to ‘Normal’ of digital inputs: Delay time used when a digital channel status becomes "Normal" after an "Alarm" is solved. Delay to Normal for all digital input channels of this link. Range of 0.0-99.0 sec in tenth of seconds. • Alarm on Sensor/Wire Failures (YES/NO), default YES: Flag if Sensor Failure has to be handled as an alarm • Handle analog value on Sensor Failure: Channel Update Flag in case of sensor failure. o freeze last valid; display ' ---- ' o freeze last valid; display last valid o update, display update o update, display ' ---- ' • Two Wire PTD: Enables configuration option in analog input channel dialog. Switch it on if you need to correct PTD values. • System Common Mode Rejection (Hz): Select the Frequency to be handled for Common Mode Rejection (50 or 60 Hz can be used).

> **[Figure]** Screenshot of the MEGA-GUARD PAL configuration tool showing an XP processor setup, General Board Setup tab. Tab row: General Settings | Processor Position Table | Communication Settings | General Board Setup (active) | Permissions - FieldBus. General Setup Input Channels section: Delay before return to NORMAL of digital inputs field: 1.0; Alarm on Sensor/Wire Failures: Yes (dropdown); Handle analog value on Sensor Failure: freeze last valid; display last valid (dropdown); Two Wire PTD: Yes (dropdown); System Common Mode Rejection (Hz): 50 (dropdown). Purpose: configuring XP I/O board behavior for digital/analog input failure handling in the MEGA-GUARD field bus processor.

#### 7.6.1.2 Communication settings

The following dialog appears when in the tree of the previous paragraph the ‘Communication Settings’ has been selected:

Server Settings: • Control Processor (XP) life check time out (active link timer): Wait time in seconds between the point that XP’s missing and the system reports diagnostic error and actually switches to standby link. • Control Processor (XP) life check time out (inactive link timer): Wait time in seconds between the point that XP’s missing and the system reports diagnostic error and actually switches to standby link. • Send download if XP is empty: When XP has no set-up information it will automatically ask to IO-Server give me my setup information. XP will always do this, with this flag IO-Server can be set not to answer to this call. • Value to zero if XP is not present: When XP becomes not present the channel values will be set to zero if this flag is set to Yes, if set to No the values will Freeze.

#### 7.6.1.3 Add and delete XP’s and Modules

• Adding an XP: • Group: • Select the Product Group to be used for the XP. • Nr / •P: • Enter the XP number in the field ‘Nr’ in the table. This number represents the unique number for each XP. Valid entries are from 1 until 99. • Panel: • Enter module type by selecting the area the system will offer a dropdown list to select the desired module type.

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing the Communication Settings tab for an XP processor. Tab row: General Settings | Processor Position Table | Communication Settings (active) | General Board Setup | Permissions - FieldBus. Server Settings section: IO-Board Life Check Time-out (active link timer): 2 Sec; IO-Board Life Check Time-out (inactive link timer): 2 Sec; Send download if board is empty: Yes (dropdown); Value to zero if board is not present: No (dropdown). Purpose: configuring the fieldbus communication timeout and board presence handling parameters for an XP I/O processor in MEGA-GUARD.

> **[Vector Diagram — Page 171]** Page 171 documents MEGA-GUARD IOM hardware configuration in the PAL1131/OWS tree including module type selection dropdown and DIN rail mounted XP setup.

Diagram 1: PAL1131 Module Type Selection Dropdown. Type: Software UI screenshot. Shows module type selection dropdown in the IOM configuration table. Dropdown options visible include: (blank/Not installed), various IOM hardware types by code including: Cabin N, DI/O Nx (Digital I/O variants), AI/O Nx (Analog I/O variants), LCD panels (LOP types), Virtual modules. Up to 5 hardware I/O modules can be installed on one I/O processor (IOM), with up to 5 LCD (LOP) panels per processor.

Text: Module Table Configuration rules:
- Select 'Not installed' to remove module from configuration
- Module type dropdown: select type for desired hardware module; system offers dropdown list of available hardware types
- Deleting a module: select the specific type in dropdown then press Delete

Diagram 2: DIN Rail Mounted XP Module Layout. Type: Hardware block diagram. Shows DIN rail mounting configuration for XP (Control Processor) with modules: XP unit at center, IOM modules (labeled IOM-N) to left and right, connection arrows showing DIN rail bus communication. Note: Up to 4 hardware or virtual I/O modules on each I/O processor. LCD (LOP) panels: up to 5 hardware entries.

Page 171 is from sections 7.6 ('I/O Configuration') and 7.6.2 ('ON rail mounted XP table setup'). Explains the PAL1131/OWS hardware configuration interface where engineers define physical I/O module types connected to each XP processor in the MEGA-GUARD system.

• SwID: • Enter module type by selecting the area the system will offer a dropdown list to select the desired module type. • Module type: • Select this area in the module table. The system will offer a dropdown list to select the desired module.

There can be up to 8 hardware or virtual (‘NoHW’) I/O modules installed on one I/O processor. LCD (PMS) panels can have up to 5 hardware or virtual modules.

• Deleting (a) module(s): • Select the specific type. And select ‘None’ in the dropdown list. The related module(s) will be deleted from the table.

|  | [INFO] Modules connected to a processor must be continues. No gaps in the address |  |
| --- | --- | --- | |
|  | numbers are allowed. For example, if module 3 is set to "None", and module 4 is a |  |
|  | "NoHW", then the setup will not work. Module 4 should be moved to the position of |  |
|  | 3. |  |

### 7.6.2 DIN rail mounted type XP table setup

Each DIN type I/O processor has a table for the connection of local system functions to local I/O channels, the location of these tables is in the tree area just below the module table, see the following image of the tree area:

> **[Figure]** Screenshot of PAL 6.0.0.11 processor configuration - General Settings tab. Name: Virtual Proc. Board Setup: IP Address 192.168.1.20, Port 502. Use Order Printer (ComPort 1), Use Local Time On Order Printer, Use Master Clock Update checkboxes. Folder name: PROC-20. Purpose: PAL virtual processor configuration with IP address 192.168.1.20.

By selecting one of the XP the setup area will show the settings at the right side of the tree.

#### 7.6.2.1 General settings

This setup enables setting the tag creation, communication and several other functionalities:

• Name: The name of the XP which can be used in other fields (such as Automatic Tag Creation) • Automatic Tag Creation: The format for the tags that the channels on this XP will be created by the system. Several special keywords can be used which will change per channel.

> **[Vector Diagram — Page 173]** Page 173 documents MEGA-GUARD XP processor configuration parameters including keyword substitution fields and standalone/redundant configuration options in the OWS iObserver setup.

Keyword Substitution Configuration:
- The %XP% keyword will be replaced by the XP IP number at runtime
- The %rXP% keyword will be replaced by the 2-digit XP Channel number
- These keywords appear in XP address fields and are substituted when the configuration is applied

Automatic Display / Redundant XP Configuration Options:
- 'Stand-alone display, deviation automatically' checkbox:
  When checked: display deviation changes at channel configuration and automatically at IOM (deviation overview)
  When unchecked: no deviation tracking (stand-alone, no redundant panel)
- Deviation display: for redundant XP pairs, tracks deviation between primary and secondary XP processor values

Stand-alone Panel (no redundancy):
- Single display; no redundant panel installed
- 'Stand-alone display, deviation automatically' is unchecked

Use Processor Range field:
- Enter value to apply range to both XP units (primary and redundant) in a redundant pair
- Field accepts IP addresses: format XP1_IP / XP2_IP, e.g., 192.168.0.101 / 192.168.0.102

IP Address field: for information only (not configurable here); %XP% keyword replaced by actual IP at runtime.

Automatic Deviation Start of Child: when redundant panel is connected, enables automatic handoff tracking between primary and secondary XP processors.

Page 173 is from section 7.6.2 ('XP Configuration'). Defines how each Control Processor (XP) is set up in the MEGA-GUARD network including IP addressing, redundancy configuration, and channel deviation display settings for the OWS.

The <XP> keyword will be replaced for a 2 digit XP number. The <B> keyword will be replaced for a 1 digit Module number. The <CH> keyword will be replaced for a 2 digit Channel number. • Automatic Display Deviation: • When checked: display deviation will hidden at channel configuration, and automatically set at highest precision. Example: nr of decimals = 1, display deviation = 0.1. • Stand-alone Panel – No Download • Checkbox on for a processor configured as stand-alone Panel (sometimes referred to as Mini-guard). For example Fire-Alarm Panel. There are no configuration settings downloaded to the panel by the IOServer (Marine-PC). This type of panels have their own configuration and needs configured by the panel itself. But the system (IOServer / Camclient) needs some configuration to know the panel is present and for display the channels values from this panel. • Use Processor Range: • When having a configuration where several processors which have exactly the same configuration. And local channels needs to send/receive to other processor with same configuration, this feature needed to be used. For Example: a PMS having 3 generators with the same configuration

## (XP61..XP63):

1) download XP61 to first Panel (address XP 61) 2) download XP61 to second Panel (power down first panel, make address also XP 61 on second panel) 3) download XP61 to third Panel (power down first and second panel, make address also XP 61 on third panel) 4) change address on second Panel (address should be made XP 62) 5) change address on third Panel (address should be made XP 63) • IP Address: This field is for information purpose only. The IP address must be used as automatic defined by the system (can not be changed). • Port: This field is for information purpose only. The Port must be used as automatic defined by the system, it cannot be changed • Use order printer: The order printer will print alarms. • ComPort: The Comport Nr. To be used for Order Printer. • Use local time on order printer: The System will take time zone into consideration and print local time instead of GMT (Universal Time). • Use Master clock update: Master clock pulse inputs connected to XP will update the system time. • Remote data: Add or remove Remote Data DLL’s to this XP. • Folder name: Set name of the folder in which the XP must be grouped in the tree. • Status text set number: Select which set of status texts are used for channels on this XP • Document Database:

• Description: For generating IOList with MsExcel a program is created with name DocGen.exe; for its output it is possible to document with PAL. For each processor it's location and it's function description can be documented. • Location: For generating IOList with MsExcel a program is created with name DocGen.exe; for its output it is possible to document with PAL. For each processor it's location and it's function description can be documented.

#### 7.6.2.2 Miscellaneous Table

This setup enables XP functions that can be connected to local I/O channels:

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing a LOP/EAS Processor configuration panel. Fields visible: Processor Number: 20 (greyed/read-only). Configuration input channel assignments: Acknowledge Input: 0, Stop Horn Input: 0, Lamp Test Input: 0, System On Output: 0, Horn Output follows Channel: 0, System Fail: 0, 1131 Restart: 0, 1131 Restart Exit LCD Parameter: 0 (field), Enter LCD Parameter Menu: 0, Exit LCD Parameter Menu: 0. Purpose: configuring hardware I/O channel numbers for EAS/LOP processor control signals in MEGA-GUARD alarm system.

The local system functions can be defined as follows: • Acknowledge Input: • The digital input channel will, when active, acknowledge the active alarms of this XP. • Stop Horn Input: • The digital input channel will, when active, de-activate the local Horn Output of this XP. • Lamp Test Input: • The digital input channel will, when active, activate all alarm indicators (and digital outputs with 'lamptest' on) of this XP. • System On Output: • The digital output channel will be activated when the XP is switched on and is running. • Horn Output Follows Channel: • The digital input channel, will force the Horn output of this XP. • System fail: • The system fail LED input channel, is used to set the XP in system fail. • 1131 Restart:

• The configured digital input channel connected to this function will restart IEC-1131 program of this I/O Processor. • 1131 Restart Exit LCD Parameter: • The configured digital input channel connected to this function will restart IEC-1131 program of this I/O Processor. This will only be done after LCD Menu is used on this I/O Processor. • Enter LCD Parameter Menu: • The configured digital input channel connected to this function will have status "ON" when LCD Menu is being use on this I/O Processor. • Exit LCD Parameter Menu: • The configured digital input channel connected to this function will have status "ON" after LCD Menu is used on this I/O Processor.

#### 7.6.2.3 I/O Module setup

Expanding the tree area on the specific module will give you for example the following image:

If you select the module in the tree area the system will show you the right setup area.

For each module you can setup channels (hardware or virtual), conversion tables, function block implementations, parameter layout and eventual stored pulse counters.

The following setup can be entered for the selected type: • Name: • Enter the name for this XP. This field is used for documentary reasons only. The Name will be used in the tree area. • Type: • Module type selected when inserting. This field cannot been changed afterwards. • Number: • Module number defined at insertion. This field cannot been changed. • Disable Board – No Alarms and No Download: • If this is checked the alarming of the IOBoard will not be done.

#### 7.6.2.4 Channel setup general

Selecting the 'Channels' folder in the tree area will expand the tree with all channels for that specific module. Selecting a channel will give you the specific setup fields of the selected channel. The setup fields are related to the channel type of that specific. The following channel types are supported: • Analog input • Digital input • Analog output • Digital output • Pulse input • Average

> **[Figure]** Screenshot of PAL channel configuration for a Digital Input. Channel: 10105, Description: Boegschroef Hydr. Unit nivo (Bow thruster hydraulic unit level). Type: Digital Input, Source: Hardware Input. Fail Detect: None, Norm. Cond.: Closed. Report: Alarm. Area Groups: 11-Verstelbare schroef SB. Alarm Delay: 3 sec. Status Texts: Normal, Laag (yellow), SensFail (red). Purpose: PAL digital input channel for a bow thruster hydraulic unit level sensor with 3-second alarm delay.

#### 7.6.2.5 Digital Input Channel Setup

If you select a channel with the channel-type set to Digital input the system will provide you with the following setup fields:

7.6.2.5.1 Standard Set-up Digital Input Channel

• Tag Name: Enter any tag up to 10 characters. Tags must be unique. The system will automatically assign a tag number based on the settings in the General XP setup. • Description: Enter any descriptive text up to 40 characters. • Type: • For digital hardware inputs: select ‘Digital Input’.

• For analog hardware inputs: select ‘Digital Input'. If you use this option, in some cases you will need a digital input Sensor Adapter on the module for this channel (Refer to project related I/O list for Sensor Adapter Type). • If you select a Type which does not correspond with the physical hardware related to that channel (for example 'ANALOG' for a real hardware digital input channel) the channel will behave as a virtual channel of that selected type (See paragraph Virtual Channels , page 216). • Skip: • Select ‘NO’ (channel is processed). • Select ‘YES’ (channel is NOT processed). • Source: • Select ‘Not Installed’ to set this channel as 'Not Installed, the value of this channel is undefined. • Select 'Hardware Input', to use the value of the physical hardware input. • Select 'Other Channel', to use the status information from another channel. • Select ‘Mimic’, to use the value of a Mimic. • Select ‘Mimic Pulse’, to use the value of a Mimic Once (Requires IEC – 1131). • Select 'Remote Data', to use this digital value to be driven by an external device. • Select ‘IEC – 1131’, to use this digital value to be driven by IEC – 1131. • Norm.Cond.: • Select ‘OPEN’ for a, default Normally Open, contact on the input or normal value from source = 1. • Select ‘CLOSED’ for a, default Normally Closed, contact on the input or normal value from source = 0. • Fail Detect: This is an option to enable 'Wire Failure' detection on the sensor. If a Failure is detected it will be reported as an alarm message line on the printer and on the 'ALARM PAGE' on the monitor and if the value of this channel is used in a Graphic Page the value will change its color to red. • For digital hardware inputs: • Select ‘NONE’ if no wire failure detection is required (hardware wire failure detection circuitry is not available for this type of input). • For analog hardware inputs, set-up to be used as digital input, set one of the following options: • Select 'NONE' if no wire failure detection is required. • Select 'SENSOR' if wire failure detection is required. (For connection of sensors, refer to 'Typical Signal and Sensor Connection Diagram' in the project related drawings). • Select ‘Channel’, to use the Sensfail status of this channel. • Select ‘Channel Status’, to use the Limit status of this channel. • Report: The Report option is to select what alarm report feature(s) will be activated if the alarm, or status change is detected. The following selections are possible:

• Status: For group listing and mimic display. Channel not listed in alarm list. • Alarm No Horn: Deprecated, for backward compatibility. Shown in alarm list, but no audible • Emergency alarm: An alarm which indicates that immediate danger to human life or to the ship and its machinery exists and that immediate action should be taken. • Alarm: An alarm is a high priority of an alert. Condition requiring immediate attention and action, to maintain the safe navigation and operation of the ship. • Warning: Condition requiring no immediate attention or action. Warnings are presented for precautionary reasons to bring awareness of changed conditions which are not immediately hazardous, but may become so if no action is taken. • Caution: Lowest priority of an alert. Awareness of a condition which does not warrant an alarm or warning condition, but still requires attention out of the ordinary consideration of the situation or of given information.

Status Report The Report Option 'Status' signifies that the signal is not activating an alarm message on the 'ALARM PAGE' and is not activating the HORN output. But it will activate the posting of a status message line on the printer if the status changes (If Print Status option is set to 'YES').

|  |  | If the Sensor Failure is used and the Sensor Failure is activated, it will create an |  |
| --- | --- | --- | --- | |
|  |  | alarm message on the 'ALARM PAGE' and it will post an alarm message line on the |  |
|  |  | printer. |  |

Alarm no horn When 'Alarm No Horn' is configured it will not activate the HORN output on XP Board, but it will activate horn on active server (plays the wave file via MPC speaker)

Alarm The other report options configure that the signal shows an alarm message on the 'ALARM PAGE' and activates the 'HORN' output.

The HORN on XP Board and on active server workstation will both turn on. The active server requires group configuration for this.

Warning and Caution Warning and Caution have different alarm behavior as the other options.

When Warning becomes active, the horn and it's flash state stays on for 2 seconds. After that time horn output is deactivated and the warning flash state is turned off.

But the warning state stays unacknowledged and after 5 minutes the warning priority will change into Alarm. Only in case there was no human intervention or the cause of the warning was not rectified.

When Caution becomes active, the system shows visual steady alarm (no flash). The caution will disappear as soon as the cause of the caution is rectified. It is also possible to have separate alarm-lists with only 'Emergency Alarms', or only 'Cautions', or only 'Warnings'.

• Area Groups: Each channel can be included in up to 8 Area Groups. Area Groups can be used as 'GROUP PAGE' for display (Max 128 'GROUP PAGES') and/or it can be configured to activate (an) LED indicator(s) on a Bridge Group Panel, Mess room Panel or Cabin Panel and it will activate the Horn Output of the corresponding Panel. In the system we have a maximum of 256 Area Groups: • Print Status: Note: Alarm message lines are always sent to the printer. The following selections are possible for status information: • With Report Option 'OFF', you can select: • No posting of status message lines on the printer for this channel. • With Report Option 'ACTIVE ONLY', you can select: • Posting a status message line on the printer each time a status change from 'OFF' to 'ON' is detected for this channel. • With Report Option 'BOTH', you can select: • Posting a status message line on the printer each time a status change is detected for this channel. • Alarm Delay: Enter 0 to 99 sec (seconds) or min (minutes) before an alarm condition is to be reported. • Inhibitor.: Type '0' to select ‘NONE’ if no alarm inhibit is desired, or enter the channel number(refer to paragraph 4.2 Channel, Table, Numbering, page 35) which must inhibit the alarming of this channel. • Inhib Delay: Enter 0 to 99 sec (seconds) or min (minutes) before the inhibition is released after the inhibiting channel reverts to default. • Status Texts: Depending on the Report setting the system will show you either Alarm Text Messages or Status Text Messages. Select from 16 groups of texts and associated (text) colors shown in the window, to represent the channel’s status. (Texts themselves can be modified from another menu (page 221).

7.6.2.5.2 Status Source Other Channel

A digital and a virtual input can be configured, to be driven by another channel’s status. This channel can be a digital in- or output, or an analog input:

> **[Figure]** Screenshot of PAL channel configuration - Digital Input from Other Channel. Channel: 10105, Description: Boegschroef Hydr. Unit nivo. Type: Digital Input, Source: Other Channel. From Channel: 10101. Fail Detect: None, Norm. Cond.: Closed. Report: Alarm. Area Groups: 11-Verstelbare schroef SB. Alarm Delay: 3 sec. Status Texts: Normal, Laag (yellow), SensFail (red). Purpose: PAL digital input channel configured to receive its value from another channel (10101) rather than hardware.

• Type: Select ‘Digital Input’, to use this channel as a digital channel. • Source: Select ‘Other channel’ to use the status information from another channel. • Norm.Cond.: Select ‘OPEN’ or ‘CLOSED’ for the default signal from the other channel. • From Chan: Enter the channel (see paragraph 4.2.1 Channel Numbering, page 35) whose status to use as input.

For all other entries of this screen refer to paragraph 7.6.2.5.1 Standard Set-up Digital Input Channel, page 176.

7.6.2.5.3 Status Only With Logging Option

When no alarming is desired, a channel can be used for monitoring only. In this case you can still log the channel to a printer:

> **[Figure]** Screenshot of PAL channel configuration - Digital Input with Sensor fail detection. Channel: 10105, Description: Boegschroef Hydr. Unit nivo. Type: Digital Input, Source: Hardware Input. Fail Detect: Sensor, Norm. Cond.: Closed. Report: Status. Alarm Delay: 3 sec. Status Texts: Geopend (yellow), SensFail (red). Purpose: PAL digital input with sensor fail detection enabled and status reporting only (no alarm).

• Report: Select 'Status' • Print Status: Select 'Both' to log the status changes to the printer, 'Off' Otherwise. If you select 'Active Only' this channel will only be reported on the printer if the value changes from zero to one. Note: If the Fail Detect is set to 'Sensor' or 'Channel' or ‘Channel Status’ and there is an active failure signal, this will be reported on the Alarm Page (and printer).

For all other entries of this screen refer to paragraph 7.6.2.5.1 Standard Set-up Digital Input Channel, page 176.

#### 7.6.2.6 Analog Input Channel Setup

If you select a channel with the channel-type set to Analog input the system will provide you with the following setup fields:

> **[Figure]** Screenshot of PAL channel configuration - Analog Input for motor power measurement. Channel: 10201, Description: Boegschroef elektromotor elektris. verm. (Bow thruster electric motor power). Type: Analog Input, Source: 0-1V. Eng Unit Low: 0, Eng Unit High: 100. Displ. Deviat: 0.1, Filtersamples: 1. Limit Type: None. Report: Alarm. Purpose: PAL analog input for bow thruster motor electrical power, 0-1V source.

Prior to setting up an analog input a hardware analog input module must be configured. This module can be setup in the Processor Position table.

7.6.2.6.1 Standard Set-Up Analog Input Channel

• Tag Name: Enter any tag up to 10 characters. Tags must be unique. • Description: Enter any descriptive text up to 40 characters. • Type: • Select ‘ANALOG INPUT’ for a hardware analog input channel. Analog channels can be set-up and used as Digital inputs, refer to paragraph 7.6.2.5 Digital Input Channel Setup, page 176. • If you select a Type which does not correspond with the physical hardware related to that channel (for example 'DIG-OUT' for a real hardware analog input channel) the channel will behave as a virtual channel of that selected type (See paragraph 7.6.2.16, page 216). • Skip: • Select ‘No’ (channel is processed), • Select ‘Yes’ (channel is NOT processed).

• Source: • Select from the drop down list to set-up this channel (see below), • Select Not used to set this channel as 'Not Used', the value of this channel is undefined. • Scan Rate: Select a time at which interval the channel must be processed. • Fail Detect: This is an option to enable 'Failure' detection on the sensor. If a Failure is detected it will be reported as an alarm message line on the printer and on the 'ALARM PAGE' on the monitor and if the value of this channel is used in a Graphic Page the value will change its color to red. • Select 'None' if no failure detection is required. • Select 'Sensor' if failure detection is required. The detection is activated if one of the measurable limits are exceeded. (For connection of sensors, refer to 'Typical Signal and Sensor Connection Diagram' in the project related drawings). • Select ‘Channel’, to use the Sensorfail status of this Channel. • Select ‘Channel Status’, to use the limit status of this Channel. • Filter Samples: Enter the number of samples (Scans) which has to be used to calculate the running average. Valid entries are from 1 until 8. The running average will be used for displaying and alarming. • Displ. Deviat: Enter the minimal deviation of the value from the last update, to exceed before the value is updated (on the screen) again. • Limit Type: Select from 6 options on which condition(s) an alarm must be generated. • Nr Of Dec: Enter the number of decimals and this will be used for display. When this item is changed the display deviation will change automatically also. • Lowest Limit: Enter value for the lower alarm limit. • Highest Limit: Enter value for the higher alarm limit. • Rate Alarm: • Enter a value change (in ‘Eng Unit’ per scan) which must generate an alarm if exceeded. • Select ‘NONE’ if no rate alarm is desired. • Report: The Report option is to select what alarm report feature(s) will be activated if the alarm, or status change is detected. The following selections are possible: • Status: For group listing and mimic display. Channel not listed in alarm list. • Alarm No Horn: Deprecated, for backward compatibility. Shown in alarm list, but no audible • Emergency alarm: An alarm which indicates that immediate danger to human life or to the ship and its machinery exists and that immediate action should be taken. • Alarm: An alarm is a high priority of an alert. Condition requiring immediate attention and action, to maintain the safe navigation and operation of the ship.

• Warning: Condition requiring no immediate attention or action. Warnings are presented for precautionary reasons to bring awareness of changed conditions which are not immediately hazardous, but may become so if no action is taken. • Caution: Lowest priority of an alert. Awareness of a condition which does not warrant an alarm or warning condition, but still requires attention out of the ordinary consideration of the situation or of given information.

Status Report The Report Option 'Status' signifies that the signal is not activating an alarm message on the 'ALARM PAGE' and is not activating the HORN output. But it will activate the posting of a status message line on the printer if the status changes (If Print Status option is set to 'YES').

|  |  | If the Sensor Failure is used and the Sensor Failure is activated, it will create an |  |
| --- | --- | --- | --- | |
|  |  | alarm message on the 'ALARM PAGE' and it will post an alarm message line on the |  |
|  |  | printer. |  |

Alarm no horn When 'Alarm No Horn' is configured it will not activate the HORN output on XP Board, but it will activate horn on active server (plays the wave file via MPC speaker)

Alarm and Emergency The other report options configure that the signal shows an alarm message on the 'ALARM PAGE' and activates the 'HORN' output.

The HORN on XP Board and on active server workstation will both turn on. The active server requires group configuration for this.

Warning and Caution Warning and Caution have different alarm behavior as the other options.

When Warning becomes active, the horn and it's flash state stays on for 2 seconds. After that time horn output is deactivated and the warning flash state is turned off. But the warning state stays unacknowledged and after 5 minutes the warning priority will change into Alarm. Only in case there was no human intervention or the cause of the warning was not rectified.

When Caution becomes active, the system shows visual steady alarm (no flash). The caution will disappear as soon as the cause of the caution is rectified. It is also possible to have separate alarm-lists with only 'Emergency Alarms', or only 'Cautions', or only 'Warnings'.

• Area Groups:

Each channel can be included in up to 8 Area Groups. Area Groups can be used as 'GROUP PAGE' for display (Max 128 'GROUP PAGES') and/or it can be configured to activate (an) LED indicator(s) on a Bridge Group Panel, Mess room Panel or Cabin Panel and it will activate the Horn Output of the corresponding Panel. In the system we have a maximum of 256 Area Groups: • Print Status: Note: Alarm message lines are always sent to the printer. The following selections are possible for status information: • With Report Option 'OFF', you can select: • No posting of status message lines on the printer for this channel. • With Report Option 'ACTIVE ONLY', you can select: • Posting a status message line on the printer each time a status change from 'OFF' to 'ON' is detected for this channel. • With Report Option 'BOTH', you can select: • Posting a status message line on the printer each time a status change is detected for this channel. • Alarm Delay: Enter 0 to 99 sec (seconds) or min (minutes) before an alarm condition is to be reported. • Dead Band: Enter the band (% of ‘Eng Unit’ range) below an alarm limit in which the alarm condition must remain. • Inhibitor.: Type '0' to select ‘NONE’ if no alarm inhibit is desired, or enter the channel number(refer to paragraph 4.2 Channel, Table, Numbering, page 35) which must inhibit the alarming of this channel. • Inhib Delay: Enter 0 to 99 sec (seconds) or min (minutes) before the inhibition is released after the inhibiting channel reverts to default. • Status Texts: Depending on the Report setting the system will show you either Alarm Text Messages or Status Text Messages. Select from 16 groups of texts and associated (text) colors shown in the window, to represent the channel’s status. (Texts themselves can be modified from another menu (page 221).

7.6.2.6.2 Pre-defined Thermocouple (TC/PT100) On Mixed boards only it is possible with appropriate sensor adapter to measure temperatures with accuracy of 0.25% of the range.

> **[Figure]** Screenshot of PAL channel configuration - Analog Input with source type dropdown open. Channel: 01101, Description: Temperature Cooling System. Type: Analog Input, Source dropdown showing options: Not Installed, J TC (0-355C, 0-695C, 0-760C), K TC (0-470C, 0-945C, 0-1230C), 3w RTD: -40 145C (highlighted blue), 3w RTD: -40 750C, 0-20mA, 4-20mA, 0-1V, 0-10V, Other Channel, Remote Data, IEC-1131. Eng Unit Low: 40, Eng Unit High: 145, Eng Unit Type: DegC. Purpose: PAL analog input sensor type selection showing all available input types including thermocouples, RTD, current/voltage, and digital options.

An analog hardware input can be configured as a pre-defined thermocouple sensor: Sensor: Select the corresponding thermocouple sensor. Cold Junction: Enter the channel (refer to paragraph 4.2.1 Channel Numbering, page 35) to compensate for ambient temperature.

7.6.2.6.3 Pre-defined RTD (Resistance Temperature Detectors / PT100) An analog hardware input can be configured as a pre-defined RTD sensor: Sensor: Select the corresponding RTD sensor. The accuracy is 0.25% of the range: For 3 wired RTD: -40 to 145°C the accuracy is 0.25%*185°C = 0.463°C. For 3 wired RTD: -40 to 750°C the accuracy is 0.25%*790°C = 1.975°C. The sensor deviation (PT100 sensor tolerance) must also be taken into account: Class A: dT = ± (0,15 °C + 0,002 • |T|) (source WikiPedia) Class B: dT = ± (0,30 °C + 0,005 • |T|) (source WikiPedia) Deviation at 145°C : Klass A = 0.44°C, Klass B = 1.65°C Deviation at 750°C : Klass A = 1.03°C, Klass B = 4.05°C The sensor deviation has to be added to the input tolerance.

|  |  |  | PT100 formula from https://nl.wikipedia.org/wiki/Pt100 |
| --- | --- | --- | --- | |

7.6.2.6.4 User Defined Sensor An analog hardware input can be configured for a user defined sensor: Enter the following settings: • Sensor: Select the corresponding sensor. • Convert Table: Select 'None’: a linear range can now be set-up (see next). • Eng Unit Low: Enter the low end of the linear range. • Eng Unit High: Enter the high end of the linear range. • Eng Unit Type: Enter up to 4 characters to represent the unit type of the range.

> **[Figure]** Screenshot of PAL channel configuration - Analog Input with Convert Table dropdown open. Channel: 10502, Description: Pressure tank 101. Type: Analog Input, Sensor: 0-20mA. Convert Table dropdown showing: None (highlighted), Tank Table 1023, Tank Table 1024, Tank Table 1033, Table 4, Table 5, Table 6. Eng Unit High: 500, Eng Unit Type: mBar. Purpose: PAL analog input with tank/conversion table selection for non-linear sensor linearization.

For all other entries of this screen refer to paragraph 7.6.2.6.1 Standard Set-Up Analog Input Channel, page 182.

It is also possible to choose from one of 16 user defined linearization tables, e.g. a tank table. The tables themselves can be modified from another menu, see paragraph 7.6.3 Conversion Tables, page 219).

Enter the following settings: • Source: Select the corresponding sensor (Not pre-defined Thermocouple or pre- defined RTD). • Convert Table: Select the required conversion table. The system will automatically fill in the high- and low engineering unit range according to the selected conversion table.

• Eng Unit Type: Enter up to 4 characters to represent the unit type of the range.

For all other entries of this screen refer to paragraph 7.6.2.6.1 Standard Set-Up Analog Input Channel, page 182.

7.6.2.6.5 Value Source Other Channel

An analog and a virtual input can be configured to take as its input from another analog input channel’s process value (e.g. to convert height into contents with a tank table):

> **[Figure]** Screenshot of PAL channel configuration - Analog Input from Other Channel. Channel: 10202, Description: Tankinhoudsmeting Grijswatertank 3 (Grey water tank 3 level). Type: Analog Input, Source: Other Channel. From Channel: 10101. Eng Unit Low: 0, Eng Unit High: 100. Report: Alarm No Horn. Purpose: PAL analog input deriving its value from another channel (10101) for grey water tank measurement.

Enter the following settings: • Type: Select ‘Analog Input’. • Source: Select 'Other Channel Value' to select this option. • From Chan: Enter the channel (see paragraph 4.2.1 Channel Numbering, page 35) whose value to use as input. • Fail Detect: ‘Sensor’ is not available.

For all other entries of this screen refer to paragraph 7.6.2.6.1 Standard Set-Up Analog Input Channel, page 182.

7.6.2.6.6 Value Source 1131 Variable

An analog and a virtual input can be configured to follow the analog output of IEC - 1131:

> **[Figure]** Screenshot of PAL channel configuration - Analog Input with source type dropdown showing IEC-1131 option. Channel: 01144. Source dropdown open: Not Installed, Other Channel, Remote Data, IEC-1131 (highlighted blue). Eng Unit Low: 0.0, Eng Unit High: 100.0, Eng Unit Type: DegC. Limit Type: L/H, Lowest 0.0, Highest 100.0. Report: Alarm. Purpose: PAL analog input source selection showing the IEC-1131 source option for receiving values from PLC programs.

Enter the following settings: • Type: Select ‘Analog Input’. • Source: IEC - 1131 to select this option. • Fail Detect: Select ‘Sensor’ to generate an alarm if the function value is outside the ‘Eng Unit’ range, or choose ‘NONE'. • Eng Unit Low: Enter the low cut-off end of the function value. • Eng Unit High: Enter the high cut-off end of the function value.

For all other entries of this screen refer to paragraph 7.6.2.6.1 Standard Set-Up Analog Input Channel, page 182.

7.6.2.6.7 Failure Forced By 1131

Any type of analog input can be forced into a failure status according to the digital output of another channel:

> **[Figure]** Screenshot of PAL channel configuration - Analog Input with IEC-1131 source and Channel fail detection. Channel: 01144. 1131 Name: NOT USED-C144-(FINT). Type: Analog Input, Source: IEC-1131. Fail Detect: Channel dropdown value 01145. Eng Unit Low: 0.0, Eng Unit High: 100.0, Eng Unit Type: DegC. Limit Type: L/H, Lowest 0.0, Highest 100.0. Report: Alarm. Purpose: PAL IEC-1131 analog input with channel 01145 used as sensor fail detection source.

Enter the following settings: • Fail Detect: Enter the function connection scheme name and function output (see paragraph 4.2.2 Interface with 1131 , page 36) to use as failure signal.

For all other entries of this screen refer to paragraph 7.6.2.6.1 Standard Set-Up Analog Input Channel, page 182.

7.6.2.6.8 Status Only With Logging Option

When no alarming is desired, a channel can be used for monitoring only. In this case you can still log the channel to a printer:

> **[Figure]** Screenshot of PAL channel configuration - Analog Input with thermocouple J TC source. Channel: 10202, Description: Tankinhoudsmeting Grijswatertank 3. Type: Analog Input, Source: J TC: 0 450C. Cold Junction: 0. Eng Unit High: 457 (greyed), Eng Unit Type: degC. Report: Status. Print Status dropdown open: Off, Active Only, Both. Purpose: PAL thermocouple input configuration with Print Status dropdown showing options.

Enter the following settings: • Report: Select ‘Status'. • Print Status: Select 'Both' to log the status changes to the printer, 'Off' Otherwise. The setting 'Active Only' will only report this channel on the printer if the value changes from zero to one. Note: If the Fail Detect is set and there is an active failure signal, this will be reported on the Alarm Page (and printer).

For all other entries of this screen refer to paragraph 7.6.2.6.1 Standard Set-Up Analog Input Channel, page 182.

#### 7.6.2.7 Pulse Input as frequency measurement Channel Setup

A pulse input can be used as frequency counter (Sensor Type 1). In this case the hardware counter will count the pulses during the Scan Rate interval and process the accumulation at the end of Scan Rate interval. When a pulse-input channel is selected the following appears on the screen:

Pulse/Conversion Range Enter a value between 1 and 3000 to indicate the number of pulses per Conversion Range (interval) Conversion Range Range limit when during the Scan Rate the number of Pulses / Scan are counted Scan rate Processing interval on which the counter value will be evaluated (processed)

> **[Figure]** Screenshot of PAL channel configuration - Pulse Input (Frequency counter). Channel: 11102, Description: frequency. Type: Pulse Input, Source: Frequency Measure. Pulse/Conversion Range: 3, Conversion Range: 10.000, Scan Rate: 0.1. Max Range: 1000.000, Eng Unit Type: Lit/s. Displ. Deviat: 0.001, Nr Dec.: 3. Limit Type: L/H, Lowest Limit: 0.000, Highest Limit: 999.000. Purpose: PAL pulse input configured as a frequency counter for flow measurement in liters/second.

Pulse Counter number of pulses recorded in Scan Rate period of time Pulse Input Channel Value Value from above formula, clamped at Max Range value

Example: A flow meter with a frequency of 0-40 Hz for a flow of 0-500Liter. Use a Scan rate of 5 to process each 5 seconds (Scan Rate). When 150 pulses are counted (which equals 30Hz) within this interval the value of this channel will indicate 375 liter.

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

#### 7.6.2.8 Pulse Input as pulse counter Channel Setup

Pulse Input used as Pulse Counter A pulse input can be used for pulse counting (Sensor Type 2). In this case the hardware counter will count pulses starting at the moment that the Start Count input will change from ‘False’ to ‘True’. The counting will stop at the moment the Stop Count will change from ‘False’ to ‘True’. The counter will reset at the moment the Reset Count will change from ‘False’ to True’.

> **[Figure]** Screenshot of PAL channel configuration - Pulse Input (Pulse counter). Channel: 11103, Description: flow meter. Type: Pulse Input, Source: Pulse counter. Pulse/Conversion Range: 40, Conversion Range: 100.000. Start Count: 0, Stop Count: 0, Reset Count: 0, Direction Channel: None. Max Range: 1000.000, Eng Unit Type: Liter. Displ. Deviat: 0.001, Nr Dec.: 3. Limit Type: L/H, Lowest Limit: 0.000, Highest Limit: 100.000. Purpose: PAL pulse counter input for flow meter measuring in liters.

Pulse / Scan Enter a value between 1 and 3000 to indicate the number of pulses to be counted to set the output to 100% of the range. Range Range limit for the output value. Start Count Transition from ‘False’ to ‘True’ on this channel will start the counting process. This channel must be a local channel on same I/O module Stop Count Transition from ‘False’ to ‘True’ on this channel will stop the counting process. This channel must be a local channel on same I/O Module Reset Count Transition from ‘False’ to ‘True’ on this channel will reset the counter. This channel must be a local channel on same I/O Module. If the reset is defined as the pulse input channel itself, it will execute the reset command as soon as the output passes the highest limit. Direction External Channel as direction input. The direction of pulse counting follows the channel value. On this manner up/down functionality can be implemented. Local channel on same IO Module as direction output. It can be used to read the automatic detected direction. The direction is detected by the by IO Module software. This software evaluates the phase shifting between paired channels. On 24MIX these are inputs 2, 3 and 14, 15. On 36DI these are inputs 25, 26 and 33, 34. During counting the output will be equal to:

> **[Vector Diagram — Page 194]** Page 194 documents the Standard Set-Up Pulse Input Channel for MEGA-GUARD IOM, including the pulse input value conversion formula and all configuration parameters.

Formula: Pulse Input Channel Value Calculation (displayed prominently):
Pulse Input Channel Value = Pulse Counter x (Conversion Range / Pulse/Conversion Range)
The formula uses fraction notation with 'Conversion Range' as numerator and 'Pulse/Conversion Range' as denominator. Input variable: Pulse Counter (raw count of pulses received per scan interval). Output: engineering unit value of the channel.

Note (hand icon warning): 'Pulse input channels can be used for high frequency when configured on special input locations. For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2 kHz, others 100 Hz. For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to 2 kHz, others 100 Hz.'

Section 7.6.2.1: Standard Set-Up Pulse Input Channel parameters:
- Tag Name: up to 10 characters, must be unique
- Description: up to 40 characters
- Type: 'Pulse' (channel type preset)
- Source: Not Installed / Select Pulse Counter / Speed Counter Up/Down / Stored Pulse Counter
- Fall Detect: No (fall detection not available for pulse type)
- Eng Unit Type: select from 6 options
- Input Deviation: minimal deviation from last update needed before value is updated (applies to all updates between XPs and between XP and OWS)
- Limit Type: select from 6 options for alarm limit types
- Nr Of Limits: up to 15, selectable from dropdown

Page 194 is from section 7.6.2 ('I/O Channel Setup'). Pulse input configuration is used on MEGA-GUARD IOM modules for flow meters, RPM sensors, and similar frequency-generating transducers on ships.

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

7.6.2.8.1 Standard Set-Up Pulse Input Channel

Tag Name: • Enter any tag up to 10 characters. Tags must be unique. Description: • Enter any descriptive text up to 40 characters. Type: • Shows ‘Pulse Input’ as information only. Skip: • Select ‘No’ (channel is processed). • Select ‘Yes’ (channel is NOT processed). Source: • Select 'Not Installed' to remove this channel from set-up. • Select 'Frequency Counter' to use this input as a frequency counter. • Select 'Pulse Counter' to use this channel as a pulse counter. • Select 'Cascaded Frequency' to use this channel as a cascaded frequency counter. • Select 'Speed Counter' to use this channel as a speed counter (interrupt driven) • Select 'Up/Down Counter' to use a channel of this module as an Up- Down Counter • Select 'Stored Pulse Counter' to use this cannel for stored pulse counting Fail Detect: • Select ‘None’ (fail detection is not available). • Failure detection can be driven via an output of a function block connection scheme. Eng Unit Type: • Enter up to 4 characters to represent the unit type of the range. Displ. Deviat: • Minimal deviation of the value from the last update, to exceed before the value is updated again. This is used for all updates, between XP’s and between XP and server. Limit Type: • Select from 6 options on which condition(s) an alarm must be generated. Nr Of Dec:

> **[Vector Diagram — Page 195]** Page 195 continues the MEGA-GUARD IOM pulse input channel setup, documenting Report/Status, Alarm types, sensor failure behavior, and Horn configuration.

Continued Parameter Documentation: Standard Set-Up Pulse Input Channel.

Lower Limit / Upper Limit: Enter engineering unit value for the lower/upper alarm limit. Repeated for each of up to 6 alarm limit options.

Status/Source options (continued): Not Installed / Cascaded Frequency Counter / Up/Down Counter / Stored Pulse Counter.

Report option types:
- Status: Signal does NOT activate an alarm message on the ALARM PAGE; displayed as status only
- Alarm: Signal activates alarm on ALARM PAGE and printout
- Emergency alarm: Requires immediate attention; highest priority
- Warning alarm: Condition requires attention but not immediately hazardous
- Advisory: Attention of operating personnel required for the condition

Status Display Logic (note box): 'If the Sensor Failure is used and the Sensor Failure is activated, it will create an alarm message on the ALARM PAGE and it will post a status message line on the printer.'

Alarm no Horn note: 'If the Sensor Failure is used and the Alarm no Horn is configured it will not activate the HORN output on XP Board, but it will activate alarm service via MPC speaker.'

Report option 'Status': signifies the signal is not activating an alarm message on the ALARM PAGE. Select 'Alarm' type: signal activates alarm on ALARM PAGE and printout.

Page 195 continues section 7.6.2.1. Documents Report/Status alarm classification options for IOM pulse input channels in MEGA-GUARD OWS iObserver alarm management display.

• Enter the number of decimals and this will be used for display. When this item is changed the display deviation will change automatically also. Lowest Limit: • Enter value for the lower alarm limit. Highest Limit: • Enter value for the higher alarm limit. Rate Alarm: • Enter a value change (in ‘Eng Unit’ per scan) which must generate an alarm if exceeded. Select ‘None’ if no rate alarm is desired. Report: The Report option is to select what alarm report feature(s) will be activated if the alarm, or status change is detected. The following selections are possible: • Status: For group listing and mimic display. Channel not listed in alarm list. • Alarm No Horn: Deprecated, for backward compatibility. Shown in alarm list, but no audible • Emergency alarm: An alarm which indicates that immediate danger to human life or to the ship and its machinery exists and that immediate action should be taken. • Alarm: An alarm is a high priority of an alert. Condition requiring immediate attention and action, to maintain the safe navigation and operation of the ship. • Warning: Condition requiring no immediate attention or action. Warnings are presented for precautionary reasons to bring awareness of changed conditions which are not immediately hazardous, but may become so if no action is taken. • Caution: Lowest priority of an alert. Awareness of a condition which does not warrant an alarm or warning condition, but still requires attention out of the ordinary consideration of the situation or of given information.

Status Report The Report Option 'Status' signifies that the signal is not activating an alarm message on the 'ALARM PAGE' and is not activating the HORN output. But it will activate the posting of a status message line on the printer if the status changes (If Print Status option is set to 'YES').

|  |  | If the Sensor Failure is used and the Sensor Failure is activated, it will create an |  |
| --- | --- | --- | --- | |
|  |  | alarm message on the 'ALARM PAGE' and it will post an alarm message line on the |  |
|  |  | printer. |  |

Alarm no horn When 'Alarm No Horn' is configured it will not activate the HORN output on XP Board, but it will activate horn on active server (plays the wave file via MPC speaker)

Alarm The other report options configure that the signal shows an alarm message on the 'ALARM PAGE' and activates the 'HORN' output.

The HORN on XP Board and on active server workstation will both turn on. The active server requires group configuration for this.

Warning and Caution Warning and Caution have different alarm behavior as the other options.

When Warning becomes active, the horn and it's flash state stays on for 2 seconds. After that time horn output is deactivated and the warning flash state is turned off. But the warning state stays unacknowledged and after 5 minutes the warning priority will change into Alarm. Only in case there was no human intervention or the cause of the warning was not rectified.

When Caution becomes active, the system shows visual steady alarm (no flash). The caution will disappear as soon as the cause of the caution is rectified. It is also possible to have separate alarm-lists with only 'Emergency Alarms', or only 'Cautions', or only 'Warnings'.

Area Groups: Each channel can be included in up to 8 Area Groups. Area Groups can be used as 'GROUP PAGE' for display (Max 128 'GROUP PAGES') and/or it can be configured to activate (an) LED indicator(s) on a Bridge Group Panel, Mess room Panel or Cabin Panel and it will activate the Horn Output of the corresponding Panel. In the system we have a maximum of 256 Area Groups: Print Status: Note: Alarm message lines are always sent to the printer. The following selections are possible for status information: • With Report Option 'OFF', you can select: • No posting of status message lines on the printer for this channel. • With Report Option 'ACTIVE ONLY', you can select: • Posting a status message line on the printer each time a status change from 'OFF' to 'ON' is detected for this channel. • With Report Option 'BOTH', you can select: • Posting a status message line on the printer each time a status change is detected for this channel. Alarm Delay: • Enter 1 to 99 sec(onds) or min(utes) before an alarm condition is to be reported. Dead Band: • Enter the band (% of ‘Eng Unit’ range) below an alarm limit in which the alarm condition must remain. Inhibitor.: • Select ‘None’ if no alarm inhibit is desired, or enter the channel number(refer to paragraph 4.2 Channel, Table, Numbering, page 35) which must inhibit the alarming of this channel. Inhib Delay:

• Enter 1 to 99 sec(onds) or min(utes) before the inhibition is released after the inhibiting channel reverts to default. Status Texts: • Select from 16 groups of texts shown in the window, to represent the channel’s status. Texts themselves can be modified from another menu (See paragraph 7.5.4 Status text).

|  |  | Note: When using only 1 frequency measurement the maximum pulse input |  |
| --- | --- | --- | --- | |
|  |  | frequency for is approximately 4kHz. |  |

7.6.2.8.2 Pulse Input Channel used as Frequency Counter A pulse input can be used as frequency counter (Select Sensor Type 'Frequency Counter'). In this case the hardware counter will count the pulses during the Scan Rate interval and process the accumulation at the end of Scan Rate interval.

> **[Figure]** Screenshot of PAL channel configuration - Pulse Input (Frequency counter) for flow tank. Channel: 10502, Description: Input Flow Tank1054. Type: Pulse Input, Sensor: Frequency counter. Pulse/Scan: 200, Scan Rate: 5 sec. Range: 500, Eng Unit Type: Liter. Displ. Deviat: 1, Limit Type: H, Highest Limit: 500. Report: Alarm. Purpose: PAL frequency counter pulse input for tank input flow measurement.

• Pulse / Scan: Enter a value between 1 and 3000 to indicate the number of pulses per Scan Rate (interval) • Scan Rate: Processing interval on which the counter value will be evaluated (processed) • Range: Range limit when during the Scan Rate the number of Pulses / Scan are counted.

Channel 2,3,

For all other entries of this screen refer to paragraph 0

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

#### 7.6.2.9 Pulse Input as pulse counter Channel Setup

Pulse Input used as Pulse Counter A pulse input can be used for pulse counting (Sensor Type 2). In this case the hardware counter will count pulses starting at the moment that the Start Count input will change from ‘False’ to ‘True’. The counting will stop at the moment the Stop Count will change from ‘False’ to ‘True’. The counter will reset at the moment the Reset Count will change from ‘False’ to True’.

> **[Figure]** Screenshot of PAL Pulse Input configuration - Pulse counter. Channel: 11103, Description: flow meter. Type: Pulse Input, Source: Pulse counter. 40 pulses/Conversion Range 100.000, Liters. Limit Type: L/H, Lowest: 0.000, Highest: 100.000. Purpose: reference configuration for PAL pulse counter flow meter channel.

Pulse / Scan Enter a value between 1 and 3000 to indicate the number of pulses to be counted to set the output to 100% of the range. Range Range limit for the output value. Start Count Transition from ‘False’ to ‘True’ on this channel will start the counting process. This channel must be a local channel on same I/O module Stop Count Transition from ‘False’ to ‘True’ on this channel will stop the counting process. This channel must be a local channel on same I/O Module Reset Count Transition from ‘False’ to ‘True’ on this channel will reset the counter. This channel must be a local channel on same I/O Module. If the reset is defined as the pulse input channel itself, it will execute the reset command as soon as the output passes the highest limit. Direction External Channel as direction input. The direction of pulse counting follows the channel value. On this manner up/down functionality can be implemented. Local channel on same IO Module as direction output. It can be used to read the automatic detected direction. The direction is detected by the by IO Module software. This software evaluates the phase shifting between paired channels. On 24MIX these are inputs 2, 3 and 14, 15. On 36DI these are inputs 25, 26 and 33, 34. During counting the output will be equal to:

> **[Vector Diagram — Page 200]** Page 200 presents the Pulse Input Channel Value formula as a section header, a note on high-frequency pulse input locations, a worked calculation example, and a page reference.

Formula (section header):
Pulse Input Channel Value = Pulse Counter x (Conversion Range / Pulse/Conversion Range)
Typeset as fraction: Conversion Range (numerator) over Pulse/Conversion Range (denominator).

Note (hand icon): 'Pulse input channels can be used for high frequency when configured on special input locations. For 24 Mixed IO Module: input 2, 3, 14, 15 -> Frequency up to 2 kHz, others 100 Hz. For 36 Digital Input Module: input 25, 26, 33, 34 -> Frequency up to 2 kHz, others 100 Hz.'

Reference text: 'Standard Set-Up Pulse Input Channel, page 192.'

Worked Calculation Example: 'A flow meter that gives a frequency of 0-40 Hz for a flow of 0-500 Liter. In the above sample the value will be processed each 5 seconds (Scan Rate). If we count 150 pulses (equal to 30 Hz) within this interval the value of this channel will indicate:'

Formula rendered as fraction:
150 (input) / 200 (Pulses/Scan) x 500 (range) = 375 Liter

Where: 150 = pulses counted in 5-second scan interval; 200 = Pulse/Conversion Range setting (full-scale pulses per scan); 500 = Conversion Range (engineering unit full scale, 500 Liters); Result = 375 Liters.

Page 200 is from section 7.6.2 ('Pulse Input Channel Setup'). Demonstrates how MEGA-GUARD IOM converts raw pulse counts from flow meters, RPM sensors into engineering unit values for OWS display and alarming.

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

Standard Set-Up Pulse Input Channel, page 192.

Example:

A flow meter that gives a frequency of 0-40 Hz for a flow of 0-500 Liter. In the above sample the value will be processed each 5 seconds (Scan Rate). If we count 150 pulses (equal to 30Hz) within this interval the value of this channel will indicate

1 5 0 ( i n p u t ) • 5 0 0 ( r a n g e ) = 3 7 5 L i t e r . 2 0 0 ( P u l s e s / S c a n )

7.6.2.9.1 Pulse Input Channel used as Pulse Counter A pulse input can be used for pulse counting (Select Sensor Type 'Pulse Counter'). In this case the hardware counter will count pulses starting at the moment that the Start Count input will change from ‘False’ to ‘True’. The counting will stop at the moment the Stop Count will change from ‘False’ to ‘True’. The counter will reset at the moment the Reset Count will change from ‘False’ to True’. The following screen view will give you an example:

> **[Figure]** Screenshot of PAL channel configuration - Pulse Input (Pulse counter for compressor). Channel: 10502, Description: Compressor Running. Type: Pulse Input, Sensor: Pulse counter. Pulse/Range: 2000. Start Count: 4, Stop Count: 5, Reset: 6. Range: 500, Eng Unit Type: Min. Limit Type: H, Highest Limit: 500. Report: Alarm. Purpose: PAL pulse counter measuring compressor running time in minutes, with separate start/stop/reset control channels.

• Pulse / Range: Enter a value between 1 and 3000 to indicate the number of pulses to be counted to set the output to 100% of the range. During counting the output will be equal Countervalue to: xRange=Output Pulse/Scan • Range: Range limit for the output value. • Start Count: Transition from ‘False’ to ‘True’ on this channel will start the counting process. This channel must be a local channel on this I/O module. • Stop Count: Transition from ‘False’ to ‘True’ on this channel will stop the counting process. This channel must be a local channel on this I/O module. • Reset: Transition from ‘False’ to ‘True’ on this channel will reset the counter. This channel must be a local channel on this I/O module. If the reset is defined as the pulse input channel itself, it will execute the reset command as soon as the output has passed the highest limit.

For all other entries of this screen refer to paragraph

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

#### 7.6.2.10 Pulse Input as pulse counter Channel Setup

Pulse Input used as Pulse Counter A pulse input can be used for pulse counting (Sensor Type 2). In this case the hardware counter will count pulses starting at the moment that the Start Count input will change from ‘False’ to ‘True’. The counting will stop at the moment the Stop Count will change from ‘False’ to ‘True’. The counter will reset at the moment the Reset Count will change from ‘False’ to True’.

> **[Figure]** Screenshot of PAL Pulse Input configuration - Pulse counter. Channel: 11103, Description: flow meter. Identical configuration to p193_i2. Purpose: another reference instance of PAL flow meter pulse counter configuration.

Pulse / Scan Enter a value between 1 and 3000 to indicate the number of pulses to be counted to set the output to 100% of the range. Range Range limit for the output value. Start Count Transition from ‘False’ to ‘True’ on this channel will start the counting process. This channel must be a local channel on same I/O module Stop Count Transition from ‘False’ to ‘True’ on this channel will stop the counting process. This channel must be a local channel on same I/O Module Reset Count Transition from ‘False’ to ‘True’ on this channel will reset the counter. This channel must be a local channel on same I/O Module. If the reset is defined as the pulse input channel itself, it will execute the reset command as soon as the output passes the highest limit. Direction External Channel as direction input. The direction of pulse counting follows the channel value. On this manner up/down functionality can be implemented. Local channel on same IO Module as direction output. It can be used to read the automatic detected direction. The direction is detected by the by IO Module software. This software evaluates the phase shifting between paired channels. On 24MIX these are inputs 2, 3 and 14, 15. On 36DI these are inputs 25, 26 and 33, 34. During counting the output will be equal to:

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

> **[Figure]** Screenshot of PAL channel configuration - Pulse Input (Speed counter for main engine RPM). Channel: 10502, Description: Main Engine RPM. Type: Pulse Input, Sensor: Speed counter. Teeth/Rev.: 180, Nr.Cylinder: 12. Range: 200, Eng Unit Type: Hz. Displ. Deviat: 1, Limit Type: H, Overspeed: 20 and 150. Report: Alarm. Purpose: PAL speed counter pulse input for Main Engine RPM measurement with overspeed detection.

Standard Set-Up Pulse Input Channel, page 192.

7.6.2.10.1 Pulse Input Channel used as a Speed Counter (Interrupt driven) The use of a pulse input as speed counter: The following screen view shows you the setup

• Teeth/Rev.: Enter the number of teeth on the flywheel for one revolution. Nr. Cylinder: Enter the number of cylinders for this engine • Range: Range limit. • Oversp. Teeth: Enter the detection level on the number of teeth per cylinder when we have to detect the over speed. • Overspeed RPM: Enter the limit for detection of over speed on RPM of the engine.

For all other entries of this screen refer to paragraph

> **[Vector Diagram — Page 204]** Page 204 contains only a high-frequency pulse input note (hand icon warning) for the MEGA-GUARD IOM Standard Set-Up Pulse Input Channel section.

Note (hand/stop icon warning):
'Pulse input channels can be used for high frequency when configured on special input locations.
For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz
For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to 2Khz, others 100Hz'

No diagrams or tables are present on this page beyond this cautionary note. The page specifies frequency capability restrictions for MEGA-GUARD IOM pulse input channels: only the specifically designated inputs (inputs 2, 3, 14, 15 on 24MIO or inputs 25, 26, 33, 34 on 36DI) support high-frequency pulse counting up to 2 kHz. All other IOM pulse inputs are limited to 100 Hz maximum counting frequency.

This distinction is critical for correct wiring of flow meters, RPM sensors, or other high-frequency transducers to the MEGA-GUARD IOM. Page 204 is part of section 7.6.2 ('Pulse Input Channel Setup').

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

#### 7.6.2.11 Pulse Input as pulse counter Channel Setup

Pulse Input used as Pulse Counter A pulse input can be used for pulse counting (Sensor Type 2). In this case the hardware counter will count pulses starting at the moment that the Start Count input will change from ‘False’ to ‘True’. The counting will stop at the moment the Stop Count will change from ‘False’ to ‘True’. The counter will reset at the moment the Reset Count will change from ‘False’ to True’.

> **[Figure]** Screenshot of PAL Pulse Input configuration - Pulse counter. Channel: 11103, Description: flow meter. Same configuration as p193_i2. Purpose: additional reference instance of PAL pulse counter configuration.

|  | Pulse / |  |  | Enter a value between 1 and 3000 to indicate the number of pulses to be counted |  |
| --- | --- | --- | --- | --- | --- | |
|  | Scan |  |  | to set the output to 100% of the range. |  |
|  | Range |  |  | Range limit for the output value. |  |
|  | Start |  |  | Transition from ‘False’ to ‘True’ on this channel will start the counting process. This |  |
|  | Count |  |  | channel must be a local channel on same I/O module |  |
|  | Stop |  |  | Transition from ‘False’ to ‘True’ on this channel will stop the counting process. This |  |
|  | Count |  |  | channel must be a local channel on same I/O Module |  |
| Reset Count | Reset |  |  | Transition from ‘False’ to ‘True’ on this channel will reset the counter. This channel |  |
|  | Count |  |  | must be a local channel on same I/O Module. If the reset is defined as the pulse |  |
|  |  |  |  | input channel itself, it will execute the reset command as soon as the output passes |  |
|  |  |  |  | the highest limit. |  |
| Direction |  |  |  | External Channel as direction input. The direction of pulse counting follows the |  |
|  |  |  |  | channel value. On this manner up/down functionality can be implemented. |  |
|  |  |  |  | Local channel on same IO Module as direction output. It can be used to read the |  |
|  |  |  |  | automatic detected direction. The direction is detected by the by IO Module |  |
|  |  |  |  | software. This software evaluates the phase shifting between paired channels. On |  |
|  |  |  |  | 24MIX these are inputs 2, 3 and 14, 15. On 36DI these are inputs 25, 26 and 33, 34. |  |

During counting the output will be equal to:

> **[Vector Diagram — Page 206]** Page 206 presents section headings 7.6.2.12, 7.6.2.13, and 7.6.2.14 with the pulse input channel formula header repeated as a section marker and a high-frequency note.

Section headings present (content on subsequent pages):
- Section 7.6.2.12 (heading only, no body content on this page)
- Section 7.6.2.13 (heading only)
- Section 7.6.2.14 (heading with note below)

Formula (section header repeated):
Pulse Input Channel Value = Pulse Counter x (Conversion Range / Pulse/Conversion Range)
Typeset as fraction.

Note under section 7.6.2.14 (hand icon): 'Pulse input channels can be used for high frequency when configured on special input locations. For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz. For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to 2Khz, others 100Hz.'

Reference: 'Standard Set-Up Pulse Input Channel, page 192.'

Page 206 is from section 7.6.2 of the Engineering Guide. The three sub-section headings (7.6.2.12, 7.6.2.13, 7.6.2.14) represent three different pulse input channel setup variants sharing the same base formula (Pulse Counter x Conversion Range / Pulse/Conversion Range) and frequency input location restriction.

7.6.2.12

7.6.2.13

7.6.2.14

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

Standard Set-Up Pulse Input Channel, page 192.

7.6.2.14.1 Pulse Input Channel used as an Up- Down Counter This setup is valid for the 6018-610 I/O module type. Pulse input channel xxx13 until xxx15 can be used as an Up- Down counter. The UP or DOWN detection is realized via the phase shift of two pulse inputs (channel xxx09 and channel xxx11) and is automatically setting the count direction. Channels xxx09 and xxx11 must be setup as cascaded counter. Channel xxx10 is used for can only be used as a digital input to be able to read back the status ‘UP’. Channel xxx12 is used for can only be used as a digital input to be able to read back the status ‘DOWN’, detected by the hardware on this module. The following screen view gives you an overview of the setup of such a counter:

> **[Figure]** Screenshot of PAL channel configuration - Pulse Input (Up/Down counter). Channel: 10502, Description: Up/Down Counter. Type: Pulse Input, Sensor: Up/Down counter. Pulse/Range: 500. Start Count: Up, Stop Count: Down, Reset: Up. Range: 500. Limit Type: L/H, Lowest: 0, Highest Limit: 500. Report: Alarm. Purpose: PAL up/down counter pulse input for bidirectional position or count measurement.

• Pulse / Range: Enter a value between 1 and 3000 to indicate the number of pulses to be counted to set the output to 100% of the range. During counting the output will be equal Countervalue to: xRange=Output Pulse/Range • Range: Range limit for the output value. • Start Count: This field can be set to ‘UP’ to start the counter by the detection of up counting (internal bit, see above). If this field is set to ‘DOWN’ the counter will start counting by the detection of the status down counting (internal bit, see above). • Stop Count: This field can be set to ‘UP’ to stop the counter by the detection of up counting (internal bit, see above). If this field is set to ‘DOWN’ the counter will stop counting by the detection of the status by down counting (internal bit, see above). • Reset: This field can be set to ‘UP’ to reset the counter by the detection of up counting (internal bit, see above). If this field is set to ‘DOWN’ the counter will reset counting by the detection of the status by down counting (internal bit, see above).

> **[Vector Diagram — Page 208]** Page 208 presents the pulse input formula header, a cross-reference note, and the high-frequency note only for a specific pulse input channel sub-section.

Formula (section header):
Pulse Input Channel Value = Pulse Counter x (Conversion Range / Pulse/Conversion Range)

Cross-reference text: 'For all other entries of this screen refer to paragraph 0'
Indicates shared parameter documentation for this particular pulse input variant; most parameters are common with the standard setup.

Note (hand icon): 'Pulse input channels can be used for high frequency when configured on special input locations. For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz. For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to 2Khz, others 100Hz.'

No additional diagrams or tables present. This brief page is part of section 7.6.2 of the Engineering Guide, likely covering a specific pulse input sub-type (speed counter, up/down counter, or stored pulse variant) where most parameters are identical to the standard setup with only a few differences documented on adjacent pages.

For all other entries of this screen refer to paragraph 0

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

#### 7.6.2.15 Pulse Input as pulse counter Channel Setup

Pulse Input used as Pulse Counter A pulse input can be used for pulse counting (Sensor Type 2). In this case the hardware counter will count pulses starting at the moment that the Start Count input will change from ‘False’ to ‘True’. The counting will stop at the moment the Stop Count will change from ‘False’ to ‘True’. The counter will reset at the moment the Reset Count will change from ‘False’ to True’.

> **[Figure]** Screenshot of PAL Pulse Input - Pulse counter. Channel: 11103, Description: flow meter. Same configuration as p193_i2. Purpose: reference configuration copy for PAL pulse counter.

|  | Pulse / |  |  | Enter a value between 1 and 3000 to indicate the number of pulses to be counted |  |
| --- | --- | --- | --- | --- | --- | |
|  | Scan |  |  | to set the output to 100% of the range. |  |
|  | Range |  |  | Range limit for the output value. |  |
|  | Start |  |  | Transition from ‘False’ to ‘True’ on this channel will start the counting process. This |  |
|  | Count |  |  | channel must be a local channel on same I/O module |  |
|  | Stop |  |  | Transition from ‘False’ to ‘True’ on this channel will stop the counting process. This |  |
|  | Count |  |  | channel must be a local channel on same I/O Module |  |
| Reset Count | Reset |  |  | Transition from ‘False’ to ‘True’ on this channel will reset the counter. This channel |  |
|  | Count |  |  | must be a local channel on same I/O Module. If the reset is defined as the pulse |  |
|  |  |  |  | input channel itself, it will execute the reset command as soon as the output passes |  |
|  |  |  |  | the highest limit. |  |
| Direction |  |  |  | External Channel as direction input. The direction of pulse counting follows the |  |
|  |  |  |  | channel value. On this manner up/down functionality can be implemented. |  |
|  |  |  |  | Local channel on same IO Module as direction output. It can be used to read the |  |
|  |  |  |  | automatic detected direction. The direction is detected by the by IO Module |  |
|  |  |  |  | software. This software evaluates the phase shifting between paired channels. On |  |
|  |  |  |  | 24MIX these are inputs 2, 3 and 14, 15. On 36DI these are inputs 25, 26 and 33, 34. |  |

During counting the output will be equal to:

> **[Vector Diagram — Page 210]** Page 210 presents section headings 7.6.2.16, 7.6.2.17, 7.6.2.18 (with high-frequency note), and section 7.6.2.19 covering the Average Channel Setup for MEGA-GUARD IOM.

Formula header: Pulse Input Channel Value = Pulse Counter x (Conversion Range / Pulse/Conversion Range)

Section 7.6.2.16, 7.6.2.17: Section headings only (detailed content on adjacent pages).

Section 7.6.2.18 note (hand icon): 'Pulse input channels can be used for high frequency when configured on special input locations. For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz. For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to 2Khz, others 100Hz.' Reference: 'Standard Set-Up Pulse Input Channel, page 192.'

Section 7.6.2.19: Average Channel Setup. Type: Configuration parameter reference.
- The Limit Type is not configurable; the reset channel is automatically set to the bottom of the group; Highest Limit counter will be automatically set.
- Alarming: Select YES to generate an alarm when the counter deviates too much from the group average.
- Low Limit: Enter deviation value for Low Limit Alarm - if deviation below threshold, generate alarm.
- High Limit: Enter deviation value for High Limit Alarm - if deviation above threshold, generate alarm.

Average Channel is used in MEGA-GUARD IOM for monitoring temperature distributions across multiple cylinders (e.g., exhaust gas temperature averaging). The channel computes the mean of a group of input channels and alarms when any channel deviates excessively from the group average. Page 210 is from section 7.6.2.

7.6.2.16

7.6.2.17

7.6.2.18

|  |  | Pulse input channels can be used for high frequency when configured on special input |  |
| --- | --- | --- | --- | |
|  |  | locations. |  |
|  |  | For 24 Mixed IO Module; input 2, 3, 14, 15 -> Frequency up to 2Khz, others 100Hz |  |
|  |  | For 36 Digital Input Module; input 25, 26, 33, 34 -> Frequency up to up to 2Khz, others |  |
|  |  | 100Hz |  |

Standard Set-Up Pulse Input Channel, page 192.

Note: The Limit Type is not configurable and the reset channel is automatically set to the current channel (not configurable), if the counter reaches the 'Highest Limit' the counter will be reset and the counting continues.

#### 7.6.2.19 Average Channel Setup

To guard engine cylinder temperatures the average channel is available. An average channel is the average of multiple analog channels measuring the temperature of each cylinder. The average channel can give an alarm when one of the channels differs to much from the average.

Average channel setup dialog has the following fields: Alarming:

Select ‘YES’ to generate an alarm on any channel from the list, which deviates too • much from the average (average alarm). Select ‘NO’ for average value calculation only.

Low Limit:

• Enter the limit, in engineering units above which the average must be to evaluate average alarms.

Enter the deviation from the average, in engineering units, beyond which an average alarm is generated: Deviation (at Low Limit):

• Enter here the deviation at the ‘Low Limit’.

High Range:

• Enter a high range value if a non-linear deviation is desired.

Deviation at (High Range):

Enter here the deviation at the ‘High Range’. •

Note: For a linear deviation (you can enter ‘0’) both the High Range and corresponding Deviation fields are not shown unless the cursor is on these fields. In this case the High Range has no meaning and both Deviation fields hold the same value. Status Texts:

Select from 16 groups of texts shown in the window, to represent the channel’s • status. (Texts themselves can be modified from another item).

Groups: Each alarm can activate up to 8 Group Alarms. Which will activate an LED indicator on a Group Panel and it will activate the Horn Output of the corresponding Group Panel. In the system we have a maximum of 256 Groups: Table Enter the channel list:

**CHANNEL:**

• Enter the channels. Enter a blank field to remove a channel; enter ‘0’ to create a new field. When getting beyond the last displayed channel, all channels are scrolled one upwards (the ‘<<<’ sign shows more channels are present). When getting beyond the first displayed channel, all channels are scrolled one downwards (the ‘>>>’ sign shows more channels are present). An out of memory message is displayed when all channels are used.

**BIAS:**

Enter for each channel in the second field the bias, in engineering units, with which • the channel’s value is compensated before evaluating any average alarm.

An Average Channel can be setup from channel number 37 and higher. The low limit will inhibit alarming if the average temperature is lower than the low limit. The deviation at low limit will care that an alarm is set when the difference of between the different channels is higher than the deviation at low limit. With "High range" a different deviation can be used when the average is at this high range. The deviation between the "low limit" and "high range" is calculated. Example:

• Eng Unit = DegC Low Limit = 0 Deviation at Low Limit = 30 High Range = 500 Deviation at High Range = 20

Now if the average temperature is 250 degrees, the deviation may be 250 / (500-0) = 0.5 (temperature is 50% of High range-Low limit) 20 - 30 = 10 (deviation difference is 10) 10 * 0.5 = 5 (50% of 10 is 5) 20 + 5 = 25 (deviation at 250 DegC is 25 DegC) The BIAS factor is added to the channel value before it is used in average calculation. A negative BIAS factor can be used to subtract values.

#### 7.6.2.20 Digital Output Channel Setup

A digital output channel (relay) can be driven by one of several selectable conditions. When a digital output channel is selected the following appears on the screen, for

> **[Figure]** Screenshot of PAL channel configuration - Digital Output (Multiple Channel). Channel: 10813, Description: MAIN BEARING SAFETY STOP. Type: Digital Output, Source: Multiple Channel. Actual Type: Limit. Lamp Test: Yes. Norm. Status: De-energized. Multiple channel table: 10801 Dig/Both, 10802 Dig/Both, 10803 Very Low, 10804 Low, 10805 High, 10806 Very High. Purpose: PAL digital output for a safety stop system combining multiple alarm inputs, with limit-type activation based on channel 10801-10806 states.

7.6.2.20.1 Standard Set-up Digital Output Channel

• Tag Name: Enter any tag up to 10 characters. Tags must be unique. • Description: Enter any descriptive text up to 40 characters. • Type: Shows ‘Digital Output' as information only. • Source: • Select ‘Not Installed’ to remove this channel from setup. • Select ‘Multiple Channel' to activate the output on the status of one or more channel(s). Maximal 125 channels can be setup in a multiple channel. • Select ‘Mimic’, to activate this output from a Mimic. • Select ‘Mimic Pulse’, if the value is to be set from a Mimic and to be used once (requires IEC – 1131). • Select 'Remote Data' (e.g. MODBUS) to activate this output via a protocol. • Select ‘IEC – 1131’, to activate this output via IEC – 1131. • Norm. Status: • Select ‘De-energized' for a, default Normally Open, contact on the output. • Select ‘Energized’ for a, default Normally Closed, contact on the output. • Print Status: The following selections are possible for status information: • With Report Option 'OFF', you can select: • No posting of status message lines on the printer for this channel. • With Report Option 'ACTIVE ONLY', you can select:

• Posting a status message line on the printer each time a status change from 'OFF' to 'ON' is detected for this channel. • With Report Option 'BOTH', you can select: • Posting a status message line on the printer each time a status change is detected for this channel. • NO-ACK Pulse: • Select ‘Yes’ if the output has to pulsate when the ‘Act. Cond.’ becomes true. In this case the output reverts to a continuous signal when the condition is acknowledged. • Select ‘No’ for continuous signal anyway. • Status Texts: Select from 16 groups of texts shown in the window, to represent the channel’s status. (Texts themselves can be modified from another menu (page 221). • Area Groups: Each channel can be included in up to 8 Area Groups. Area Groups can be used as 'GROUP PAGE' for display (Max 128 'GROUP PAGES') and/or it can be configured to activate (an) LED indicator(s) on a Bridge Group Panel, Mess room Panel or Cabin Panel and it will activate the Horn Output of the corresponding Panel. In the system we have a maximum of 256 Area Groups:

7.6.2.20.2 Digital output activated on Multiple Channel Status

A number of channels can be allocated to one output. A channel can be a digital or analog input or a digital output. The output is made active when any channel gets the ‘ALARM’ or ‘ON’ status. • Activation Type: • For repetitive average alarm: select ‘Average’. The output reverts to default when no channel has an average alarm. • For repetitive limit alarm: select ‘Limit’. The output reverts to default when no channel has the ‘ALARM’ or ‘ON’ status. • For repetitive not acknowledged limit alarm: select ‘Limit/ACK’. The output reverts to default when no channel has on not acknowledged ‘ALARM’ or ‘ON’ status. • For UMS average + limit + sensfail alarm: select ‘UMS’. The output reverts to default when all channels are acknowledged. • For repetitive average alarm including sensfail: select ‘Average + Sensor Failed'. The output reverts to default when no channel has an average alarm or sensor failure. • For repetitive limit alarm including sensfail: select ‘Limit + Sensor Failed'. The output reverts to default when no channel has the ‘ALARM’ or ‘ON’ status or sensor failure. • For repetitive not acknowledged limit alarm including sensor failure: select ‘Limit + Sensor Failed/ACK’. The output reverts to default when no channel has a not acknowledged sensor failure, ‘ALARM’ or ‘ON’ status.

• Pulse on next: • Select ‘Yes’ when the output is to revert to default for a 2 sec. pulse, when a 2nd or any further channel gets the ‘ALARM’ or ‘ON’ status (not available for average). •

## CHANNEL LIMIT:

• Enter the channels (see paragraph 4.2.1 Channel Numbering, page 35). Select the row by clicking on the row number and press delete to remove a channel; press 'ALT Insert' to create a new field in the table. Maximal 125 channels can be setup in a multiple channel. • For analog input / pulse channels select in the second field the active condition: • Dig/Both: Both limits (i.e. LOW + HIGH or HIGH + VERY HIGH, according to channel set-up). • Very Low: Very low limit (this and next should correspond to channel set-up). • Low: Low limit • High: High limit • Very High: Very high limit • For digital channels the second field should always be Dig/Both (= digital).

For all other entries of this screen refer to paragraph 7.6.2.20.1 Standard Set-up Digital Output Channel, page 212.

#### 7.6.2.21 Analog Output Channel Setup

Analog input channels can be redirected to analog output channels. When an analog output channel is selected the following appears on the screen, for example:

> **[Figure]** Screenshot of PAL channel configuration - Analog Output (Other Channel source). Channel: 20008, Description: Analog Output Channel Description. 1131 Name: C008-(FINT). Type: Analog Output, Source: Other Channel. From Channel: 20007. Output: 0-20mA. Eng Unit Low: 0.0, Eng Unit High: 100.0. Displ. Deviat: 0.1, Nr Dec.: 1. Display Output: Normal, Fail Safe Value: 0.0 (checked). Purpose: PAL analog output channel outputting 0-20mA derived from channel 20007 with fail-safe value 0.0.

7.6.2.21.1 Analog Output Standard Setup

• Tag Name: Enter any tag up to 10 characters. Tags must be unique. • Description: Enter any descriptive text up to 40 characters. • Type: Select ‘Analog Output'. • Input Type: • Select 'Other Channel', to use this channel driven by another channel • Select ‘Remote Data', to use this channel to be driven by a protocol (e.g. MODBUS) • Select ‘Mimic’, to use this channel to be driven by a Mimic. • Select ‘IEC – 1131’, to use this channel to be driven by IEC – 1131. • Select 'Not Installed' to remove this channel from set-up. • Output: Select ‘0-20’ or ‘4-20’ mA. • Displ. Deviat: Minimal deviation of the value from the last update, to exceed before the value is updated (on the screen) again. • Nr Of Dec: Enter the number of decimals and this will be used for display. When this item is changed the display deviation will change automatically also. • Eng Unit Low: Enter the low end of the output range (0/4 mA). • Eng Unit High: Enter the high end of the output range (20 mA). • Eng Unit Type: Enter up to 4 characters to represent the unit type of the range. • Area Groups: Each channel can be included in up to 8 Area Groups. Area Groups can be used as 'GROUP PAGE' for display (Max 128 'GROUP PAGES') and/or it can be configured

to activate (an) LED indicator(s) on a Bridge Group Panel, Mess room Panel or Cabin Panel and it will activate the Horn Output of the corresponding Panel. In the system we have a maximum of 256 Area Groups:

7.6.2.21.2 Analog Output Channel driven by another channel The following screen view gives you an example to use this channel to be driven by the output of another channel:

> **[Figure]** Screenshot of PAL channel configuration - Analog Output (identical to p215_i2). Channel: 20008, same Analog Output, Other Channel source, 0-20mA, From Channel 20007. Purpose: duplicate reference for PAL analog output channel configuration.

• Input Type: Select 'Other Channel’. • From Chan: Enter the channel number from the channel that will drive this analog output.

For all other entries of this screen refer to paragraph 7.6.2.21.1 Analog Output Standard Setup, page 215.

#### 7.6.2.22 Virtual Channels Setup

Virtual channels have the same functionality as real (hardware based) channels, but lack any physical I/O. They can be used for calculated input values, intermediate output results, alarming and logging purposes. The Sensor field determines where the data is coming from.

When a virtual channel is selected the following appears on the screen, for example:

> **[Figure]** Screenshot of PAL channel configuration - Analog Input with formula and 'Other Channel' source. Channel: 20007, Description: Analog Input Channel Description. Type: Analog Input, Source: Other Channel. From Channel: 20008. Eng Unit Low: 0.0, Eng Unit High: 100.0. Use Formula: Y=1.000*X+0.000. Limit Type: L/H, Lowest 0.0, Highest 100.0. Report: Alarm, Nr Dec.: 1. Retain Value: 0.0, Default Value: 0.0. Purpose: PAL analog input using formula Y=aX+b and referencing channel 20008 as source.

• Type: Select ‘Digital Input’, ’Analog Input’, ‘Digital Output' or ’Analog Output'.

For the setup of a virtual channel refer to setup of the relevant channel type of physical I/O channels.

7.6.2.22.1 Virtual Channels to be driven from a MODBUS Slave Device

It is possible to setup for a (virtual) channel to be driven by a MODBUS Slave Device.

7.6.2.22.2 Virtual Channels to be driven from a NMEA / ATC-T Device

It is possible to setup for a (virtual) channel to be driven by a NMEA / ATC-T Device.

7.6.2.22.3 Virtual Channels to be driven from an External Caterpillar Device

It is possible to setup a virtual channel driven by an External Caterpillar Device.

### 7.6.3 Conversion Tables

#### 7.6.3.1 Conversion Table setup

Expanding the tree area on the specific board will give you for example the following image:

For each board you can setup channels (hardware or virtual), conversion tables, function block implementations, parameter layout and eventual parameters for stored pulse counters.

#### 7.6.3.2 Adding and Deleting Conversion Tables

• Adding a conversion table: • Select in the related Field I/O Plugin folder, the I/O Board folder and than the Conversion Table folder in the tree and click it with the right pointing device key or press the context menu key on the keyboard. Select 'Insert' from the context menu and the following menu will appear:

• Name: • Enter the user definable field to describe the username for this table. This field is used for documentary reason only. This user name will be used in the tree area.

• Deleting a table: • Select the specific table in the tree area that should be deleted and press the delete key on the keyboard.

#### 7.6.3.3 Conversion Table Setup

User defined linearization tables (e.g. tank table) can be set-up for analog input channel conversion. Up to 16 tables can be setup for each I/O board. Select the desired Conversion Table from the Tree area or create a new table on an I/O board. The following screen will appear:

> **[Figure]** Screenshot showing PAL conversion table (Tank Table 1023). Name: Tank Table 1023. 'Use Engineering Unit for X-Values' checkbox. X-Y data table with 15 data points from (0.0, 12.5) to (1000.0, 550.0), representing tank level (%) vs volume. Graph on right shows a curved (non-linear) interpolation line plotted through the data points. Y-Value low: 12.5, Y-Value high: 545.4. Purpose: PAL tank calibration table showing non-linear volume-to-level conversion with graphical preview.

• Name: Enter the name of the table. This name will be used as indication in references to this table and in the Tree Area. • Using Engineering Unit for X-Values: If checkbox is checked, two additional fields will appear to setup the X-Value low and the X-Value high in engineering units. These values are used to 'clip' the input if desired. • X & Y Table: In the 'X' column enter values between 0 and 1000.0 per mille; they span the range of the input sensor. You must start from 0.0 (fixed!) and conclude with 1000.0 (for the 16th -last possible- entry fixed!). In the 'Y' column enter the corresponding value in engineering units. All values within one table must be either pro- or regressive. In this example half sensor scale evaluates to 250 and e.g. 98% sensor scale to 540 (m ). 3

Note: The graphic area gives a preview of the defined curve. And is just for indication.

### 7.6.4 Status Text

Up to 16 groups of status texts can be defined for four types of channels each. A status appears as the last field on e.g. Alarm Page and Demand Print. These descriptions can be changed depending on the channel type. E.g.: ‘NORMAL-ALARM!’, ‘OFF-ON’, ‘AUS-EIN’, ‘ARRET- MARCHE’, ‘FERMA-IN MAR’. For each supported channel a selection can be made from the appropriate 16 user definable possibilities. To setup the status text, open the corresponding folder in the Tree Area: Be aware that Status Texts are part of XP separated parts. Status Texts under tree-item System Parameters (5.10) are only used for diagnostic channels.

> **[Figure]** Screenshot of PAL Digital Alarm Channels status table. Title: 'Digital Alarm Channels - status'. Columns: Nr, Default, Active (colored squares), Wire Fail (colored squares). 16 rows showing combinations of status texts: Normal, Laag, Hoog, Storing, Overbelast, Gestopt, Aardfout, Alarm! for Active column and SensFail (red) for Wire Fail. Purpose: PAL board diagnostic showing status text colors for digital alarm channels across all 16 inputs.

#### 7.6.4.1 Digital Input Alarm Channels Status Description

The colors and text strings of row Nr 1 is fixed. For row 2 - 16 text of normal (Default) and alarm (Active) status and of wire failure status can be changed. Colors can be modified, but advisable is that the default colors will be used. Any not acknowledged status appears in flashing red.

#### 7.6.4.2 Digital Input / Output Status Channels Status Description

Text strings and color(s) of off (Default) and on (Active) status can be changed. Text of wire failure can be changed. For row 1 the text strings and colors are fixed as shown. Any not acknowledged wire failure status appears in flashing red. For the wire failure status the color can be modified, but advisable is that the default color will be used. (N.B.: wire failure applies to digital input channels only.)

> **[Figure]** Screenshot of PAL Digital Status Channels status table. Title: 'Digital Status Channels - status'. Columns: Nr, Default, Active (colored squares), Wire Fail (colored squares). 16 rows showing: Off, On (green), and combinations of Geopend, Gesloten, Start, Stop, Bedr gereed, In bedrijf, Gereed, Actief, Aan statuses. Wire Fail: all SensFail (red). Purpose: PAL board diagnostic showing status text configurations for digital status (non-alarm) channels.

#### 7.6.4.3 Analog and Pulse Input Alarm Channels Status Description

Row Nr 1 is fixed. For row 2 - 16 text of normal (Default), lower (Low) and higher (High) status and for sensor failure status can be changed. Colors can be modified, but advisable is that the default colors will be used. Any not acknowledged status appears in flashing red.

> **[Figure]** Screenshot of PAL Analog Status Channels status table. Title: 'Analog Status Channels - status'. Columns: Nr, Default, Low Status (colored), High Status (colored), Sensor Fail (colored). 16 rows. Row 1: Off, On (yellow), On (green), SensFail (red). Rows 2-16: Off, On (yellow/green), On (green), SensFail (red). Purpose: PAL board diagnostic showing analog status (non-alarm) channel status text configurations.

#### 7.6.4.4 Analog and Pulse Input Status Channels Status Description

Text and color of normal (Default), lower (Low) and higher (High) status can be changed. Text for sensor failure can be changed. For the sensor failure status the color can be modified, but advisable is that the default color will be used. Any not acknowledged sensor failure appears in flashing red.

> **[Figure]** Screenshot of PAL Analog Alarm Channels status table. Title: 'Analog Alarm Channels - status'. Columns: Nr, Default, Low Status (colored), High Status (colored), Sensor Fail (colored). 16 rows. Row 1: Normal, Alarm! (yellow), Alarm! (yellow), SensFail (red). Row 2: Normal, Laag. Row 3: Normal, Hoog. Other rows: Normal with various Alarm! status colors and SensFail (red). Purpose: PAL board diagnostic showing analog alarm channel status text configurations for low/high limit and sensor fail states.

> **[Vector Diagram — Page 224]** Page 224 documents MEGA-GUARD OWS section 7.7 ('Diagnostics') including System Diagnostics tree navigation and the 'Copy Channel Range' bulk setup feature.

Diagram 1: iObserver Diagnostics Tree View. Type: Software UI screenshot. Shows the OWS iObserver diagnostics panel tree structure:
  Channels
    XP: [XP_node]
      IO: [IO_Module] (S026-CA)
        Channels
          XP_S1(CH-1)
The tree shows the XP processor -> IOM -> Channels hierarchy for diagnostics navigation.

Diagram 2: Diagnostics Dialog with I/O Module Input Fields. Type: Software UI screenshot. Shows channel diagnostics detail area with: 'High Input' text input field, 'Source' dropdown showing current channel source configuration, channel number, current value, status display.

System Diagnostics Navigation (section 7.7.1):
- Location in OWS: Processor Position Table, # Advanced Features
- Note (information icon): 'With Copy or Move Channel Range is possible to setup a lot diagnostics very fast. Open Copy Channel Range dialog: fill in to range 00000 to 00030, Press OK. Now copy is made from channel 00001 to 00030 (last parameter changes automatically).'

Section 7.7.2: I/O Module Diagnostics.
'Location of the I/O module diagnostics is in the tree area under Processor Position table, # Advanced Features.'

Page 224 is from section 7.7. The diagnostics section allows MEGA-GUARD engineers to inspect real-time channel values, I/O module status, and XP processor health through OWS iObserver. The 'Copy Channel Range' feature enables efficient bulk diagnostic channel setup.

## 7.7 Diagnostics

For signaling system statuses diagnostics are there. Diagnostics can be placed at its XP or at the system parameters.

### 7.7.1 System Diagnostics

At middle of the screen, you will find:

By selection of category and it’s message, it needed to setup a diagnostic. Sometimes is it necessary to fill in extra details, like XP number or remote data number. After selection is made automatically changes is made inside the description field.

|  | [INFO] With ‘Copy or Move Channel Range’ is possible to setup a lot diagnostics very fast. |  |
| --- | --- | --- | |
|  | Open ‘Copy Channel Range’ dialog, fill in From 00001, To 00002 / 00030. Press Ok. |  |
|  | Now copy is made from channel 00001 to a range of 00002 to 00030 where last |  |
|  | parameter (like board number) is increased every time |  |

For extensive description of other items on this form refer to paragraph 7.6.2.5.1 Standard Set- up Digital Input Channel, page 176.

### 7.7.2 I/O Module diagnostics

Location of the “I/O Module diagnostics” is in the tree area under “Processor Position table”, # “Advanced Features”. See the following image of the tree area:

By selecting one of the XP the setup area will show diagnostics of equipment that can be connected to local processor:

This function is for setting up specific diagnostics in case special functionality is running on that processor. The special functionality can be anything from a protocol to the usage of Analog Input module which has earth failure diagnostics.

#### 7.7.2.1 Earth fault detection

Earth fault detection can be switched on by selecting it from the diagnostic list with a configured virtual channel. The channel that is used to store the diagnostic must be setup as a virtual remote data channel on one of the boards in the control processor.

> **[Figure]** Screenshot of the MEGA-GUARD PAL configuration tool, Board Diagnostics tab for an XP01 processor. Tab row: General Settings | Miscellaneous Table | Board Diagnostics (active) | Channel Cross Reference List | 1131 Reference List. Table with columns Nr, Channel Nr, Diagnostic: Row 1: 1, 01100, XP01-Board 1 Not Present; Row 2: 2, 01199, XP01-Board 1 Earth Fault (dropdown visible); Rows 3 and 4 empty. Purpose: configuration of diagnostic channel assignments for XP01 I/O board presence and earth fault detection in the MEGA-GUARD system.

## 7.8 Menu interface

The LCD Panel can be configured to hold menu’s to change values of settings.

## 7.9 Master clock interface

### 7.9.1 Master clock hardware connection and protocol

In the below figure is shown how to connect master clock to XP:

> **[Figure]** Installation/wiring diagram for a Serial Link Isolator module connected to a Master Clock with NMEA 0183 output. Three views: TOP VIEW (15p SUB-D connector), FRONT VIEW (detachable screw terminal strip labeled: SYSTEM ON, RS485, NMEA 0183, Baud 4800, RX ACTIVITY, MASTER CLOCK), BOTTOM VIEW (15p SUB-D female). MASTER CLOCK CUSTOMER CONNECTIONS showing Xn connector with TX-/TX+ wires to RX-/RX+ via 2x0.75sqmm shielded cable. Communication Link: PROTOCOL NMEA 0183 (TALKER), BAUDRATE 4800, DATA BIT 8, PARITY NONE, STOPBIT 1. SERIAL LINK ISOLATOR CONNECTIONS with DIP-SWITCH settings SW1-SW5 for BAUDRATE (1200-4800-9600-19200), TRANSMIT (AUTO/ALWAYS ON), and 120 Ohm termination. Purpose: wiring and DIP-switch configuration diagram for connecting a Master Clock NMEA 0183 output to MEGA-GUARD via a Serial Link Isolator.

On the right of this figure is show how the signal protocol specified.

### 7.9.2 Master clock configuration

The system supports updating of the Marine PC Local Time zones (LTZ), system clock will not be changed. The Master clock interface must be connected to the pulse inputs of a control processor (6049, via 91.6.040.500). These pulse inputs should be configured on channels 65 and 66 on the first board (LBB65 and LBB66) of the control processor in question. Both channels should be setup as follows:

> **[Figure]** Screenshot of PAL 6.0.0.11 system with FB3 plugin configuration. Left tree: Plugins > FB3-FB3(IO) > Processor Position Table > 01-Advanced Features > Additional Settings (selected). Right panel: Special Board Setup: Parameter Numbering 'Per Processor'. Use Order Printer (unchecked), ComPort 2. Use Master Clock Update (checked). Remote Data section. Purpose: PAL FB3 fieldbus plugin additional settings configuration for processor-level parameter numbering and master clock update.

In this example the first processor on Link 3 is configured to load the first board. The following switch should be checked to turn on master clock updating to windows system clock:

> **[Figure]** Screenshot of PAL channel configuration - Digital Input for Master Clock CCW. Channel: 30166, Description: MASTER CLOCK CCW. Type: Digital Input, Source: Hardware Input. Fail Detect: None, Norm. Cond.: Closed. Report: Status. Print Status: Off. Alarm Delay: 0 sec. Status Texts: Off (yellow), On (yellow), SensFail (red). Purpose: PAL digital input channel configuration for Master Clock counter-clockwise pulse signal.

To switch off the master clock interface the box must be unchecked, and the processor (XP) must be reset (switched off and on).

To get a diagnostic if the master clock interface is not functional any diagnostic channel can be setup as follows:

After download of this setup the Windows time zone will be updated according master clock.

### 7.9.3 Master clock pulse rate and error conditions

> **[Figure]** Screenshot of PAL channel configuration - Digital Input Diagnostic channel. Channel: 00001, Description: FB3 Proc1 Master Clock Not Running. Type: Digital Input, Source: Diagnostic. Norm. Cond.: Open. Category: CanBus. Dropdown: FB(%FB4) Proc(%UP24) Master Clock Not Running. FieldBus: 3, Processor: 1. Report: Status. Print Status: Off. Alarm Delay: 0 sec. Status Texts: Off (yellow), On (yellow), SensFail (red). Purpose: PAL diagnostic digital input channel monitoring Master Clock running status on the CAN bus fieldbus.

The first input is the pulse counting input. For changing time zone the interval time between 2 pulses is 0.5 second. The second input commands to move time zone forward or backward. See below table for examples:

| Pulses with 0.5 second interval | Action |
| --- | --- | |
| Less then 1 pulse per 45 seconds | Diagnostic alarm as configured above |
| 1 - 59 pulse (forward) | No action |
| 60 – 119 pulse (forward) | Time zone + 30 minutes |
| 120 – 179 pulse (forward) | Time zone + 1 hour |
| 180 – 239 pulse (forward) | Time zone + 1 hour and 30 minutes |
| 240 – 299 pulse (forward) | Time zone + 2 hour |
| Etcetera, and similar for setting time zone backward: |  |
| 116 – 120 pulse (backward) | Time zone - 1 hour |

Note: The system waits for 3 seconds after last pulse before updating time zone.

## 7.10 Special Functions

### 7.10.1 Show Changes

After selecting ‘Special’ and ‘Show Changes’

Inside text file is stored what all channel changes are. So it will always be possible to track down what has changed and when that was done.

### 7.10.2 Check Database

After selecting ‘Special’ and ‘Check Database’

A text file is generated where configuration errors are displayed. This list is built per PAL session. Press F5 for re-check database, be sure that caret (focus) is blinking inside the text form.

Example:

************No existing conversion tables are used with************ Channels - Conversion Tables List: 20239(1), Comments: if you go channel 20239, and see that Convert Table = %Table1, what means there is no table1

************No existing function implementations are used with************ Channels Function Output - Function List : 20319(-0), Comments: if you go channel 20319, and see that source is function output, but there is no function output chosen

************No existing elements are used with Clustering************ Boards List: 106(1-8), Comments: if you go cluster 01, and look at table line 8, there is board configured which is not exists.

### 7.10.3 Print Labels

After selecting ‘Special’ and Print Labels

Three types of output are possible, by pressing one of these buttons: 1. Print Labels – Boards 2. Print Labels – Processors 3. Print Labels – PMS Boards

Insert at range how many boards needed to be printed.

Check Boxes: - Processor Number (output 2), use processor number instead first board number - Skip not installed channels (output 1 + output 3), empty not installed channels - Tag name (output 1+output 3) use tag name, will be placed before description

Text fields will be placed on the output. These texts could be changed, but changes will not be stored and only be used on direct output.

### 7.10.4 Calc Processor Load

After selecting ‘Special’ and Calc Processor Load

A text file is generated where all items who are responsible for an extra bus load (=data traffic between processors (among themselves)). It is recommended keeping this bus load as low possible.

Example output file: Result of Calculation of Processor Load

---------------Estimate Load of Fieldbus --------------- Number of Channels As Inhibitor / Other Channel / Cold Junction 10 Number of Channels As Function Input / Output or Fail Detect Function 50 Number of Channels in Multiple Channel / Average 10 Number of Parameters As Channel / Conversion Table / Parameter 100 Number of Function Implementations Inputs As Channel 30 Number of Function Implementations Inputs As Function Implementations 0

### 7.10.5 Split/Merge Database

After selecting ‘Special’ and Split/Merge Database

Be sure that in same path as Config.mdb the following file(s) exists: • EmptyConfig2000.mdb • EmptyConfig97.mdb These files are coming with every release of PAL.

By pressing on ‘Split Main File into 4 New Files’, database is split into four new files. These are name config01.mdb, config02.mdb, config03.mdb and config04.mdb.

This functionality is be used at configuration level where more one person are configuring at the same setup.

Do not use this function when complete system (running IOServer) is on-line.

### 7.10.6 Channel Cross Reference List

> **[Figure]** Screenshot of MEGA-GUARD PAL Special menu tree showing Document Database section. Left tree panel showing: Special > Show Changes, Check Database, Print Labels, Calc Processor Load, Split/Merge Database, Channel Cross Reference List; Document Database (expanded) > Group Parameters > 001-Testing BMS (highlighted). Purpose: MEGA-GUARD PAL Special menu showing the Document Database feature with Group Parameters for BMS (Ballast Management System) testing documentation.

After selecting ‘Special’ and Channel Cross Reference List

> **[Figure]** Screenshot of PAL 'Channel Cross Reference List' header text configuration. Fields: Title: Channel Cross Reference List, I/O Processor: I/O Processor, Local Channel: Local Channel, Type: Type, Global Variable: Global Variable, System Channel: System Channel, From Other Channel: From Other Channel. Board Range: 101 to 101. Print button. Purpose: configuration dialog for customizing column headers of the Channel Cross Reference List report.

Insert a board range of what an output is wanted. By pressing on ‘Print’ button a list is generated where ‘Other Channel’ is used in that given board range. This feature is normally used for configuring IEC-1131.

### 7.10.7 Document Database

After selecting ‘Special’ and Document Database

Insert several items for document database. Only available if the file ‘doc.mdb’ is same path as config.mdb. This form shows project related information such as, project number, vessel, owner, yard and built number.

Create Default Layout creates default sensor information, if you go to the fast channel setup, see last columns.

## 7.11 System Parameters

### 7.11.1 General Settings

To enable the Stores Pulse Counter you have to select the System Parameter Setup\ General Settings in the Tree Area:

The following setup window will be shown:

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing the Objects in library panel for a custom library. Two-column table: Object name / Object type. Entries: FB_AVERAGE (function block, checked), FB_PULSE (function block, checked). Toggle all and Interface buttons on right. Buttons for function block (fco icon) and program (0101 icon). Purpose: showing the My_blocks library contents in PAL1131 export/import dialog with FB_AVERAGE and FB_PULSE function blocks available.

General: • Select ‘Yes’ for automatic acknowledge of channels (for testing purpose only) • Check for Redundant I/O Server (for single server should be "off") and (for main and backup server should be "on")

Server redundancy settings: • Server switch hold time: After a switch between from main to backup or vice versa the server will not switch for this period. For example, if on the main link of processor 1 fails, the system will switch to backup. It switches only to the backup when the backup has a less number

of link errors. After the switch stay on backup for at least 20 seconds, even if in the meantime the backup has more failures then the main.

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration showing Cluster 01 setup. Number: 01 (greyed). Description: Cluster 01. Table with columns Nr, Function, Link Nr, Nr: Row 1: 1, LOP, 4, 1; Row 2: 2, LOP, 4, 2; Row 3: 3, Board, 1, 1; Row 4: 4, Board, 1, 2; Row 5: 5, Board, 1, 3; Row 6: 6, Board, 1, 4; Row 7: 7, Board, 1, 5; Row 8: 8, Board, 1, 6. Purpose: configuring a MEGA-GUARD I/O cluster (Cluster 01) showing two LOP (Local Operator Panel) units on link 4 and six I/O boards on link 1.

• Server switch delay time: Delay time before a server performs a switch from active link to standby link. For example: If more boards are available on standby link the server waits 2 seconds and tests again if more boards are on the standby link. If this is the case, it switches.

• Server switch idle time: Time that server remains active after switching standby server on. Or the server waits this time before it sets itself to standby. This is done for giving other side some time to become active. On this manner the Channel data will be taken over more fluently.

### 7.11.2 Diagnostics General Texts

It’s possible to change diagnostic default texts, only for Alt. Language.

### 7.11.3 Clustering

To make groups (=clusters) with LOPs/LEDs panel and/or boards which to define when horn output should be stopped in case of accept pressed.

### 7.11.4 Display Conversion

Sometimes is preferred to display another engineering unit. Example is like: A thermal couple is delivering its value into °C but on display is °F required. In that case display conversion functionality can be helpful.

Unit1 original measure value in engineering unit 1 Unit2 display value in engineering unit 2 Formula re-calculation formula

Display Alternate Engineering Unit If turned on, it is possible to use display conversion* Test Formula a button to test the new inserted formula, it will be tested with three values: -100, 0 and 100

*by going to a channel Analog Input/Analog Output or Pulse Input a new field is shown ‘Unit Conversion’. Herewith is it possible to setup for that channel another engineering unit for display.

> **[Figure]** Screenshot of PAL 'Unit Conversion' table. Title: 'Display Alternate Engineering Unit'. Table with 8 rows showing unit conversions: M to Feet (3.281*Unit1), Bar to PSI (14.504*Unit1), DegC to DegF ((9/5)*Unit1+32), M3 to BLS (6.29*Unit1), M3 to Gal (264.172*Unit1), M3 to Ft3 (35.315*Unit1), MH2O to FH2O (3.281*Unit1), DegF to DegC ((Unit1-32)*(5/9)). Purpose: PAL engineering unit conversion table defining formulas for converting between metric and imperial units.

### 7.11.5 Engineering Units

By clicking on ‘Update From Channel Database’ all different engineering unit types are displayed.

Example: If you go analog input channel, dropdown list with all already used engineering unit types is shown.

Change Engineering Units can be found at the Special menu. An example:

After this action is everywhere in channel setup where ‘degC’ is used, will be changed into ‘DegC’.

### 7.11.6 Horns

Use EAS (cabin/mess) Groups which are setup at cabin or mess panel and also setup at here, If on one place (cabin setup or horn setup) a group like that is removed, it’s automatically removed from the other place too, (if checkbox is checked) Add/Sort/Delete Buttons to insert/delete groups which needed to be signaled horn outputs

## 7.12 Hour counters

Hour counter has the following fields:

Channel • the channel number, can’t be changed TagName • Enter any tag up to 10 characters. Tags must be unique. Description • Enter any descriptive text up to 40 characters Alt. Description • Enter any descriptive text up to 40 characters for support a secondary language, if you like to use a another language you should fill in here your description, especially when your language is not based on Roman alphabet, so when using Chinese, Korean or Japanese Texts, please use this field Type • Type of the channel, Analog Input (fixed) Source: Choose a selection from the combo box to set-up this channel (see below), • Not Installed • Counter Choose ‘Not Installed’ to set this channel as 'Not Used', the value of this channel is undefined. Report:

## • EMERGENCY

▪ General emergency alarm. An alarm given in the case of an emergency to all persons on board summoning passengers and crew to assembly stations. ▪ Fire alarm. An alarm to summon the crew in the case of fire. ▪ Water ingress detection main alarm. An alarm given when the water level reaches the main alarm level in cargo holds or other spaces on bulk carriers or single hold cargo ships. ▪ Those alerts giving warning of immediate personnel hazard, including: o Fire-extinguishing pre-discharge alarm. An alarm warning of the imminent release of fire- extinguishing medium into a space. o Power-operated sliding watertight door closing alarm. An alarm required by SOLAS regulation II-1/15.7.1.6, warning of the closing of a power-operated sliding watertight door.

• For special ships (e.g., high-speed craft), additional alarms may be classified as emergency alarms in addition to the ones defined above.

## • ALARM

If the Report Option ''ALARM' is selected the system will post an alarm message line on the printer and the 'ALARM PAGE' and it will activate the HORN output. The return to normal condition will change the alarm status text on the alarm message line on the 'ALARM PAGE' and it will post an alarm message line to the printer with the actual channel information. Machinery alarm. An alarm which indicates a malfunction or other abnormal condition of the machinery and electrical installations. Steering gear alarm. An alarm which indicates a malfunction or other abnormal condition of the steering gear system, e.g., overload alarm, phase failure alarm, no-voltage alarm and hydraulic oil tank low-level alarm. Control system fault alarm. An alarm which indicates a failure of an automatic or remote control system, e.g., the navigation bridge propulsion control failure alarm. Bilge alarm. An alarm which indicates an abnormally high level of bilge water. Water ingress detection pre-alarm. An alarm given when the water level reaches a lower level in cargo holds or other spaces on bulk carriers or single hold cargo ships. Engineers’ alarm. An alarm to be operated from the engine control room or at the maneuvering platform, as appropriate, to alert personnel in the engineers’ accommodation that assistance is needed in the engine- room. Personnel alarm. An alarm to confirm the safety of the engineer on duty when alone in the machinery spaces. Bridge Navigational Watch Alarm System (BNWAS). Second and third stage remote audible alarm as required by resolution MSC.128(75). Fire detection alarm. An alarm to alert the crew in the onboard safety centre, the continuously manned central control station, the navigation bridge or main fire control station or elsewhere that a fire has been detected. Fixed local application fire-extinguishing system activation alarm. An alarm to alert the crew that the system has been discharged, with indication of the section activated. Alarms indicating faults in alert management or detection systems or loss of their power supplies. Cargo alarm. An alarm which indicates abnormal conditions originating in cargo, or in systems for the preservation or safety of cargo. Gas detection alarm. An alarm which indicates that gas has been detected. Power-operated watertight door fault alarms. Alarms which indicate low level in hydraulic fluid reservoirs, low gas pressure or loss of stored

energy in hydraulic accumulators, and loss of electrical power supply for power-operated sliding watertight doors. Navigation-related alarms as specified in the Revised Performance Standards for Integrated Navigation Systems (INS) (resolution MSC.252(83), appendix 5). For special ships (e.g., high-speed craft), additional alerts may be classified as alarms in addition to the ones defined above.

### 7.12.1 WARNING

Refer to chapter 10 Alert and Indicator Locations of IMO Resolution A.1021(26); Adopted on 2 December 2009.

### 7.12.2 CAUTION

Refer to chapter 10 Alert and Indicator Locations of IMO Resolution A.1021(26); Adopted on 2 December 2009.

## • STATUS

The Report Option 'STATUS ' signifies that the signal is not activating an alarm message on the 'ALARM PAGE' and is not activating the HORN output. But it will activate the posting of a status message line on the printer if the input changes (The Print Status option is set to 'Both'). Note: If the Sensor Failure is used and the Sensor Failure is activated, it will create an alarm message on the 'ALARM PAGE' and it will post an alarm message line on the printer. Groups: Each alarm can activate up to 8 Group Alarms. Which will activate an LED indicator on a Group Panel and it will activate the Horn Output of the corresponding Group Panel. In the system we have a maximum of 256 Groups: Print Status: The Print Status option is only visible (and can be set-up) on certain Report options. With Report Options: 'ALARM' and 'ALARM NO HORN' the Print Status option is not visible. Note: In that case alarm message lines are always sent to the printer. The following selections are possible for status information: • With Report Option 'STATUS', you can select: • Select 'TO ACTIVE ONLY’ for posting a status message line on the printer each time a status change from 'OFF' to 'ON' is detected for this channel. • Select 'BOTH’ for posting a status message line on the printer each time a status change from 'OFF' to 'ON' or ‘ON’ to ‘OFF’ is detected for this channel. • Select 'OFF' to disable printing of status changes for this channel. Status Texts: • Select from 16 groups of texts shown in the window, to represent the channel’s status. (Texts themselves can be modified from another menu). Start Channel: • Enter a channel number, which start hour counter counting

Stop Channel: • Enter a channel number, which stop hour counter counting On Status: • Dig/Both, information only Display Format: • HH, HH:MM, HH:MM:SS, hours, minutes, seconds Initial Value: Button, a new dialog is shown, which enables to reset hour counter values:

The hour counters file is set with a new value.

### 7.12.3 General Settings

File path and filename of the hour counters file is set.

## 7.13 Extension Alarm System with LCD display or LED

The OWS (Operator Workstation) has an interface with the EAS Extension Alarm System. For a detailed description of the Extension Alarm System refer to the relevant product technical description. The interface with the Local Operator Panel(s) and the LED Panels is achieved via the EAS Plugin. The following picture shows the tree area:

• Adding a LOP (Local Operator Panel) or LED (Light Emitting Diode)Panel: • Select the Plugin folder in the tree and click with the right pointing device key or press the context menu key on the keyboard. Select 'Insert' from the context menu. The system will ask to select the type of panel and the number (Panel type including number should be unique), a new LOP or LED Panel will be created. • Deleting a LOP (Local Operator Panel) or LED (Light Emitting Diode)Panel:

• Select the specific LOP or LED Panel which should be deleted and press the delete key on the keyboard.

The maximum number of panels on the Extension Alarm System is defined as follows: - Up to 25 LOP (Local Operator Panels), - Up to 16 LED panels. A Local Operator Panel can be used / configured as part of the EAS system. If the Local Operator Panel is used / configured as one of the following EAS panels it is counted as an EAS panel. The following EAS panels can be defined:

Cabin Panel (1 - 8) [LOP, 8-LED or 2-LED panel] − Mess-room Panel [LOP, 8-LED or 2-LED panel] − − Group Panel [LOP, 8-LED or 2-LED panel]

On the EAS panels you can define a number of indicators: − For LED panel(s) indicator x = LED x For LOP panel(s) indicator x = a line in the EAS page −

A LOP panel can be defined as a:

Alarm Display [LOP panel (allow system accept / stop horn function)] −

### 7.13.1 Hardware Interface Signals

Via the I/O Server the following input signals are applied to the system:

- Reset Timer/Watch OFF - Attended input - Unattended input

The Reset/Watch OFF input will in active mode reset the patrol timer. The Reset-Timer switches are momentary switches. The Watch-OFF switch is a key protected switch on the entrance unit. The Attended / Unattended input is activated via the watch entrance unit. On the top of the screen the system displays if the engine room is attended or not. It also gives an indication what engineer is 'On Duty' in case the engine room will be unattended and the time when the 27-minute timer will be elapsed.

The system will provide the following outputs on the I/O Server Board:

- Patrol Timer Expired output - General Engineers Alarm output - Attended Engine Room output - Unattended Engine Room output

The Patrol Timer Expired output will be activated at:

- The moment that the pre-warning timer is elapsed.

The General Engineer Alarm output will be activated on the following conditions:

- If the 'On-Duty' engineer did not accept the alarm(s) in the ECR within a specified time. - If no reset timer button is pressed within time-out time. - If the GEA input on the I/O Server was activated

The Attended Engine Room output will be activated at:

- The moment the Attended Engine Room input was activated - The moment the 'Accept Horn' input was activated (see paragraph 7.13.2.2 General Engineer Alarm / Deadman Alarm Setup page 248). - The moment the 'Accept' input was activated (see paragraph 7.13.2.2 General Engineer Alarm / Deadman Alarm Setup page 248).

The Unattended Engine Room output will be activated at:

- The moment the Unattended Engine Room input was activated

### 7.13.2 Extension Alarm System General Setup

The following picture gives an overview of the general settings of the Extension Alarm System:

#### 7.13.2.1 EAS text setup

The EAS text setup is used to define the text strings on the top rows of the system and for the strings send to the EAS page of the Local Operator Panel indicator(s)

If alternate language (See Jobs) is enabled, a second column is shown for the input of the alternate language EAS Cabin descriptions.

Text used for the Status Indication Buttons (button color is yellow) and LOP indicator(s):

• Selected On Duty Engineer status: The status indication button / LOP indicator can indicate the following text (max 10 characters):

− Cabin1 - CHIEF ENG. − Cabin2 - 1-ST ENG. − Cabin3 - 2-ND ENG. − Cabin4 - 3-RD ENG. − Cabin5 - 4-TH ENG. − Cabin6 - 5-TH ENG. − Cabin7 - 6-TH ENG. − Cabin8 - 7-TH ENG.

> **[Figure]** Screenshot of the MEGA-GUARD EAS Text Table configuration in PAL. Shows a two-column table with cabin/role assignments on the left and corresponding text values on the right: Cabin1=Chief Eng., Cabin2=1st Engineer, Cabin3=2nd Engineer, Cabin4=3rd Engineer, Cabin5=4th Engineer, Cabin6=5th Engineer, Cabin7=6th Engineer, Cabin8=7th Engineer. Then: ECR extended line 1=Attended, ECR unattended line 1=Unattended. Then alarm indicator text: Alarm indicator status text active=Alarm, Alarm indicator status text inactive=Normal, Call indicator status text active=Call, Call indicator status text inactive=(empty dash), On duty indicator status text active=OnDuty, On duty indicator status text inactive=(dash), Attended indicator status text active=Att, Attended indicator status text inactive=(dash), Unattended indicator status text active=UnAtt, Unattended indicator status text inactive=(dash). Purpose: EAS text table mapping cabin positions to engineering crew roles and defining status display text for the MEGA-GUARD engineer alarm system.

• Attended / unattended status: The status indication button / LOP indicator can indicate the following text (max 10 characters):

## ATTENDED

## − UNATTENDED

The positions for these two status indication buttons are the two most right locations. If one of these buttons is pressed the system will show the `On duty` (mimic) page.

#### 7.13.2.2 General Engineer Alarm / Deadman Alarm Setup

The following screen gives you an overview of the alarm handling for General Engineers Alarm, Deadman Alarm and how to configure the Attended State of the ECR. The GEA is an alarm which will be activated if the (On Duty) engineer did not acknowledge the engine room alarm within a predefined time. A Deadman Alarm is initiated from a manned ECR. It occurs if the timer of the Patrol Alarm Unit (Timer Unit) has expired, or if the engineer in the ECR presses the ‘GEA’ button on the Patrol Alarm Unit.

> **[Figure]** Screenshot of PAL 'Cabin - Alarm Setup' configuration for General Engineering Alarm and Dead Man Alarm. GEA section: Function: UnAttended, Tag Name: *GEA*, Current Accept: Stop Horn, Time-out for E.R. Alarm before G.E.A.: 180 sec, Description: General Engineer Alarm. Deadman section: Function: Attended, Tag Name: Deadman, Accept key: 'Engine Room Attended', Current Accept: Ack, Pre-warning: 27 min, Time-Out: 30 min, Description: Dead Man Alarm. General section: Keyswitch on 'Watch Off' sets Attended Selection (checked), Accept Unattended Selection (checked). Purpose: PAL EAS configuration for GEA (General Engineer Alarm) and Dead Man/Patrol alarm system in unattended engine room mode.

The following parameter setup area determines the general EAS setup:

General Engineer Alarm Setup: • Function: This field can be set to the following values: - None: Indicate that no condition will activate the General Engineer Alarm - Unattended: The GEA will only be activated in case the Engine Room is unattended. - Both: The GEA will be activated regardless if the Engine Room is attended or unattended (Default).

• Tag Name: This is the text you can enter to indicate in the ‘TAG’ field on the Local Operator Panel(s) and OWS Operator Work Station(s) if a GEA is activated. Maximum number of characters is 10. Remind you if you change the text and you ask for this entry in setup, it will indicate you the new string. • Current Accept: This field can be set to the following values: - NONE: No functionality assigned to the Acknowledgement of alarms on the I/O server(s) in the ECR. - ACK: The Acknowledgement of alarms in the ECR will acknowledge the GEA. - STOP HORN: The Stop Horn action in the ECR will acknowledge the GEA. - BOTH: The Acknowledgement of alarms and/or Stop Horn action in the ECR will acknowledge the GEA (Default). • Time –Out for accept of ER ALARM before General Engineers Alarm (GEA): This is the time between the activation of an engine room alarm and the pressing of the Accept button in the ECR. Default value is 180 seconds. Valid entries are between 0 and 9999 seconds. • Description: This is the text you can enter to indicate in the ‘Description’ field on the Local Operator Panel(s) and OWS Operator Work Station(s) if a GEA is activated. Maximum number of characters 40. Remind you if you change the text and you ask for this entry in setup, it will indicate you the new string. • Alt. Description: This is the text you can enter to indicate in the ‘Description’ field on the Local Operator Panel(s) and OWS Operator Work Station(s) if a GEA is activated. Maximum number of characters 40. Remind you if you change the text and you ask for this entry in setup, it will indicate you the new string if the Alt Language is Active.

Dead Man Alarm Setup: • Function: This field can be set to the following values: - None: Indicate that no condition will activate the Dead Man Alarm - Attended: The Dead Man Alarm will only be activated in case the Engine Room is Attended. - Both: The Dead Man Alarm will be activated regardless if the Engine Room is attended or unattended (Default). • Tag Name: This is the text you can enter to indicate in the ‘TAG’ field on the Local Operator Panel(s) and OWS Operator Work Station(s) if a DEADM is activated. Maximum number of characters 10. Remind you if you change the text and you ask for this entry in setup, it will indicate you the new string. • Accept key to signal ENGINE ROOM ATTENDED - NONE – The ‘ECR Attended’ state will not be activated by pressing either the Acknowledge button or the STOP HORN button in the ECR.

- ACK – By pressing the Acknowledge button in the ECR, the ‘ECR Attended’ state will be activated. - STOP HORN – By pressing the STOP HORN button in the ECR, the ‘ECR Attended’ state will be activated. - BOTH – By pressing either the STOP HORN or the Acknowledge button in the ECR, the ‘ECR Attended’ state will be activated (Default).

> **[Figure]** Screenshot of PAL EAS Cabin indicator and horn settings table. Columns: Description, Alt Description, Function, Mode (two), Type, Reset. 16 rows including: BRG Calls (Call from Bridge/Tone/Yes), Propulsion Alarms (Group/0/O.D/UnAtt/Tone/Yes), Switchboard Alarms (Group/1/O.D/UnAtt/Tone/Yes), Other Alarms (None), GEA or DeadMan (GEA or Deadman/Pulse/No), On Duty (On Duty & UnAttended), ECR Calls (Call from ECR/Tone), ECR Alarm 1 (Group/7/Both/UnAtt/Tone/Yes), DeadMan Alarm (Deadman/Both/Off). Dutch and Japanese alternative descriptions included. Purpose: EAS cabin indicator/horn settings table configuring alarm types, multilingual descriptions, attendant modes, and response behaviors.

• Prewarning (min): This is the time between the activation of a Deadman alarm and the pressing of the Accept button in the ECR. Default value is 27 min. Valid entries are between 1 and 60 minutes. • Time-Out (min): This is the time between the activation of a Deadman alarm and the pressing of the Accept button in the ECR. Default value is 30 min. Valid entries are between 1 and 60 minutes. • Description: This is the text you can enter to indicate in the ‘Description’ field on the Local Operator Panel(s) and OWS Operator Work Station(s) if a DEADM is activated. Maximum number of characters 40. Remind you if you change the text and you ask for this entry in setup, it will indicate you the new string. • Alt. Description: This is the text you can enter to indicate in the ‘Description’ field on the Local Operator Panel(s) and OWS Operator Work Station(s) if a DEADM is activated. Maximum number of characters 40. Remind you if you change the text and you ask for this entry in setup, it will indicate you the new string if the Alternate Language is Active.

#### 7.13.2.3 Cabin Page Setup

Within the general setting you can define the Cabin Page Layout. This layout will be used for all cabin (type) panels on board of the ship. Selecting the Cabin setup folder from the tree will give you the following setup area:

Indicator Settings

• Description: • Descriptive text for the selected function. This text is transmitted to the EAS page of the Local Operator Panel in case this panel is setup as cabin unit. • Alt. Description: • Alt. Descriptive text for the selected function. This text is transmitted to the EAS page of the Local Operator Panel in case this panel is setup as cabin unit. • Function: • The indicator can be activated with the following alarm functions: NONE No activation of this indicator. Group xx The indicator will be activated as soon as one or more channels in this group is(are) going into the alarm state. The group number is specified in the second column of the function. GEA The indicator will be activated in case of a General Engineer Alarm. DEADMAN The indicator will be activated in case of a Deadman Alarm. GEA or DEADMAN The indicator will be activated in case of a General Engineer Alarm or/and Deadman alarm.

• The indicator can be activated with the following status functions: ATTENDED The indicator will be activated in case of an attended state of the engine room. UNATTENDED The indicator will be activated in case of an unattended state of the engine room. ON DUTY & The indicator will be activated in case of an UNATTENDED unattended state of the engine room and when this cabin is selected to be the on duty engineer. ON DUTY on The indicator will be activated in case that the duty SELECTED selection x is selected. CALL FROM ECR The indicator will be activated in case that the engineer is called from the Engine Control Room. CALL FROM The indicator will be activated in case that the BRIDGE engineer is called from the bridge. CALL ALL FROM The indicator will be activated in case that all ECR engineers are called from the Engine Control Room. CALL ALL FROM The indicator will be activated in case that all BRIDGE engineers are called from the bridge.

• Mode: • The mode is a setting to indicate when the function will activate the indicator. The following modes can be selected:

> **[Vector Diagram — Page 252]** Page 252 documents MEGA-GUARD EAS (Extended Alarm System) horn and indicator mode configuration options for watch system panels.

Table 1: ON DUTY Indicator Mode Options. Type: Configuration reference table. Describes when the ON DUTY indicator activates based on mode:
- OFF: Indicator activates only if the cabin unit is selected (cabin-specific)
- ATT: Indicator activates only if the attendance/engine room is attended (watch present)
- UNATT: Indicator activates only if the engine room is unattended (no watch)
- BOTH: Indicator activates in both attended and unattended states

Table 2: Horn Mode Options. Type: Configuration reference table. Same mode structure:
- OFF: Horn activates only if the cabin unit is selected
- ATT: Horn activates only when attendance room/engine room is attended
- UNATT: Horn activates only when engine room is unattended
- BOTH: Horn activates in both attended and unattended states

Type Field (Sound type):
- TONE: The horn makes a continuous sound
- PULSE: The horn makes an intermittent (pulsing) sound

Reset Field:
- YES: The horn will be stopped by pressing the accept button
- NO: The horn will NOT be stopped by pressing the accept button

Note: Section 7.13.2.4 - 'The default setting is: No Automatic start of the Patrol Timer with an alarm.'

Page 252 is from section 7.13 ('EAS - Extended Alarm System'). These settings control how EAS panels on board respond to alarm conditions based on the bridge/engine room attendance state in the MEGA-GUARD watch system, enabling different horn/indicator behavior for attended vs. unattended machinery spaces.

- ON DUTY The indicator will only be activated by the selected function if the cabin unit is selected On Duty. - ATT The indicator will only be activated by the selected function if the engine room is attended. - UNATT The indicator will only be activated by the selected function if the engine room is unattended. - BOTH The indicator will only be activated by the selected function if the engine room is attended or unattended.

Horn Settings:

• Mode: • The mode is a setting to indicate when the function will activate the horn. The following modes can be selected: - OFF The horn will never be activated by the selected function. - ATT The horn will only be activated by the selected function if the engine room is attended. - UNATT The horn will only be activated by the selected function if the engine room is unattended. - BOTH The horn will only be activated by the selected function if the engine room is attended or unattended. • Type: • The type is a setting to determine what sound the horn will make. The following modes can be selected: - TONE The horn will make a continues sound - PULSE The horn will make an intermittent sound. • Reset: • The reset is a setting to determine whether the horn should be stopped or not when pressing the accept button. The following modes can be selected: - YES The horn will be stopped pressing the accept button. - NO The horn will not be stopped pressing the accept button.

#### 7.13.2.4 Mess room page setup

Within the general setting you can define the Mess room Page Layout. This layout will be used for all mess room (type) panels on board of the ship. For setup of this page, refer to the paragraph 7.13.2.3 Cabin Page Setup page 250.

|  | [INFO] For setup of the mode of the indicator for the mess room page, the selection 'On Duty' |  |
| --- | --- | --- | |
|  | is not available. |  |

#### 7.13.2.5 LOP Setup

Once the LOP is inserted the setup area will give you the following settings:

> **[Figure]** Screenshot of PAL LOP (Local Operator Panel) configuration. Local Operator Panel Number: 1, Panel type: Cabin1. LOP Menu Items 1-6: Alarm Page, EAS Page, Group Page, Channel Page, Dimming Page, Along Side Page. Default Page: Alarm Page. Sync Alarm Page with Cabin/Mess Groups (checked). Groups: 1-TC1 PROPULSION (TFT ALARMS), 2-TC1 STEERING, 3-TC1 THRUSTER/PUMP, 4-TC1 LIFTING, 5-TC1 OTHER/SYSTEM, 6-TC1 IFS SIGNALS, 7-TC1 IFA SIGNALS, 8-TC1 CODES. Purpose: PAL LOP configuration defining menu structure, page assignments, display settings and alarm group syncing for a cabin alarm panel.

• Local Operator Panel Number: • Number of the LOP not changeable from this location. • Panel type: • The following panel types can be selected: - Cabin x This selection will assign the pre-defined functionality of the xth cabin to this LOP. Refer to paragraph 7.13.2.1 EAS text setup page 246 to see which engineer is related to what cabin panel.

- Mess This selection will assign the pre-defined functionality of a mess room panel to this LOP. - Group This selection will assign the functionality of a group alarm panel to this LOP. Assignment of the EAS indicator and horn activation can be selected freely. For set up of indicator(s) and horn functionality refer to paragraph

#### 7.13.2.3 Cabin Page Setup page 250.

- Alarm Display This selection will assign the functionality of an alarm display panel to this LOP. There is no EAS indicator setup available for this type of panel. • LOP selection key setup: • On a LOP a number of keys can be assigned to specific functions. The picture below shows you the front panel of the Local Operator Panel and the location of these function keys:

> **[Figure]** Screenshot of the MEGA-GUARD EAS (Extended Alarm System) hardware panel - Engineer Call Station / Local Operator Panel. Black rectangular panel with green LCD display at top showing: ER: UNATTENDED  DUTY: CHIEF ENG.  15:23:45, followed by alarm entries: 2040B 14:23:45 M/E EXH. GAS TEMP. AFTER NO.4 CYL HIGH!, 21107 15:03:12 M/E L.O. INLET PRESSURE LOW!, 21711 15:03:53 OILY BILGE TANK LEVEL HIGH!. Below the display, 8 red/yellow square group buttons arranged in 2 rows: Row 1: CALL ECR, GROUP1 MAIN ENGINE, GROUP2 GENERATOR ENGINE, GROUP3 AUX MACHINERY, GROUP4 SAFETY SYSTEM, ON DUTY. Row 2: CALL BRIDGE, GROUP5 TANK & BILGE, GROUP6 ELECTRICAL, GROUP7 STEERING GEAR, ENGINEER OF WATCH, STOP HORN. Navigation/function buttons below: ACK, left/right arrows, up/down arrows, STOP HORN. At bottom: SYSTEM ON indicator (green), FAULT indicator (red), PRAXIS logo. Purpose: physical EAS engineer call station panel showing live alarm display with unattended state indication in MEGA-GUARD.

The following key functions can be assigned to these keys: - Channel Page Pressing this key will select the Channel Page. You can now add channels to this page by selecting the channel and pressing 'Enter'. - Group # Page Pressing this key will display the Group Page selection display. You can now enter a group number and selecting this Group Page by pressing 'Enter'. - Up Pressing this key will display the previous 4 lines of the selected display. - Down Pressing this key will display the next 4 lines of the selected display.

• Default Page on LOP: • With this selection you can determine the default page to be displayed on startup of the system. Possible selections are: - None No page will be displayed at startup. - Alarm Page The Alarm Page will be displayed at system startup. - Channel Page The Channel Page will be displayed at system startup. - EAS Page The EAS indicator page will be displayed at startup.

#### 7.13.2.6 EAS Panel (LOP) node number setup

The functionality of the Extension Alarm System (EAS) Local Operator Panel (LOP) is depending on a proper communication over the Ethernet network with MPC running IOServer.exe. The LOP node number must be setup according the number configured in PAL.

This node number is the last number of the 4 number IP address used for communication, and it must be unique. No other LOP in the system can have the same node number.

On LCD panel the node number can be setup as follows:

• Power on the LOP while keeping “Accept” key pressed • A menu appears allowing to set node number using Arrow Up/Down keys • Use the menu to save after input. Then power panel off and on

Ethernet connection is not required at this point

On TFT panel the node number has to be setup by placing correct address resistor at backside of the panel (see drawings).

#### 7.13.2.7 EAS 5.7” TFT Panel Setup

5.7” TFT EAS Panel setup is configured by inserting an LOP and ticking the checkbox at the right top of the LOP# configuration dialog.

A message box is popup, “Are you sure you want to add TFT Connection”:

Choose OK. The system will now configure and install required files.

> **[Vector Diagram — Page 256]** Page 256 documents MEGA-GUARD LOP (Local Operator Panel) LED indicator configuration options and EAS language pack availability.

Language Packs Table. Type: Configuration reference table. Available language packs for EAS/LOP panels with availability by panel type (TFF 2.5, TFF 5*, TFF 8*, LCD):
- English: available on all panel types
- French: available on TFF panels
- Buttons: available on TFF panels
- German: available on TFF panels
- VhfMtg: LCD only
- VhfMtg3: LCD only

Text: LOP Panel LED Configuration (section 7.13.2.8 LOP LED Setup):
- LED Panel Number: number of the LOP, not changeable from this location
- LED Array: panel types selectable from dropdown listing

Diagram: LOP Module Type Dropdown. Type: Software UI screenshot (partial). Shows module type selection dropdown for LOP panel hardware configuration. Multiple panel hardware types listed in the dropdown.

Text: LOP EAS Setup Notes:
- If the LED Panel is of the type with 8 LED LOPs, the first eight indicator lines from the EAS indicator table will be used; remaining lines not available for 8-LED configurations
- Selection of LED array type determines which EAS indicator table entries are active

Note (information icon): 'If the LED Panel is of the type with 8 LED LOPs, the first eight indicator lines will be used from this table.'

Page 256 is from sections 7.13.2 ('LOP Setup') and 7.13.3 ('Language Setup'). LOP LED configuration maps alarm signals to physical LED indicators on Local Operator Panel hardware; language pack determines text displayed on the LOP for alarm descriptions.

For Software versions 6.0.1.10 to 6.0.1.21 it is required to recompile the PAL1131 program of the 5.7” TFT using the PAL1131.exe program: • Start PAL1131.exe from D:\Software\System\PAL1131 • Open XP76 project from D:\Software\System\Setup\XP76. • Press Build button to recompile the program • Close PAL1131 (and save the project).

#### 7.13.2.8 EAS LED Panel Setup

Once the LED Panel is inserted the setup area will give you the following settings:

• LED Panel Number: • Number of the LOP not changeable from this location. • Panel type: • The following panel types can be selected: - Cabin x This selection will assign the pre-defined functionality of the xth cabin to this LOP. Refer to paragraph 7.13.2.1 EAS text setup page 246 to see which engineer is related to what cabin panel. - Mess This selection will assign the pre-defined functionality of a mess room panel to this LOP. - Group This selection will assign the functionality of a group alarm panel to this LOP. Assignment of the EAS indicator and horn activation can be selected freely. For set up of indicator(s) and horn functionality refer to paragraph

#### 7.13.2.3 Cabin Page Setup page 250.

- Alarm Display This selection will assign the functionality of an alarm display panel to this LOP. There is no EAS indicator setup available for this type of panel.

|  | [INFO] If the LED Panel is of the type with two LEDs, the first two indicator lines will be used |  |
| --- | --- | --- | |
|  | of the table. If the LED Panel is of the type with eight LEDs, the first eight indicator |  |
|  | lines will be used of the table. |  |

### 7.13.3 Attended / unattended switching confirmation

According rules for DNV (added in 2003 and 2004) it is required that the Bridge is made aware when ECR / ER switches to unattended. This is implemented as follows:

Location Action

• ECR / ER Select to go unattended (via EAS mimic) • Flashing lights on Watch entrance unit.

## ECR / ER

• Bridge Audible warning and unattended text is flashing. • Bridge Accept or acknowledge button confirms to switch to unattended. • ECR / ER System unattended indication is shown on display. • Bridge System unattended indication is shown on display. System is unattended.

Following settings in PAL must be changed to enable unattended switching confirmation:

> **[Figure]** Screenshot of the MEGA-GUARD PAL LOP (Local Operator Panel) configuration screen. Left tree: Plugins > FB1-FB(IO) > eac-FB4(EAS) > General Settings; LOP01-(Mess) > LOP01-Display (highlighted). Right panel: Local Operator Panel Number field (empty), Panel type: Mess (dropdown). LOP Selection Key assignments: F1=Alarm Page, F2=Group Page, F3=Channel Page, F4=EAS Page (left column); F5=Page Down, F6=Page Up, F7=Full/Hall, F8=/ (right column). Default Page on LOP: Alarm Page (dropdown). External Relay: None (dropdown). Accept Unattended Selection checkbox (unchecked). Purpose: configuring the key assignments and default page for a Mess-type Local Operator Panel in the MEGA-GUARD EAS (Extended Alarm System).

• Check the "Accept unattended selection" option.

This will set the system to go to unattended only when it is allowed from the Bridge. On the Bridge a LOP or Workstation must be present to support this functionality. The Workstation setting is explained in paragraph 7.1.2 "Permissions". The LOP setting is set using PAL:

> **[Figure]** Screenshot of PAL EAS plugin configuration showing GEA/Deadman settings. Left tree: Plugins > eas-FB4(EAS) > General Settings > Server Settings, EAS Text Setup, GEA/Deadman (selected), Cabin Display, Mess Display > LOP01-(Alarm Display) > LOP01-Display, FD1-FD1(IO). Right panel: Cabin-Alarm Setup / Dead Man Alarm: Function None, Current Accept: None, Pre-warning: 27 min, Time-Out: 30 min, Description: Dead Man Alarm. Purpose: PAL EAS plugin GEA and Deadman alarm configuration within the EAS system tree.

• Check the option "Accept unattended selection"

The configured LOP is now enabled to allow unattended state.

|  | [INFO] Unattended mode is only allowed if at least one LOP or Workstation is setup and |  |
| --- | --- | --- | |
|  | running. |  |

> **[Vector Diagram — Page 258]** Page 258 covers the MEGA-GUARD 'Along side / Sailing' mode configuration for watch systems, including LOP and OWS procedures.

Text: Along side / Sailing Mode (section 7.13.3.1):
Functionality to disable attended/unattended switching confirmation temporarily. Called 'Along side' mode when the ship is docked (port state).

LOP Procedure for Along side / Sailing mode:
1. Press 'General'
2. If dimming appears, again press 'General'
3. Select 'Along side' page
4. Select 'Along side' or 'Sailing' buttons
5. Press '1' and Enter to set 'Along side' mode
6. Press '2' and Enter to select 'Sailing' mode

Note (information icon): 'Alarm will not switch on the buzzer the bridge when the system is in along side mode. Display will not show text flashing.'

OWS Workstation Procedure:
- Press 'EAS selection mimic (aligned app) (Watch Responsibility system)'
- Press 'Along side' or 'Sailing' buttons to switch the system in appropriate mode

Page 258 is from section 7.13.3.1 of the Engineering Guide. The Along side mode is a key MEGA-GUARD watch system feature that suppresses bridge alarm activation when the vessel is in port, preventing alarm nuisance to harbour personnel and complying with class society requirements for port state operations (UMS certification).

#### 7.13.3.1 Along side / Sailing setting

The system has functionality to disable attended / unattended switch confirmation temporary. This is used when the ship is along side. This option is called Along side / Sailing, and can be set as follows.

On the LOP: • Press "General", • if dimming appears, again press "General" • "General page" appears (see image below) • Select "Along side" page, the page appears • "1" and Enter sets "Along side", "2" and Enter selects "Sailing" The setting is saved in configuration. When the system is started for the first time (without the setting) it will be in "Sailing" mode.

On the Workstation: • Select EAS selection mimic (selpanel.ggg) (Watch Responsibility system) • Press "Along side" or "Sailing" buttons to switch the system in appropriate mode.

|  | [INFO] Alarm will not switch on the buzzer the bridge when the system is in along side mode. |  |
| --- | --- | --- | |
|  | The display will show alarm text flashing. |  |

### 7.13.4 Watch entrance unit

The Watch entrance unit with patrol timer enables switching between attended and unattended mode (key required) and activates the Deadman Timer (no key required).

code number 93.0.371

#### 7.13.4.1 Attended mode

When the ATTENDED mode is selected on the Watch Entrance Unit (or via the EAS Page on the Workstation) the (Patrol) timer is activated. The lamp in the TIMER ON/OFF (switch) on the Watch Entrance Unit is illuminated. It is not possible to switch the timer off by means of the TIMER ON/OFF switch on the Watch Entrance Unit. With the key switch on the Watch Entrance Unit the timer can be switched off (override). If the timer is expired (default after 27 minutes), the Timer Expired Output is activated. If the Reset Timer Input is not activated within 3 minutes (default) the system will generate a Dead Man Alarm.

#### 7.13.4.2 Unattended mode

When the UN-ATTENDED mode is selected on the Watch Entrance Unit (or via the EAS Page on the Workstation) the timer is in-active. Via the TIMER ON/OFF switch on the Watch Entrance Unit the timer it can be switched ON (the lamp will be illuminated) and OFF by pressing the switch again. With the key switch on the Watch Entrance Unit the timer can be switched off (override). The Timer Expired Output will be activated after the timer has expired (default after 27 minutes). If the Reset Timer Input is not activated within 3 minutes (default) the system will generate a Dead Man Alarm.

#### 7.13.4.3 Automatic Start of the Deadman Timer with an alarm

Automatic start of Patrol Timer is driven by the following setting:

> **[Vector Diagram — Page 260]** Page 260 documents the Automatic Start of Patrol Timer with Alarm feature and Engineer Calling Name Indication LOP display layout for the MEGA-GUARD EAS.

Text: Automatic Start of Patrol Timer with Alarm (section 7.13.4.4):
- If this setting is active, the Patrol Timer automatically switches on when an alarm is received from the AMS (Alarm Monitoring System)
- Default setting: 'No Automatic start of the Patrol Timer with an alarm.'
- When enabled, ensures watch engineer patrol response is automatically tracked on alarm events

Diagram: OWS LOP Engineer Calling Display. Type: Software UI screenshot. Shows the OWS iObserver LOP layout panel with engineer calling names. The display shows multiple engineer call lines (one call per line in the LOP). Each line shows cabin/engineer identification. The layout is visible as a grid of LED indicator positions with engineer name/identifier per line.

Text: Multiple Engineer Calling:
'Multiple engineers can be called. Each call will occupy one line in the LOP. The layout for the LOP_PAGE is as follows:'

LOP Layout Table for Engineer Calling. Type: Display layout reference. Shows LOP display positions per line for engineer calls:
[Line 1 - Engineer 1 identifier]
[Line 2 - Engineer 2 identifier]
[...additional lines...]
Each engineer call occupies exactly one line in the LOP page display.

Page 260 is from section 7.13.4 ('Watch System Configuration'). The Patrol Timer with automatic alarm start and Engineer Calling features are critical MEGA-GUARD EAS functions for Unmanned Machinery Space (UMS) operations - ensuring watch engineers are alerted and their presence tracked.

Option: Automatic start of the Patrol Timer with an alarm

> **[Figure]** Screenshot of PAL EAS Cabin indicator/horn settings table with Dutch descriptions. Columns: Description, AltDescription, Function, Mode (two), Type, Reset. 16 rows: BRG Calls/Brug Roept::/Call from Bridge, Propulsion Alarms/Propulsie Alarmen/Group 1, Switchboard Alarms/Switchboard Alarmen/Group 3, Other Alarms/Andere Alarmen, GEA or DeadMan/GEA Of Dode Man, On Duty/Dienst!, ECR Calls/ECR Roept::, ECR Alarm 1-4/Machine Kamer Alarm 1-4/Group 7-10/UnAtt, Fire Alarm/Brand Alarm/Group 255, Call All from Bridge/Brug Roept Iedereen Op, Call All from ECR/ECR Roept Iedereen Op, General Engineers Alarm/Algemeen Engineers Alarm/GEA, Deadman Alarm/Dodeman Alarm. Purpose: EAS cabin indicator/horn configuration in Dutch showing full alarm system function assignments.

If this setting is active, the timer will automatically be switched on with an alarm from the AMS. The setting ‘Function’ in the PAL (EAS Deadman Setup) should automatically switch to both in this case and is not selectable anymore.

The default setting is: No Automatic start of the Patrol Timer with an alarm.

The default will be not active as this is compatible with systems without this option.

#### 7.13.4.4 Engineer Calling with Engineers Name Indication

Multiple engineers can be called. Each call will occupy one line in the LOP. The layout for the EAS PAGE is as follows: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2

|  |  |  |  |  | E | A | S |  |  |  | P | A | G | E |  | E | C | R | : |  | A | T | T | E | N | D | E | D |  |  |  | 2 | 2 | : | 2 | 3 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | |
|  |  |  |  |  | O | N | - | D | U | T | Y |  | E | N | G | I | N | E | E | R | : | C | h | i | e | f |  | E | n | g | i | n | e | e | r |  |  |  |  |  |  |
|  |  |  |  |  | B | R | I | D | G | E |  | C | A | L | L | S |  | E | N | G | I | N | E | E | R |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | B | R | I | D | G | E |  | C | A | L | L | S |  | E | N | G | I | N | E | E | R |  | 2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  | B | R | I | D | G | E |  | G | R | O | U | P |  | 1 |  |  |  |  |  |  |  |  |  |  | A | L | A | R | M |  |  | ! |  |  |  |  |  |
|  |  |  |  |  | B | R | I | D | G | E |  | G | R | O | U | P |  | 7 |  |  |  |  |  |  |  |  |  |  | A | L | A | R | M |  |  | ! |  |  |  |  |  |
|  |  |  |  |  | E | C | R |  | C | A | L | L | S |  | C | H | I | E | F |  | E | N | G | I | N | E | E | R |  |  |  |  |  |  |  |  |  |  |  |  |  |

This is configured as displayed in following picture:

#### 7.13.4.5 Header Line of the LOP

> **[Vector Diagram — Page 261]** Page 261 documents EAS LOP header line format specification and EAS header line character layout examples for MEGA-GUARD LOP panel displays.

Text: LOP Header Line Setup (section 7.13.5):
Documents header line format for each LOP type. The PAL allows adding header line setting for each LOP via: Go to Processor > Add Item > Add > Program.

Table: EAS Header Line Format for LOP. Type: Data format table with field definitions:
- Alarm/Menu Name: 9 characters
- Alarm/Menu Address: 8 characters
- Space: 1 character
- On-Off indicator: 1 character ('e' for alarm, 'm' for menu)
- DIO (In-State): 1 character
- CIO (Out-state): 1 character
- Alarm type: 1 character

Note (information icon): 'If this setting is de-activated, the header information is compatible with the previous software version(s).'

Option: EAS info in header line of LOP. Documents the option for EAS-specific header information:
'In the PAL you will be able to add the following header line setting for each LOP.'

EAS Header Line Character Examples. Type: Character position layout examples. Shows character-by-character position assignments for different LOP page types:
1. EAS Menu pages (Cabin, Mess, Alarm, Group pages)
2. Exact character layout for EAS, Menu, Alarm, and Group LOP pages

Table: EAS Header Line for LOP - character positions. Shows position assignments in grid format where each cell represents one character position, with example content showing alarm name, address, on/off state, and alarm type indicator fields.

Page 261 is from section 7.13.5 ('LOP Header Configuration'). The LOP header line format determines alarm information presentation on the Local Operator Panel physical display.

In the PAL you will be able to add the following header line setting for each LOP

Option: EAS info in header line of LOP

If you setup new LOP’s (or upgrade the existing software) the default will be for CABIN, MESS and Group LOP’s this setting will be activated; for ALARM LOP’s this setting will be de-activated).

|  | [INFO] If this setting is de-activated, the header information is compatible with the previous software version(s). |
| --- | --- | |

EAS header line for LOP:

| Page Indication (3 characters) | Space (2 characters) | Engine Room State (8 characters) | Space (1 character) | On-Duty Engineer (20 characters) | Space (1 character) | Time with flashing semi column for running indication (5 characters) |
| --- | --- | --- | --- | --- | --- | --- | |
| ALM (for ALARM PAGE) |  | ER:ATT (for ATTENDED) |  | DUTY:First Engineer |  | HH:MM |
| EAS (for EAS PAGE) |  | ER:UNATT (for UN-ATTENDED) |  |  |  |  |
| CHN (for CHANNEL PAGE) |  |  |  |  |  |  |
| GRP (for GROUP PAGE) |  |  |  |  |  |  |

EAS Header Line examples for EAS, Menu, Alarm and Group pages: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2

| E A S P A G E |  | E C R : | A T T E N D E D |  |  | 2 2 : 2 3 |
| --- | --- | --- | --- | --- | --- | --- | |
| O N - D U T Y E N G I N E E R : |  |  |  | C h i e f E n g i n e e r |  |  |

| M E N U P A G E |  | E C R : | U N A T T E N D E D |  |  | 2 2 : 2 3 |
| --- | --- | --- | --- | --- | --- | --- | |
| O N - D U T Y E N G I N E E R : |  |  |  | C h i e f E n g i n e e r |  |  |
| A L A R M P A G E E C R : A |  |  |  | T T E N D E D 2 2 : 2 3 |  |  |
| O N - D U T Y E N G I N E E R : |  |  |  | C h i e f E n g i n e e r |  |  |

| G R O U P P A G E |  | E C R : | A T T E N D E D |  |  | 2 2 : 2 3 |
| --- | --- | --- | --- | --- | --- | --- | |
| O N - D U T Y E N G I N E E R : |  |  |  | C h i e f E n g i n e e r |  |  |

### 7.13.5 Language Packs for the EAS Panel and Alt Font Support

The EAS panel utilises language packs to properly display fonts. Currently there are 3 different language packs available.

For English and other languages that use the latin script, please use “lp-lcd-english.bin”

For Cyrillic or Russian characters use “lp-lcd-russian.bin”

When the EAS is configured to display alternate language descriptions in large character format, the EAS panels will use a different layout. Refer to section 6.6 in the “PTD_Mega-Guard_E- Series_OWS” document, revision 1.22 and up for full details on the layout.

# 8 DOCUMENTATION WITH DOCGEN

To provide a “fast way” to generate data reports of configuration of Error! Reference source n ot found. System, now the DocGen program is being introduced. This program requires a proper installed version of the application Microsoft Excel ‘97. Via OLE-Automation Excel functionality is used to generate a Excel report. After this report is created it will be stored to a file on hard-disk. The generated file is according the Microsoft Excel 97 format. It is also required that a printer is installed.

## 8.1 Using DocGen

After starting docgen.exe the following screen appear:

The user has the choice of three types of reports. These are:

1. -IO List

After selecting the correct file paths of templates files and where to put generated files, a report could be created. Press the "Start" button to do this.

The following templates files are used:

> **[Figure]** Screenshot of Document Generator 8.0.4 tool. Title: 'Document Generator - 8.0.4 - Seakid1000 - Microsoft Word'. Fields: Type Report: ID-List Index (selected), ID-List (no event), ID-List (Loop Layout). Link Number: FeedList. Processor Numbers From/To: 101/101. Path of Template Files: L:\Project_kt\Setup\Template\. Path of Generated Files: L:\Project_kt\Setup\. Checkboxes: Hardware Channels (checked), Panels (checked), Header (checked), Footer (checked). Start button. Purpose: Document Generator tool for creating MEGA-GUARD system documentation from PAL configuration data.

> **[Figure]** Screenshot of Document Generator 'Select Folder' dialog showing available XLS template files. Template folder contains: FB.xls, FB_Index.xls, full_IO_16HW.xls, full_IO_20Dio.xls, full_IO_24Di.xls, full_IO_24Dio.xls, full_IO_33Dio.xls, full_IO_36Dio.xls, Group_One.xls, hw_only_IO variants, IO_16HW.xls, IO_20Dio.xls, IO_24Di.xls, IO_24Dio.xls, IO_33Dio.xls, IO_36Dio.xls, IO_Index.xls, IO_Index_Rev002.xls, IO_NOHW.xls, IO_One.xls, IO_panel.xls, IO_PMS.xls, Mimic.xls (216KB), PM.xls, PM_Index.xls. Purpose: Document Generator template file selection showing available XLS report templates for different I/O board configurations.

If Document Generator is started on a Windows System without Microsoft Excel ’97 the above message is shown. The report could not be created.

|  |  |  |  | If a system has a large configuration it can take a few minutes to create the report. For |  |
| --- | --- | --- | --- | --- | --- | |
|  | [INFO] |  |  | your convenience a progress bar is added to the document generator. |  |
|  |  |  |  | During time of generating the .xls file DO NOT OPEN EXCEL via explorer by clicking |  |
|  | [INFO] |  |  | another .xls file. |  |

After creating the report exit Document Generator and go via a program like explorer to generated file.

“IO_List_FB1.xls” is new generated file.

> **[Figure]** Screenshot of MEGA-GUARD PAL configuration folder showing database/configuration files. File browser panel showing contents with Name and Size columns: Template (folder), clientconfig.mdb (110 KB), Config.mdb (552 KB), EmptyClientConfig2000.mdb (172 KB), EmptyClientConfig97.mdb (100 KB), EmptyConfig2000.mdb (876 KB), EmptyConfig97.mdb (552 KB), IO_List_FB1.xls (259 KB, highlighted). Purpose: showing the MEGA-GUARD PAL configuration database files including the main Config.mdb, empty template databases, and an Excel I/O list file IO_List_FB1.xls.

> **[Vector Diagram — Page 266]** Page 266 covers MEGA-GUARD language pack configuration for EAS TFT panels and LOP displays including available language packs and language generation procedures.

Text: Section 9.1 ('Standard Language Packs for LCD, 5" and 8" TFT').

Language Pack Availability Table. Type: Configuration reference table. Shows language packs available per panel type (TFF 2.5, TFF 5*, TFF 8*, LCD):
- English: all panel types
- French: TFF panels
- Buttons: TFF panels
- German: TFF panels
- VhfMtg: LCD only
- VhfMtg3: LCD only

Note: '* Only CJK characters are not implemented yet.' Indicates Chinese/Japanese/Korean character support not available for TFT panels as of Rev 6.33.

Note (information icon): 'Only CJK characters are not implemented yet.'

Text: Language Pack Generation Procedure (section 9.1.2 'Generating Language Pack'):
'It is possible to create project language packs from scratch via the CJK EAS TFT Support application. Refer to section 9.3 for details of the language generation process.'

Language Generation Steps documented:
1. Download XP1 to second Panel (power down first panel, make address XP 61)
2. Download XP1 to second Panel (power down first panel)
3. Download XP1 to third Panel (power down second panel)
4. Change settings on second Panel (address should be XP 62)
7. Save the source code in VXL file

Page 266 is from section 9 ('Language'). The language pack system enables multi-language alarm text display on MEGA-GUARD EAS TFT and LOP panels for international vessels, with English as primary language and additional European languages available.

# 9 ALT LANGUAGE

## 9.1 Standard Language Packs for LCD, 5.7” and 8.4” TFT

Both LCD and TFT panels utilize language packs to display fonts. There are currently 3 different language packs available for each panel and a special large character file. Each Language Pack is stored in a file and contains a specific set of characters that are used in the most common projects.

| Language pack files | TFT 5.7”, 8.4” | TFT 2.4” | LCD |
| --- | --- | --- | --- | |
| English (Latin) | lp-tft-en.bin | lp-tft-24-en.bin | lp-lcd-en.bin |
| Russian (Cyrillic) | lp-tft-ru.bin | lp-tft-24-ru.bin | lp-lcd-ru.bin |
| Chin, Jap, Kor (CJK)* | lp-tft-cjk.bin | lp-tft-24-cjk.bin | lp-lcd-cjk.bin |
| English Large** | lp-tft-large-en.bin |  |  |

* CJK is abbreviation for Chinese, Japanese, Korean ** Only characters: +-0123456789.NSEWKMAVW It is possible to create project specific language files to support more characters with the CJK TFT support application (see paragraph 9.2).

### 9.1.1 Generating CJK Language Packs for LCD, 5.7” and 8.4” TFT

In order to ensure that all CJK characters can be displayed from a system configuration, a fresh language pack has to be generated. This can be done via the “CJK EAS TFT Support Application”. Please refer to section 9.3 for further details on how to use this program and generate the language pack.

In general, the support application should be used when the system is configured for the first time and after every modification that occurs where descriptions are altered.

### 9.1.2 For 5.7” and 8.4” TFT

“” If using the TFT in an “Alt language” configuration, the char or a blank row is displayed when a character cannot be found in the language pack. Ensure that the proper language pack is uploaded to the TFT panel or generate a new language pack if using CJK characters.

### 9.1.3 PAL1131G

PAL1131G checks against a chosen language pack in order to generate mimics. If certain characters cannot be found, it will not be displayed on the generated mimic. The configuration can still however be properly saved and generating a fresh language pack afterwards will allow PAL1131G to properly display the desired texts.

## 9.2 Chinese Japanese and Korean text in LCD and TFT panels

Before a Chinese, Japanese or Korean symbol can be used in an LCD or 2.4”, 5.7”, 8.4” TFT panel it must be configured using the CJK EAS TFT Support Application.

### 9.2.1 Introduction

The “CJK EAS TFT Support Application” is used to generate language pack files that will enable the following products to display Chinese, Japanese and Korean characters:

> **[Figure]** Screenshot of CJK for TFT and EAS utility. Title: 'CJK for TFT and EAS'. Browse button with path 'D:\Software\System'. EAS tab active (TFT tab also shown). Buttons: Full Generation (Generates fresh language pack based on configuration database), Smart Generation (Only updates if current config contains characters not in existing pack), Generate Only (Only generates Language Pack file, no upload), Upload Only (Does not generate, requires existing pack). Right panel: black empty log area. Purpose: CJK (Chinese-Japanese-Korean) language pack generation tool for MEGA-GUARD TFT and EAS panels.

The application will support all Chinese, Japanese or Korean glyphs up until UTF-8 range 0xFFFF with a maximum character list of 1000 unique characters due to memory restrictions.

### 9.2.2 When to use CJK EAS TFT Support Application

The application will only know which characters to generate for the language packs after a system has been configured. Please run this application when all configurations to the system has been made.

The application should also be run whenever descriptions in the configuration have been altered or there seem to be absent characters within a TFT or EAS panel. Absent characters can be determined within the TFT panel when “” character is displayed, or when a non-coherent character is displayed on the EAS panel. The application should also be run after configuring 1131G in order to generate proper mimics.

### 9.2.3 Using CJK EAS TFT Support Application

When the application is launched, ensure that the program is correctly pointed to the System folder. The application should have already detected where the folder is located. If a different folder needs to be used, clicking the “Browse…” button will allow the application to be directed to the proper path.

> **[Vector Diagram — Page 268]** Page 268 documents MEGA-GUARD LOP language generation procedures including Smart Generation, Upload Only modes, and language pack binary file structure.

Text: Smart Generation (section 9.2.1):
'When pressing the Smart Generation dialog, the application will check against the existing network (if applicable) to determine if a fresh language pack needs to be generated. It will search for detectable changes.'
- If no LOP panel installed: only search for applicable changes
- If module 3 installed on same network: check the IP address
- Copy made from console at CN -> END_FOR

Text: Upload Only (section 9.2.3.1):
'Upload Only will not attempt to generate a new language pack. The application will only search for and upload an existing language pack if applicable.'

Text: Language Pack File Locations and Binary File Structure:
1. Language pack binary file: 'Existing.bit' created in Praxis Firmware folder and Praxis Warehouse folder; stores Unicode Siemens log format
2. Binary file: 'ExistingList.bit' stores log
3. If applicable, another folder called 'Includes' containing a bitmap file will be created if the character limit is exceeded

Reset/Horn configuration (referenced): YES = horn stopped by accept button. NO = horn not stopped by accept button.

Page 268 is from section 9.2 ('LOP Language Generation'). The language pack generation system creates binary language files (.bit format) uploaded to MEGA-GUARD EAS LOP hardware panels, enabling localized alarm text display on physical panel LEDs and displays. Smart Generation detects changes and only regenerates when needed; Upload Only skips regeneration.

There will be a section with two tabs, one labelled “EAS” and another “TFT”. Each tab contains 4 buttons similarly labelled between tabs and containing a brief description below it.

When generating a language pack, the application will create a folder in the System\Setup directory. Depending on whether generating a language pack for the EAS or TFT, the folders will be accordingly named “CJKEAS” and “CJKTFT”. Successful generation of a language pack will also create in their respective folders the following:

1. Language Pack binary file.

If creating a language pack for TFT panels, a backup of “lp-cjk.bin” will be created in the Praxis Firmware folder and be replaced by the newly generated language pack.

2. Binary file named “ExistingList.bin” storing Unicode values of the last generated language pack.

3. If applicable another folder called “Excluded” containing a bitmap file will be created should the character limit be exceeded.

#### 9.2.3.1 “Full Generation” and “Generate Only”

If running this application for the first time, this is a good option to begin with. Both options will generate a language pack regardless if the new language pack will contain the same information as the previous one (if applicable). The only exception is if there are no detectable characters to be created. If the application can identify the I.P addresses of each panel, “Full Generation” will also attempt to upload the according language pack files.

#### 9.2.3.2 “Smart Generation”

“Smart Generation” will check against the “ExistingList.bin” file to determine if a new language pack needs to be created. It will then attempt to upload the language pack to the according panels if panel I.P addresses can be determined.

#### 9.2.3.3 “Upload Only”

“Upload only” will not attempt to generate a language pack. The application will only search for and upload language packs to an appropriate panel.

|  | [INFO] Language packs can also be uploaded to a panel by the “Updater” program. |  |
| --- | --- | --- | |

### 9.2.4 Troubleshooting

If the application does not successfully generate a proper language pack, please ensure the following:

1. If running this application for EAS support; language pack “lp-lcd-cjk.bin” should be present within the Firmware folder.

> **[Figure]** Screenshot of Windows Font selection dialog. Font list: MS Gothic (selected/highlighted), MS Mincho, MS PGothic, MS PMinchoG, MS Sans Serif. Font style: Regular (selected). Size: 9. Effects: Strikeout (unchecked), Underline (unchecked). Color: Black. Sample: shows Japanese characters (示めき字幕). Script: Japanese (dropdown, highlighted red box). OK and Cancel buttons. Purpose: Windows font configuration dialog showing Japanese (MS Gothic) font selection, relevant to MEGA-GUARD multi-language support requiring Japanese character display.

2. If running this application for TFT Support; language pack “lp-cjk.bin” should be present within the Firmware folder.

3. Microsoft TrueTypeFonts “SimSun” has to be installed on the working computer.

> **[Figure]** Screenshot of PAL [Main Server] configuration tool showing the Job and Language section selected (Sounds/Language highlighted in blue). Right panel shows: Edit Message field (empty), All Language checkbox (checked), Port field: Name - MIS-Block - Size: 0 (fields). The main window menu bar: File, View, Special, Help. Left tree shows: Channels, Extended Alarm System, Graphics Pages, Groups, Hour Counters, Job and Language (expanded, Sounds/Language selected), Passwords, Printers, Remote Data, Special, Status Texts, System Parameters. Status bar: PAL I/O, Direct I/O, time 17:52. Purpose: showing the language/sounds configuration section in the PAL MEGA-GUARD engineering tool.

## 9.3 Configure workstation and printer font for Japanese

The system is able to display CJK (Asiatic languages such as Chinese / Japanese / Korean) using the “Alt language” language option.

### 9.3.1 Display Japanese by setting Alternate Font in PAL

To display it is required to set the Alternate Font to MS Gothic and script to Japanese

In PAL select the “Job and Language” branch. Next select “General Settings”. On the right hand dialog switch on the “Use Alt Language” check box.

The Font must be set to MS Gothic with script Japanese. The Font name might differ depending on the regional settings.

### 9.3.2 Print Japanese by setting Alternate Font in PAL

To print it is required to set the Alternate Font to MS Gothic and script to Japanese:

In PAL select Printers branch. Next select the printer in this branch that must print Japanese. WinPrint.dll is required as printer driver. The brand and share name of your printer may differ from the example on the right.

Configure the Code page 932 – Japanese and the Font at the bottom of the page to “MS Gothic” with Script setting to Japanese.

### 9.3.3 Input Japanese by setting Regional settings in Windows

Via Control Panel > Regional Settings the following dialogs must be configured accordingly to use Japanese:

> **[Figure]** Screenshot of PAL [Main Server] configuration tool showing Printer settings. Left tree: Printers > Printer-01 (selected). Right panel: Printer Driver: \[ELTSE175\SM-LBD262]\OX[series Printer (dropdown); Printer Name: Brother HL-LBD26]N series Printer (dropdown); Timer Format: (field); Detail on New Page: Number of descriptions per area per header; Use Printer Pocket: Use tabs Text with WinPrint. Use full Language as Printer: Use Suite Printer As Headers (checkboxes). Code Page: Japanese (JIS) (dropdown). Large section with checkboxes: Use Color of new Alarm Line, Use Bold Font of new Alarm Line, Number of Seconds before Printing: 5640.0, Number of Alarms per Page: 25, Use 2nd Line Printer with WinPrint, Use SM/F (network pointer) checkbox. Font button. Bottom: Warning text in red (alarm printer configuration note), status bar: PAL MBJ, Direct PS, time 17:37. Purpose: PAL printer driver configuration for alarm hardcopy printing in MEGA-GUARD.

Notice that additional settings may be required to use proper keyboard layout.

# 10 NETWORK CONFIGURATION

## 10.1 Overview

MEGA-GUARD system has an internal network that connects Workstations to the Control Processor via an Ethernet Fieldbus. This consists of looped network configurations controlled by RSTP for redundancy. RSTP = Rapid Spanning Tree Protocol.

This internal network may not be connected to external (3th party, non MEGA-GUARD) devices. If this is required then read in next paragraphs how this must be constructed.

> **[Figure]** System architecture diagram showing the MEGA-GUARD shipboard automation network topology. Full-width diagram spanning Cargo Room (left), Bridge (center), Accommodation (center), and Engine Room (right). Bridge zone shows six operator workstations (two labeled Operator Workstation/Cargo Control Room, one Operator Workstation, two Operator Workstation/Bridge, two Operator Workstation/Engine Control Room) connected via a horizontal network bus. Ship icon is shown in the Bridge area with Internet Switch connectivity. Cargo Room: DPU (distributed processing unit) with I/O, Power Control System. Accommodation: multiple EAS Operator Panels (six units) connected to the network via Hubs. Engine Room: two DPUs with I/O. Reference scale markers: 1:10 (cargo side) and 1:5 (engine side) at bottom corners. Labels for each zone with vertical dividers. Purpose: system-level network topology overview of the MEGA-GUARD integrated ship automation system.

## 10.2 Connection to Internet

To connect the network to Internet for remote Monitoring or Service an Ship View MarinePC is used in above configuration. Link A is connected to the MEGA-GUARD internal network, Link B is connected to an external network with access to the internet. This link is shielded with firewall and does not allow any connection from external to the ShipView MPC. The software in the ShipView PC makes a secure connection directly to the ShipView Internet (Cloud) Server.

## 10.3 Connection to external devices

For exchanging data external (3th party, non MEGA-GUARD) devices must be connected to the MEGA-GUARD system this must be done with several provisions: External systems should only be able to communicate to the MEGA-GUARD component that is used for I/O (Remote Data Plugins). This can be achieved by placing VLAN configuration in the network switch or Control Processor unit. External systems may not be connected redundantly or they may not forward data to a second (redundant) connection.

The VLAN options in the control processor (XP) must be switched on for port C and D. The external device can be connected to Ethernet port C or D and will only be able to communicate to the XP, not to other devices that are connected via port A and B. The External devices must be checked to only send exchange data to the XP. No other data is allowed. The XP will disregard this data.

## 10.4 MarinePC/PanelPC Redundant network

The MPC’s are equipped with two Ethernet connections ports and the software uses UDP and TCP/IP for communication with static IP addresses. The first Ethernet port is connected to the main network; the second board is connected to the backup network. Rednetwork is the Windows application that manages the redundant network. This application creates a third “communication” network by adding an extra IP address to the main or backup network.

This communication network is used by the applications. For this reason we call the IP addresses of the communication network communication IP’s. Under normal conditions the communication IP is added to the main (primary) network. If there are problems with the primary network, the redundant network application will switch the communication IP to the backup (secondary) network.

The status of the networks is send to the IOServer to generate failure diagnostics. To check the status of the main and backup network the application uses the static IPs (configured in Windows).

To install the redundant network application you have to do the following: • Initialization with rednetwork.exe • Change Windows IP settings • Start rednetwork.exe

## 10.5 Configurate rednetwork.exe

Start the rednetwork.exe application in the “BIN” directory. If the application cannot find the configuration settings (see next paragraph) the initialize dialog will be launched:

> **[Figure]** Screenshot of Rednetwork.ini file settings dialog. Fields: Nr of Switches: 2, Nr of Servers: 2 (highlighted blue), Nr of Clients: 5. Pri. Subnet: 192.168.1, Sec. Subnet: 192.168.2, Com. Subnet: 192.168.0. Mask: 255.255.255.0. Ping Delay: 200ms, Filter Samples: 3. Table: server 1 (pri 192.168.1.1, sec 192.168.2.1, comm 192.168.0.1), server 2 (192.168.1.2, .2.2, .0.2), clients 1-5 (192.168.1.11-15, .2.11-15, .0.11-15). Purpose: MEGA-GUARD redundant network configuration for dual-server/5-client system with primary, secondary, and communication subnets.

In the grid in the middle the ip addresses of each adapter is configured. Rednetwork will check all IP addresses of the network interfaces until it finds these IP’s, and it will add the communication IP to one of the networks. The other options are described here:

• Nr of Switches: Enter the number of switches in the project. • Nr of Servers: setup number of servers in the project • Nr of Clients: setup number of clients in the project • Pri. Subnet, Sec. Subnet, Com. Subnet and Mask: At Pri, Sec and Com. Subnet and Mask for the IP subnet’s for the 3 networks (Main, Backup and Communication). • Use Gateway: Enables use for redundant communication with external devices. • Gateway: Input address of router for redundant communication with external devices. • (ms) Ping Delay: Default for ping delay: time in between 2 ping tests. • SNMP Delay: Time for switching from one network to other. Setup to 30 seconds to prevent for false network alarms. • Filter Samples: Determine when network switch will occur. In case of an error on the main Rednetwork will switch after 3 filter samples (ping) with 200 ms ping delay. This will take 400 milliseconds (sample, delay, sample, delay, sample). After switching

> **[Vector Diagram — Page 274]** Page 274 documents the MEGA-GUARD OWS Rednetwork (redundant network) configuration settings and Windows network adapter IP setup for OWS redundant communication.

Rednetwork Configuration Parameters Table. Type: Configuration reference table. Parameters with descriptions:
- Auto start: Enables Rednetwork connection at computer startup
- Com_IP_Enable/Disable: Shows button to enable or disable the communication IP
- Disable com on all shutdown: Disables communication IP when clicking shutdown command
- Multiple Clients on same computer: Maximum number of OWS clients that can run on one computer (default: 1)
- Shutdown allowed: Whether the Shutdown dialog appears; if set, can appear on mimic page
- Set minutes shutdown: Time in minutes for automatic shutdown timeout
- Status dialog: Shows/hides network status dialog on the mimic
- Local time on shutdown dialog: Show local time (as opposed to ship time)
- Remote Data GUI: Enable Remote Data GUI connection
- Status text: Min text which is applied during status display

Network Configuration Diagram: IP Address Assignment Table. Type: Wiring/configuration diagram. Shows computer name and IP address table:
- Columns: Computer Name | IP address Main network (Primary) | IP address backup network (Secondary)
- Each OWS computer has both a primary and a secondary/backup IP address

Rednetwork Description text: 'Rednetwork will continue to check the main network, and switch back as soon as it is working again.' 'Auto start: Enables Rednetwork connection at computer startup.'

Page 274 is from section 10.5 ('Change Rednetwork configuration'). Rednetwork provides Ethernet redundancy for MEGA-GUARD OWS, maintaining backup IP address connections to XP processors, ensuring continuous monitoring if primary network fails.

Rednetwork will continue to check the main network, and switch back as soon as it is working again. • Auto start: Enables Rednetwork startup at computer startup. Changes registry, write to disk required (see EWF).

• System menu access: status dialog shows system management button on the status dialog. • Com IP Enable/Disable button: Shows the button to enable or disable the communication IP in the runtime dialog. • Disable com IP at shutdown: Removes Communication IP when closing system from Rednetwork dialog. • Multiple Clients on same computer: Check if more then 1 CamClient.exe are running on a workstation. This can occur if multiple systems are used, or if multiple screens are connected to the workstation. • Nr of multiple clients: Number of CamClient that will run on the workstation. Default is 1, and for 2 screens 2 is advised. • Show shutdown buttons: option will show system buttons in the system management menu (it is possible to hide them to prevent stations from stopping the system). • Shutdown allowed: Shows button in Rednetwork to stop the system. This also enables other applications to do a system shutdown by signaling rednetwork.exe • Sets event at shutdown: signals third party software to not start the CAMclient. • Shutdown delay: Wait time before closing IOServer.

If the application should startup automatically at log on check the checkbox “Auto start” at the left bottom of dialog (4th from bottom). Click on OK to save the settings and close initialization.

### 10.5.1 Change Rednetwork configuration

Rednetwork checks the registry where the program is installed and finds the Rednetwork configuration file via the Path.ini in the program directory. To change Rednetwork configuration after first initialization a shortcut can be created with the special “/init” argument. For example use Windows Start menu and Run option with this command:

D:\Software\System\Bin\Rednetwork.exe /init

Starting this will show the dialog in the previous paragraph.

### 10.5.2 Configure IP settings of Windows

Each MPC has two network cards which should both be configured according the following table:

| Computer Name | IP address Main network (Primary) | IP address backup network (Secudary) |
| --- | --- | --- | |

| Server_1 | 192.168.1.101 | 192.168.2.101 |
| --- | --- | --- | |
| Server_2 | 192.168.1.102 | 192.168.2.102 |
| Client_1 | 192.168.1.111 | 192.168.2.111 |
| Client_n (n = 10 + client nr) | 192.168.1.100 + n | 192.168.1.100 + n |

The IP of the main network adapter matches with the IP in the Primary IP column of the rednetwork dialogs. The IP of the backup network adapter matches with the IP for this computer in the Secondary IP column. RedNetwork.exe uses the IPs of the adapters to determine which server or client this computer is.

> **[Figure]** Screenshot of Windows 'Network and Dial-up Connections' control panel with 'Local Area Connection 2 Properties' and 'Internet Protocol (TCP/IP) Properties' dialog open. IP settings: Use the following IP address: 192.168.2.70, Subnet mask: 255.255.255.0, Default gateway: (empty). DNS servers both empty. Purpose: Windows TCP/IP configuration for the secondary network adapter of a MEGA-GUARD workstation, showing IP 192.168.2.70 on subnet 192.168.2.x.

In the following picture is shown how to configure Windows network:

Use a static (fixed) IP address with the “Use the following IP address” option.

|  | If the computer has only 1 network interface it is possible to add both (main and backup) IP |  |
| --- | --- | --- | |
|  | addresses to this device via the “Advanced” option. In Rednetwork this will appear as a |  |
|  | redundant system. |  |

After configuring the rednetwork.exe has to be started. It is recommended to check the configuration status in the status information dialog.

## 10.6 The icon on the taskbar

The redundant network application will appear as an icon in the taskbar. Figure 8 shows the icon on the taskbar (The redundant network icon is encircled). The color off the icon shows the connection of the communication IP.

Figure 8 Communication IP not added to an adapter

Communication IP added to Main adapter (Icon is black)

Communication IP added to Backup adapter (Icon is red)

### 10.6.1 The popup menu

When you press your right mouse button above the redundant network Icon you get the popup menu.

## 10.7 The Status information dialog

The redundant network application can show a status information dialog. You can call up this dialog in several ways. The first one is choosing “Redundant Network Status” in the popup menu. The second possibility is double click with the left mouse button on the Icon on the taskbar. The last possibility is typing “NWD” in the debug window of the CamClient. These options show the status information dialog:

> **[Figure]** Screenshot of the MEGA-GUARD System Management dialog. Table shows four computers with status columns CAMclient running and IOserver running: Server 1 (Unknown, Unknown - highlighted in red), Server 2 (Yes, Yes), Client 1 (Yes, No), Client 2 (Unknown, Unknown - greyed). Annotation above table: System management could not reach Server 1 and Client 2 (with arrows pointing to those rows). Buttons at bottom: System shutdown, System startup, Close CAMClient on this computer, Start CAMClient on this computer. OK button top right. Purpose: MEGA-GUARD system management console showing network status of distributed alarm management servers and clients, with unreachable nodes indicated.

### 10.7.1 System management dialog

> **[Figure]** Screenshot of MEGA-GUARD 'Status information Redundant network' diagnostic dialog. Header: 'Configured as Client 3, Com IP=192.168.0.70'. Table: Computer, Pri IP, Status Pri IP, Sec IP, Status Sec IP, Com IP, Status Com IP. Rows: Server 1 (192.168.1.1 NOT ok, 192.168.2.1 NOT ok, 192.168.0.1 OK), Server 2 (similar), Client 1 (192.168.1.11 not ok), Client 2 (192.168.1.12 OK, 192.168.2.12 OK), Client 3 (192.168.1.70 OK, 192.168.2.70 OK, 192.168.0.70 Added to primary). Configuration status: Status-OK. Main network adapter MAC 00:10:60:7E:84:88, IP 192.168.1.70. Backup network adapter IP 192.168.2.70. Purpose: MEGA-GUARD redundant network status diagnostic showing primary/secondary/communication network health for all nodes.

Redundant network supports a system management dialog, which you can use to see at which computer a CAMClient or IOServer is running. The dialog also has a general system shutdown feature to shut down the complete system. The system management dialog is shown in the following picture:

> **[Vector Diagram — Page 278]** Page 278 documents MEGA-GUARD OWS Windows event logging entries for Rednetwork service events, with event types, storage flags, and solutions.

Text: Section 10.8 ('Event logging') - events generated by MEGA-GUARD Rednetwork service, viewable in Windows Event Viewer.

Windows Event Log Entries Table. Type: Troubleshooting reference table. Columns: Event, Event type, Storage (Yes/No), Solution.

Documented events:
- Start Rednetwork: Type=Information. When Rednetwork started by system management or restart. Action: Initialize network adapters.
- Rednetwork installed: Type=Information. Network installed successfully.
- IRQ Interrupt Routine Queue: Type=Information.
- Event/Event Max: Type=Information.
- Rednetwork connection is disabled: Type=Warning. When Rednetwork over is network (IP adapter). The disabling of the communication IP is done at startup. Do not disable unless unwanted communication IP.
- IP adapter not found in registry: Type=Error, Storage=Yes. Solution: Registry settings are not correct.
- IP adapter not found in registry (ERR): Type=Error, Storage=Yes. Solution: Registry settings are not correct.
- IP adapter configuration match not found in registry: Type=Error, Storage=Yes. Solution: Registry settings are not correct.
- XML The primary IP of this panel is different from XP IP registry: Type=Error, Storage=Yes. Solution: Change the IP in the Windows 'Network and Connection' dialog.
- XML The primary IP of this panel is different from XP IP (ERR): Type=Error, Storage=Yes. Solution: Change IP in Windows TCP/IP settings or change IP in XP.

Page 278 is from section 10.8 ('Event logging'). These Windows event log entries from the MEGA-GUARD Rednetwork service help engineers diagnose network connectivity issues between OWS and XP processors.

## 10.8 Event logging and trouble shooting

### 10.8.1 Event logging

The application logs several events in the Windows event log. These events you can see in the “event viewer” application. The events are logged in the Application log.

The following events are logged:

| Event | Event type | Message box | Occurs |
| --- | --- | --- | --- | |
| Start RedNetwork | Information | - | When the RedNetwork.exe is started automatically or by a user. |
| RedNetwork initialized | Information | - | RedNetwork initialization is done. |
| RedNetwork initialize cancelled | Information | - | RedNetwork initialization is cancelled by the user. |
| RedNetwork closed | Information | - | When the RedNetwork.exe is closed by the user |
| RedNetwork already started | Warning | - | When the RedNetwork.exe detects that the application is already started. The second instance will be closed automatically |
| Could not configure as Server or Client | Warning | - | The IP of the main network adapter does not match with any primary IP in the registry and the IP of the backup adapter does not match with any secondary IP |
| Sockets init failed | Error | Yes | The application could not start because the initialization of sockets failed. This means that there are serious problems with the installation of Windows NT/2000. |
| PrimaryIP of servers\serverX not found in registry | Error | Yes | Registry settings are not correct |
| SecundaryIP of servers\serverX not found in registry | Error | Yes | Registry settings are not correct |
| CommunicationIP of servers\serverX not found in registry | Error | Yes | Registry settings are not correct |
| PrimaryIP of Clients\ClientX not found in registry | Error | Yes | Registry settings are not correct |
| SecundaryIP of Clients\ClientX not found in registry | Error | Yes | Registry settings are not correct |
| CommunicationIP of Clients\ClientX not found in registry | Error | Yes | Registry settings are not correct |
| IP conflict found in registry (IP:xx.xx.xx.xx) Conflict betweem pri/sec/com IP of ClientX/ServerX and pri/sec/com IP of ClientY/ServerY | Error | Yes | Dupplicate IPs in registry settings |
| Registry settings network adapters in HKEY_LOCAL_MACHINE are not found or incorrect | Error | Yes | Registry settings of network adapters are not found or incorrect |

> **[Vector Diagram — Page 279]** Page 279 documents continued MEGA-GUARD Rednetwork error events and the Problems and Solutions troubleshooting table for Rednetwork communication issues.

Rednetwork Error Status Table (continuation from page 278). Type: Troubleshooting reference table. Additional event entries:

- XML: The adapter in registry is found as adapter (IP) not found in registry: Type=Error, Storage=Yes. Solution: Registry settings are not correct.
- XML: The IP of the primary panel is different from the XP IP in registry: The IP of this panel is different from the XP IP: Type=Error, Storage=Yes. Solution: Change the IP in Windows 'Network and Connection' dialog.
- XML: The primary IP of this panel is different from XP IP (secondary): The IP address: Type=Error, Storage=Yes. Solution: Change IP in Windows TCP/IP settings or change IP in XP.
- XML: Pin the primary IP to the DIN of this panel to the adapter (IP): Type=Error, Storage=Yes. Solution: Change IP in Windows TCP/IP settings.

Problems and Solutions Table (section 10.8.2). Type: Troubleshooting guide.

Problem: The communication IP is disabled.
Solution: Start from the system management dialog. The disabling of the communication IP is done at startup. Reset the computer or initialize network adapters (Windows XP: restart the computer).

Problem: The communication IP is not added to an adapter (connection is grey).
Solution steps:
1. Check Configuration status in the 'Network and Internet connection' dialog of Windows.
2. Check if the network adapter with the same network (IP) is installed.
3. If not found: install the network adapter in Windows again.
4. Change the IP in Windows TCP/IP settings or change the IP in the network.

Additional Problem: Communication IP not added to adapter (second scenario).
Solution:
1. Application crashes/non-start because main network (IP) is not the same. Reinstall and disable; configure settings for Windows again.
2. Shut down Windows, RESTART and try again.
3. Communication IP disabled by general system pulldown. Try in OWS information dialog - there will be a line 'con disabled'.

Page 279 is from section 10.8.2 ('Problems and solutions'). Helps MEGA-GUARD engineers and service technicians diagnose and resolve Rednetwork IP address configuration issues on the OWS Windows computer.

### 10.8.2 Error status table

| Error | Solution |
| --- | --- | |
| ERR: The primary adapter in the registry is not found in the computer | Initialize the network adapters again |
| ERR: The secondary adapter in the registry is not found in the computer | Initialize the network adapters again |
| ERR: Number of adapters in registry not equal to number of adapters in computer | A network adapter is added or removed. Initialize the network adapters again |
| ERR: Adapters in registry are not equal to adapters in computer | A network adapter is replaced by an other. Initialize the network adapters again |
| ERR: The IP of the secondary adapter is different from IP in the registry | Change the IP in the windows TCP/IP settings or change the IP in the registry |
| ERR: The IP of the primary adapter is different from IP in the registry | Change the IP in the windows TCP/IP settings or change the IP in the registry |
| ERR: Adapter IPs not found in client server configuration in the registry. COULD NOT START ALGORITM | Change the IPs in the windows TCP/IP settings or change the IP in the registry |

### 10.8.3 Problems & solutions

| Problem | Solution |
| --- | --- | |
| The communication IP is disabled | Start the System from the system management dialog or restart rednetwork.exe. The disabling of the communication IP is done at shutting down the system from the system management dialog. If you don’t want this, initialize rednetwork and change settings (see previous chapter) |
| The communication IP is not add to an adapter (Icon is gray) | There are some reasons to do not add the communication IP. 1. There are configuration errors. Check Configuration status in the status dialog 2. There was an error during adding the communication IP, because the IP already exist. Disable the network adapters in the “Network and Dial-up connection” dialog of Windows and enable them again. (Windows NT, restart the computer). This problem occurs when you End the rednetwork.exe process by the Windows task manager. 3. The communication IP is disabled by the general system shutdown. You can check this on the status information dialog. There will be a line “Com IP disabled”. |

# 12 APPENDIX ALARM HANDLING AND REPORT

The alarm handling and presentation of the alarms on the Alarm Page or in an Alarm Window should be according to the following specifications:

Class Rule and Regulation changes of Lloyds Register July 2012; Part 6, Chapter 1 item 2.3.3: Alarms and warnings associated with machinery and equipment required to satisfy this sub- Section are to be categorised according to the urgency and type of response required by the crew, as described in the IMO Code on Alerts and Indicators, 2009. The assignment of a category to each alert is to be evaluated on the basis not only of the machinery or equipment being monitored, but also the complete installation. Categories not included in an alarm system may be omitted from the system design.

Resolution MSC.302(87) (adopted on 17 May 2010). Adoption of Performance Standards for Bridge Alert Management: Module A - Presentation and handling of alerts on the bridge. Module B – Central alert management (CAM) functionality.

IMO Resolution A.1021(26); Adopted on 2 December 2009 (Agenda item 10):

## 12.1 Code on Alerts and Indicators, 2009

### 12.1.1 Definitions

Alert: Alerts announce abnormal situations and conditions requiring attention. Alerts are divided in four priorities: emergency alarms, alarms, warnings and cautions.

• Emergency alarm: An alarm which indicates that immediate danger to human life or to the ship and its machinery exists and that immediate action should be taken. • Alarm: An alarm is a high priority of an alert. Condition requiring immediate attention and action, to maintain the safe navigation and operation of the ship. • Warning: Condition requiring no immediate attention or action. Warnings are presented for precautionary reasons to bring awareness of changed conditions which are not immediately hazardous, but may become so if no action is taken. • Caution: Lowest priority of an alert. Awareness of a condition which does not warrant an alarm or warning condition, but still requires attention out of the ordinary consideration of the situation or of given information.

## 12.2 Alarms within a certain Alert priority (Report Type)

### 12.2.1 Emergency Alarms

If an Emergency Alarm occurs the system should initiate an audible signal, accompanied by the visual (flashing) alarm announcement. The audible signal can be stopped by a Stop Horn action. The visual (flashing) alarm announcement will become a steady visual alarm announcement by

issuing an Acknowledgement Action. The visual alarm announcement will disappear as soon as the cause of the alarm is rectified.

Following alarms must be included: • General emergency alarm. An alarm given in the case of an emergency to all persons on board summoning passengers and crew to assembly stations. • Fire alarm. An alarm to summon the crew in the case of fire. • Water ingress detection main alarm. An alarm given when the water level reaches the main alarm level in cargo holds or other spaces on bulk carriers or single hold cargo ships. • Those alerts giving warning of immediate personnel hazard, including: o Fire-extinguishing pre-discharge alarm. An alarm warning of the imminent release of fire- extinguishing medium into a space. o Power-operated sliding watertight door closing alarm. An alarm required by SOLAS regulation II-1/15.7.1.6, warning of the closing of a power-operated sliding watertight door. • For special ships (e.g., high-speed craft), additional alarms may be classified as emergency alarms in addition to the ones defined above.

### 12.2.2 Alarms

If an Alarm occurs the system should initiate an audible signal, accompanied by the visual (flashing) alarm announcement. The audible signal can be stopped by a Stop Horn action. The visual (flashing) alarm announcement will become a steady visual alarm announcement by issuing an Acknowledgement Action. The visual alarm announcement will disappear as soon as the cause of the alarm is rectified.

• Machinery alarm. An alarm which indicates a malfunction or other abnormal condition of the machinery and electrical installations. • Steering gear alarm. An alarm which indicates a malfunction or other abnormal condition of the steering gear system, e.g., overload alarm, phase failure alarm, no- voltage alarm and hydraulic oil tank low-level alarm. • Control system fault alarm. An alarm which indicates a failure of an automatic or remote control system, e.g., the navigation bridge propulsion control failure alarm. • Bilge alarm. An alarm which indicates an abnormally high level of bilge water. • Water ingress detection pre-alarm. An alarm given when the water level reaches a lower level in cargo holds or other spaces on bulk carriers or single hold cargo ships. • Engineers’ alarm. An alarm to be operated from the engine control room or at the maneuvering platform, as appropriate, to alert personnel in the engineers’ accommodation that assistance is needed in the engine-room. • Personnel alarm. An alarm to confirm the safety of the engineer on duty when alone in the machinery spaces. • Bridge Navigational Watch Alarm System (BNWAS). Second and third stage remote audible alarm as required by resolution MSC.128(75).

• Fire detection alarm. An alarm to alert the crew in the onboard safety center, the continuously manned central control station, the navigation bridge or main fire control station or elsewhere that a fire has been detected. • Fixed local application fire-extinguishing system activation alarm. An alarm to alert the crew that the system has been discharged, with indication of the section activated. • Alarms indicating faults in alert management or detection systems or loss of their power supplies. • Cargo alarm. An alarm which indicates abnormal conditions originating in cargo, or in systems for the preservation or safety of cargo. • Gas detection alarm. An alarm which indicates that gas has been detected. • Power-operated watertight door fault alarms. Alarms which indicate low level in hydraulic fluid reservoirs, low gas pressure or loss of stored energy in hydraulic accumulators, and loss of electrical power supply for power-operated sliding watertight doors. • Navigation-related alarms as specified in the Revised Performance Standards for Integrated Navigation Systems (INS) (resolution MSC.252(83), appendix 5). • For special ships (e.g., high-speed craft), additional alerts may be classified as alarms in addition to the ones defined above.

### 12.2.3 Warning

If a Warning occurs the system should initiate a momentarily audible signal, accompanied by the visual (flashing) alarm announcement. The audible signal will be stopped automatically after a period of 2 seconds. The visual (flashing) alarm announcement will become a steady visual alarm announcement by issuing an Acknowledgement Action. The visual alarm announcement will disappear as soon as the cause of the alarm is rectified.

#### 12.2.3.1 Alert escalation

The alert escalation should be compliant with the alert escalation requirements of the individual performance standards. An unacknowledged Warning should be: Changed to Alarm priority after a limited time period not exceeding 5 min.

Refer to chapter 10 Alert and Indicator Locations of IMO Resolution A.1021(26); Adopted on 2 December 2009.

### 12.2.4 Caution

If a Caution occurs the system should initiate a visual steady alarm announcement. The visual alarm announcement will disappear as soon as the cause of the alarm is rectified.

Refer to chapter 10 Alert and Indicator Locations of IMO Resolution A.1021(26); Adopted on 2 December 2009.

# 13 APPENDIX PANELPC CONFIGURATION

It is possible to control dimming via Serial Port. Configure PanelPC.INI as in this sample:

# The PanelPC Application # # By Passing the following NMEA message to one # of the COM ports the dimming value can be # controlled. # # Please note the dimming level in the message # equals the actual dimming value +1. # # $--DDC,a,xx,a,a*hh<CR><LF> # | | | | | | # | | | | | *6A Checksum data # | | | | Sentence Status Flag (see Note 4) # | | | Colour palette (see Note 3) # | | Brightness percentage 00 to 99 (see Note 2) # | Display dimming preset (see Note 1) # RMC Recommended Minimum sentence C

[Settings] OnScreenDisplay=1 UseMegaGuardDim=0 UseVirtualComPort=0 LocalTCPLogging=0 UseInverseDimming=0

## REPORTDIAGNOSTICS=0

#INI File GPIO Service [Virtual_COMPort] Port=9 Baud=4800 Databits=8 Parity=0 StopBits=1 HandShake=1 TimeOut=10000

[EXT_COMPort] Enable=1 Port=1 Baud=4800 Databits=8 Parity=0 StopBits=1 TimeOut=1000

[SERVER_1-Specific] SyncDimmingToGroup=0 SyncLocalDimmingToGroup=0 DimmingGroup=0

[SERVER_2-Specific] SyncDimmingToGroup=0 SyncLocalDimmingToGroup=0 DimmingGroup=0

[Preset] Day=75 Dusk=50 Dawn=10

# 14 DOCUMENT INFORMATION

Naming Conventions: Name of the Product Line: MEGA-GUARD SERIES Product Name MEGA-GUARD Operator Workstation: OWS Operator Workstation: OWS I/O Server: I/O-Ser
