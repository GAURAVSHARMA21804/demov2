# from datetime import datetime
# from io import BytesIO
# import time
# from tkinter import Image
# import traceback
# import mysql.connector
# import base64
# import json
# import os
# from flask import jsonify, make_response
# import pytz
# class update_model():
#     def __init__(self):
#         try:
#             self.con =  mysql.connector.connect(host="localhost",user="root",password="Ga2001pillu14##",database="vft_app")
#             self.con.autocommit = True
#             self.con.connect_timeout = 25
#             self.cur = self.con.cursor(dictionary=True)
#             self.con2 =  mysql.connector.connect(host="localhost",user="root",password="Ga2001pillu14##",database="dunit")
#             self.con2.autocommit = True
#             self.con2.connect_timeout = 25
#             self.cur2 = self.con2.cursor(dictionary=True)
#             print("success")
#         except mysql.connector.Error as err:
#             print(f"Error: {err}")
    
#     # 1 UPDATE HEADLMAP TEST ONE
#     def addHeadlampTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testheadlamp
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#             UPDATE tests
#             SET testheadlamp = %s
#             WHERE id = %s
#         """, (status, id))
#             self.con.commit()
#             # print(len(img))
#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},402)
        

#     # 2 UPDATE TOPLIGHT TEST ONE
#     def addTopLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,p6,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testtoplight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, p6 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, p6, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testtoplight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# # 3 UPDATE STOPLIGHT TEST ONE
#     def addStopLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE teststoplight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET teststoplight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             traceback.print_exc()
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# # 4 UPDATE PARKINGLIGHT TEST ONE
#     def addParkingLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testparkinglight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testparkinglight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# # 5 UPDATE FOGLIGHT TEST ONE
#     def addFogLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testfoglight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testfoglight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# # 6 UPDATE WARNINGLIGHT TEST ONE
#     def addWarningLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testwarninglight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testwarninglight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# #7 UPDATE NUMBEPLATELIGHT TEST ONE
#     def addPlateLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testnumberplatelight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testnumberplatelight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# # 8 UPDATE MARKERLIGHT TEST ONE
#     def addMarkerLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testoutlinemarkerlight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testoutlinemarkerlight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# # 9 UPDATE MARKERLIGHT TEST ONE
#     def addDirectionLightTest_one_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testdirectionlight
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testdirectionlight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

# # 10 UPDATE HAZARDLIGHT TEST ONE
#     def addHazardLightTest_one_model_update(self, id,p1,p2,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testhazardlight
#                        SET p1 = %s, p2 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testhazardlight = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     # 11 UPDATE SUPRESSOR TEST ONE
#     def addSupressorTest_one_model_update(self, id,p1,p2,p3,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testsupressor
#                        SET p1 = %s, p2 = %s, p3 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testsupressor = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             traceback.print_exc()
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     # 12 UPDATE REAR MIRROR ONE
#     def addRearMirror_model_update(self, id,p1,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testrearmirror
#                        SET p1 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testrearmirror = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(e)
#             traceback.print_exc()
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

  
#     # 13 UPDATE SAFETY GLASS TEST ONE
#     def addSafetyGlassTest_one_model_update(self, id,p1,p2,p3,remark,status,img):
#         try:
#             self.con.start_transaction()
            
#             self.cur.execute(""" UPDATE testsafetyglass
#                        SET p1 = %s, p2 = %s, p3 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testsafetyglass = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#     # 14 UPDATE HORN TEST ONE
#     def addHornTest_one_model_update(self, id,p1,p2,p3,p4,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testhorn
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testhorn = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             print(e)
#             return make_response({"status":"Rolled Back"},400)

#     # 15 UPDATE EXHAUST TEST ONE
#     def addexhaustTest_one_model_update(self, id,p1,p2,p3,p4,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testsilencer
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testsilencer = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#     # 16 UPDATE WIPER SYSTEM TEST ONE
#     def addwsystemTest_one_model_update(self, id,p1,p2,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testwipersystem
#                        SET p1 = %s, p2 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testwipersystem = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#     # 17 UPDATE WIPER BLADE TEST ONE
#     def addwbladeTest_one_model_update(self, id,p1,p2,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testwiperblade
#                        SET p1 = %s, p2 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testwiperblade = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#     # 18 UPDATE DASH TEST ONE
#     def addDashTest_one_model_update(self, id,p1,p2,p3,p4,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testdashboard
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testdashboard = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#     # 19 UPDATE TEST BRAKING MANUAL
#     def addTestBraking_model_update(self, id,p1,p2,p3,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testbrakingmanual
#                        SET p1 = %s, p2 = %s, p3 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testbrakingmanual = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#     # 20 UPDATE TEST PARKING BRAKING MANUAL
#     def addTestParkingBraking_model_update(self, id,p1,p2,p3,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testparkingbrakingmanual
#                        SET p1 = %s, p2 = %s, p3 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testparkingbrakingmanual = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#     #21 UPDATE TEST STEERING MANUAL
#     def addTestSteering_model_update(self, id,p1,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE teststeering
#                        SET p1 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET teststeering = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     # 22 UPDATE TEST JOINTPLAY MANUAL
#     def addTestJointPlay_model_update(self, id,p1,p2,p3,p4,p5,p6,p7,p8,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testjointplay
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, p6 = %s, p7 = %s, p8 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, p6, p7, p8, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testjointplay = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     # 23 UPDATE TEST SPEEDOMETER MANUAL
#     def addTestSpeedometerManual_model_update(self, id,p1,p2,p3,p4,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testspeedometermanual
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testspeedometermanual = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     # 24  UPDATE TEST RUPD MANUAL
#     def addTestrupd_model_update(self, id,p1,p2,p3,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testrupd
#                        SET p1 = %s, p2 = %s, p3 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testrupd = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     #25 UPDATE TEST LUPD MANUAL
#     def addTestlupd_model_update(self, id,p1,p2,p3,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testlupd
#                        SET p1 = %s, p2 = %s, p3 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testlupd = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     #26 UPDATE TEST FASTAG MANUAL
#     def addTestfastag_model_update(self, id,p1,p2,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testfastag
#                        SET p1 = %s, p2 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testfastag = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             traceback.print_exc()
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)
 

#     # 27 UPDATE TEST OTHERS
#     def addTestothers_model_update(self, id,p1,p2,p3,p4,p5,p6,p7,p8,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testothers
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, p6 = %s, p7 = %s, p8 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, p6, p7, p8, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testothers = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             traceback.print_exc()
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     # 28 UPDATE TEST WHEEL
#     def addTestWheel_model_update(self, id,p1,p2,p3,p4,p5,p6,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testwheel
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, p6 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, p6, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testwheel = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)


#     # 29 UPDATE TEST VLT
#     def addTestVlt_model_update(self, id,p1,p2,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testvlt
#                        SET p1 = %s, p2 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testvlt = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)
 

#     # 30 UPDATE TEST HSRP
#     def addTestHsrp_model_update(self, id,p1,p2,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testhsrp
#                        SET p1 = %s, p2 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testhsrp = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test Added"},200)
#             else:
#                 return make_response({"status":"Cannot add test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)
 
 
#     # 31 UPDATE TEST BATTERY
#     def addTestBattery_model_update(self, id,p1,p2,p3,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testbattery
#                        SET p1 = %s, p2 = %s, p3 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testbattery = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)
 
  
#     # 32 UPDATE TEST SAFETYBELT
#     def addTestSafetyBelt_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testsafetybelt
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testsafetybelt = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)
 
  
#     # 33 UPDATE TEST SPEED GOVERNER
#     def addTestSpeedG_model_update(self, id,p1,p2,p3,p4,p5,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testspeedgoverner
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testspeedgoverner = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)
 


#     # 34 UPDATE TEST SPRAY
#     def addTestSpray_model_update(self, id,p1,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testspray
#                        SET p1 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1,remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testspray = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)
 


#     # 35 UPDATE TEST TYRES
#     def addTestTyres_model_update(self, id,p1,p2,p3,p4,p5,p6,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testtyres
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, p6 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, p6, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testtyres = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)

#   # 36 UPDATE TEST TYRES
#     def addTestRetro_model_update(self, id,p1,p2,p3,p4,p5,p6,p7,p8,p9,remark,status,img):
#         try:
#             self.con.start_transaction()

#             self.cur.execute(""" UPDATE testretro
#                        SET p1 = %s, p2 = %s, p3 = %s, p4 = %s, p5 = %s, p6 = %s, p7 = %s, p8 = %s, p9 = %s, remark = %s, status = %s, img = %s
#                        WHERE id = %s """, (p1, p2, p3, p4, p5, p6, p7, p8, p9, remark, status, img, id))
#             self.cur.execute("""
#                UPDATE tests
#                 SET testretro = %s
#                 WHERE id = %s
#                     """, (status, id))
#             self.con.commit()

#             result =  self.cur.fetchone()
#             if self.cur.rowcount>0:
#                 return make_response({"status":"Test updated"},200)
#             else:
#                 return make_response({"status":"Cannot update test"},401)
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             traceback.print_exc()
#             self.con.rollback()
#             return make_response({"status":"Rolled Back"},400)



