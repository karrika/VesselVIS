init_workbook = '''import xlsxwriter
import time

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('VIS-TestCaseCollection_report.xlsx')
worksheet = workbook.add_worksheet("VIS Test Case Summary")
worksheet.set_column(0, 10, 15)
VIS001sheet = workbook.add_worksheet("VIS001")
VIS001sheet.set_column(0, 0, 5)
VIS001sheet.set_column(1, 1, 20)
VIS001sheet.set_column(2, 2, 10)
VIS001sheet.set_column(3, 3, 10)
VIS001sheet.set_column(4, 4, 20)
VIS001sheet.set_column(5, 5, 8)
VIS001sheet.set_column(6, 4, 20)
VIS002sheet = workbook.add_worksheet("VIS002")
VIS002sheet.set_column(0, 0, 5)
VIS002sheet.set_column(1, 1, 20)
VIS002sheet.set_column(2, 2, 10)
VIS002sheet.set_column(3, 3, 10)
VIS002sheet.set_column(4, 4, 20)
VIS002sheet.set_column(5, 5, 8)
VIS002sheet.set_column(6, 4, 20)
VIS003sheet = workbook.add_worksheet("VIS003")
VIS004sheet = workbook.add_worksheet("VIS004")
VIS005sheet = workbook.add_worksheet("VIS005")
VIS006sheet = workbook.add_worksheet("VIS006")
VIS007sheet = workbook.add_worksheet("VIS007")
VIS008sheet = workbook.add_worksheet("VIS008")
VIS009sheet = workbook.add_worksheet("VIS009")
VIS010sheet = workbook.add_worksheet("VIS010")

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

normal = workbook.add_format()
normal.set_text_wrap()
normalright = workbook.add_format()
normalright.set_align('right')
bold = workbook.add_format({'bold': True})
bold.set_text_wrap()
boldcenter = workbook.add_format({'bold': True})
boldcenter.set_align('center')
boldcenter.set_text_wrap()


worksheet.write(row, 0, "VIS Test Protocol", bold)

row = 2
worksheet.write(row, 0, "Executed by", bold)
worksheet.write(row, 1, "Karri Kaksonen", bold)
row = 3
worksheet.write(row, 0, "Executed date", bold)
worksheet.write(row, 1, time.strftime("%Y-%m-%d"), bold)

row = 5
worksheet.add_table('A6:K34')
worksheet.write(row, 0, "Designed by", boldcenter)
worksheet.write(row, 1, "Design date", boldcenter)
worksheet.write(row, 2, "Title", boldcenter)
worksheet.write(row, 3, "Description", boldcenter)
worksheet.write(row, 4, "Component", boldcenter)
worksheet.write(row, 5, "Testcase ID", boldcenter)
worksheet.write(row, 6, "Main or Variant", boldcenter)
worksheet.write(row, 7, "Link to Detailed", boldcenter)
worksheet.write(row, 8, "Test Data", boldcenter)
worksheet.write(row, 9, "Pass/Fail", boldcenter)
worksheet.write(row, 10, "Finding & Comment", boldcenter)

row = 6
VIS_001_row = row
VIS_001_col = 9
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Authorize and Publish Voyage Plan", bold)
worksheet.write(row, 3, "Test publish voyage plan and give authorization (access) to chosen identities. Authorized identities (organisations) can request (GET) and subscribe to voyage plans", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 8, "RTZ-001", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 7
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan with validityPeriod", bold)
worksheet.write(row, 3, "Publish old voyage plan where validityPeriod has passed", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-3", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 8, "RTZ with different validityPeriods", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 8
VIS_001_4_row = row
VIS_001_4_col = 9
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan based on different schema versions", bold)
worksheet.write(row, 3, "Publish future voyage plan according to different schema versions", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-4", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 9
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish incorrect voyage plan according to schema", bold)
worksheet.write(row, 3, "Publish incorrect voyage plan according to RTZ schema", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-5", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 10
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan for another ship", bold)
worksheet.write(row, 3, "Test/show behaviour for VIS if an ship publishes a RTZ for another ship", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-6", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 11
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Publish voyage plan without UVID and/or status", bold)
worksheet.write(row, 3, "Test/show behaviour of VIS if publishing a voyage plan with no or incorrect vesselVoyage and/or routeStatus", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-001-6", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 12
VIS_002_row = row
VIS_002_col = 9
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Request Voyage Plan", bold)
worksheet.write(row, 3, "Test request (get) voyage plan(s)", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-002", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 13
VIS_002_1_row = row
VIS_002_1_col = 9
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant – Test rule “Only 1 voyage plan used for monitoring per ship”", bold)
worksheet.write(row, 3, "Test maintained rule « Only one voyage per ship can be in status « Used for monitoring » (7) when requesting voyage plans", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-002-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 14
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Subscribe to Voyage Plan", bold)
worksheet.write(row, 3, "Test subscription on voyage plans", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 7, "Link to Detailed", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 15
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Subscribe to Voyage Plan – incorrect callback endpoint", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 16
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Subscribe to Voyage Plan – incorrect UVID", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 17
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Duplicate subscription requests", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-003-3", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 18
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Remove Subscription to Voyage Plan", bold)
worksheet.write(row, 3, "Remove subscription to the voyage plan(s)", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-004", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 19
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Remove subscription with incorrect parameters", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-004-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 20
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Upload Voyage Plan", bold)
worksheet.write(row, 3, "Find VIS and send (upload) a voyage plan. No ACK is requested. The STM Module is notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 21
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with ACK request", bold)
worksheet.write(row, 3, "Same as TEST-005 but ACK is requested.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 22
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with ACK request but no STM Module retrieves the message", bold)
worksheet.write(row, 3, "Same as TEST-005-1 but no STM Module receives the message.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 23
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with explicit callback endpoint", bold)
worksheet.write(row, 3, "Upload voyage plan (RTZ) with explicit callback endpoint where returned result is expected", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-3", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 24
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Voyage Plan for another ship to a ship", bold)
worksheet.write(row, 3, "Test/show the behaviour of VIS if a service provider uploads a voyage plan for another ship than the receiver", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-005-4", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 25
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Upload Text Message", bold)
worksheet.write(row, 3, "Test upload text message to VIS. No ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-006", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 26
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Text Message with ACK request", bold)
worksheet.write(row, 3, "Same as TEST-006 but ACK is requested.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-006-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 27
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload TXT message with ACK request but no STM Module retrieves the message", bold)
worksheet.write(row, 3, "Same as TEST-006-1 but no STM Module receives the message.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-006-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 28
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Upload Area (S-124) Message", bold)
worksheet.write(row, 3, "Test send (upload) area message. No ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-007", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 29
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload Area Message with ACK request", bold)
worksheet.write(row, 3, "Test send (upload) area message. ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-007-1", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 30
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Variant - Upload S124 message with ACK request but no STM Module retrieves the message", bold)
worksheet.write(row, 3, "Same as TEST-007-1 but no STM Module receives the message.", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-007-2", bold)
worksheet.write(row, 6, "Variant", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 31
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "DEPRECATED - Notification to STM Module", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-008", bold)
worksheet.write(row, 6, "Main", bold)

row = 32
worksheet.write(row, 0, "MO", boldcenter)
worksheet.write(row, 2, "Logging in VIS", bold)
worksheet.write(row, 3, "Check log in VIS", bold)
worksheet.write(row, 4, "VIS", bold)
worksheet.write(row, 5, "VIS-009", bold)
worksheet.write(row, 6, "Main", bold)
worksheet.write(row, 9, "NOT EXECUTED", bold)

row = 33
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
VIS001sheet.write(row, 1, "Test ID", bold)
VIS001sheet.write(row, 2, "TEST-VIS-001", bold)
row = 2
VIS001sheet.write(row, 1, "Executed by", bold)
VIS001sheet.write(row, 2, "Karri Kaksonen", bold)
row = 3
VIS001sheet.write(row, 0, "Executed date", bold)
VIS001sheet.write(row, 1, time.strftime("%Y-%m-%d"), bold)
row = 5
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.write(row, 2, "Main test", normal)
row = 6
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.write(row, 2, "Test publish voyage plan and give authorization (access) to chosen identities. Authorized identities (organisations) can request (GET) and subscribe to voyage plans. ", normal)
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
VIS001sheet.write(row, 0, "Step#", boldcenter)
VIS001sheet.write(row, 1, "Test Step", boldcenter)
VIS001sheet.write(row, 2, "Test Data", boldcenter)
VIS001sheet.write(row, 3, "Expected Result", boldcenter)
VIS001sheet.write(row, 4, "Actual", boldcenter)
VIS001sheet.write(row, 5, "Pass Fail", boldcenter)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 11
VIS_001_00_row = row
VIS_001_00_col = 5
VIS001sheet.write(row, 0, "0", bold)
VIS001sheet.write(row, 1, "Preparation: No voyage plan published with chosen UVID in VIS-1 - Identify VIS-1 - Identify VIS-2", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_001_01_row = row
VIS_001_01_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "VIS-2: Request (get) voyage plan from VIS-1", bold)
VIS001sheet.write(row, 2, "RTZ-001", bold)
VIS001sheet.write(row, 3, "No voyage plans in response", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_001_02_row = row
VIS_001_02_col = 5
VIS001sheet.write(row, 0, "2", bold)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", bold)
VIS001sheet.write(row, 3, "No subscription", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_001_03_row = row
VIS_001_03_col = 5
VIS001sheet.write(row, 0, "3", bold)
VIS001sheet.write(row, 1, "VIS-1: Publish voyage plan with chosen UVID", bold)
VIS001sheet.write(row, 3, "Success", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
VIS_001_04_row = row
VIS_001_04_col = 5
VIS001sheet.write(row, 0, "4", bold)
VIS001sheet.write(row, 1, "VIS-2: Request voyage plan from VIS-1", bold)
VIS001sheet.write(row, 3, "No voyage plan received, error message “Not authorized”", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
VIS_001_05_row = row
VIS_001_05_col = 5
VIS001sheet.write(row, 0, "5", bold)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", bold)
VIS001sheet.write(row, 3, "No subscription", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
VIS_001_06_row = row
VIS_001_06_col = 5
VIS001sheet.write(row, 0, "6", bold)
VIS001sheet.write(row, 1, "VIS-1: Authorize organisation for VIS-2 to chosen UVID in VIS-1", bold)
VIS001sheet.write(row, 3, "Success", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18
VIS_001_07_row = row
VIS_001_07_col = 5
VIS001sheet.write(row, 0, "7", bold)
VIS001sheet.write(row, 1, "VIS-2: Request voyage plan from VIS-1", bold)
VIS001sheet.write(row, 3, "Voyage plan received", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 19
VIS_001_08_row = row
VIS_001_08_col = 5
VIS001sheet.write(row, 0, "8", bold)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", bold)
VIS001sheet.write(row, 3, "Success", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 20
VIS_001_09_row = row
VIS_001_09_col = 5
VIS001sheet.write(row, 0, "9", bold)
VIS001sheet.write(row, 1, "VIS-1: Remove authorization to organisation for VIS-2", bold)
VIS001sheet.write(row, 3, "Success", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 21
VIS_001_10_row = row
VIS_001_10_col = 5
VIS001sheet.write(row, 0, "10", bold)
VIS001sheet.write(row, 1, "VIS-2: Request voyage plan from VIS-1", bold)
VIS001sheet.write(row, 3, "No voyage plan received, error message “Not authorized”", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 22
VIS_001_11_row = row
VIS_001_11_col = 5
VIS001sheet.write(row, 0, "11", bold)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", bold)
VIS001sheet.write(row, 3, "No subscription", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 27
VIS001sheet.write(row, 1, "Test ID", bold)
VIS001sheet.write(row, 2, "TEST-VIS-001-3", bold)

row = 28
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.write(row, 2, "Variant – Publish voyage plan based on different schema versions", normal)

row = 29
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.write(row, 2, "Test different validity periods in RTZ to show the behaviour in VIS. Presently there is no requirement that VIS shall check the validity period.", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F33>0,"NOT EXECUTED",IF(F32>0,"FAIL","PASS"))', normalright)
row = 30
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F35:F37, "PASS")', normalright)
row = 31
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F35:F37, "FAIL")', normalright)
row = 32
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F35:F37, "NOT EXECUTED")', normalright)

VIS001sheet.add_table('A34:G37')
row = 33
VIS001sheet.write(row, 0, "Step#", boldcenter)
VIS001sheet.write(row, 1, "Test Step", boldcenter)
VIS001sheet.write(row, 2, "Test Data", boldcenter)
VIS001sheet.write(row, 3, "Expected Result", boldcenter)
VIS001sheet.write(row, 4, "Actual", boldcenter)
VIS001sheet.write(row, 5, "Pass Fail", boldcenter)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 34
VIS_001_12_03_1_row = row
VIS_001_12_03_1_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "VIS-1: Select VP with validityPeriodStart and validityPeriodStop in past and publish to subscribers ", bold)
VIS001sheet.write(row, 3, "Ok, message published and shared", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 35
VIS_001_12_03_2_row = row
VIS_001_12_03_2_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "Change validityPeriodStop to future and publish to VIS-1", bold)
VIS001sheet.write(row, 3, "Ok, message published and shared", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 36
VIS_001_12_03_3_row = row
VIS_001_12_03_3_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "Change validityPeriodStart to future and publish to VIS-1", bold)
VIS001sheet.write(row, 3, "Ok, message published and shared", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 38
VIS001sheet.write(row, 1, "Test ID", bold)
VIS001sheet.write(row, 2, "TEST-VIS-001-4", bold)

row = 39
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.write(row, 2, "Variant – Publish voyage plan based on different schema versions", normal)

row = 40
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.write(row, 2, "Test different RTZ schema versions", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F44>0,"NOT EXECUTED",IF(F43>0,"FAIL","PASS"))', normalright)

row = 41
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F46:F48, "PASS")', normalright)

row = 42
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F46:F48, "FAIL")', normalright)

row = 43
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F46:F48, "NOT EXECUTED")', normalright)

VIS001sheet.add_table('A45:G48')
row = 44
VIS001sheet.write(row, 0, "Step#", boldcenter)
VIS001sheet.write(row, 1, "Test Step", boldcenter)
VIS001sheet.write(row, 2, "Test Data", boldcenter)
VIS001sheet.write(row, 3, "Expected Result", boldcenter)
VIS001sheet.write(row, 4, "Actual", boldcenter)
VIS001sheet.write(row, 5, "Pass Fail", boldcenter)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 46
VIS_001_12_04_1_row = row
VIS_001_12_04_1_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ 1.0 and publish to VIS-1", bold)
VIS001sheet.write(row, 3, "Success", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 47
VIS_001_12_04_2_row = row
VIS_001_12_04_2_col = 5
VIS001sheet.write(row, 0, "2", bold)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ 1.1 and publish to VIS-1", bold)
VIS001sheet.write(row, 3, "Success", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 48
VIS_001_12_04_3_row = row
VIS_001_12_04_3_col = 5
VIS001sheet.write(row, 0, "3", bold)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ STM 2.0 and publish to VIS-1", bold)
VIS001sheet.write(row, 3, "Success", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 53
VIS001sheet.write(row, 1, "Test ID", bold)
VIS001sheet.write(row, 2, "TEST-VIS-001-5", bold)

row = 54
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.write(row, 2, "Variant – Publish incorrect voyage plan according to schema", normal)

row = 55
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.write(row, 2, "Test error handling in VIS for incorrect RTZ XML and RTZ not according to schema", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F59>0,"NOT EXECUTED",IF(F58>0,"FAIL","PASS"))', normalright)

row = 56
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F61:F62, "PASS")', normalright)

row = 57
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F61:F62, "FAIL")', normalright)

row = 58
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F61:F62, "NOT EXECUTED")', normalright)


VIS001sheet.add_table('A60:G62')
row = 59
VIS001sheet.write(row, 0, "Step#", boldcenter)
VIS001sheet.write(row, 1, "Test Step", boldcenter)
VIS001sheet.write(row, 2, "Test Data", boldcenter)
VIS001sheet.write(row, 3, "Expected Result", boldcenter)
VIS001sheet.write(row, 4, "Actual", boldcenter)
VIS001sheet.write(row, 5, "Pass Fail", boldcenter)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 60
VIS_001_12_05_1_row = row
VIS_001_12_05_1_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "Select VP in incorrect XML and publish to VIS-1 ", bold)
VIS001sheet.write(row, 3, "STM-Module-1 gets error in response. Log entry in VIS-1", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 61
VIS_001_12_05_2_row = row
VIS_001_12_05_2_col = 5
VIS001sheet.write(row, 0, "2", bold)
VIS001sheet.write(row, 1, "Select VP not following schema RTZ  and publish to VIS-1 ", bold)
VIS001sheet.write(row, 3, "STM-Module-1 gets error in response. Log entry in VIS-1", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 66
VIS001sheet.write(row, 1, "Test ID", bold)
VIS001sheet.write(row, 2, "TEST-VIS-001-6", bold)

row = 67
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.write(row, 2, "Variant – Publish voyage plan for another ship", normal)

row = 68
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.write(row, 2, "Test/show behaviour for VIS if an ship publishes a RTZ for another ship", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F72>0,"NOT EXECUTED",IF(F71>0,"FAIL","PASS"))', normalright)

row = 69
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F74:F74, "PASS")', normalright)

row = 70
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F74:F74, "FAIL")', normalright)

row = 71
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F74:F74, "NOT EXECUTED")', normalright)

VIS001sheet.add_table('A73:G74')
row = 72
VIS001sheet.write(row, 0, "Step#", boldcenter)
VIS001sheet.write(row, 1, "Test Step", boldcenter)
VIS001sheet.write(row, 2, "Test Data", boldcenter)
VIS001sheet.write(row, 3, "Expected Result", boldcenter)
VIS001sheet.write(row, 4, "Actual", boldcenter)
VIS001sheet.write(row, 5, "Pass Fail", boldcenter)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 73
VIS_001_12_06_1_row = row
VIS_001_12_06_1_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "Select VP for another ship and publish to subscribers", bold)
VIS001sheet.write(row, 3, "Voyage Plan is published and sent to nominated actors (subscribing actors)", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 76
VIS001sheet.write(row, 1, "Test ID", bold)
VIS001sheet.write(row, 2, "TEST-VIS-001-7", bold)

row = 77
VIS001sheet.write(row, 1, "Title", bold)
VIS001sheet.write(row, 2, "Variant – Publish voyage plan without UVID and/or status", normal)

row = 78
VIS001sheet.write(row, 1, "Description", bold)
VIS001sheet.write(row, 2, "Test/show behaviour of VIS if publishing a voyage plan with no or incorrect vesselVoyage and/or routeStatus", normal)
VIS001sheet.write(row, 4, "Total:", normalright)
VIS001sheet.write(row, 5, '=IF(F82>0,"NOT EXECUTED",IF(F81>0,"FAIL","PASS"))', normalright)

row = 79
VIS001sheet.write(row, 1, "Preconditions", bold)
VIS001sheet.write(row, 4, "Pass:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F84:F87, "PASS")', normalright)

row = 80
VIS001sheet.write(row, 1, "Dependencies", bold)
VIS001sheet.write(row, 4, "Fail:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F84:F87, "FAIL")', normalright)

row = 81
VIS001sheet.write(row, 4, "Not executed:", normalright)
VIS001sheet.write(row, 5, '=COUNTIF(F84:F87, "NOT EXECUTED")', normalright)

VIS001sheet.add_table('A83:G87')
row = 82
VIS001sheet.write(row, 0, "Step#", boldcenter)
VIS001sheet.write(row, 1, "Test Step", boldcenter)
VIS001sheet.write(row, 2, "Test Data", boldcenter)
VIS001sheet.write(row, 3, "Expected Result", boldcenter)
VIS001sheet.write(row, 4, "Actual", boldcenter)
VIS001sheet.write(row, 5, "Pass Fail", boldcenter)
VIS001sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 83
VIS_001_12_07_1_row = row
VIS_001_12_07_1_col = 5
VIS001sheet.write(row, 0, "1", bold)
VIS001sheet.write(row, 1, "Select voyage plan with missing vesselVoyage and publish to subscribers", bold)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 84
VIS_001_12_07_2_row = row
VIS_001_12_07_2_col = 5
VIS001sheet.write(row, 0, "2", bold)
VIS001sheet.write(row, 1, "Select voyage plan with incorrect syntax of  vesselVoyage and publish to subscribers", bold)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 85
VIS_001_12_07_3_row = row
VIS_001_12_07_3_col = 5
VIS001sheet.write(row, 0, "3", bold)
VIS001sheet.write(row, 1, "Select voyage plan with missing routeStatus and publish to subscribers", bold)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 86
VIS_001_12_07_4_row = row
VIS_001_12_07_4_col = 5
VIS001sheet.write(row, 0, "4", bold)
VIS001sheet.write(row, 1, "Select voyage plan with incorrect syntax of  routeStatus and publish to subscribers", bold)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", bold)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 0
col = 0
VIS002sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS002sheet.write(row, 1, "Test ID", bold)
VIS002sheet.write(row, 2, "TEST-VIS-002", bold)
row = 2
VIS002sheet.write(row, 1, "Executed by", bold)
VIS002sheet.write(row, 2, "Karri Kaksonen", bold)
row = 3
VIS002sheet.write(row, 0, "Executed date", bold)
VIS002sheet.write(row, 1, time.strftime("%Y-%m-%d"), bold)
row = 5
VIS002sheet.write(row, 1, "Title", bold)
VIS002sheet.write(row, 2, "Test request (get) voyage plan(s)", normal)
row = 6
VIS002sheet.write(row, 1, "Description", bold)
VIS001sheet.write(row, 2, "VIS-1 act as SHIP. VIS-2 act as Service Provider or Shore Centre", normal)
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
VIS002sheet.write(row, 0, "Step#", boldcenter)
VIS002sheet.write(row, 1, "Test Step", boldcenter)
VIS002sheet.write(row, 2, "Test Data", boldcenter)
VIS002sheet.write(row, 3, "Expected Result", boldcenter)
VIS002sheet.write(row, 4, "Actual", boldcenter)
VIS002sheet.write(row, 5, "Pass Fail", boldcenter)
VIS002sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 11
VIS_002_00_row = row
VIS_002_00_col = 5
VIS002sheet.write(row, 0, "0", bold)
VIS002sheet.write(row, 1, "Preparation:Organisation for VIS-2 authorized to exactly one published voyage plan with routestatus=7 and chosen UVID", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_002_01_row = row
VIS_002_01_col = 5
VIS002sheet.write(row, 0, "1", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan from VIS-1, no specific UVID or status, hence no parameters given - getVoyagePlan()", bold)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_002_02_row = row
VIS_002_02_col = 5
VIS002sheet.write(row, 0, "2", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with chosen UVID from VIS-1, no specific status - getVoyagePlan(UVID)", bold)
VIS002sheet.write(row, 3, "VIS-2 request voyage plan with chosen UVID from VIS-1, no specific status", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_002_03_row = row
VIS_002_03_col = 5
VIS002sheet.write(row, 0, "3", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with routeStatus= 7 from VIS-1, no specific UVID  - getVoyagePlan(routeStatus)", bold)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
VIS_002_04_row = row
VIS_002_04_col = 5
VIS002sheet.write(row, 0, "4", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with chosen UVID and routeStatus=7 from VIS-1 - getVoyagePlan(UVID, routeStatus)", bold)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
VIS_002_05_row = row
VIS_002_05_col = 5
VIS002sheet.write(row, 0, "5", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with another (non published) UVID and routeStatus=7 from VIS-1 - getVoyagePlan(UVID, routeStatus)", bold)
VIS002sheet.write(row, 3, "No voyage plans received", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
VIS_002_06_row = row
VIS_002_06_col = 5
VIS002sheet.write(row, 0, "6", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with chosen UVID and routeStatus=6 from VIS-1", bold)
VIS002sheet.write(row, 3, "No voyage plans received", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18
VIS_002_07_row = row
VIS_002_07_col = 5
VIS002sheet.write(row, 0, "7", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with another (non published) UVID from VIS-1, no specific status", bold)
VIS002sheet.write(row, 3, "No voyage plans received", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 19
VIS_002_08_row = row
VIS_002_08_col = 5
VIS002sheet.write(row, 0, "8", bold)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with routeStatus= 6 (non published)  from VIS-1, no specific UVID ", bold)
VIS002sheet.write(row, 3, "No voyage plans received", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 22
VIS002sheet.write(row, 1, "Title", bold)
VIS002sheet.write(row, 2, "variant - Test rule “Only 1 voyage plan used for monitoring per ship”", normal)
row = 23
VIS002sheet.write(row, 1, "Description", bold)
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
VIS002sheet.write(row, 0, "Step#", boldcenter)
VIS002sheet.write(row, 1, "Test Step", boldcenter)
VIS002sheet.write(row, 2, "Test Data", boldcenter)
VIS002sheet.write(row, 3, "Expected Result", boldcenter)
VIS002sheet.write(row, 4, "Actual", boldcenter)
VIS002sheet.write(row, 5, "Pass Fail", boldcenter)
VIS002sheet.write(row, 6, "Findings & Comments", boldcenter)

row = 28
VIS_002_1_0_row = row
VIS_002_1_0_col = 5
VIS002sheet.write(row, 0, "0", bold)
VIS002sheet.write(row, 1, "Preparation: Organisation for VIS-2 authorized to chosen UVID", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 29
VIS_002_1_1_row = row
VIS_002_1_1_col = 5
VIS002sheet.write(row, 0, "1", bold)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

row = 30
VIS_002_1_2_row = row
VIS_002_1_2_col = 5
VIS002sheet.write(row, 0, "2", bold)
VIS002sheet.write(row, 1, "VIS-2 : Request voyage plans from VIS-1", bold)
VIS002sheet.write(row, 3, "1 voyage plan received", bold)
VIS002sheet.write(row, 5, "NOT EXECUTED", bold)

'''

f = open('create_worksheet.py', 'w')
f.write(init_workbook)
f.close()

