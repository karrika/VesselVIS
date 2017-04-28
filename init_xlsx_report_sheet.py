init_workbook = '''import xlsxwriter
import time

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('testCaseCollection_V1_Furuno.xlsx')
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
SPIS001sheet = workbook.add_worksheet("SPIS001")
SPIS001sheet.set_column(0, 0, 10)
SPIS001sheet.set_column(1, 1, 40)
SPIS001sheet.set_column(2, 2, 10)
SPIS001sheet.set_column(3, 3, 40)
SPIS001sheet.set_column(4, 4, 10)
SPIS001sheet.set_column(5, 5, 15)
SPIS001sheet.set_column(6, 4, 20)
SPIS002sheet = workbook.add_worksheet("SPIS002")
SPIS002sheet.set_column(0, 0, 10)
SPIS002sheet.set_column(1, 1, 40)
SPIS002sheet.set_column(2, 2, 10)
SPIS002sheet.set_column(3, 3, 40)
SPIS002sheet.set_column(4, 4, 10)
SPIS002sheet.set_column(5, 5, 15)
SPIS002sheet.set_column(6, 4, 20)
SPIS003sheet = workbook.add_worksheet("SPIS003")
SPIS003sheet.set_column(0, 0, 10)
SPIS003sheet.set_column(1, 1, 40)
SPIS003sheet.set_column(2, 2, 10)
SPIS003sheet.set_column(3, 3, 40)
SPIS003sheet.set_column(4, 4, 10)
SPIS003sheet.set_column(5, 5, 15)
SPIS003sheet.set_column(6, 4, 20)


normal = workbook.add_format()
normal.set_text_wrap()
normal.set_align('top')
normalright = workbook.add_format()
normalright.set_align('right')
bold = workbook.add_format({'bold': True})
bold.set_text_wrap()
bold.set_align('top')
mainbold = workbook.add_format({'bold': True})
mainbold.set_text_wrap()
mainbold.set_align('top')
mainbold.set_bg_color('#cccccc')
variantbold = workbook.add_format({'bold': True})
variantbold.set_text_wrap()
variantbold.set_align('top')
variantbold.set_bg_color('#dddddd')
boldbld = workbook.add_format({'bold': True})
boldbld.set_text_wrap()
boldbld.set_align('top')
boldbld.set_bg_color('#ccccFF')
boldbl = workbook.add_format({'bold': True})
boldbl.set_text_wrap()
boldbl.set_align('top')
boldbl.set_bg_color('#ddddFF')
boldblue = workbook.add_format({'bold': True})
boldblue.set_text_wrap()
boldblue.set_bg_color('#ccccFF')
boldcenter = workbook.add_format({'bold': True})
boldcenter.set_align('center')
boldcenter.set_align('top')
boldcenter.set_text_wrap()
mainboldcenter = workbook.add_format({'bold': True})
mainboldcenter.set_align('center')
mainboldcenter.set_align('top')
mainboldcenter.set_text_wrap()
mainboldcenter.set_bg_color('#cccccc')
variantboldcenter = workbook.add_format({'bold': True})
variantboldcenter.set_align('center')
variantboldcenter.set_align('top')
variantboldcenter.set_text_wrap()
variantboldcenter.set_bg_color('#dddddd')
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
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Authorize and Publish Voyage Plan", mainbold)
worksheet.write(row, 3, "Test publish voyage plan and give authorization (access) to chosen identities. Authorized identities (organisations) can request (GET) and subscribe to voyage plans", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-001", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "RTZ-001", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 7
VIS_001_3_row = row
VIS_001_3_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant – Publish voyage plan with validityPeriod", variantbold)
worksheet.write(row, 3, "Publish old voyage plan where validityPeriod has passed", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-001-3", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "RTZ with different validityPeriods", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 8
VIS_001_4_row = row
VIS_001_4_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant – Publish voyage plan based on different schema versions", variantbold)
worksheet.write(row, 3, "Publish future voyage plan according to different schema versions", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-001-4", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 9
VIS_001_5_row = row
VIS_001_5_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant – Publish incorrect voyage plan according to schema", variantbold)
worksheet.write(row, 3, "Publish incorrect voyage plan according to RTZ schema", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-001-5", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 10
VIS_001_6_row = row
VIS_001_6_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant – Publish voyage plan for another ship", variantbold)
worksheet.write(row, 3, "Test/show behaviour for VIS if an ship publishes a RTZ for another ship", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-001-6", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 11
VIS_001_7_row = row
VIS_001_7_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant – Publish voyage plan without UVID and/or status", variantbold)
worksheet.write(row, 3, "Test/show behaviour of VIS if publishing a voyage plan with no or incorrect vesselVoyage and/or routeStatus", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-001-7", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 12
VIS_002_row = row
VIS_002_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Request Voyage Plan", mainbold)
worksheet.write(row, 3, "Test request (get) voyage plan(s)", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-002", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 13
VIS_002_1_row = row
VIS_002_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant – Test rule “Only 1 voyage plan used for monitoring per ship”", variantbold)
worksheet.write(row, 3, "Test maintained rule « Only one voyage per ship can be in status « Used for monitoring » (7) when requesting voyage plans", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-002-1", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 14
VIS_003_row = row
VIS_003_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Subscribe to Voyage Plan", mainbold)
worksheet.write(row, 3, "Test subscription on voyage plans", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-003", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 15
VIS_003_1_row = row
VIS_003_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Subscribe to Voyage Plan – incorrect callback endpoint", variantbold)
worksheet.write(row, 3, "", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-003-1", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 16
VIS_003_2_row = row
VIS_003_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Subscribe to Voyage Plan – incorrect UVID", variantbold)
worksheet.write(row, 3, "", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-003-2", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 17
VIS_003_3_row = row
VIS_003_3_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Duplicate subscription requests", variantbold)
worksheet.write(row, 3, "", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-003-3", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 18
VIS_004_row = row
VIS_004_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Remove Subscription to Voyage Plan", mainbold)
worksheet.write(row, 3, "Remove subscription to the voyage plan(s)", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-004", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 19
VIS_004_1_row = row
VIS_004_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Remove subscription with incorrect parameters", variantbold)
worksheet.write(row, 3, "", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-004-1", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 20
VIS_005_row = row
VIS_005_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Upload Voyage Plan", mainbold)
worksheet.write(row, 3, "Find VIS and send (upload) a voyage plan. No ACK is requested. The STM Module is notified by VIS and the message is retrieved.", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-005", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 21
VIS_005_1_row = row
VIS_005_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with ACK request", variantbold)
worksheet.write(row, 3, "Same as TEST-005 but ACK is requested.", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-005-1", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 22
VIS_005_2_row = row
VIS_005_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with ACK request but no STM Module retrieves the message", variantbold)
worksheet.write(row, 3, "Same as TEST-005-1 but no STM Module receives the message.", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-005-2", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 23
VIS_005_3_row = row
VIS_005_3_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload Voyage Plan with explicit callback endpoint", variantbold)
worksheet.write(row, 3, "Upload voyage plan (RTZ) with explicit callback endpoint where returned result is expected", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-005-3", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 24
VIS_005_4_row = row
VIS_005_4_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload Voyage Plan for another ship to a ship", variantbold)
worksheet.write(row, 3, "Test/show the behaviour of VIS if a service provider uploads a voyage plan for another ship than the receiver", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-005-4", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 25
VIS_006_row = row
VIS_006_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Upload Text Message", mainbold)
worksheet.write(row, 3, "Test upload text message to VIS. No ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-006", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 26
VIS_006_1_row = row
VIS_006_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload Text Message with ACK request", variantbold)
worksheet.write(row, 3, "Same as TEST-006 but ACK is requested.", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-006-1", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 27
VIS_006_2_row = row
VIS_006_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload TXT message with ACK request but no STM Module retrieves the message", variantbold)
worksheet.write(row, 3, "Same as TEST-006-1 but no STM Module receives the message.", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-006-2", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 28
VIS_007_row = row
VIS_007_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Upload Area (S-124) Message", mainbold)
worksheet.write(row, 3, "Test send (upload) area message. No ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-007", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 29
VIS_007_1_row = row
VIS_007_1_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload Area Message with ACK request", variantbold)
worksheet.write(row, 3, "Test send (upload) area message. ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-007-1", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 30
VIS_007_2_row = row
VIS_007_2_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", variantboldcenter)
worksheet.write(row, 1, "", variantbold)
worksheet.write(row, 2, "Variant - Upload S124 message with ACK request but no STM Module retrieves the message", variantbold)
worksheet.write(row, 3, "Same as TEST-007-1 but no STM Module receives the message.", variantbold)
worksheet.write(row, 4, "VIS", variantbold)
worksheet.write(row, 5, "VIS-007-2", variantbold)
worksheet.write(row, 6, "Variant", variantbold)
worksheet.write(row, 7, "", variantbold)
worksheet.write(row, 8, "", variantbold)
worksheet.write(row, 9, "NOT EXECUTED", variantbold)

row = 31
VIS_008_row = row
VIS_008_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "DEPRECATED - Notification to STM Module", mainbold)
worksheet.write(row, 3, "", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-008", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "", mainbold)

row = 32
VIS_009_row = row
VIS_009_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Logging in VIS", mainbold)
worksheet.write(row, 3, "Check log in VIS", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-009", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 33
VIS_010_row = row
VIS_010_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Find Voyage Information Services", mainbold)
worksheet.write(row, 3, "Test search for voyage information services to consume", mainbold)
worksheet.write(row, 4, "VIS", mainbold)
worksheet.write(row, 5, "VIS-010", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 34
SPIS_001_row = row
SPIS_001_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Publish Port Call Message", mainbold)
worksheet.write(row, 3, "Test publish voyage plan and give authorization (access) to chosen identities. Authorized identities (organisations) can request (GET) and subscribe to voyage plans", mainbold)
worksheet.write(row, 4, "SPIS", mainbold)
worksheet.write(row, 5, "SPIS-001", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 35
SPIS_002_row = row
SPIS_002_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Receive Port Call Message", mainbold)
worksheet.write(row, 3, "Receive PCM from PortCDM", mainbold)
worksheet.write(row, 4, "SPIS", mainbold)
worksheet.write(row, 5, "SPIS-002", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

row = 36
SPIS_003_row = row
SPIS_003_col = 9
worksheet.set_row(row, 30)
worksheet.write(row, 0, "MO", mainboldcenter)
worksheet.write(row, 1, "", mainbold)
worksheet.write(row, 2, "Logging in SPIS", mainbold)
worksheet.write(row, 3, "Check log in SPIS", mainbold)
worksheet.write(row, 4, "SPIS", mainbold)
worksheet.write(row, 5, "SPIS-003", mainbold)
worksheet.write(row, 6, "Main", mainbold)
worksheet.write(row, 7, "", mainbold)
worksheet.write(row, 8, "", mainbold)
worksheet.write(row, 9, "NOT EXECUTED", mainbold)

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

worksheet.write(VIS_001_row, VIS_001_col, '=VIS001.F7', mainbold)

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
VIS001sheet.write(row, 0, "1", boldbld)
VIS001sheet.write(row, 1, "VIS-2: Request (get) voyage plan from VIS-1", boldbld)
VIS001sheet.write(row, 2, "RTZ-001", boldbld)
VIS001sheet.write(row, 3, "No voyage plans in response", boldbld)
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
VIS001sheet.write(row, 0, "3", boldbld)
VIS001sheet.write(row, 1, "VIS-1: Publish voyage plan with chosen UVID", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "Success", boldbld)
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
VIS001sheet.write(row, 0, "5", boldbld)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "No subscription", boldbld)
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
VIS001sheet.write(row, 0, "7", boldbld)
VIS001sheet.write(row, 1, "VIS-2: Request voyage plan from VIS-1", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "Voyage plan received", boldbld)
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
VIS001sheet.write(row, 0, "9", boldbld)
VIS001sheet.write(row, 1, "VIS-1: Remove authorization to organisation for VIS-2", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "Success", boldbld)
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
VIS001sheet.write(row, 0, "11", boldbld)
VIS001sheet.write(row, 1, "VIS-2: Subscribe to voyage plan from VIS-1", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "No subscription", boldbld)
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

worksheet.write(VIS_001_3_row, VIS_001_3_col, '=$VIS001.F27', variantbold)

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
VIS_001_12_3_1_row = row
VIS_001_12_3_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "VIS-1: Select VP with validityPeriodStart and validityPeriodStop in past and publish to subscribers ", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Ok, message published and shared", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 32
VIS_001_12_3_2_row = row
VIS_001_12_3_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbld)
VIS001sheet.write(row, 1, "Change validityPeriodStop to future and publish to VIS-1", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "Ok, message published and shared", boldbld)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 33
VIS_001_12_3_3_row = row
VIS_001_12_3_3_col = 5
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

worksheet.write(VIS_001_4_row, VIS_001_4_col, '=$VIS001.F38', variantbold)

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
VIS_001_12_4_1_row = row
VIS_001_12_4_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ 1.0 and publish to VIS-1", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "Success", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 43
VIS_001_12_4_2_row = row
VIS_001_12_4_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "2", boldbld)
VIS001sheet.write(row, 1, "Select VP according to schema RTZ 1.1 and publish to VIS-1", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "Success", boldbld)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 44
VIS_001_12_4_3_row = row
VIS_001_12_4_3_col = 5
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

worksheet.write(VIS_001_5_row, VIS_001_5_col, '=$VIS001.F49', variantbold)

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
VIS_001_12_5_1_row = row
VIS_001_12_5_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Select VP in incorrect XML and publish to VIS-1 ", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "STM-Module-1 gets error in response. Log entry in VIS-1", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 54
VIS_001_12_5_2_row = row
VIS_001_12_5_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "2", boldbld)
VIS001sheet.write(row, 1, "Select VP not following schema RTZ  and publish to VIS-1 ", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "STM-Module-1 gets error in response. Log entry in VIS-1", boldbld)
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

worksheet.write(VIS_001_6_row, VIS_001_6_col, '=$VIS001.F59', variantbold)

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
VIS_001_12_6_1_row = row
VIS_001_12_6_1_col = 5
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

worksheet.write(VIS_001_7_row, VIS_001_7_col, '=$VIS001.F68', variantbold)

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
VIS_001_12_7_1_row = row
VIS_001_12_7_1_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "1", boldbl)
VIS001sheet.write(row, 1, "Select voyage plan with missing vesselVoyage and publish to subscribers", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 73
VIS_001_12_7_2_row = row
VIS_001_12_7_2_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "2", boldbld)
VIS001sheet.write(row, 1, "Select voyage plan with incorrect syntax of  vesselVoyage and publish to subscribers", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbld)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 74
VIS_001_12_7_3_row = row
VIS_001_12_7_3_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "3", boldbl)
VIS001sheet.write(row, 1, "Select voyage plan with missing routeStatus and publish to subscribers", boldbl)
VIS001sheet.write(row, 2, "", boldbl)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbl)
VIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 75
VIS_001_12_7_4_row = row
VIS_001_12_7_4_col = 5
VIS001sheet.set_row(row, 30)
VIS001sheet.write(row, 0, "4", boldbld)
VIS001sheet.write(row, 1, "Select voyage plan with incorrect syntax of  routeStatus and publish to subscribers", boldbld)
VIS001sheet.write(row, 2, "", boldbld)
VIS001sheet.write(row, 3, "No voyage plan received by subscribers", boldbld)
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

worksheet.write(VIS_002_row, VIS_002_col, '=$VIS002.F7', mainbold)

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
VIS002sheet.write(row, 0, "1", boldbld)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan from VIS-1, no specific UVID or status, hence no parameters given - getVoyagePlan()", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", boldbld)
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
VIS002sheet.write(row, 0, "3", boldbld)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with routeStatus= 7 from VIS-1, no specific UVID  - getVoyagePlan(routeStatus)", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "VIS-2 receives the voyage plan in response", boldbld)
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
VIS002sheet.write(row, 0, "5", boldbld)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with another (non published) UVID and routeStatus=7 from VIS-1 - getVoyagePlan(UVID, routeStatus)", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "No voyage plans received", boldbld)
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
VIS002sheet.write(row, 0, "7", boldbld)
VIS002sheet.write(row, 1, "VIS-2 request voyage plan with another (non published) UVID from VIS-1, no specific status", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "No voyage plans received", boldbld)
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
VIS002sheet.merge_range(row, 2, row, 3, "TEST-VIS-002-1", boldblue)
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

worksheet.write(VIS_002_1_row, VIS_002_1_col, '=$VIS002.F24', variantbold)

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
VIS002sheet.write(row, 0, "1", boldbld)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "", boldbld)
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
VIS002sheet.write(row, 0, "3", boldbld)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with chosen UVID and routeStatus=7", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "", boldbld)
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
VIS002sheet.write(row, 0, "5", boldbld)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with new UVID for the same ship and routeStatus=7", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "", boldbld)
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
VIS002sheet.write(row, 0, "7", boldbld)
VIS002sheet.write(row, 1, "VIS-1 : Publish voyage plan with new UVID for another ship and routeStatus=7", boldbld)
VIS002sheet.write(row, 2, "", boldbld)
VIS002sheet.write(row, 3, "", boldbld)
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

worksheet.write(VIS_003_row, VIS_003_col, '=$VIS003.F7', mainbold)

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
VIS003sheet.write(row, 0, "2", boldbld)
VIS003sheet.write(row, 1, "VIS-2 logs event", boldbld)
VIS003sheet.write(row, 2, "", boldbld)
VIS003sheet.write(row, 3, "event logged", boldbld)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "There is a separate test suite for logging. Why should VIS003 micro-manage logging?", normal)

row = 13
VIS_003_03_row = row
VIS_003_03_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "3", boldbl)
VIS003sheet.write(row, 1, "VIS-1 gets a POST subscription request", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "event logged", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "Completely redundant. If you already received 200 as a response to your POST.", normal)

row = 14
VIS_003_04_row = row
VIS_003_04_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "4", boldbld)
VIS003sheet.write(row, 1, "VIS-1 logs event", boldbld)
VIS003sheet.write(row, 2, "", boldbld)
VIS003sheet.write(row, 3, "event logged", boldbld)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "There is a separate test suite for logging. Why should VIS003 micro-manage logging?", normal)

row = 15
VIS_003_05_row = row
VIS_003_05_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "5", boldbl)
VIS003sheet.write(row, 1, "VIS-1 checks against ACL and get OK", boldbl)
VIS003sheet.write(row, 2, "", boldbl)
VIS003sheet.write(row, 3, "check", boldbl)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "Completely redundant. You already received 200 instead of 403 as a response to your POST.", normal)

row = 16
VIS_003_06_row = row
VIS_003_06_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "6", boldbld)
VIS003sheet.write(row, 1, "VIS-1 returns the latest published voyage plan for each UVID with routeStatus<8", boldbld)
VIS003sheet.write(row, 2, "", boldbld)
VIS003sheet.write(row, 3, "list of voyagePlans", boldbld)
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

worksheet.write(VIS_003_1_row, VIS_003_1_col, '=$VIS003.F22', variantbold)

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
VIS003sheet.write(row, 6, "How can VIS-1 find out that the callbackEndpoint is invalid? Should it be checked against the service registry? The problem here is that the subscription can not be validated during this POST operation.", normal)

row = 27
VIS_003_1_2_row = row
VIS_003_1_2_col = 5
VIS003sheet.set_row(row, 30)
VIS003sheet.write(row, 0, "2", boldbld)
VIS003sheet.write(row, 1, "Publish voyage plan to VIS 1 instance", boldbld)
VIS003sheet.write(row, 2, "", boldbld)
VIS003sheet.write(row, 3, "Notification in VIS-1 of incorrect callbackEndpoint. No voyage plans in VIS-2", boldbld)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "How can VIS-1 find out that the callbackEndpoint is invalid? Should it be checked against the service registry? What about temporary network problems for POSTing voyage plans. Is this an incorrect callbackEndpoint?", normal)

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

worksheet.write(VIS_003_2_row, VIS_003_2_col, '=$VIS003.F32', variantbold)

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
VIS003sheet.write(row, 0, "2", boldbld)
VIS003sheet.write(row, 1, "Publish voyage plan to VIS 1 instance", boldbld)
VIS003sheet.write(row, 2, "", boldbld)
VIS003sheet.write(row, 3, "No voyage plans in VIS-2", boldbld)
VIS003sheet.write(row, 5, "NOT EXECUTED", bold)
VIS003sheet.write(row, 6, "What is the idea of this test case? The request did already fail in last step meaning that no subscription exists. If we want to run this test then what UVID should we use?", normal)

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

worksheet.write(VIS_003_3_row, VIS_003_3_col, '=$VIS003.F42', variantbold)

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
VIS003sheet.write(row, 0, "2", boldbld)
VIS003sheet.write(row, 1, "VIS-2: Request subscription from VIS-1", boldbld)
VIS003sheet.write(row, 2, "", boldbld)
VIS003sheet.write(row, 3, "Subscription denied due to already a subscriber", boldbld)
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
VIS003sheet.write(row, 0, "4", boldbld)
VIS003sheet.write(row, 1, "Subscription denied due to already a subscriber", boldbld)
VIS003sheet.write(row, 2, "", boldbld)
VIS003sheet.write(row, 3, "Subscription denied due to already a subscriber", boldbld)
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

worksheet.write(VIS_004_row, VIS_004_col, '=$VIS004.F7', mainbold)

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
VIS004sheet.write(row, 0, "2", boldbld)
VIS004sheet.write(row, 1, "VIS-1: Publish voyage plan to VIS-1 instance", boldbld)
VIS004sheet.write(row, 2, "", boldbld)
VIS004sheet.write(row, 3, "VIS-2 receives voyage plan", boldbld)
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
VIS004sheet.write(row, 0, "4", boldbld)
VIS004sheet.write(row, 1, "VIS-1: Publish voyage plan to VIS-1 instance", boldbld)
VIS004sheet.write(row, 2, "", boldbld)
VIS004sheet.write(row, 3, "VIS-2 don’t receive any voyage plan", boldbld)
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

worksheet.write(VIS_004_1_row, VIS_004_1_col, '=$VIS004.F19', variantbold)

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
VIS004sheet.write(row, 0, "2", boldbld)
VIS004sheet.write(row, 1, "VIS-2: Request remove of subscription to voyage plan with unknown UVID from VIS-1", boldbld)
VIS004sheet.write(row, 2, "", boldbld)
VIS004sheet.write(row, 3, "Subscription not removed", boldbld)
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
VIS004sheet.write(row, 0, "4", boldbld)
VIS004sheet.write(row, 1, "VIS-2: Request remove of subscription to voyage plan with unknown callbackEndpoint from VIS-1", boldbld)
VIS004sheet.write(row, 2, "", boldbld)
VIS004sheet.write(row, 3, "Subscription not removed", boldbld)
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


row = 0
col = 0
VIS005sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS005sheet.write(row, 1, "Executed by", bold)
VIS005sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS005sheet.write(row, 1, "Executed date", bold)
VIS005sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS005sheet.write(row, 0, "", boldblue)
VIS005sheet.write(row, 1, "Test ID", boldblue)
VIS005sheet.merge_range(row, 2, row, 3, "TEST-VIS-005", boldblue)
VIS005sheet.write(row, 3, "", boldblue)
VIS005sheet.write(row, 4, "", boldblue)
VIS005sheet.write(row, 5, "", boldblue)
VIS005sheet.write(row, 6, "", boldblue)

row = 5
VIS005sheet.write(row, 1, "Title", bold)
VIS005sheet.merge_range(row, 2, row, 3, "Main test-Upload Voyage Plan", normal)

row = 6
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 1, "Description", bold)
VIS005sheet.merge_range(row, 2, row, 3, "Find VIS and send (upload) a voyage plan. No ACK is requested. The STM Module is notified by VIS and the message is retrieved.", normal)
VIS005sheet.write(row, 4, "Total:", normalright)
VIS005sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS005sheet.write(row, 1, "Preconditions", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Pass:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F12:F13, "PASS")', normalright)

row = 8
VIS005sheet.write(row, 1, "Dependencies", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Fail:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F12:F13, "FAIL")', normalright)

row = 9
VIS005sheet.write(row, 4, "Not executed:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F12:F13, "NOT EXECUTED")', normalright)

worksheet.write(VIS_005_row, VIS_005_col, '=$VIS005.F7', mainbold)

VIS005sheet.add_table('A11:G13')
row = 10
VIS005sheet.write(row, 0, "Step#", boldcenterwhite)
VIS005sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS005sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS005sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS005sheet.write(row, 4, "Actual", boldcenterwhite)
VIS005sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS005sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_005_01_row = row
VIS_005_01_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "1", boldbl)
VIS005sheet.write(row, 1, "VIS-2: Select voyage plan and send (upload) the voyage plan to VIS-1, no ACK requested, no callback expected", boldbl)
VIS005sheet.write(row, 2, "", boldbl)
VIS005sheet.write(row, 3, "VIS-1 receives the uploaded voyage plan", boldbl)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_005_02_row = row
VIS_005_02_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "2", boldbld)
VIS005sheet.write(row, 1, "Private application (such as STM Module) retrieves messages from VIS-1", boldbld)
VIS005sheet.write(row, 2, "", boldbld)
VIS005sheet.write(row, 3, "Private application of VIS-1 receives the uploaded voyage plan. The sender is clearly identifiable", boldbld)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13

row = 14
VIS005sheet.write(row, 0, "", boldblue)
VIS005sheet.write(row, 1, "Test ID", boldblue)
VIS005sheet.merge_range(row, 2, row, 3, "TEST-VIS-005-1", boldblue)
VIS005sheet.write(row, 3, "", boldblue)
VIS005sheet.write(row, 4, "", boldblue)
VIS005sheet.write(row, 5, "", boldblue)
VIS005sheet.write(row, 6, "", boldblue)

row = 15
VIS005sheet.write(row, 1, "Title", bold)
VIS005sheet.merge_range(row, 2, row, 3, "Variant-Upload Voyage Plan with ACK request", normal)

row = 16
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 1, "Description", bold)
VIS005sheet.merge_range(row, 2, row, 3, "", normal)
VIS005sheet.write(row, 4, "Total:", normalright)
VIS005sheet.write(row, 5, '=IF(F20>0,"NOT EXECUTED",IF(F19>0,"FAIL","PASS"))', normalright)

row = 17
VIS005sheet.write(row, 1, "Preconditions", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Pass:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F22:F24, "PASS")', normalright)

row = 18
VIS005sheet.write(row, 1, "Dependencies", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Fail:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F22:F24, "FAIL")', normalright)

row = 19
VIS005sheet.write(row, 4, "Not executed:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F22:F24, "NOT EXECUTED")', normalright)

worksheet.write(VIS_005_1_row, VIS_005_1_col, '=$VIS005.F17', variantbold)

VIS005sheet.add_table('A21:G24')
row = 20
VIS005sheet.write(row, 0, "Step#", boldcenterwhite)
VIS005sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS005sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS005sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS005sheet.write(row, 4, "Actual", boldcenterwhite)
VIS005sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS005sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 21
VIS_005_1_1_row = row
VIS_005_1_1_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "1", boldbl)
VIS005sheet.write(row, 1, "VIS-2: Select voyage plan and send (upload) the voyage plan to VIS-1 with Acknowledgement requested (with ACKendpoint), no callback expected", boldbl)
VIS005sheet.write(row, 2, "", boldbl)
VIS005sheet.write(row, 3, "VIS-1 receives the uploaded voyage plan. VIS-1 logs the upload event and data", boldbl)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 22
VIS_005_1_2_row = row
VIS_005_1_2_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "2", boldbld)
VIS005sheet.write(row, 1, "STM Module retrieves messages from VIS-1", boldbld)
VIS005sheet.write(row, 2, "", boldbld)
VIS005sheet.write(row, 3, "STM Module receives the uploaded voyage plan VIS-1 sends ACK to VIS-2. VIS-2 receives ACK. VIS-2 logs ACK event", boldbld)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 23
VIS_005_1_3_row = row
VIS_005_1_3_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "3", boldbld)
VIS005sheet.write(row, 1, "STM Module-2 uploads response voyage plan to callbackEndpoint", boldbld)
VIS005sheet.write(row, 2, "", boldbld)
VIS005sheet.write(row, 3, "VIS-1 receives the uploaded voyage plan", boldbld)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 24

row = 25
VIS005sheet.write(row, 0, "", boldblue)
VIS005sheet.write(row, 1, "Test ID", boldblue)
VIS005sheet.merge_range(row, 2, row, 3, "TEST-VIS-005-2", boldblue)
VIS005sheet.write(row, 3, "", boldblue)
VIS005sheet.write(row, 4, "", boldblue)
VIS005sheet.write(row, 5, "", boldblue)
VIS005sheet.write(row, 6, "", boldblue)

row = 26
VIS005sheet.write(row, 1, "Title", bold)
VIS005sheet.merge_range(row, 2, row, 3, "Variant - Upload Voyage Plan with ACK request but no STM Module retrieves the message", normal)

row = 27
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 1, "Description", bold)
VIS005sheet.merge_range(row, 2, row, 3, "", normal)
VIS005sheet.write(row, 4, "Total:", normalright)
VIS005sheet.write(row, 5, '=IF(F31>0,"NOT EXECUTED",IF(F30>0,"FAIL","PASS"))', normalright)

row = 28
VIS005sheet.write(row, 1, "Preconditions", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Pass:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F33:F34, "PASS")', normalright)

row = 29
VIS005sheet.write(row, 1, "Dependencies", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Fail:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F33:F34, "FAIL")', normalright)

row = 30
VIS005sheet.write(row, 4, "Not executed:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F33:F34, "NOT EXECUTED")', normalright)

worksheet.write(VIS_005_2_row, VIS_005_2_col, '=$VIS005.F28', variantbold)

VIS005sheet.add_table('A32:G34')
row = 31
VIS005sheet.write(row, 0, "Step#", boldcenterwhite)
VIS005sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS005sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS005sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS005sheet.write(row, 4, "Actual", boldcenterwhite)
VIS005sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS005sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 32
VIS_005_2_1_row = row
VIS_005_2_1_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "1", boldbl)
VIS005sheet.write(row, 1, "In VIS-2, select voyage plan and send (upload) the voyage plan to VIS-1 with ACKendpoint", boldbl)
VIS005sheet.write(row, 2, "", boldbl)
VIS005sheet.write(row, 3, "VIS-1 receives the uploaded voyage plan", boldbl)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 33
VIS_005_2_2_row = row
VIS_005_2_2_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "2", boldbld)
VIS005sheet.write(row, 1, "No private application retrieves/receives the message", boldbld)
VIS005sheet.write(row, 2, "", boldbld)
VIS005sheet.write(row, 3, "", boldbld)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)
VIS005sheet.write(row, 6, "What is this test case supposed to accomplish? Measuring the wait time of what?", normal)

row = 34

row = 35
VIS005sheet.write(row, 0, "", boldblue)
VIS005sheet.write(row, 1, "Test ID", boldblue)
VIS005sheet.merge_range(row, 2, row, 3, "TEST-VIS-005-3", boldblue)
VIS005sheet.write(row, 3, "", boldblue)
VIS005sheet.write(row, 4, "", boldblue)
VIS005sheet.write(row, 5, "", boldblue)
VIS005sheet.write(row, 6, "", boldblue)

row = 36
VIS005sheet.write(row, 1, "Title", bold)
VIS005sheet.merge_range(row, 2, row, 3, "Variant - Upload Voyage Plan with explicit callback endpoint", normal)

row = 37
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 1, "Description", bold)
VIS005sheet.merge_range(row, 2, row, 3, "", normal)
VIS005sheet.write(row, 4, "Total:", normalright)
VIS005sheet.write(row, 5, '=IF(F41>0,"NOT EXECUTED",IF(F40>0,"FAIL","PASS"))', normalright)

row = 38
VIS005sheet.write(row, 1, "Preconditions", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Pass:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F43:F45, "PASS")', normalright)

row = 39
VIS005sheet.write(row, 1, "Dependencies", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Fail:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F43:F45, "FAIL")', normalright)

row = 40
VIS005sheet.write(row, 4, "Not executed:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F43:F45, "NOT EXECUTED")', normalright)

worksheet.write(VIS_005_3_row, VIS_005_3_col, '=$VIS005.F38', variantbold)

VIS005sheet.add_table('A42:G45')
row = 41
VIS005sheet.write(row, 0, "Step#", boldcenterwhite)
VIS005sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS005sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS005sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS005sheet.write(row, 4, "Actual", boldcenterwhite)
VIS005sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS005sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 42
VIS_005_3_1_row = row
VIS_005_3_1_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "1", boldbl)
VIS005sheet.write(row, 1, "VIS-1: Select voyage plan and upload the voyage plan to VIS-2 with explicit callbackEndpoint", boldbl)
VIS005sheet.write(row, 2, "", boldbl)
VIS005sheet.write(row, 3, "VIS-2 receives the uploaded voyage plan", boldbl)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)
VIS005sheet.write(row, 6, "There is no such thing as an explicit callbackEndpoint", normal)

row = 43
VIS_005_3_2_row = row
VIS_005_3_2_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "2", boldbld)
VIS005sheet.write(row, 1, "STM Module-1 retrieves messages from VIS-2", boldbld)
VIS005sheet.write(row, 2, "", boldbld)
VIS005sheet.write(row, 3, "STM Module-2 receives the uploaded voyage plan", boldbld)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 44
VIS_005_3_3_row = row
VIS_005_3_3_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "3", boldbl)
VIS005sheet.write(row, 1, "STM Module-2 uploads response voyage plan to callbackEndpoint", boldbl)
VIS005sheet.write(row, 2, "", boldbl)
VIS005sheet.write(row, 3, "VIS-1 receives the uploaded voyage plan", boldbl)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)
VIS005sheet.write(row, 6, "There is no such thing as an explicit callbackEndpoint", normal)

row = 45

row = 46
VIS005sheet.write(row, 0, "", boldblue)
VIS005sheet.write(row, 1, "Test ID", boldblue)
VIS005sheet.merge_range(row, 2, row, 3, "TEST-VIS-005-4", boldblue)
VIS005sheet.write(row, 3, "", boldblue)
VIS005sheet.write(row, 4, "", boldblue)
VIS005sheet.write(row, 5, "", boldblue)
VIS005sheet.write(row, 6, "", boldblue)

row = 47
VIS005sheet.write(row, 1, "Title", bold)
VIS005sheet.merge_range(row, 2, row, 3, "Variant - Upload Voyage Plan for another ship to a ship", normal)

row = 48
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 1, "Description", bold)
VIS005sheet.merge_range(row, 2, row, 3, "", normal)
VIS005sheet.write(row, 4, "Total:", normalright)
VIS005sheet.write(row, 5, '=IF(F52>0,"NOT EXECUTED",IF(F51>0,"FAIL","PASS"))', normalright)

row = 49
VIS005sheet.write(row, 1, "Preconditions", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Pass:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F54:F54, "PASS")', normalright)

row = 50
VIS005sheet.write(row, 1, "Dependencies", bold)
VIS005sheet.write(row, 2, "", normal)
VIS005sheet.write(row, 4, "Fail:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F54:F54, "FAIL")', normalright)

row = 51
VIS005sheet.write(row, 4, "Not executed:", normalright)
VIS005sheet.write(row, 5, '=COUNTIF(F54:F54, "NOT EXECUTED")', normalright)

worksheet.write(VIS_005_4_row, VIS_005_4_col, '=$VIS005.F49', variantbold)

VIS005sheet.add_table('A53:G54')
row = 52
VIS005sheet.write(row, 0, "Step#", boldcenterwhite)
VIS005sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS005sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS005sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS005sheet.write(row, 4, "Actual", boldcenterwhite)
VIS005sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS005sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 53
VIS_005_4_1_row = row
VIS_005_4_1_col = 5
VIS005sheet.set_row(row, 30)
VIS005sheet.write(row, 0, "1", boldbl)
VIS005sheet.write(row, 1, "VIS-1: Select voyage plan for another ship than VIS-2, and upload the voyage plan to VIS-2", boldbl)
VIS005sheet.write(row, 2, "", boldbl)
VIS005sheet.write(row, 3, "VIS-2 receives the uploaded voyage plan", boldbl)
VIS005sheet.write(row, 5, "NOT EXECUTED", bold)

row = 0
col = 0
VIS006sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS006sheet.write(row, 1, "Executed by", bold)
VIS006sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS006sheet.write(row, 1, "Executed date", bold)
VIS006sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS006sheet.write(row, 0, "", boldblue)
VIS006sheet.write(row, 1, "Test ID", boldblue)
VIS006sheet.merge_range(row, 2, row, 3, "TEST-VIS-006", boldblue)
VIS006sheet.write(row, 3, "", boldblue)
VIS006sheet.write(row, 4, "", boldblue)
VIS006sheet.write(row, 5, "", boldblue)
VIS006sheet.write(row, 6, "", boldblue)

row = 5
VIS006sheet.write(row, 1, "Title", bold)
VIS006sheet.merge_range(row, 2, row, 3, "Main test - Upload Text Message", normal)

row = 6
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 1, "Description", bold)
VIS006sheet.merge_range(row, 2, row, 3, "Test upload text message to VIS.", normal)
VIS006sheet.write(row, 4, "Total:", normalright)
VIS006sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS006sheet.write(row, 1, "Preconditions", bold)
VIS006sheet.write(row, 2, "", normal)
VIS006sheet.write(row, 4, "Pass:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F12:F14, "PASS")', normalright)

row = 8
VIS006sheet.write(row, 1, "Dependencies", bold)
VIS006sheet.write(row, 2, "", normal)
VIS006sheet.write(row, 4, "Fail:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F12:F14, "FAIL")', normalright)

row = 9
VIS006sheet.write(row, 4, "Not executed:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F12:F14, "NOT EXECUTED")', normalright)

worksheet.write(VIS_006_row, VIS_006_col, '=$VIS006.F7', mainbold)

VIS006sheet.add_table('A11:G14')
row = 10
VIS006sheet.write(row, 0, "Step#", boldcenterwhite)
VIS006sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS006sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS006sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS006sheet.write(row, 4, "Actual", boldcenterwhite)
VIS006sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS006sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_006_01_row = row
VIS_006_01_col = 5
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 0, "1", boldbl)
VIS006sheet.write(row, 1, "VIS-2: Select TXT message and send (upload) the TXT message to VIS-1", boldbl)
VIS006sheet.write(row, 2, "", boldbl)
VIS006sheet.write(row, 3, "Test Message received", boldbl)
VIS006sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_006_02_row = row
VIS_006_02_col = 5
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 0, "2", boldbld)
VIS006sheet.write(row, 1, "", boldbld)
VIS006sheet.write(row, 2, "", boldbld)
VIS006sheet.write(row, 3, "STM Module receives the uplodaded txt message. VIS-1 sends ACK to VIS-2", boldbld)
VIS006sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_006_03_row = row
VIS_006_03_col = 5
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 0, "3", boldbl)
VIS006sheet.write(row, 1, "", boldbl)
VIS006sheet.write(row, 2, "", boldbl)
VIS006sheet.write(row, 3, "VIS-2 receives ACK. VIS-2 logs ACK event", boldbl)
VIS006sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14

row = 15
VIS006sheet.write(row, 0, "", boldblue)
VIS006sheet.write(row, 1, "Test ID", boldblue)
VIS006sheet.merge_range(row, 2, row, 3, "TEST-VIS-006-1", boldblue)
VIS006sheet.write(row, 3, "", boldblue)
VIS006sheet.write(row, 4, "", boldblue)
VIS006sheet.write(row, 5, "", boldblue)
VIS006sheet.write(row, 6, "", boldblue)

row = 16
VIS006sheet.write(row, 1, "Title", bold)
VIS006sheet.merge_range(row, 2, row, 3, "Variant - Upload Text Message with ACK request", normal)

row = 17
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 1, "Description", bold)
VIS006sheet.merge_range(row, 2, row, 3, "Test upload text message to VIS.", normal)
VIS006sheet.write(row, 4, "Total:", normalright)
VIS006sheet.write(row, 5, '=IF(F21>0,"NOT EXECUTED",IF(F20>0,"FAIL","PASS"))', normalright)

row = 18
VIS006sheet.write(row, 1, "Preconditions", bold)
VIS006sheet.write(row, 2, "", normal)
VIS006sheet.write(row, 4, "Pass:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F23:F24, "PASS")', normalright)

row = 19
VIS006sheet.write(row, 1, "Dependencies", bold)
VIS006sheet.write(row, 2, "", normal)
VIS006sheet.write(row, 4, "Fail:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F23:F24, "FAIL")', normalright)

row = 20
VIS006sheet.write(row, 4, "Not executed:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F23:F24, "NOT EXECUTED")', normalright)

worksheet.write(VIS_006_1_row, VIS_006_1_col, '=$VIS006.F18', variantbold)

VIS006sheet.add_table('A22:G24')
row = 21
VIS006sheet.write(row, 0, "Step#", boldcenterwhite)
VIS006sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS006sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS006sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS006sheet.write(row, 4, "Actual", boldcenterwhite)
VIS006sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS006sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 22
VIS_006_1_1_row = row
VIS_006_1_1_col = 5
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 0, "1", boldbl)
VIS006sheet.write(row, 1, "In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint", boldbl)
VIS006sheet.write(row, 2, "", boldbl)
VIS006sheet.write(row, 3, "Message received", boldbl)
VIS006sheet.write(row, 5, "NOT EXECUTED", bold)

row = 23
VIS_006_1_2_row = row
VIS_006_1_2_col = 5
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 0, "2", boldbld)
VIS006sheet.write(row, 1, "Retrieve/receive the uploaded message in private application of VIS-1", boldbld)
VIS006sheet.write(row, 2, "", boldbld)
VIS006sheet.write(row, 3, "Acknowledgement received by VIS-2", boldbld)
VIS006sheet.write(row, 5, "NOT EXECUTED", bold)

row = 24

row = 25
VIS006sheet.write(row, 0, "", boldblue)
VIS006sheet.write(row, 1, "Test ID", boldblue)
VIS006sheet.merge_range(row, 2, row, 3, "TEST-VIS-006-2", boldblue)
VIS006sheet.write(row, 3, "", boldblue)
VIS006sheet.write(row, 4, "", boldblue)
VIS006sheet.write(row, 5, "", boldblue)
VIS006sheet.write(row, 6, "", boldblue)

row = 26
VIS006sheet.write(row, 1, "Title", bold)
VIS006sheet.merge_range(row, 2, row, 3, "Variant -  Upload TXT message with ACK request but no STM Module retrieves the message", normal)

row = 27
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 1, "Description", bold)
VIS006sheet.merge_range(row, 2, row, 3, "Test upload of Text Message with no receiver for the message", normal)
VIS006sheet.write(row, 4, "Total:", normalright)
VIS006sheet.write(row, 5, '=IF(F31>0,"NOT EXECUTED",IF(F30>0,"FAIL","PASS"))', normalright)

row = 28
VIS006sheet.write(row, 1, "Preconditions", bold)
VIS006sheet.write(row, 2, "", normal)
VIS006sheet.write(row, 4, "Pass:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F33:F34, "PASS")', normalright)

row = 29
VIS006sheet.write(row, 1, "Dependencies", bold)
VIS006sheet.write(row, 2, "", normal)
VIS006sheet.write(row, 4, "Fail:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F33:F34, "FAIL")', normalright)

row = 30
VIS006sheet.write(row, 4, "Not executed:", normalright)
VIS006sheet.write(row, 5, '=COUNTIF(F33:F34, "NOT EXECUTED")', normalright)

worksheet.write(VIS_006_2_row, VIS_006_2_col, '=$VIS006.F28', variantbold)

VIS006sheet.add_table('A32:G34')
row = 31
VIS006sheet.write(row, 0, "Step#", boldcenterwhite)
VIS006sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS006sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS006sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS006sheet.write(row, 4, "Actual", boldcenterwhite)
VIS006sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS006sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 32
VIS_006_2_1_row = row
VIS_006_2_1_col = 5
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 0, "1", boldbl)
VIS006sheet.write(row, 1, "In VIS-2, select TXT message and send (upload) to VIS-1 with ACKendpoint", boldbl)
VIS006sheet.write(row, 2, "", boldbl)
VIS006sheet.write(row, 3, "VIS-1 receives the uploaded TXT message", boldbl)
VIS006sheet.write(row, 5, "NOT EXECUTED", bold)

row = 33
VIS_006_2_2_row = row
VIS_006_2_2_col = 5
VIS006sheet.set_row(row, 30)
VIS006sheet.write(row, 0, "2", boldbld)
VIS006sheet.write(row, 1, "No private application retrieves/receives the message", boldbld)
VIS006sheet.write(row, 2, "", boldbld)
VIS006sheet.write(row, 3, "No private application (such as STM Module, ECDIS, etc) retrieves/receives the message.", boldbld)
VIS006sheet.write(row, 5, "NOT EXECUTED", bold)
VIS006sheet.write(row, 6, "What is this test testing? Timeouts somewhere? Why does it fail?", normal)

row = 0
col = 0
VIS007sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS007sheet.write(row, 1, "Executed by", bold)
VIS007sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS007sheet.write(row, 1, "Executed date", bold)
VIS007sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS007sheet.write(row, 0, "", boldblue)
VIS007sheet.write(row, 1, "Test ID", boldblue)
VIS007sheet.merge_range(row, 2, row, 3, "TEST-VIS-007", boldblue)
VIS007sheet.write(row, 3, "", boldblue)
VIS007sheet.write(row, 4, "", boldblue)
VIS007sheet.write(row, 5, "", boldblue)
VIS007sheet.write(row, 6, "", boldblue)

row = 5
VIS007sheet.write(row, 1, "Title", bold)
VIS007sheet.merge_range(row, 2, row, 3, "Main test - –Upload Area Message with ACK request", normal)

row = 6
VIS007sheet.set_row(row, 30)
VIS007sheet.write(row, 1, "Description", bold)
VIS007sheet.merge_range(row, 2, row, 3, "Test send (upload) area message. ACK is requested. The STM Module gets notified by VIS and the message is retrieved.", normal)
VIS007sheet.write(row, 4, "Total:", normalright)
VIS007sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS007sheet.write(row, 1, "Preconditions", bold)
VIS007sheet.write(row, 2, "Configuration A", normal)
VIS007sheet.write(row, 4, "Pass:", normalright)
VIS007sheet.write(row, 5, '=COUNTIF(F12:F13, "PASS")', normalright)

row = 8
VIS007sheet.write(row, 1, "Dependencies", bold)
VIS007sheet.write(row, 2, "VIS, SR, IR, S124", normal)
VIS007sheet.write(row, 4, "Fail:", normalright)
VIS007sheet.write(row, 5, '=COUNTIF(F12:F13, "FAIL")', normalright)

row = 9
VIS007sheet.write(row, 4, "Not executed:", normalright)
VIS007sheet.write(row, 5, '=COUNTIF(F12:F13, "NOT EXECUTED")', normalright)

worksheet.write(VIS_007_row, VIS_007_col, '=$VIS007.F7', mainbold)

VIS007sheet.add_table('A11:G13')
row = 10
VIS007sheet.write(row, 0, "Step#", boldcenterwhite)
VIS007sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS007sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS007sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS007sheet.write(row, 4, "Actual", boldcenterwhite)
VIS007sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS007sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_007_01_row = row
VIS_007_01_col = 5
VIS007sheet.set_row(row, 30)
VIS007sheet.write(row, 0, "1", boldbl)
VIS007sheet.write(row, 1, "VIS-2;  Select S124 message and send (upload) to VIS-1 with ACKendpoint", boldbl)
VIS007sheet.write(row, 2, "", boldbl)
VIS007sheet.write(row, 3, "Message received", boldbl)
VIS007sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_007_02_row = row
VIS_007_02_col = 5
VIS007sheet.set_row(row, 30)
VIS007sheet.write(row, 0, "2", boldbld)
VIS007sheet.write(row, 1, "STM Module retrieves messages from VIS-1", boldbld)
VIS007sheet.write(row, 2, "", boldbld)
VIS007sheet.write(row, 3, "VIS-2 receives ACK", boldbld)
VIS007sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13

row = 14
VIS007sheet.write(row, 0, "", boldblue)
VIS007sheet.write(row, 1, "Test ID", boldblue)
VIS007sheet.merge_range(row, 2, row, 3, "TEST-VIS-007-1", boldblue)
VIS007sheet.write(row, 3, "", boldblue)
VIS007sheet.write(row, 4, "", boldblue)
VIS007sheet.write(row, 5, "", boldblue)
VIS007sheet.write(row, 6, "", boldblue)

row = 15
VIS007sheet.write(row, 1, "Title", bold)
VIS007sheet.merge_range(row, 2, row, 3, "Variant- Upload S124 message with ACK request but no STM Module retrieves the message", normal)

row = 16
VIS007sheet.set_row(row, 30)
VIS007sheet.write(row, 1, "Description", bold)
VIS007sheet.merge_range(row, 2, row, 3, "", normal)
VIS007sheet.write(row, 4, "Total:", normalright)
VIS007sheet.write(row, 5, '=IF(F20>0,"NOT EXECUTED",IF(F19>0,"FAIL","PASS"))', normalright)

row = 17
VIS007sheet.write(row, 1, "Preconditions", bold)
VIS007sheet.write(row, 2, "", normal)
VIS007sheet.write(row, 4, "Pass:", normalright)
VIS007sheet.write(row, 5, '=COUNTIF(F22:F23, "PASS")', normalright)

row = 18
VIS007sheet.write(row, 1, "Dependencies", bold)
VIS007sheet.write(row, 2, "VIS, SR, IR, S124", normal)
VIS007sheet.write(row, 4, "Fail:", normalright)
VIS007sheet.write(row, 5, '=COUNTIF(F22:F23, "FAIL")', normalright)

row = 19
VIS007sheet.write(row, 4, "Not executed:", normalright)
VIS007sheet.write(row, 5, '=COUNTIF(F22:F23, "NOT EXECUTED")', normalright)

worksheet.write(VIS_007_1_row, VIS_007_1_col, '=$VIS007.F17', variantbold)

VIS007sheet.add_table('A21:G23')
row = 20
VIS007sheet.write(row, 0, "Step#", boldcenterwhite)
VIS007sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS007sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS007sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS007sheet.write(row, 4, "Actual", boldcenterwhite)
VIS007sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS007sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 21
VIS_007_1_1_row = row
VIS_007_1_1_col = 5
VIS007sheet.set_row(row, 30)
VIS007sheet.write(row, 0, "1", boldbl)
VIS007sheet.write(row, 1, "In VIS-2, select S124 message and send (upload) to VIS-1 with ACKendpoint", boldbl)
VIS007sheet.write(row, 2, "", boldbl)
VIS007sheet.write(row, 3, "VIS-1 receives the uploaded S124 message", boldbl)
VIS007sheet.write(row, 5, "NOT EXECUTED", bold)

row = 22
VIS_007_1_2_row = row
VIS_007_1_2_col = 5
VIS007sheet.set_row(row, 30)
VIS007sheet.write(row, 0, "2", boldbld)
VIS007sheet.write(row, 1, "No private application retrieves the message", boldbld)
VIS007sheet.write(row, 2, "", boldbld)
VIS007sheet.write(row, 3, "No Acknowledgement received", boldbld)
VIS007sheet.write(row, 5, "NOT EXECUTED", bold)
VIS007sheet.write(row, 6, "What is this test testing? Timeouts somewhere? Why does it fail?", normal)

row = 0
col = 0
VIS009sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS009sheet.write(row, 1, "Executed by", bold)
VIS009sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS009sheet.write(row, 1, "Executed date", bold)
VIS009sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS009sheet.write(row, 0, "", boldblue)
VIS009sheet.write(row, 1, "Test ID", boldblue)
VIS009sheet.merge_range(row, 2, row, 3, "TEST-VIS-009", boldblue)
VIS009sheet.write(row, 3, "", boldblue)
VIS009sheet.write(row, 4, "", boldblue)
VIS009sheet.write(row, 5, "", boldblue)
VIS009sheet.write(row, 6, "", boldblue)

row = 5
VIS009sheet.write(row, 1, "Title", bold)
VIS009sheet.merge_range(row, 2, row, 3, "Main test -  Logging in VIS", normal)

row = 6
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 1, "Description", bold)
VIS009sheet.merge_range(row, 2, row, 3, "Check log in VIS", normal)
VIS009sheet.write(row, 4, "Total:", normalright)
VIS009sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS009sheet.write(row, 1, "Preconditions", bold)
VIS009sheet.write(row, 2, "Messages exchanged with VIS", normal)
VIS009sheet.write(row, 4, "Pass:", normalright)
VIS009sheet.write(row, 5, '=COUNTIF(F12:F24, "PASS")', normalright)

row = 8
VIS009sheet.write(row, 1, "Dependencies", bold)
VIS009sheet.write(row, 2, "VIS, SR, IR, S124", normal)
VIS009sheet.write(row, 4, "Fail:", normalright)
VIS009sheet.write(row, 5, '=COUNTIF(F12:F24, "FAIL")', normalright)

row = 9
VIS009sheet.write(row, 4, "Not executed:", normalright)
VIS009sheet.write(row, 5, '=COUNTIF(F12:F24, "NOT EXECUTED")', normalright)

worksheet.write(VIS_009_row, VIS_009_col, '=$VIS009.F7', mainbold)

VIS009sheet.add_table('A11:G24')
row = 10
VIS009sheet.write(row, 0, "Step#", boldcenterwhite)
VIS009sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS009sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS009sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS009sheet.write(row, 4, "Actual", boldcenterwhite)
VIS009sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS009sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_009_01_row = row
VIS_009_01_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "1", boldbl)
VIS009sheet.write(row, 1, "Open log and check events and data", boldbl)
VIS009sheet.write(row, 2, "", boldbl)
VIS009sheet.write(row, 3, "Times, events and data exchanged logged. Format correct", boldbl)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_009_02_row = row
VIS_009_02_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "2", boldbld)
VIS009sheet.write(row, 1, "Request voyage plan from VIS", boldbld)
VIS009sheet.write(row, 2, "", boldbld)
VIS009sheet.write(row, 3, "", boldbld)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_009_03_row = row
VIS_009_03_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "3", boldbl)
VIS009sheet.write(row, 1, "Request subscription from VIS", boldbl)
VIS009sheet.write(row, 2, "", boldbl)
VIS009sheet.write(row, 3, "", boldbl)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_009_04_row = row
VIS_009_04_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "4", boldbld)
VIS009sheet.write(row, 1, "Remove subscription", boldbld)
VIS009sheet.write(row, 2, "", boldbld)
VIS009sheet.write(row, 3, "", boldbld)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
VIS_009_05_row = row
VIS_009_05_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "5", boldbl)
VIS009sheet.write(row, 1, "Upload voyage plan", boldbl)
VIS009sheet.write(row, 2, "", boldbl)
VIS009sheet.write(row, 3, "", boldbl)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
VIS_009_06_row = row
VIS_009_06_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "6", boldbld)
VIS009sheet.write(row, 1, "Upload text message", boldbld)
VIS009sheet.write(row, 2, "", boldbld)
VIS009sheet.write(row, 3, "", boldbld)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
VIS_009_07_row = row
VIS_009_07_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "7", boldbl)
VIS009sheet.write(row, 1, "Upload area message", boldbl)
VIS009sheet.write(row, 2, "", boldbl)
VIS009sheet.write(row, 3, "", boldbl)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18
VIS_009_08_row = row
VIS_009_08_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "8", boldbld)
VIS009sheet.write(row, 1, "Receive Acknowledgement", boldbld)
VIS009sheet.write(row, 2, "", boldbld)
VIS009sheet.write(row, 3, "", boldbld)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 19
VIS_009_09_row = row
VIS_009_09_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "9", boldbl)
VIS009sheet.write(row, 1, "Send voyage plan to subscribers", boldbl)
VIS009sheet.write(row, 2, "", boldbl)
VIS009sheet.write(row, 3, "", boldbl)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 20
VIS_009_10_row = row
VIS_009_10_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "10", boldbld)
VIS009sheet.write(row, 1, "findServices", boldbld)
VIS009sheet.write(row, 2, "", boldbld)
VIS009sheet.write(row, 3, "", boldbld)
VIS009sheet.write(row, 5, "NOT APPLICABLE", bold)
VIS009sheet.write(row, 6, "Not applicable as we do not use the SSC private API.", normal)

row = 21
VIS_009_11_row = row
VIS_009_11_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "11", boldbl)
VIS009sheet.write(row, 1, "callService", boldbl)
VIS009sheet.write(row, 2, "", boldbl)
VIS009sheet.write(row, 3, "", boldbl)
VIS009sheet.write(row, 5, "NOT APPLICABLE", bold)
VIS009sheet.write(row, 6, "Not applicable as we do not use the SSC private API.", normal)

row = 22
VIS_009_12_row = row
VIS_009_12_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "12", boldbld)
VIS009sheet.write(row, 1, "findIdentities", boldbld)
VIS009sheet.write(row, 2, "", boldbld)
VIS009sheet.write(row, 3, "", boldbld)
VIS009sheet.write(row, 5, "NOT APPLICABLE", bold)
VIS009sheet.write(row, 6, "Not applicable as we do not use the SSC private API.", normal)

row = 23
VIS_009_13_row = row
VIS_009_13_col = 5
VIS009sheet.set_row(row, 30)
VIS009sheet.write(row, 0, "13", boldbl)
VIS009sheet.write(row, 1, "Test both successful calls and erroneous calls", boldbl)
VIS009sheet.write(row, 2, "", boldbl)
VIS009sheet.write(row, 3, "", boldbl)
VIS009sheet.write(row, 5, "NOT EXECUTED", bold)

row = 0
col = 0
VIS010sheet.write(row, 1, "Test Protocol", bold)

row = 1
VIS010sheet.write(row, 1, "Executed by", bold)
VIS010sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
VIS010sheet.write(row, 1, "Executed date", bold)
VIS010sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
VIS010sheet.write(row, 0, "", boldblue)
VIS010sheet.write(row, 1, "Test ID", boldblue)
VIS010sheet.merge_range(row, 2, row, 3, "TEST-VIS-010", boldblue)
VIS010sheet.write(row, 3, "", boldblue)
VIS010sheet.write(row, 4, "", boldblue)
VIS010sheet.write(row, 5, "", boldblue)
VIS010sheet.write(row, 6, "", boldblue)

row = 5
VIS010sheet.write(row, 1, "Title", bold)
VIS010sheet.merge_range(row, 2, row, 3, "Find Voyage Information Services", normal)

row = 6
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 1, "Description", bold)
VIS010sheet.merge_range(row, 2, row, 3, "Test search for voyage information services to consume using different search parameters.", normal)
VIS010sheet.write(row, 4, "Total:", normalright)
VIS010sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
VIS010sheet.write(row, 1, "Preconditions", bold)
VIS010sheet.write(row, 2, "Service Instances registered", normal)
VIS010sheet.write(row, 4, "Pass:", normalright)
VIS010sheet.write(row, 5, '=COUNTIF(F12:F25, "PASS")', normalright)

row = 8
VIS010sheet.write(row, 1, "Dependencies", bold)
VIS010sheet.write(row, 2, "SR, IR", normal)
VIS010sheet.write(row, 4, "Fail:", normalright)
VIS010sheet.write(row, 5, '=COUNTIF(F12:F25, "FAIL")', normalright)

row = 9
VIS010sheet.write(row, 4, "Not executed:", normalright)
VIS010sheet.write(row, 5, '=COUNTIF(F12:F25, "NOT EXECUTED")', normalright)

worksheet.write(VIS_010_row, VIS_010_col, '=$VIS010.F7', mainbold)

VIS010sheet.add_table('A11:G25')
row = 10
VIS010sheet.write(row, 0, "Step#", boldcenterwhite)
VIS010sheet.write(row, 1, "Test Step", boldcenterwhite)
VIS010sheet.write(row, 2, "Test Data", boldcenterwhite)
VIS010sheet.write(row, 3, "Expected Result", boldcenterwhite)
VIS010sheet.write(row, 4, "Actual", boldcenterwhite)
VIS010sheet.write(row, 5, "Pass Fail", boldcenterwhite)
VIS010sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
VIS_010_01_row = row
VIS_010_01_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "1", boldbl)
VIS010sheet.write(row, 1, "Find keyword ROS", boldbl)
VIS010sheet.write(row, 2, "", boldbl)
VIS010sheet.write(row, 3, "", boldbl)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
VIS_010_02_row = row
VIS_010_02_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "2", boldbld)
VIS010sheet.write(row, 1, "Find keyword ROS + SSPA", boldbld)
VIS010sheet.write(row, 2, "", boldbld)
VIS010sheet.write(row, 3, "", boldbld)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
VIS_010_03_row = row
VIS_010_03_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "3", boldbl)
VIS010sheet.write(row, 1, "Find keyword RO", boldbl)
VIS010sheet.write(row, 2, "", boldbl)
VIS010sheet.write(row, 3, "", boldbl)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
VIS_010_04_row = row
VIS_010_04_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "4", boldbld)
VIS010sheet.write(row, 1, "Find keyword ros", boldbld)
VIS010sheet.write(row, 2, "", boldbld)
VIS010sheet.write(row, 3, "", boldbld)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
VIS_010_05_row = row
VIS_010_05_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "5", boldbl)
VIS010sheet.write(row, 1, "Find keyword voyage", boldbl)
VIS010sheet.write(row, 2, "", boldbl)
VIS010sheet.write(row, 3, "", boldbl)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
VIS_010_06_row = row
VIS_010_06_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "6", boldbld)
VIS010sheet.write(row, 1, "Find keyword service", boldbld)
VIS010sheet.write(row, 2, "", boldbld)
VIS010sheet.write(row, 3, "", boldbld)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
VIS_010_07_row = row
VIS_010_07_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "7", boldbl)
VIS010sheet.write(row, 1, "Find IMO 8719188", boldbl)
VIS010sheet.write(row, 2, "", boldbl)
VIS010sheet.write(row, 3, "", boldbl)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18
VIS_010_08_row = row
VIS_010_08_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "8", boldbld)
VIS010sheet.write(row, 1, "Find ship VIS by MMSI", boldbld)
VIS010sheet.write(row, 2, "", boldbld)
VIS010sheet.write(row, 3, "", boldbld)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 19
VIS_010_09_row = row
VIS_010_09_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "9", boldbl)
VIS010sheet.write(row, 1, "Find ship VIS by serviceType", boldbl)
VIS010sheet.write(row, 2, "", boldbl)
VIS010sheet.write(row, 3, "", boldbl)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 20
VIS_010_10_row = row
VIS_010_10_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "10", boldbld)
VIS010sheet.write(row, 1, "Find IMO 8719188 + Keyword ROS", boldbld)
VIS010sheet.write(row, 2, "", boldbld)
VIS010sheet.write(row, 3, "", boldbld)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 21
VIS_010_11_row = row
VIS_010_11_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "11", boldbl)
VIS010sheet.write(row, 1, "Find Route Optimization Service to consume", boldbl)
VIS010sheet.write(row, 2, "", boldbl)
VIS010sheet.write(row, 3, "", boldbl)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 22
VIS_010_12_row = row
VIS_010_12_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "12", boldbld)
VIS010sheet.write(row, 1, "Find Route Check Service to consume", boldbld)
VIS010sheet.write(row, 2, "", boldbld)
VIS010sheet.write(row, 3, "", boldbld)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 23
VIS_010_13_row = row
VIS_010_13_col = 5
VIS010sheet.set_row(row, 30)
VIS010sheet.write(row, 0, "13", boldbl)
VIS010sheet.write(row, 1, "Find Enhanced Monitoring Service to consume", boldbl)
VIS010sheet.write(row, 2, "", boldbl)
VIS010sheet.write(row, 3, "", boldbl)
VIS010sheet.write(row, 5, "NOT EXECUTED", bold)

row = 0
col = 0
SPIS001sheet.write(row, 1, "Test Protocol", bold)

row = 1
SPIS001sheet.write(row, 1, "Executed by", bold)
SPIS001sheet.merge_range(row, 2, row, 3, "Karri Kaksonen", bold)

row = 2
SPIS001sheet.write(row, 1, "Executed date", bold)
SPIS001sheet.merge_range(row, 2, row, 3, time.strftime("%Y-%m-%d %H:%M"), bold)

row = 3

row = 4
SPIS001sheet.write(row, 0, "", boldblue)
SPIS001sheet.write(row, 1, "Test ID", boldblue)
SPIS001sheet.merge_range(row, 2, row, 3, "TEST-SPIS-001", boldblue)
SPIS001sheet.write(row, 3, "", boldblue)
SPIS001sheet.write(row, 4, "", boldblue)
SPIS001sheet.write(row, 5, "", boldblue)
SPIS001sheet.write(row, 6, "", boldblue)

row = 5
SPIS001sheet.write(row, 1, "Title", bold)
SPIS001sheet.merge_range(row, 2, row, 3, "Publish Port Call Message", normal)

row = 6
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 1, "Description", bold)
SPIS001sheet.merge_range(row, 2, row, 3, "Nominate port and publish PortCall Messages to PortCDM@Port", normal)
VIS010sheet.write(row, 4, "Total:", normalright)
VIS010sheet.write(row, 5, '=IF(F10>0,"NOT EXECUTED",IF(F9>0,"FAIL","PASS"))', normalright)

row = 7
SPIS001sheet.write(row, 1, "Preconditions", bold)
SPIS001sheet.write(row, 2, "PortCDM service registered in SR for SEGOT", normal)
SPIS001sheet.write(row, 4, "Pass:", normalright)
SPIS001sheet.write(row, 5, '=COUNTIF(F12:F25, "PASS")', normalright)

row = 8
SPIS001sheet.write(row, 1, "Dependencies", bold)
SPIS001sheet.write(row, 2, "SPIS for IMO 7505346, YMER, PortCDM, SSC, Service and Identity Registry", normal)
SPIS001sheet.write(row, 4, "Fail:", normalright)
SPIS001sheet.write(row, 5, '=COUNTIF(F12:F25, "FAIL")', normalright)

row = 9
SPIS001sheet.write(row, 4, "Not executed:", normalright)
SPIS001sheet.write(row, 5, '=COUNTIF(F12:F25, "NOT EXECUTED")', normalright)

worksheet.write(SPIS_001_row, SPIS_001_col, '=$SPIS001.F7', mainbold)

SPIS001sheet.add_table('A11:G25')
row = 10
SPIS001sheet.write(row, 0, "Step#", boldcenterwhite)
SPIS001sheet.write(row, 1, "Test Step", boldcenterwhite)
SPIS001sheet.write(row, 2, "Test Data", boldcenterwhite)
SPIS001sheet.write(row, 3, "Expected Result", boldcenterwhite)
SPIS001sheet.write(row, 4, "Actual", boldcenterwhite)
SPIS001sheet.write(row, 5, "Pass Fail", boldcenterwhite)
SPIS001sheet.write(row, 6, "Findings & Comments", boldcenterwhite)

row = 11
SPIS_001_01_row = row
SPIS_001_01_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "0", boldbl)
SPIS001sheet.write(row, 1, "Preparation: No active distribution of PCM to PortCDM", boldbl)
SPIS001sheet.write(row, 2, "", boldbl)
SPIS001sheet.write(row, 3, "", boldbl)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 12
SPIS_001_02_row = row
SPIS_001_02_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "1", boldbld)
SPIS001sheet.write(row, 1, "STM Module->SPIS-1: Nominate PortCDM@Port SEGOT to data (local or global port call id)", boldbld)
SPIS001sheet.write(row, 2, "", boldbld)
SPIS001sheet.write(row, 3, "", boldbld)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 13
SPIS_001_03_row = row
SPIS_001_03_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "2", boldbld)
SPIS001sheet.write(row, 1, "STM Module->SPIS-1: Publish TTA to nominated port", boldbld)
SPIS001sheet.write(row, 2, "PCM-001", boldbld)
SPIS001sheet.write(row, 3, "PortCDM-1 received the published PCM", boldbld)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 14
SPIS_001_04_row = row
SPIS_001_04_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "3", boldbld)
SPIS001sheet.write(row, 1, "STM Module->SPIS-1: Publish ETA to nominated port", boldbld)
SPIS001sheet.write(row, 2, "PCM-002", boldbld)
SPIS001sheet.write(row, 3, "PortCDM-1 received the published PCM", boldbld)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 15
SPIS_001_05_row = row
SPIS_001_05_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "3", boldbld)
SPIS001sheet.write(row, 1, "STM Module->SPIS-1: Publish ATA to nominated port", boldbld)
SPIS001sheet.write(row, 2, "PCM-003", boldbld)
SPIS001sheet.write(row, 3, "PortCDM-1 received the published PCM", boldbld)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 16
SPIS_001_06_row = row
SPIS_001_06_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "4", boldbld)
SPIS001sheet.write(row, 1, "STM Module->SPIS-1: Publish TTD to nominated port", boldbld)
SPIS001sheet.write(row, 2, "PCM-004", boldbld)
SPIS001sheet.write(row, 3, "PortCDM-1 received the published PCM", boldbld)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 17
SPIS_001_07_row = row
SPIS_001_07_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "4", boldbld)
SPIS001sheet.write(row, 1, "STM Module->SPIS-1: Publish ETD to nominated port", boldbld)
SPIS001sheet.write(row, 2, "PCM-005", boldbld)
SPIS001sheet.write(row, 3, "PortCDM-1 received the published PCM", boldbld)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

row = 18
SPIS_001_08_row = row
SPIS_001_08_col = 5
SPIS001sheet.set_row(row, 30)
SPIS001sheet.write(row, 0, "5", boldbld)
SPIS001sheet.write(row, 1, "STM Module->SPIS-1: Publish ATD to nominated port", boldbld)
SPIS001sheet.write(row, 2, "PCM-006", boldbld)
SPIS001sheet.write(row, 3, "PortCDM-1 received the published PCM", boldbld)
SPIS001sheet.write(row, 5, "NOT EXECUTED", bold)

'''

f = open('create_worksheet.py', 'w')
f.write(init_workbook)
f.close()

