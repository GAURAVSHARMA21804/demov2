# import json
# from app import app
# from model.update_model import update_model
# from flask import request
# obj1 = update_model()

# @app.route("/test/headlamp/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addHeadlampTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     # img = request_data.get('img', '')
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     # img = "hh"
#     # img_bytes = base64.b64decode(img_base64)
#     return obj1.addHeadlampTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 


# #TAB_LIGHTTEST_TWO
# @app.route("/test/toplight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<p6>/<remark>/<status>", methods=["POST"])
# def addTopLightTest_one_update(id,p1,p2,p3,p4,p5,p6,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTopLightTest_one_model_update(id,p1,p2,p3,p4,p5,p6,remark,status,img) 


# #TAB_LIGHTTEST_THREE
# @app.route("/test/stoplight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addStopLightTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addStopLightTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 


# #TAB_LIGHTTEST_FOUR
# @app.route("/test/parkinglight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addParkingLightTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addParkingLightTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 


# #TAB_FOGLIGHTTEST_FIVE
# @app.route("/test/foglight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addFogLightTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addFogLightTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 


# #TAB_WARNINGLIGHTTEST_FIVE
# @app.route("/test/warninglight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addWarningLightTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addWarningLightTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 


# #TAB_NUMBEPLATELIGHTTEST_FIVE
# @app.route("/test/numberplatelight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addPlateLightTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addPlateLightTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 


# #TAB_MARKERLIGHTTEST_FIVE
# @app.route("/test/markerlight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addMarkerLightTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addMarkerLightTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 


# #TAB_DIRECTIONLIGHTTEST_FIVE
# @app.route("/test/directionlight/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addDirectionLightTest_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addDirectionLightTest_one_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 

# #TAB_DIRECTIONLIGHTTEST_FIVE
# @app.route("/test/hazardlight/update/<id>/<p1>/<p2>/<remark>/<status>", methods=["POST"])
# def addHazardLightTest_one_update(id,p1,p2,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addHazardLightTest_one_model_update(id,p1,p2,remark,status,img) 



# #TAB_SUPRESSORTEST_ONE
# @app.route("/test/suppressor/update/<id>/<p1>/<p2>/<p3>/<remark>/<status>", methods=["POST"])
# def addSupressorTest_one_update(id,p1,p2,p3,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addSupressorTest_one_model_update(id,p1,p2,p3,remark,status,img) 


# #TAB_REAR_MIRROR
# @app.route("/test/rearmirror/update/<id>/<p1>/<remark>/<status>", methods=["POST"])
# def addRearMirror_one_update(id,p1,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addRearMirror_model_update(id,p1,remark,status,img) 





# #TAB_SAFETYGLASSTEST_ONE
# @app.route("/test/safetyglass/update/<id>/<p1>/<p2>/<p3>/<remark>/<status>", methods=["POST"])
# def addSafetyGlassTest_one_update(id,p1,p2,p3,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addSafetyGlassTest_one_model_update(id,p1,p2,p3,remark,status,img) 


# #TAB_HORNTEST_ONE
# @app.route("/test/horn/update/<id>/<p1>/<p2>/<p3>/<p4>/<remark>/<status>", methods=["POST"])
# def addHornTest_one_update(id,p1,p2,p3,p4,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addHornTest_one_model_update(id,p1,p2,p3,p4,remark,status,img) 

# #TAB_WIPERBLADETEST_ONE
# @app.route("/test/wblade/update/<id>/<p1>/<p2>/<remark>/<status>", methods=["POST"])
# def addwbladeTest_one_update(id,p1,p2,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addwbladeTest_one_model_update(id,p1,p2,remark,status,img) 

# #TAB_WIPERSYSTEMTEST_ONE
# @app.route("/test/wsystem/update/<id>/<p1>/<p2>/<remark>/<status>", methods=["POST"])
# def addwsystemTest_one_update(id,p1,p2,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addwsystemTest_one_model_update(id,p1,p2,remark,status,img) 

# #TAB_EXHAUSTTEST_ONE
# @app.route("/test/exhaust/update/<id>/<p1>/<p2>/<p3>/<p4>/<remark>/<status>", methods=["POST"])
# def addexhaustTest_one_update(id,p1,p2,p3,p4,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addexhaustTest_one_model_update(id,p1,p2,p3,p4,remark,status,img) 


# #TAB_DASHTEST_ONE
# @app.route("/test/dash/update/<id>/<p1>/<p2>/<p3>/<p4>/<remark>/<status>", methods=["POST"])
# def addDashTest_one_update(id,p1,p2,p3,p4,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addDashTest_one_model_update(id,p1,p2,p3,p4,remark,status,img) 


# #TAB_BRAKING_MANUAL_ONE
# @app.route("/test/brakingmanual/update/<id>/<p1>/<p2>/<p3>/<remark>/<status>", methods=["POST"])
# def addTestBraking_one_update(id,p1,p2,p3,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestBraking_model_update(id,p1,p2,p3,remark,status,img) 


# #TAB_PARKING_BRAKING_MANUAL_ONE
# @app.route("/test/parkingbrakingmanual/update/<id>/<p1>/<p2>/<p3>/<remark>/<status>", methods=["POST"])
# def addTestParkingBraking_one_update(id,p1,p2,p3,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestParkingBraking_model_update(id,p1,p2,p3,remark,status,img) 


# #TAB_STEERING_ONE
# @app.route("/test/steering/update/<id>/<p1>/<remark>/<status>", methods=["POST"])
# def addTestSteering_one_update(id,p1,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestSteering_model_update(id,p1,remark,status,img) 


# #TAB_JOINTPLAY
# @app.route("/test/jointplay/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<p6>/<p7>/<p8>/<remark>/<status>", methods=["POST"])
# def addTestJointPlay_one_update(id,p1,p2,p3,p4,p5,p6,p7,p8,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestJointPlay_model_update(id,p1,p2,p3,p4,p5,p6,p7,p8,remark,status,img) 


# #TAB_SPEEDOMETERMANUAL
# @app.route("/test/speedometermanual/update/<id>/<p1>/<p2>/<p3>/<p4>/<remark>/<status>", methods=["POST"])
# def addTestSpeedometerManual_one_update(id,p1,p2,p3,p4,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestSpeedometerManual_model_update(id,p1,p2,p3,p4,remark,status,img) 


# #TAB_LUPD
# @app.route("/test/rupd/update/<id>/<p1>/<p2>/<p3>/<remark>/<status>", methods=["POST"])
# def addTestrupd_one_update(id,p1,p2,p3,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestrupd_model_update(id,p1,p2,p3,remark,status,img) 

# #TAB_RUPD
# @app.route("/test/lupd/update/<id>/<p1>/<p2>/<p3>/<remark>/<status>", methods=["POST"])
# def addTestlupd_one_update(id,p1,p2,p3,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestlupd_model_update(id,p1,p2,p3,remark,status,img) 


# #TAB_FASTAG
# @app.route("/test/fastag/update/<id>/<p1>/<p2>/<remark>/<status>", methods=["POST"])
# def addTestfastag_one_update(id,p1,p2,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestfastag_model_update(id,p1,p2,remark,status,img) 

# #TAB_OTHERS
# @app.route("/test/others/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<p6>/<p7>/<p8>/<remark>/<status>", methods=["POST"])
# def addTestothers_one_update(id,p1,p2,p3,p4,p5,p6,p7,p8,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestothers_model_update(id,p1,p2,p3,p4,p5,p6,p7,p8,remark,status,img) 


# #TAB_WHEEL
# @app.route("/test/wheel/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<p6>/<remark>/<status>", methods=["POST"])
# def addTestWheel_one_update(id,p1,p2,p3,p4,p5,p6,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestWheel_model_update(id,p1,p2,p3,p4,p5,p6,remark,status,img) 



# #TAB_VLT
# @app.route("/test/vlt/update/<id>/<p1>/<p2>/<remark>/<status>", methods=["POST"])
# def addTestVlt_one_update(id,p1,p2,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestVlt_model_update(id,p1,p2,remark,status,img) 



# #TAB_HSRP
# @app.route("/test/hsrp/update/<id>/<p1>/<p2>/<remark>/<status>", methods=["POST"])
# def addTestHsrp_one_update(id,p1,p2,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestHsrp_model_update(id,p1,p2,remark,status,img) 


# #TAB_BATTERY
# @app.route("/test/battery/update/<id>/<p1>/<p2>/<p3>/<remark>/<status>", methods=["POST"])
# def addTestBattery_one_update(id,p1,p2,p3,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestBattery_model_update(id,p1,p2,p3,remark,status,img) 

# #TAB_SAFETYBELT
# @app.route("/test/safetybelt/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addTestSafetyBelt_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestSafetyBelt_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 

# #TAB_SPEEDGOVERNER
# @app.route("/test/speedgoverner/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<remark>/<status>", methods=["POST"])
# def addTestSpeedG_one_update(id,p1,p2,p3,p4,p5,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestSpeedG_model_update(id,p1,p2,p3,p4,p5,remark,status,img) 

# #TAB_TESTSPRAY
# @app.route("/test/spray/update/<id>/<p1>/<remark>/<status>", methods=["POST"])
# def addTestSpray_one_update(id,p1,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestSpray_model_update(id,p1,remark,status,img) 

# #TAB_TYRES
# @app.route("/test/tyres/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<p6>/<remark>/<status>", methods=["POST"])
# def addTestTyres_one_update(id,p1,p2,p3,p4,p5,p6,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestTyres_model_update(id,p1,p2,p3,p4,p5,p6,remark,status,img) 

# #TAB_RETRO
# @app.route("/test/retro/update/<id>/<p1>/<p2>/<p3>/<p4>/<p5>/<p6>/<p7>/<p8>/<p9>/<remark>/<status>", methods=["POST"])
# def addTestRetro_one_update(id,p1,p2,p3,p4,p5,p6,p7,p8,p9,remark,status):
#     request_data = json.loads(request.data)
#     print(request_data)
#     img = request_data.get('nameValuePairs', {}).get('img', '')
#     print(img)
#     return obj1.addTestRetro_model_update(id,p1,p2,p3,p4,p5,p6,p7,p8,p9,remark,status,img) 

