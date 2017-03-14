init_workbook = '''import xlsxwriter
import time

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('VIS-TestCaseCollection_report.xlsx')
worksheet = workbook.add_worksheet("VIS Test Case Summary")
worksheet.set_column(0, 10, 15)
VIS001sheet = workbook.add_worksheet("VIS001")
VIS001sheet.set_column(0, 0, 10)
VIS001sheet.set_column(1, 1, 40)
VIS001sheet.set_column(2, 2, 10)
VIS001sheet.set_column(3, 3, 40)
VIS001sheet.set_column(4, 4, 10)
VIS001sheet.set_column(5, 5, 15)
VIS001sheet.set_column(6, 4, 20)
VIS002sheet = workbook.add_worksheet("VIS002")
VIS002sheet.set_column(0, 0, 10)
VIS002sheet.set_column(1, 1, 40)
VIS002sheet.set_column(2, 2, 10)
VIS002sheet.set_column(3, 3, 40)
VIS002sheet.set_column(4, 4, 10)
VIS002sheet.set_column(5, 5, 15)
VIS002sheet.set_column(6, 4, 20)
VIS003sheet = workbook.add_worksheet("VIS003")
VIS003sheet.set_column(0, 0, 10)
VIS003sheet.set_column(1, 1, 40)
VIS003sheet.set_column(2, 2, 10)
VIS003sheet.set_column(3, 3, 40)
VIS003sheet.set_column(4, 4, 10)
VIS003sheet.set_column(5, 5, 15)
VIS003sheet.set_column(6, 4, 20)
VIS004sheet = workbook.add_worksheet("VIS004")
VIS004sheet.set_column(0, 0, 10)
VIS004sheet.set_column(1, 1, 40)
VIS004sheet.set_column(2, 2, 10)
VIS004sheet.set_column(3, 3, 40)
VIS004sheet.set_column(4, 4, 10)
VIS004sheet.set_column(5, 5, 15)
VIS004sheet.set_column(6, 4, 20)
VIS005sheet = workbook.add_worksheet("VIS005")
VIS005sheet.set_column(0, 0, 10)
VIS005sheet.set_column(1, 1, 40)
VIS005sheet.set_column(2, 2, 10)
VIS005sheet.set_column(3, 3, 40)
VIS005sheet.set_column(4, 4, 10)
VIS005sheet.set_column(5, 5, 15)
VIS005sheet.set_column(6, 4, 20)
VIS006sheet = workbook.add_worksheet("VIS006")
VIS006sheet.set_column(0, 0, 10)
VIS006sheet.set_column(1, 1, 40)
VIS006sheet.set_column(2, 2, 10)
VIS006sheet.set_column(3, 3, 40)
VIS006sheet.set_column(4, 4, 10)
VIS006sheet.set_column(5, 5, 15)
VIS006sheet.set_column(6, 4, 20)
VIS007sheet = workbook.add_worksheet("VIS007")
VIS007sheet.set_column(0, 0, 10)
VIS007sheet.set_column(1, 1, 40)
VIS007sheet.set_column(2, 2, 10)
VIS007sheet.set_column(3, 3, 40)
VIS007sheet.set_column(4, 4, 10)
VIS007sheet.set_column(5, 5, 15)
VIS007sheet.set_column(6, 4, 20)
VIS008sheet = workbook.add_worksheet("VIS008")
VIS008sheet.set_column(0, 0, 10)
VIS008sheet.set_column(1, 1, 40)
VIS008sheet.set_column(2, 2, 10)
VIS008sheet.set_column(3, 3, 40)
VIS008sheet.set_column(4, 4, 10)
VIS008sheet.set_column(5, 5, 15)
VIS008sheet.set_column(6, 4, 20)
VIS009sheet = workbook.add_worksheet("VIS009")
VIS009sheet.set_column(0, 0, 10)
VIS009sheet.set_column(1, 1, 40)
VIS009sheet.set_column(2, 2, 10)
VIS009sheet.set_column(3, 3, 40)
VIS009sheet.set_column(4, 4, 10)
VIS009sheet.set_column(5, 5, 15)
VIS009sheet.set_column(6, 4, 20)
VIS010sheet = workbook.add_worksheet("VIS010")
VIS010sheet.set_column(0, 0, 10)
VIS010sheet.set_column(1, 1, 40)
VIS010sheet.set_column(2, 2, 10)
VIS010sheet.set_column(3, 3, 40)
VIS010sheet.set_column(4, 4, 10)
VIS010sheet.set_column(5, 5, 15)
VIS010sheet.set_column(6, 4, 20)


normal = workbook.add_format()
normal.set_text_wrap()
normal.set_align('top')
normalright = workbook.add_format()
normalright.set_align('right')
bold = workbook.add_format({'bold': True})
bold.set_text_wrap()
bold.set_align('top')
boldbl = workbook.add_format({'bold': True})
boldbl.set_text_wrap()
boldbl.set_align('top')
boldbl.set_bg_color('#ccccFF')
boldblue = workbook.add_format({'bold': True})
boldblue.set_text_wrap()
boldblue.set_bg_color('#ccccFF')
boldcenter = workbook.add_format({'bold': True})
boldcenter.set_align('center')
boldcenter.set_align('top')
boldcenter.set_text_wrap()
boldcenterwhite = workbook.add_format({'bold': True})
boldcenterwhite.set_align('center')
boldcenterwhite.set_text_wrap()
boldcenterwhite.set_font_color('white')
boldcenterwhite.set_bg_color('black')

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

worksheet.merge_range(row, 0, row, 2, "VIS Test Protocol", bold)

row = 2
worksheet.write(row, 0, "Executed by", bold)
worksheet.merge_range(row, 1, row, 2, "Karri Kaksonen", bold)

row = 3
worksheet.write(row, 0, "Executed date", bold)
worksheet.merge_range(row, 1, row, 2, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 5
worksheet.add_table('A6:K34')
worksheet.write(row, 0, "Designed by", boldcenterwhite)
worksheet.write(row, 1, "Design date", boldcenterwhite)
worksheet.write(row, 2, "Title", boldcenterwhite)
worksheet.write(row, 3, "Description", boldcenterwhite)
worksheet.write(row, 4, "Component", boldcenterwhite)
worksheet.write(row, 5, "Testcase ID", boldcenterwhite)
worksheet.write(row, 6, "Main or Variant", boldcenterwhite)
worksheet.write(row, 7, "Link to Detailed", boldcenterwhite)
worksheet.write(row, 8, "Test Data", boldcenterwhite)
worksheet.write(row, 9, "Pass/Fail", boldcenterwhite)
worksheet.write(row, 10, "Finding & Comment", boldcenterwhite)

row = 6
VIS_001_row = row
VIS_001_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Authorize and Publish Voyage Plan", bold)
worksheet.write(row, 3, "Test publish voyage plan and give authorization (access) to chosen identities. Authorized identities (organisations) can request (GET) and subscribe to voyage plans", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 8, "RTZ-001", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 7
VIS_001_3_row = row
VIS_001_3_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan with validityPeriod", bold)
worksheet.write(row, 3, "Publish old voyage plan where validityPeriod has passed", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-3", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 8, "RTZ with different validityPeriods", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 8
VIS_001_4_row = row
VIS_001_4_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan based on different schema versions", bold)
worksheet.write(row, 3, "Publish future voyage plan according to different schema versions", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-4", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 9
VIS_001_5_row = row
VIS_001_5_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish incorrect voyage plan according to schema", bold)
worksheet.write(row, 3, "Publish incorrect voyage plan according to RTZ schema", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-5", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 10
VIS_001_6_row = row
VIS_001_6_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan for another ship", bold)
worksheet.write(row, 3, "Test/show behaviour for VIS if an ship publishes a RTZ for another ship", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-6", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 11
VIS_001_7_row = row
VIS_001_7_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan without UVID and/or status", bold)
worksheet.write(row, 3, "Test/show behaviour of VIS if publishing a voyage plan with no or incorrect vesselVoyage and/or routeStatus", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-7", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 12
VIS_002_row = row
VIS_002_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Request Voyage Plan", bold)
worksheet.write(row, 3, "Test request (get) voyage plan(s)", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-002", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 13
VIS_002_1_row = row
VIS_002_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Test rule “Only 1 voyage plan used for monitoring per ship”", bold)
worksheet.write(row, 3, "Test maintained rule « Only one voyage per ship can be in status « Used for monitoring » (7) when requesting voyage plans", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-002-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 14
VIS_003_row = row
VIS_003_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Subscribe to Voyage Plan", bold)
worksheet.write(row, 3, "Test subscription on voyage plans", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 15
VIS_003_1_row = row
VIS_003_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Subscribe to Voyage Plan – incorrect callback endpoint", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 16
VIS_003_2_row = row
VIS_003_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Subscribe to Voyage Plan – incorrect UVID", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 17
VIS_003_3_row = row
VIS_003_3_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Duplicate subscription requests", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003-3", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 18
VIS_004_row = row
VIS_004_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Remove Subscription to Voyage Plan", bold)
worksheet.write(row, 3, "Remove subscription to the voyage plan(s)", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-004", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 19
VIS_004_1_row = row
VIS_004_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Remove subscription with incorrect parameters", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-004-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 20
VIS_005_row = row
VIS_005_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Upload Voyage Plan", bold)
worksheet.write(row, 3, "Find VIS and send (upload) a voyage plan. No ACK is requested. The STM Module is notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 21
VIS_005_1_row = row
VIS_005_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with ACK request", bold)
worksheet.write(row, 3, "Same as TEST-005 but ACK is requested.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 22
VIS_005_2_row = row
VIS_005_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with ACK request but no STM Module retrieves the message", bold)
worksheet.write(row, 3, "Same as TEST-005-1 but no STM Module receives the message.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 23
VIS_005_3_row = row
VIS_005_3_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with explicit callback endpoint", bold)
worksheet.write(row, 3, "Upload voyage plan (RTZ) with explicit callback endpoint where returned result is expected", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-3", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 24
VIS_005_4_row = row
VIS_005_4_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan for another ship to a ship", bold)
worksheet.write(row, 3, "Test/show the behaviour of VIS if a service provider uploads a voyage plan for another ship than the receiver", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-4", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 25
VIS_006_row = row
VIS_006_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Upload Text Message", bold)
worksheet.write(row, 3, "Test upload text message to VIS. No ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-006", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 26
VIS_006_1_row = row
VIS_006_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Text Message with ACK request", bold)
worksheet.write(row, 3, "Same as TEST-006 but ACK is requested.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-006-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 27
VIS_006_2_row = row
VIS_006_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload TXT message with ACK request but no STM Module retrieves the message", bold)
worksheet.write(row, 3, "Same as TEST-006-1 but no STM Module receives the message.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-006-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 28
VIS_007_row = row
VIS_007_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Upload Area (S-124) Message", bold)
worksheet.write(row, 3, "Test send (upload) area message. No ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-007", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 29
VIS_007_1_row = row
VIS_007_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Area Message with ACK request", bold)
worksheet.write(row, 3, "Test send (upload) area message. ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-007-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 30
VIS_007_2_row = row
VIS_007_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload S124 message with ACK request but no STM Module retrieves the message", bold)
worksheet.write(row, 3, "Same as TEST-007-1 but no STM Module receives the message.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-007-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 31
VIS_008_row = row
VIS_008_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "DEPRECATED - Notification to STM Module", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-008", bold)
worksheet.write(row, 6, "Main", bold)

row = 32
VIS_009_row = row
VIS_009_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Logging in VIS", bold)
worksheet.write(row, 3, "Check log in VIS", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-009", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 33
VIS_010_row = row
VIS_010_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Find Voyage Information Services", bold)
worksheet.write(row, 3, "Test search for voyage information services to consume", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-010", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 0
col = 0
VIS001sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS001sheet.write(row, 1, "Executed by", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS001sheet.write(row, 1, "Executed date", bold)
VIS001sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS001sheet.write(row, 0, "", boldblue)
VIS001sheet.write(row, 1, "Test ID", boldblue)
VIS001sheet.merge_range(row, 2, row, 3, "TEST-VIS-001", boldblue)
VIS001sheet.write(row, 3, "", boldblue)
VIS001sheet.write(row, 4, "", boldblue)
VIS001sheet.write(row, 5, "", boldblue)
VIS001sheet.write(row, 6, "", boldblue)

row = 5
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Main test", normal)

row = 6
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Test publish voyage plan and give authorization (access) to chosen identities. Authorized identities (organisations) can request (GET) and subscribe to voyage plans. ", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F12:F23, "PASS")', normalright)

row = 8
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F12:F23, "FAIL")', normalright)

row = 9
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F12:F23, "NOT EXECUTED")', normalright)

worksheet.write(VIS_001_row, VIS_001_col, '=VIS001.F7', bold)

VIS001sheet.add_table('A11:G23')

row = 10
VIS001sheet.write(row, 0, "Step#", boldcenterwhite)
VIS001sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS001sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS001sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS001sheet.write(row, 4, "Actual", boldcenterwhite)
VIS001sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_001_00_row = row
VIS_001_00_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "0", boldbl)
VIS001sheet.write(row, 1, "Preparation: No voyage plan published with chosen UVID in VIS-1 - Identify VIS-1 - Identify VIS-2", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_001_01_row = row
VIS_001_01_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Request (get) voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "RTZ-001", boldbl)
VIS001sheet.write(row, 3, "No voyage plans in response", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_001_02_row = row
VIS_001_02_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "2", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No subscription", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_001_03_row = row
VIS_001_03_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "3", boldbl)
VIS001sheet.write(row, 1, "VIS-1: Publish voyage plan with chosen UVID", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
VIS_001_04_row = row
VIS_001_04_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "4", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Request voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received, error message “Not authorized”", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
VIS_001_05_row = row
VIS_001_05_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "5", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No subscription", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
VIS_001_06_row = row
VIS_001_06_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "6", boldbl)
VIS001sheet.write(row, 1, "VIS-1: Authorize organisation for VIS-2 to chosen UVID in VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18
VIS_001_07_row = row
VIS_001_07_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "7", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Request voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Voyage plan received", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 19
VIS_001_08_row = row
VIS_001_08_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "8", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 20
VIS_001_09_row = row
VIS_001_09_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "9", boldbl)
VIS001sheet.write(row, 1, "VIS-1: Remove authorization to organisation for VIS-2", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 21
VIS_001_10_row = row
VIS_001_10_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "10", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Request voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received, error message “Not authorized”", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 22
VIS_001_11_row = row
VIS_001_11_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "11", boldbl)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No subscription", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 23

row = 24

VIS001sheet.write(row, 0, "", boldblue)
VIS001sheet.write(row, 1, "Test ID", boldblue)
VIS001sheet.merge_range(row, 2, row, 3, "TEST-VIS-001-3", boldblue)
VIS001sheet.write(row, 3, "", boldblue)
VIS001sheet.write(row, 4, "", boldblue)
VIS001sheet.write(row, 5, "", boldblue)
VIS001sheet.write(row, 6, "", boldblue)

row = 25
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Variant – Publish voyage plan based on different schema versions", normal)

row = 26
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Test different validity periods in RTZ to show the behaviour in VIS. Presently there is no requirement that VIS shall check the validity period.", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F30>0,"NOT EXECUTED",IF(F29>0,"FAIL","PASS"))', normalright)

row = 27
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F32:F34, "PASS")', normalright)

row = 28
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F32:F34, "FAIL")', normalright)

row = 29
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F32:F34, "NOT EXECUTED")', normalright)

worksheet.write(VIS_001_3_row, VIS_001_3_col, '=VIS001.F27', bold)

VIS001sheet.add_table('A31:G34')
row = 30
VIS001sheet.write(row, 0, "Step#", boldcenterwhite)
VIS001sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS001sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS001sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS001sheet.write(row, 4, "Actual", boldcenterwhite)
VIS001sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 31
VIS_001_12_03_1_row = row
VIS_001_12_03_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "VIS-1: Select VP with validityPeriodStart and validityPeriodStop in past and publish to subscribers ", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Ok, message published and shared", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 32
VIS_001_12_03_2_row = row
VIS_001_12_03_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Change validityPeriodStop to future and publish to VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Ok, message published and shared", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 33
VIS_001_12_03_3_row = row
VIS_001_12_03_3_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Change validityPeriodStart to future and publish to VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Ok, message published and shared", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 34

row = 35
VIS001sheet.write(row, 0, "", boldblue)
VIS001sheet.write(row, 1, "Test ID", boldblue)
VIS001sheet.merge_range(row, 2, row, 3, "TEST-VIS-001-4", boldblue)
VIS001sheet.write(row, 3, "", boldblue)
VIS001sheet.write(row, 4, "", boldblue)
VIS001sheet.write(row, 5, "", boldblue)
VIS001sheet.write(row, 6, "", boldblue)

row = 36
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Variant – Publish voyage plan based on different schema versions", normal)

row = 37
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Test different RTZ schema versions", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F41>0,"NOT EXECUTED",IF(F40>0,"FAIL","PASS"))', normalright)

row = 38
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F43:F45, "PASS")', normalright)

row = 39
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F43:F45, "FAIL")', normalright)

row = 40
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F43:F45, "NOT EXECUTED")', normalright)

worksheet.write(VIS_001_4_row, VIS_001_4_col, '=VIS001.F38', bold)

VIS001sheet.add_table('A42:G45')
row = 41
VIS001sheet.write(row, 0, "Step#", boldcenterwhite)
VIS001sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS001sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS001sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS001sheet.write(row, 4, "Actual", boldcenterwhite)
VIS001sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 42
VIS_001_12_04_1_row = row
VIS_001_12_04_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ 1.0 and publish to VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 43
VIS_001_12_04_2_row = row
VIS_001_12_04_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "2", boldbl)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ 1.1 and publish to VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 44
VIS_001_12_04_3_row = row
VIS_001_12_04_3_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "3", boldbl)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ STM 2.0 and publish to VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 45

row = 46
VIS001sheet.write(row, 0, "", boldblue)
VIS001sheet.write(row, 1, "Test ID", boldblue)
VIS001sheet.merge_range(row, 2, row, 3, "TEST-VIS-001-5", boldblue)
VIS001sheet.write(row, 3, "", boldblue)
VIS001sheet.write(row, 4, "", boldblue)
VIS001sheet.write(row, 5, "", boldblue)
VIS001sheet.write(row, 6, "", boldblue)

row = 47
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Variant – Publish incorrect voyage plan according to schema", normal)

row = 48
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Test error handling in VIS for incorrect RTZ XML and RTZ not according to schema", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F52>0,"NOT EXECUTED",IF(F51>0,"FAIL","PASS"))', normalright)

row = 49
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F54:F55, "PASS")', normalright)

row = 50
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F54:F55, "FAIL")', normalright)

row = 51
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F54:F55, "NOT EXECUTED")', normalright)

worksheet.write(VIS_001_5_row, VIS_001_5_col, '=VIS001.F49', bold)

VIS001sheet.add_table('A53:G55')
row = 52
VIS001sheet.write(row, 0, "Step#", boldcenterwhite)
VIS001sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS001sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS001sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS001sheet.write(row, 4, "Actual", boldcenterwhite)
VIS001sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 53
VIS_001_12_05_1_row = row
VIS_001_12_05_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Select VP in incorrect XML and publish to VIS-1 ", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "STM-Module-1 gets error in response. Log entry in VIS-1", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 54
VIS_001_12_05_2_row = row
VIS_001_12_05_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "2", boldbl)
VIS001sheet.write(row, 1, "Select VP not following schema RTZ  and publish to VIS-1 ", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "STM-Module-1 gets error in response. Log entry in VIS-1", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 55

row = 56
VIS001sheet.write(row, 0, "", boldblue)
VIS001sheet.write(row, 1, "Test ID", boldblue)
VIS001sheet.merge_range(row, 2, row, 3, "TEST-VIS-001-6", boldblue)
VIS001sheet.write(row, 3, "", boldblue)
VIS001sheet.write(row, 4, "", boldblue)
VIS001sheet.write(row, 5, "", boldblue)
VIS001sheet.write(row, 6, "", boldblue)

row = 57
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Variant – Publish voyage plan for another ship", normal)

row = 58
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Test/show behaviour for VIS if an ship publishes a RTZ for another ship", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F62>0,"NOT EXECUTED",IF(F60>1,"FAIL","PASS"))', normalright)

row = 59
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F64:F64, "PASS")', normalright)

row = 60
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F64:F64, "FAIL")', normalright)

row = 61
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F64:F64, "NOT EXECUTED")', normalright)

worksheet.write(VIS_001_6_row, VIS_001_6_col, '=VIS001.F59', bold)

VIS001sheet.add_table('A63:G64')
row = 62
VIS001sheet.write(row, 0, "Step#", boldcenterwhite)
VIS001sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS001sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS001sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS001sheet.write(row, 4, "Actual", boldcenterwhite)
VIS001sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 63
VIS_001_12_06_1_row = row
VIS_001_12_06_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Select VP for another ship and publish to subscribers", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Voyage Plan is published and sent to nominated actors (subscribing actors)", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 64

row = 65
VIS001sheet.write(row, 0, "", boldblue)
VIS001sheet.write(row, 1, "Test ID", boldblue)
VIS001sheet.merge_range(row, 2, row, 3, "TEST-VIS-001-7", boldblue)
VIS001sheet.write(row, 3, "", boldblue)
VIS001sheet.write(row, 4, "", boldblue)
VIS001sheet.write(row, 5, "", boldblue)
VIS001sheet.write(row, 6, "", boldblue)

row = 66
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Variant – Publish voyage plan without UVID and/or status", normal)

row = 67
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.merge_range(row, 2, row, 3, "Test/show behaviour of VIS if publishing a voyage plan with no or incorrect vesselVoyage and/or routeStatus", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F71>0,"NOT EXECUTED",IF(F70>0,"FAIL","PASS"))', normalright)

row = 68
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F73:F76, "PASS")', normalright)

row = 69
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F73:F76, "FAIL")', normalright)

row = 70
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F73:F76, "NOT EXECUTED")', normalright)

worksheet.write(VIS_001_7_row, VIS_001_7_col, '=VIS001.F68', bold)

VIS001sheet.add_table('A72:G76')
row = 71
VIS001sheet.write(row, 0, "Step#", boldcenterwhite)
VIS001sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS001sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS001sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS001sheet.write(row, 4, "Actual", boldcenterwhite)
VIS001sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 72
VIS_001_12_07_1_row = row
VIS_001_12_07_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Select voyage plan with missing vesselVoyage and publish to subscribers", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 73
VIS_001_12_07_2_row = row
VIS_001_12_07_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "2", boldbl)
VIS001sheet.write(row, 1, "Select voyage plan with incorrect syntax of  vesselVoyage and publish to subscribers", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 74
VIS_001_12_07_3_row = row
VIS_001_12_07_3_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "3", boldbl)
VIS001sheet.write(row, 1, "Select voyage plan with missing routeStatus and publish to subscribers", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 75
VIS_001_12_07_4_row = row
VIS_001_12_07_4_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "4", boldbl)
VIS001sheet.write(row, 1, "Select voyage plan with incorrect syntax of  routeStatus and publish to subscribers", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 0
col = 0
VIS002sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS002sheet.write(row, 1, "Executed by", bold)
VIS002sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS002sheet.write(row, 1, "Executed date", bold)
VIS002sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS002sheet.write(row, 0, "", boldblue)
VIS002sheet.write(row, 1, "Test ID", boldblue)
VIS002sheet.merge_range(row, 2, row, 3, "TEST-VIS-002", boldblue)
VIS002sheet.write(row, 3, "", boldblue)
VIS002sheet.write(row, 4, "", boldblue)
VIS002sheet.write(row, 5, "", boldblue)
VIS002sheet.write(row, 6, "", boldblue)

row = 5
VIS002sheet.write(row, 1, "Title", bold)
VIS002sheet.merge_range(row, 2, row, 3, "Test request (get) voyage plan(s)", normal)

row = 6
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 1, "Description", bold)
VIS002sheet.merge_range(row, 2, row, 3, "VIS-1 act as SHIP. VIS-2 act as Service Provider or Shore Centre", normal)
VIS002sheet.write(row, 4, "Total:", normalright)
VIS002sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS002sheet.write(row, 1, "Preconditions", bold)
VIS002sheet.write(row, 4, "Pass:", normalright)
VIS002sheet.write(row, 5, '=COUNTIF(F12:F20, "PASS")', normalright)

row = 8
VIS002sheet.write(row, 1, "Dependencies", bold)
VIS002sheet.write(row, 4, "Fail:", normalright)
VIS002sheet.write(row, 5, '=COUNTIF(F12:F20, "FAIL")', normalright)

row = 9
VIS002sheet.write(row, 4, "Not executed:", normalright)
VIS002sheet.write(row, 5, '=COUNTIF(F12:F20, "NOT EXECUTED")', normalright)

worksheet.write(VIS_002_row, VIS_002_col, '=VIS002.F7', bold)

VIS002sheet.add_table('A11:G20')
row = 10
VIS002sheet.write(row, 0, "Step#", boldcenterwhite)
VIS002sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS002sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS002sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS002sheet.write(row, 4, "Actual", boldcenterwhite)
VIS002sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS002sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_002_00_row = row
VIS_002_00_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "0", boldbl)
VIS002sheet.write(row, 1, "Preparation:Organisation for VIS-2 authorized to exactly one published voyage plan with routestatus=7 and chosen UVID", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_002_01_row = row
VIS_002_01_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "1", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan from VIS-1, no specific UVID or status, hence no parameters given - getVoyagePlan()", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_002_02_row = row
VIS_002_02_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "2", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with chosen UVID from VIS-1, no specific status - getVoyagePlan(UVID)", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "VIS-2 request voyage plan with chosen UVID from VIS-1, no specific status", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_002_03_row = row
VIS_002_03_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "3", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with routeStatus= 7 from VIS-1, no specific UVID  - getVoyagePlan(routeStatus)", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
VIS_002_04_row = row
VIS_002_04_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "4", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with chosen UVID and routeStatus=7 from VIS-1 - getVoyagePlan(UVID, routeStatus)", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
VIS_002_05_row = row
VIS_002_05_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "5", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with another (non published) UVID and routeStatus=7 from VIS-1 - getVoyagePlan(UVID, routeStatus)", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "No voyage plans received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
VIS_002_06_row = row
VIS_002_06_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "6", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with chosen UVID and routeStatus=6 from VIS-1", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "No voyage plans received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18
VIS_002_07_row = row
VIS_002_07_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "7", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with another (non published) UVID from VIS-1, no specific status", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "No voyage plans received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 19
VIS_002_08_row = row
VIS_002_08_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "8", boldbl)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with routeStatus= 6 (non published)  from VIS-1, no specific UVID ", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "No voyage plans received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 20

row = 21
VIS002sheet.write(row, 0, "", boldblue)
VIS002sheet.write(row, 1, "Test ID", boldblue)
VIS002sheet.merge_range(row, 2, row, 3, "TEST-VIS-002", boldblue)
VIS002sheet.write(row, 3, "", boldblue)
VIS002sheet.write(row, 4, "", boldblue)
VIS002sheet.write(row, 5, "", boldblue)
VIS002sheet.write(row, 6, "", boldblue)

row = 22
VIS002sheet.write(row, 1, "Title", bold)
VIS002sheet.merge_range(row, 2, row, 3, "variant - Test rule “Only 1 voyage plan used for monitoring per ship”", normal)

row = 23
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 1, "Description", bold)
VIS002sheet.merge_range(row, 2, row, 3, "", normal)
VIS002sheet.write(row, 4, "Total:", normalright)
VIS002sheet.write(row, 5, '=IF(F27>0,"NOT EXECUTED",IF(F26>0,"FAIL","PASS"))', normalright)

row = 24
VIS002sheet.write(row, 1, "Preconditions", bold)
VIS002sheet.write(row, 4, "Pass:", normalright)
VIS002sheet.write(row, 5, '=COUNTIF(F29:F37, "PASS")', normalright)

row = 25
VIS002sheet.write(row, 1, "Dependencies", bold)
VIS002sheet.write(row, 4, "Fail:", normalright)
VIS002sheet.write(row, 5, '=COUNTIF(F29:F37, "FAIL")', normalright)

row = 26
VIS002sheet.write(row, 4, "Not executed:", normalright)
VIS002sheet.write(row, 5, '=COUNTIF(F29:F37, "NOT EXECUTED")', normalright)

worksheet.write(VIS_002_1_row, VIS_002_1_col, '=VIS002.F24', bold)

VIS002sheet.add_table('A28:G37')
row = 27
VIS002sheet.write(row, 0, "Step#", boldcenterwhite)
VIS002sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS002sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS002sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS002sheet.write(row, 4, "Actual", boldcenterwhite)
VIS002sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS002sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 28
VIS_002_1_0_row = row
VIS_002_1_0_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "0", boldbl)
VIS002sheet.write(row, 1, "Preparation: Organisation for VIS-2 authorized to chosen UVID", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 29
VIS_002_1_1_row = row
VIS_002_1_1_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "1", boldbl)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 30
VIS_002_1_2_row = row
VIS_002_1_2_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "2", boldbl)
VIS002sheet.write(row, 1, "VIS-2 : Request voyage plans from VIS-1", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "1 voyage plan received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 31
VIS_002_1_3_row = row
VIS_002_1_3_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "3", boldbl)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 32
VIS_002_1_4_row = row
VIS_002_1_4_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "4", boldbl)
VIS002sheet.write(row, 1, "VIS-2 : Request voyage plans from VIS-1", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "1 voyage plan received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 33
VIS_002_1_5_row = row
VIS_002_1_5_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "5", boldbl)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with new UVID for the same ship and routeStatus=7", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 34
VIS_002_1_6_row = row
VIS_002_1_6_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "6", boldbl)
VIS002sheet.write(row, 1, "VIS-2 : Request voyage plans from VIS-1", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "1 voyage plan received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 35
VIS_002_1_7_row = row
VIS_002_1_7_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "7", boldbl)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with new UVID for another ship and routeStatus=7", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 36
VIS_002_1_8_row = row
VIS_002_1_8_col = 5
VIS002sheet.set_row(row, 30)
VIS002sheet.write(row, 0, "8", boldbl)
VIS002sheet.write(row, 1, "VIS-2 : Request voyage plans from VIS-1", boldbl)
VIS002sheet.write(row, 2, "", boldbl)
VIS002sheet.write(row, 3, "2 voyage plan received", boldbl)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)
VIS002sheet.write(row, 6, "The problem here is that there is no good way to receive more than one voyage plan and also keep the uvid. For Furuno we may have to accept that there will be vessels that are not filling in the routeStatus or the vesselVoyage field. For these vessels the only way to be compatible with STM would be the external envelope of passing routeStatus and uvid with the RTZ file. My suggestion is to add these fields to the VoyagePlan model. Then we could implement this test case.", normal)

row = 0
col = 0
VIS003sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS003sheet.write(row, 1, "Executed by", bold)
VIS003sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS003sheet.write(row, 1, "Executed date", bold)
VIS003sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS003sheet.write(row, 0, "", boldblue)
VIS003sheet.write(row, 1, "Test ID", boldblue)
VIS003sheet.merge_range(row, 2, row, 3, "TEST-VIS-003", boldblue)
VIS003sheet.write(row, 3, "", boldblue)
VIS003sheet.write(row, 4, "", boldblue)
VIS003sheet.write(row, 5, "", boldblue)
VIS003sheet.write(row, 6, "", boldblue)

row = 5
VIS003sheet.write(row, 1, "Title", bold)
VIS003sheet.merge_range(row, 2, row, 3, "Main test - Test subscription on voyage plans", normal)

row = 6
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 1, "Description", bold)
VIS003sheet.merge_range(row, 2, row, 3, "The purpose is to test subscription of voyage plans, removal of subscription and publish voyage plans to subscribers. VIS shall only accept subscriptions on voyage plans that the receiver are authorized to. VIS shall/should only accept subscription on the latest voyage with routeStatus in 'Under monitoring' for one ship, but can accept subscriptions on several voyage plans with routeStatus < 7.", normal)
VIS003sheet.write(row, 4, "Total:", normalright)
VIS003sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS003sheet.write(row, 1, "Preconditions", bold)
VIS003sheet.write(row, 2, "Configuration A. A registered VIS instance with MMSI=12345678 and subscribeToVoagePlan implemented. Valid certificates loaded in each SSC. Voyage plan published to VIS-1. VIS-2 (Org-2) authorized in VIS-1. VIS-2 not a subscriber to VIS-1", normal)
VIS003sheet.write(row, 4, "Pass:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F12:F18, "PASS")', normalright)

row = 8
VIS003sheet.write(row, 1, "Dependencies", bold)
VIS003sheet.write(row, 2, "VIS, SSC, Identity and Service Registry", normal)
VIS003sheet.write(row, 4, "Fail:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F12:F18, "FAIL")', normalright)

row = 9
VIS003sheet.write(row, 4, "Not executed:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F12:F18, "NOT EXECUTED")', normalright)

worksheet.write(VIS_003_row, VIS_003_col, '=VIS003.F7', bold)

VIS003sheet.add_table('A11:G18')
row = 10
VIS003sheet.write(row, 0, "Step#", boldcenterwhite)
VIS003sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS003sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS003sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS003sheet.write(row, 4, "Actual", boldcenterwhite)
VIS003sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS003sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_003_01_row = row
VIS_003_01_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "1", boldbl)
VIS003sheet.write(row, 1, "In VIS-2, request subscription on voyage plans from VIS-1 ", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "VIS-2 logs event", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_003_02_row = row
VIS_003_02_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "2", boldbl)
VIS003sheet.write(row, 1, "VIS-2 logs event", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "event logged", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_003_03_row = row
VIS_003_03_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "3", boldbl)
VIS003sheet.write(row, 1, "VIS-1 gets a POST subscription request", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "event logged", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_003_04_row = row
VIS_003_04_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "4", boldbl)
VIS003sheet.write(row, 1, "VIS-1 logs event", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "event logged", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
VIS_003_05_row = row
VIS_003_05_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "5", boldbl)
VIS003sheet.write(row, 1, "VIS-1 checks against ACL and get OK", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "check", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
VIS_003_06_row = row
VIS_003_06_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "6", boldbl)
VIS003sheet.write(row, 1, "VIS-1 returns the latest published voyage plan for each UVID with routeStatus<8", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "list of voyagePlans", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
VIS_003_07_row = row
VIS_003_07_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "7", boldbl)
VIS003sheet.write(row, 1, "Publish voyage plan to VIS 1 instance", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "VIS-2 receives the published voyage plan", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18

row = 19
VIS003sheet.write(row, 0, "", boldblue)
VIS003sheet.write(row, 1, "Test ID", boldblue)
VIS003sheet.merge_range(row, 2, row, 3, "TEST-VIS-003-1", boldblue)
VIS003sheet.write(row, 3, "", boldblue)
VIS003sheet.write(row, 4, "", boldblue)
VIS003sheet.write(row, 5, "", boldblue)
VIS003sheet.write(row, 6, "", boldblue)

row = 20
VIS003sheet.write(row, 1, "Title", bold)
VIS003sheet.merge_range(row, 2, row, 3, "Variant - Subscribe to Voyage Plan – incorrect callback endpoint", normal)

row = 21
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 1, "Description", bold)
VIS003sheet.merge_range(row, 2, row, 3, "", normal)
VIS003sheet.write(row, 4, "Total:", normalright)
VIS003sheet.write(row, 5, '=IF(F25>0,"NOT EXECUTED",IF(F24>0,"FAIL","PASS"))', normalright)

row = 22
VIS003sheet.write(row, 1, "Preconditions", bold)
VIS003sheet.write(row, 2, "", normal)
VIS003sheet.write(row, 4, "Pass:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F27:F28, "PASS")', normalright)

row = 23
VIS003sheet.write(row, 1, "Dependencies", bold)
VIS003sheet.write(row, 2, "", normal)
VIS003sheet.write(row, 4, "Fail:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F27:F28, "FAIL")', normalright)

row = 24
VIS003sheet.write(row, 4, "Not executed:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F27:F28, "NOT EXECUTED")', normalright)

worksheet.write(VIS_003_1_row, VIS_003_1_col, '=VIS003.F22', bold)

VIS003sheet.add_table('A26:G28')
row = 25
VIS003sheet.write(row, 0, "Step#", boldcenterwhite)
VIS003sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS003sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS003sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS003sheet.write(row, 4, "Actual", boldcenterwhite)
VIS003sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS003sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 26
VIS_003_1_1_row = row
VIS_003_1_1_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "1", boldbl)
VIS003sheet.write(row, 1, "In VIS-2, request subscription on voyage plans from VIS-1 ", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "Notification in VIS-1 of incorrect callbackEndpoint. Response in VIS-2 that subscription request failed", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 27
VIS_003_1_2_row = row
VIS_003_1_2_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "2", boldbl)
VIS003sheet.write(row, 1, "Publish voyage plan to VIS 1 instance", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "Notification in VIS-1 of incorrect callbackEndpointi. No voyage plans in VIS-2", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 28

row = 29
VIS003sheet.write(row, 0, "", boldblue)
VIS003sheet.write(row, 1, "Test ID", boldblue)
VIS003sheet.merge_range(row, 2, row, 3, "TEST-VIS-003-2", boldblue)
VIS003sheet.write(row, 3, "", boldblue)
VIS003sheet.write(row, 4, "", boldblue)
VIS003sheet.write(row, 5, "", boldblue)
VIS003sheet.write(row, 6, "", boldblue)

row = 30
VIS003sheet.write(row, 1, "Title", bold)
VIS003sheet.merge_range(row, 2, row, 3, "Variant - Subscribe to Voyage Plan – incorrect UVID", normal)

row = 31
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 1, "Description", bold)
VIS003sheet.merge_range(row, 2, row, 3, "", normal)
VIS003sheet.write(row, 4, "Total:", normalright)
VIS003sheet.write(row, 5, '=IF(F35>0,"NOT EXECUTED",IF(F34>0,"FAIL","PASS"))', normalright)

row = 32
VIS003sheet.write(row, 1, "Preconditions", bold)
VIS003sheet.write(row, 2, "", normal)
VIS003sheet.write(row, 4, "Pass:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F37:F38, "PASS")', normalright)

row = 33
VIS003sheet.write(row, 1, "Dependencies", bold)
VIS003sheet.write(row, 2, "", normal)
VIS003sheet.write(row, 4, "Fail:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F37:F38, "FAIL")', normalright)

row = 34
VIS003sheet.write(row, 4, "Not executed:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F37:F38, "NOT EXECUTED")', normalright)

worksheet.write(VIS_003_2_row, VIS_003_2_col, '=VIS003.F32', bold)

VIS003sheet.add_table('A36:G38')
row = 35
VIS003sheet.write(row, 0, "Step#", boldcenterwhite)
VIS003sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS003sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS003sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS003sheet.write(row, 4, "Actual", boldcenterwhite)
VIS003sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS003sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 36
VIS_003_2_1_row = row
VIS_003_2_1_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "1", boldbl)
VIS003sheet.write(row, 1, "In VIS-2, request subscription on voyage plans from VIS-1, but with incorrect UVID", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "Response in VIS-2 that subscription request failed", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 37
VIS_003_2_2_row = row
VIS_003_2_2_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "2", boldbl)
VIS003sheet.write(row, 1, "Publish voyage plan to VIS 1 instance", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "No voyage plans in VIS-2", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 38

row = 39
VIS003sheet.write(row, 0, "", boldblue)
VIS003sheet.write(row, 1, "Test ID", boldblue)
VIS003sheet.merge_range(row, 2, row, 3, "TEST-VIS-003-3", boldblue)
VIS003sheet.write(row, 3, "", boldblue)
VIS003sheet.write(row, 4, "", boldblue)
VIS003sheet.write(row, 5, "", boldblue)
VIS003sheet.write(row, 6, "", boldblue)

row = 40
VIS003sheet.write(row, 1, "Title", bold)
VIS003sheet.merge_range(row, 2, row, 3, "Variant - Duplicate subscription requests", normal)

row = 41
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 1, "Description", bold)
VIS003sheet.merge_range(row, 2, row, 3, "The purpose is to test behaviour if several duplicate subscriptions is requested", normal)
VIS003sheet.write(row, 4, "Total:", normalright)
VIS003sheet.write(row, 5, '=IF(F45>0,"NOT EXECUTED",IF(F44>0,"FAIL","PASS"))', normalright)

row = 42
VIS003sheet.write(row, 1, "Preconditions", bold)
VIS003sheet.write(row, 2, "", normal)
VIS003sheet.write(row, 4, "Pass:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F47:F50, "PASS")', normalright)

row = 43
VIS003sheet.write(row, 1, "Dependencies", bold)
VIS003sheet.write(row, 2, "", normal)
VIS003sheet.write(row, 4, "Fail:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F47:F50, "FAIL")', normalright)

row = 44
VIS003sheet.write(row, 4, "Not executed:", normalright)
VIS003sheet.write(row, 5, '=COUNTIF(F47:F50, "NOT EXECUTED")', normalright)

worksheet.write(VIS_003_3_row, VIS_003_3_col, '=VIS003.F42', bold)

VIS003sheet.add_table('A46:G50')
row = 45
VIS003sheet.write(row, 0, "Step#", boldcenterwhite)
VIS003sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS003sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS003sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS003sheet.write(row, 4, "Actual", boldcenterwhite)
VIS003sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS003sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 46
VIS_003_3_1_row = row
VIS_003_3_1_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "1", boldbl)
VIS003sheet.write(row, 1, "VIS-2: Request subscription from VIS-1", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "Subscription accepted, 200", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 47
VIS_003_3_2_row = row
VIS_003_3_2_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "2", boldbl)
VIS003sheet.write(row, 1, "VIS-2: Request subscription from VIS-1", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "Subscription denied due to already a subscriber", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "Actually the subscription should return 200. As the subscription itself has succeeded. In the text field you could tell that the subscription already existed", normal)

row = 48
VIS_003_3_3_row = row
VIS_003_3_3_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "3", boldbl)
VIS003sheet.write(row, 1, "VIS-2: Request subscription from VIS-1 on known (published and access to) UVID", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "Subscription accepted, 200", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)

row = 49
VIS_003_3_4_row = row
VIS_003_3_4_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "4", boldbl)
VIS003sheet.write(row, 1, "Subscription denied due to already a subscriber", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "Subscription denied due to already a subscriber", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "Actually the subscription should return 200. As the subscription itself has succeeded. In the text field you could tell that the subscription already existed", normal)


row = 0
col = 0
VIS004sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS004sheet.write(row, 1, "Executed by", bold)
VIS004sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS004sheet.write(row, 1, "Executed date", bold)
VIS004sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS004sheet.write(row, 0, "", boldblue)
VIS004sheet.write(row, 1, "Test ID", boldblue)
VIS004sheet.merge_range(row, 2, row, 3, "TEST-VIS-004", boldblue)
VIS004sheet.write(row, 3, "", boldblue)
VIS004sheet.write(row, 4, "", boldblue)
VIS004sheet.write(row, 5, "", boldblue)
VIS004sheet.write(row, 6, "", boldblue)

row = 5
VIS004sheet.write(row, 1, "Title", bold)
VIS004sheet.merge_range(row, 2, row, 3, "Main test", normal)

row = 6
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 1, "Description", bold)
VIS004sheet.merge_range(row, 2, row, 3, "Remove subscription to the voyage plan(s)", normal)
VIS004sheet.write(row, 4, "Total:", normalright)
VIS004sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS004sheet.write(row, 1, "Preconditions", bold)
VIS004sheet.write(row, 2, "Configuration A. A registered VIS instance with MMSI=12345678 and removeSubscriptionToVoyagePlan implemented. Valid certificates loaded in each SSC. VIS-2 is a subscriber to VIS-1", normal)
VIS004sheet.write(row, 4, "Pass:", normalright)
VIS004sheet.write(row, 5, '=COUNTIF(F12:F15, "PASS")', normalright)

row = 8
VIS004sheet.write(row, 1, "Dependencies", bold)
VIS004sheet.write(row, 2, "", normal)
VIS004sheet.write(row, 4, "Fail:", normalright)
VIS004sheet.write(row, 5, '=COUNTIF(F12:F15, "FAIL")', normalright)

row = 9
VIS004sheet.write(row, 4, "Not executed:", normalright)
VIS004sheet.write(row, 5, '=COUNTIF(F12:F15, "NOT EXECUTED")', normalright)

worksheet.write(VIS_004_row, VIS_004_col, '=VIS004.F7', bold)

VIS004sheet.add_table('A11:G15')
row = 10
VIS004sheet.write(row, 0, "Step#", boldcenterwhite)
VIS004sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS004sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS004sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS004sheet.write(row, 4, "Actual", boldcenterwhite)
VIS004sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS004sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_004_01_row = row
VIS_004_01_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "1", boldbl)
VIS004sheet.write(row, 1, "VIS-2: Request subscription on VIS-1", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_004_02_row = row
VIS_004_02_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "2", boldbl)
VIS004sheet.write(row, 1, "VIS-1: Publish voyage plan to VIS-1 instance", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "VIS-2 receives voyage plan", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_004_03_row = row
VIS_004_03_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "3", boldbl)
VIS004sheet.write(row, 1, "VIS-2: Request remove of subscription to voyage plan from VIS-1", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "Subscription removed, ACL remains in VIS-1", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_004_04_row = row
VIS_004_04_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "4", boldbl)
VIS004sheet.write(row, 1, "VIS-1: Publish voyage plan to VIS-1 instance", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "VIS-2 don’t receive any voyage plan", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15

row = 16
VIS004sheet.write(row, 0, "", boldblue)
VIS004sheet.write(row, 1, "Test ID", boldblue)
VIS004sheet.merge_range(row, 2, row, 3, "TEST-VIS-004-1", boldblue)
VIS004sheet.write(row, 3, "", boldblue)
VIS004sheet.write(row, 4, "", boldblue)
VIS004sheet.write(row, 5, "", boldblue)
VIS004sheet.write(row, 6, "", boldblue)

row = 17
VIS004sheet.write(row, 1, "Title", bold)
VIS004sheet.merge_range(row, 2, row, 3, "Variant - Remove subscription with incorrect parameters", normal)

row = 18
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 1, "Description", bold)
VIS004sheet.merge_range(row, 2, row, 3, "", normal)
VIS004sheet.write(row, 4, "Total:", normalright)
VIS004sheet.write(row, 5, '=IF(F22>0,"NOT EXECUTED",IF(F21>0,"FAIL","PASS"))', normalright)

row = 19
VIS004sheet.write(row, 1, "Preconditions", bold)
VIS004sheet.write(row, 2, "", normal)
VIS004sheet.write(row, 4, "Pass:", normalright)
VIS004sheet.write(row, 5, '=COUNTIF(F24:F28, "PASS")', normalright)

row = 20
VIS004sheet.write(row, 1, "Dependencies", bold)
VIS004sheet.write(row, 2, "", normal)
VIS004sheet.write(row, 4, "Fail:", normalright)
VIS004sheet.write(row, 5, '=COUNTIF(F24:F28, "FAIL")', normalright)

row = 21
VIS004sheet.write(row, 4, "Not executed:", normalright)
VIS004sheet.write(row, 5, '=COUNTIF(F24:F28, "NOT EXECUTED")', normalright)

worksheet.write(VIS_004_1_row, VIS_004_1_col, '=VIS004.F19', bold)

VIS004sheet.add_table('A23:G28')
row = 22
VIS004sheet.write(row, 0, "Step#", boldcenterwhite)
VIS004sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS004sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS004sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS004sheet.write(row, 4, "Actual", boldcenterwhite)
VIS004sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS004sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 23
VIS_004_1_1_row = row
VIS_004_1_1_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "1", boldbl)
VIS004sheet.write(row, 1, "VIS-2: Request subscription on VIS-1", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 24
VIS_004_1_2_row = row
VIS_004_1_2_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "2", boldbl)
VIS004sheet.write(row, 1, "VIS-2: Request remove of subscription to voyage plan with unknown UVID from VIS-1", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "Subscription not removed", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 25
VIS_004_1_3_row = row
VIS_004_1_3_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "3", boldbl)
VIS004sheet.write(row, 1, "VIS-1: Publish voyage plan to VIS-1 instance", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "VIS-2 receive voyage plan", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 26
VIS_004_1_4_row = row
VIS_004_1_4_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "4", boldbl)
VIS004sheet.write(row, 1, "VIS-2: Request remove of subscription to voyage plan with unknown callbackEndpoint from VIS-1", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "Subscription not removed", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

row = 27
VIS_004_1_5_row = row
VIS_004_1_5_col = 5
VIS004sheet.set_row(row, 30)
VIS004sheet.write(row, 0, "5", boldbl)
VIS004sheet.write(row, 1, "VIS-1: Publish voyage plan to VIS-1 instance", boldbl)
VIS004sheet.write(row, 2, "", boldbl)
VIS004sheet.write(row, 3, "VIS-2 receive voyage plan", boldbl)
VIS004sheet.write(row, 5, "NOT EXECUTED", bold)

'''

f = open('create_worksheet.py', 'w')
f.write(init_workbook)
f.close()

