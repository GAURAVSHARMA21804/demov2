import mysql.connector
from datetime import timedelta
import re
import json
from flask import make_response,jsonify
from datetime import datetime
import pytz
import traceback
# class user_model():
#     def _init_(self):
#         try:
#             mCon=mysql.connector.connect(host="localhost",user="root",password="Ga2001pillu14##",database="dunit")
#             self.cur=mCon.cursor(dictionary=True)
#             mCon.autocommit=True
#             print("connected successfully")
#         except:
#             print("some error")
            
#     def user_getall_model(self):
#         self.cur.execute("SELECT * FROM stations")
#         result=self.cur.fetchall()
#         if len(result)>0:
#             res = make_response({'payload':result},200)
#             res.headers['Access-Control-Allow-Origin']="*"
#             return res
#         else:
#             return make_response({"message":"No Data found"},204)
        
        
#     def user_addone_model(self,data):
#         self.cur.execute(f"INSERT INTO users(id,name,email,phone,password,role) VALUES({data['id']},'{data['name']}','{data['email']}','{data['phone']}','{data['password']}','{data['role']}')")
        
        
#         return make_response({"message":"user created successfully"},201)

            

class demo_display_unit_model():
    def __init__(self):
        try:
            # self.con2=mysql.connector.connect(host="localhost",user="root",password="Hello123##",database="dunitv2")
            # self.cur2=self.con2.cursor(dictionary=True)
            # self.con2.autocommit=True
            self.con2=mysql.connector.connect(host="localhost",user="root",password="Ga2001pillu14##",database="dunitv2")
            self.cur2=self.con2.cursor(dictionary=True)
            self.con2.autocommit=True
            print("connected successfully")

            self.pool=mysql.connector.pooling.MySQLConnectionPool(
                pool_name="my_pool",
                pool_size=20,
                pool_reset_session=True,
                host="localhost",user="root",password="Ga2001pillu14##",database="dunitv2")

        except:
            print("some error")
    
    # def get_con2(self):
        
    #     return self.con2

    def operator_check_model(self):
        mCon = self.pool.get_connection()
        try:
            # if not mCon.is_connected():
            #     mCon.reconnect()
            cur = mCon.cursor(dictionary = True)

            cur.execute("SELECT * from login_operator")
            result = cur.fetchall()

            if len(result)>0:
            # return json.dumps(result)
            # return{"payload": result}
                res = make_response({"payload": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
            # return {"message":"No Data Found"}
                return make_response({"message":"No Data Found"},204)
             # message is not shown for 204   
        except:
                return make_response({"message":"Exception Caught"},205)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close() 
###########################   LOGIN API   ##########3################
    def operator_login_model(self,data):
        mCon = self.pool.get_connection()

        try:
            cur = mCon.cursor(dictionary = True)
            employee_code = data.get('employee_code')
            password = data.get('password')
            # Construct and execute the query
            query = f"SELECT * FROM login_operator WHERE employee_code = '{employee_code}' AND password = '{password}'"
            
            # if not mCon.is_connected():
            #     mCon.reconnect()
        
            cur.execute(query)
            result = cur.fetchone()
            cur.nextset()

            if result is not None:
                # return json.dumps(result)
            # return{"payload": result}
                res = make_response({"logindata": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
            # return {"message":"No Data Found"}
                print("good")
                res = make_response({"logindata":"No Data Found"},401)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res =  make_response({"logindata":"Got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()



###########################   GET TASK API   ##########################
    def operator_gettask_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            station_id = data.get('station_id')
            split_items = station_id.split()
            # print(split_items)
            if len(split_items) == 3:
                F1, L1, S1 = split_items

                # Further split each part
                F1_part1, F1_part2 = F1[0], F1[1:]
                L1_part1, L1_part2 = L1[0], L1[1:]
                S1_part1, S1_part2 = S1[0], S1[1:]

                # print("F1:", F1_part1, F1_part2)
                # print("L1:", L1_part1, L1_part2)
                # print("S1:", S1_part1, S1_part2)

                query = f"SELECT * FROM task_assigned WHERE line_id = '{L1_part2}' AND floor_id = '{F1_part2}'"
                
                # with mCon.cursor(dictionary=True) as cur:
                #     if not mCon.is_connected():
                #         mCon.reconnect()
                    
                cur.execute(query)
                result = cur.fetchone()
                cur.nextset()

                if result is not None:
                    res = make_response({"taskdata": result},200)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
                else:
                    print("good")
                    res = make_response({"taskdata":"No task assigned"},201)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
                    
            else:
                res = make_response({"taskdata": "Invalid Station ID"},202)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res 
        except:
            traceback.print_exc()
            res = make_response({"taskdata":"Got error"},203)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()


###########################   LOGIN ADMIN API   ##########################
    def operator_loginadmin_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            employee_code = data.get('employee_code')
            password = data.get('password')

            # Construct and execute the query
            query = f"SELECT * FROM login_admin WHERE employee_code = '{employee_code}' AND password = '{password}'"
            
            # if not mCon.is_connected():
                # mCon.reconnect()

            cur.execute(query)
            result = cur.fetchone()
            cur.nextset()


            if result is not None:
                # return json.dumps(result)
                # return{"payload": result}
                res = make_response({"logindata": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"logindata":"No Data Found"},401)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                    # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            cur.nextset()
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            traceback.print_exc()
            res = make_response({"logindata":"Got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()


###########################   GET FLOOR DETAILS API   ##########################
    def floor_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            floor_id = data.get('floor_id')
        
            # Construct and execute the query
            query = f"SELECT * FROM floors WHERE floor_id = '{floor_id}'"


            # if not mCon.is_connected():
                # mCon.reconnect()

            cur.execute(query)
            result = cur.fetchone()
            cur.nextset()

            if result is not None:
                # return json.dumps(result)
                # return{"payload": result}
                res = make_response({"floordata": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"floordata":"No Data Found"},401)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                    # message is not shown for 204 
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            traceback.print_exc()
            res = make_response({"floordata":"Got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()


    def reconnectItAgain(self, e):
        if e.errno == mysql.connector.errorcode.CR_SERVER_LOST or e.errno == mysql.connector.errorcode.CR_SERVER_GONE_ERROR:
            # Reconnect to the database
            mCon.close()
            mCon = mysql.connector.connect(
                host="10.0.3.101",
                user="DU_USER",
                password="Interface@123",
                database="DU_APP"
                # host="localhost",
                # user="root",
                # password="Ga2001pillu14##",
                # database="dunitv2"
            )
            # cur = mCon.cursor(dictionary=True)
            # Retry the query
            # cur.execute(query)
            # mCon.commit()
        else:
            raise e
        
###########################   GET STATIONS DETAILS API   ##########################
    def station_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            floor_id = data.get('floor_id')
            # Construct and execute the query
            query = f"SELECT * FROM stations"
            # if not mCon.is_connected():
            #     mCon.reconnect()
            cur.execute(query)
            result = cur.fetchall()
            print(result)

            if result is not None:
                transformed_data = []
                for row in result:
                    floor_num, line_num, station_number = row['station_id'].split(' ')
                    transformed_row = {
                        'station_id': row['station_id'],
                        'floor_num': int(floor_num[1:]),  # Extract numeric part and convert to int
                        'line_num': int(line_num[1:]),
                        'station_num': row['station_num'],
                        'e_one': row['e_one'],
                        'e_one_name': row['e_one_name'],
                        'e_one_skill': row['e_one_skill'],
                        'e_two': row['e_two'],
                        'e_two_name': row['e_two_name'],
                        'e_two_skill': row['e_two_skill'],
                        'process_id': row['process_id'],
                        'process_name': row['process_name'],
                        'process_skill': row['process_skill']
                    }
                    process_id=row['process_id']
                    query_for_process=f"SELECT is_chart_available FROM processes WHERE process_id = '{process_id}'"
                    cur.execute(query_for_process)
                    process_result = cur.fetchone()
                    cur.nextset()
                    is_chart_available=process_result['is_chart_available']
                    transformed_row['is_chart_available']=is_chart_available
                    # print(floor_id)
                    print(transformed_row.get('station_num'))
                    if str(int(floor_num[1:])) == str(floor_id):
                        transformed_data.append(transformed_row)
                
                
                # Return the transformed data in JSON format
                print(transformed_data)
                response = make_response(jsonify({'stationdata': transformed_data}), 200)
                response.headers['Access-Control-Allow-Origin'] = "*"
                response.headers['Content-Type'] = 'application/json'
                return response
            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"stationdata":"No Data Found"},401)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res = make_response({"stationdata":"got error"},401)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()
###########################   ADD LINE API   ##########################
    def add_line_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            floor_id = data.get('floor_id')
            part_id = data.get('part_id')
            part_name = data.get('part_name')
            # Construct and execute the query
            query = f"SELECT number_of_lines FROM floors WHERE floor_id = '{floor_id}'"
            # with mCon.cursor(dictionary=True) as cur:
            # if not mCon.is_connected():
            #     mCon.reconnect()
    
            cur.execute(query)
            result = cur.fetchone()
            cur.nextset()
        
            if result is not None:
                number_of_lines = int(result.get('number_of_lines', 0))
                a = "Vivo_PCB_x48"
                b = "1"
                c = number_of_lines + 1
                # print(result)
                # print(number_of_lines)
                mCon.start_transaction()
                query_update = f"UPDATE floors SET number_of_lines = '{number_of_lines}' + 1 WHERE floor_id = '{floor_id}'"
                cur.execute(query_update)
                query = "INSERT INTO assigned_parts (line_id, part_id, part_name) VALUES (%s, %s, %s)"
                values = (c, part_id,part_name)
                cur.execute(query,values)
                result = cur.fetchall()
                mCon.commit()
                if cur.rowcount > 0:          

                    res = make_response({"floordata":"Added"},200)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
                
                else:
                    print("not good")
                    mCon.rollback()
                    res = make_response({"floordata":"No Data Found"},201)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"floordata":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            traceback.print_exc()
            mCon.rollback()
            res = make_response({"floordata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

###########################   GET FLOOR PARTS API   ##########################
    def get_floor_parts_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            floor_id = data.get('floor_id')
            # Construct and execute the query
            query = f"SELECT * FROM parts WHERE floor_id = '{floor_id}'"
            # with mCon.cursor(dictionary=True) as cur:
            # if not mCon.is_connected():
            #     mCon.reconnect()

            cur.execute(query)
            result = cur.fetchall()
        
            if result is not None:
            
                res = make_response({"floorpartsdata": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"floorpartsdata":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            traceback.print_exc()
            res = make_response({"floorpartsdata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()
###########################   GET CHECKSHEET API   ##########################
    def get_checksheet_model(self):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            # Construct and execute the query
            query = f"SELECT * FROM checksheet"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
        
            cur.execute(query)
            result = cur.fetchall()
        
            if result is not None:
                res = make_response({"checksheet": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"checksheet":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            # message is not shown for 204    
        except:
            res = make_response({"checksheet":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()
 
###########################   GET INSTRUCTION API   ##########################
    def get_instructionimage_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            station_id = data.get('station_id')
            query = f"SELECT process_id FROM stations WHERE station_id = '{station_id}'"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
        
            cur.execute(query)
            result = cur.fetchone()
            cur.nextset()

        
            if result is not None:
                process_id = int(result.get('process_id', 0))
                query = f"SELECT * FROM processes WHERE process_id = '{process_id}'"
                cur.execute(query)
                result = cur.fetchone()
                cur.nextset()


                if result is not None:
                    res = make_response({"instructionImage": result},200)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
                else:
                    print("not good")
                    res = make_response({"instructionImage":"No Data Found"},201)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res

            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"instructionImage":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                    # message is not shown for 204    
        except:
            res = make_response({"instructionImage":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()


###########################   ADD CHECKSHEET DATA API   ##########################
    def add_checksheetdata_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)

            indian_timezone = pytz.timezone('Asia/Kolkata')

# Get the current time in UTC
            current_time_utc = datetime.utcnow()

# Convert UTC time to Indian time
            current_time_indian = current_time_utc.replace(tzinfo=pytz.utc).astimezone(indian_timezone)

# Print the formatted Indian time
            formatted_time = current_time_indian.strftime("%A, %B %d, %Y %H:%M:%S")
            print(formatted_time)

            # Format the datetime object as a string
            # formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            # print(formatted_time)
            
            # return "A"
        
            station_id = data.get('station_id')
            employee_id = data.get('employee_id')
            employee_name = data.get('employee_name')
            timestamp = str(formatted_time)
            p1 = data.get('p1')
            print(p1)
            
            # Construct and execute the query
            # query = f"INSERT INTO checksheet_data (station_id, employee_id, employee_name, timestamp, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10) VALUES ({station_id}, {employee_id}, {employee_name}, {timestamp}, {p1}, {p2}, {p3}, {p4}, {p5}, {p6}, {p7}, {p8}, {p9}, {p10})"
            # query = f""
            query = "INSERT INTO checksheet_data (station_id, employee_id, employee_name, timestamp, p1) VALUES (%s, %s, %s, %s, %s)"
            values = (station_id, employee_id, employee_name, timestamp, p1)
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()

            cur.execute(query, values)
            # cur.execute(query)
            result = cur.fetchall()
        
            if result is not None:
                res = make_response({"checksheetadd": "added"},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
                # return {"message":"No Data Found"}
                print("good")
                res = make_response({"checksheetadd":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                    # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            res = make_response({"checksheetadd":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'  
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()


###########################   GET PROCESS DATA API   ##########################
    def get_oneprocess_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            station_id = data.get('station_id')
            # Construct and execute the query
            query = f"SELECT * FROM stations WHERE station_id = '{station_id}'"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
        
            cur.execute(query)
            result = cur.fetchone()
            cur.nextset()

            # print("start")
        
            if result is not None:
                process_id = int(result.get('process_id', 0))
                query = f"SELECT * FROM processes WHERE process_id = '{process_id}'"
                cur.execute(query)
                result = cur.fetchone()
                cur.nextset()

                # print("not null 1")

                if result is not None:
                    res = make_response({"processdata": result},200)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
                else:
                    # print("not good")
                    res = make_response({"processdata":"No Data Found"},201)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res

            else:
                # return {"message":"No Data Found"}
                # print("good")
                res = make_response({"processdata":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                    # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            res = make_response({"processdata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()            


###########################   SAVE WORK DATA API   ##########################
    def savework_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)

            indian_timezone = pytz.timezone('Asia/Kolkata')
            # Get the current time in UTC
            current_time_utc = datetime.utcnow()
            # Convert UTC time to Indian time
            current_time_indian = current_time_utc.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
            # Print the formatted Indian time
            formatted_time = current_time_indian.strftime("%A, %B %d, %Y %H:%M:%S")
            # Format the datetime object as a string
            # formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print(formatted_time)

            month = data.get('month')
            date = data.get('date')
            station_id = data.get('station_id')
            process_id = data.get('process_id')
            part_id = data.get('part_id')
            timestamp = formatted_time
            floor_id = data.get('floor_id')
            line_id = data.get('line_id')
            status = data.get('status')
            reason = data.get('reason')
            remark = data.get('remark')
            isfilled = data.get('isfilled')
            
            p1 = data.get('p1')
            p2 = data.get('p2')
            p3 = data.get('p3')
            p4 = data.get('p4')
            p5 = data.get('p5')

            # EXECUTE TRANSACTION
            mCon.start_transaction()
            
            # Construct and execute the query
            # query = f"INSERT INTO work_f1 (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            query = "INSERT INTO work_f1 (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled)
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
       
            cur.execute(query,values)
            #Execute another query
            result = cur.fetchone()
            cur.nextset()
            # print("start")
            # print(result)
            if cur.rowcount > 0:
                cur.nextset()
                if isfilled == "0":
                    mCon.commit()
                    if result is not None:

                        myIsFilled = 0
                        myPass = 0
                        myFail = 0
                        mCount = 0

                        for entry in result:
                            mStation_id = entry["station_id"]
                            if(mStation_id == station_id):
                                mIsFilled = entry["isfilled"]
                                # floor_id = entry["floor_id"]
                                # line_id = entry["line_id"]
                                mStatus = entry["status"]
                                mCount = mCount + 1
                            
                                if(mIsFilled == "1"):
                                    myIsFilled = myIsFilled + 1
                                if(mStatus == "1"):
                                    myPass = myPass + 1
                                else:
                                    myFail = myFail + 1  

                        # Create a dictionary with the variables
                        response_dict = {
                            "myIsFilled": myIsFilled,
                            "myPass": myPass,
                            "myFail": myFail,
                            "mCount": mCount
                        }

                        # Use make_response and jsonify to create a response with the desired structure
                        res = make_response(jsonify({"workdata": response_dict}), 200)  
                        res.headers['Access-Control-Allow-Origin'] = "*"
                        res.headers['Content-Type'] = 'application/json'
                        return res
            
                query =  "INSERT INTO process_data (process_id, station_id, timestamp, p1, p2, p3, p4, p5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (process_id, station_id, timestamp, p1, p2, p3, p4, p5)
                cur.execute(query, values)
            
                result = cur.fetchone()
                cur.nextset()
                # print("not null 1")

                if cur.rowcount > 0:
                    cur.nextset()

                    query = f"SELECT * FROM work_f1 WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}'"
                    cur.execute(query)
                    result = cur.fetchall()
                    mCon.commit()

                    if result is not None:

                        myIsFilled = 0
                        myPass = 0
                        myFail = 0
                        mCount = 0

                        for entry in result:
                            mStation_id = entry["station_id"]
                            if(mStation_id == station_id):
                                mIsFilled = entry["isfilled"]
                                # floor_id = entry["floor_id"]
                                # line_id = entry["line_id"]
                                mStatus = entry["status"]
                                mCount = mCount + 1
                            
                                if(mIsFilled == "1"):
                                    myIsFilled = myIsFilled + 1
                                if(mStatus == "1"):
                                    myPass = myPass + 1
                                else:
                                    myFail = myFail + 1  

                    # Create a dictionary with the variables
                        response_dict = {
                            "myIsFilled": myIsFilled,
                            "myPass": myPass,
                            "myFail": myFail,
                            "mCount": mCount
                        }

                        # Use make_response and jsonify to create a response with the desired structure
                        res = make_response(jsonify({"workdata": response_dict}), 200)            
                        # res = make_response({"workdata": result},200)
                        res.headers['Access-Control-Allow-Origin'] = "*"
                        res.headers['Content-Type'] = 'application/json'
                        return res   

                    else:
                        mCon.rollback()
                        res = make_response({"workdata":"Cannot fetch 3"},201)
                        res.headers['Access-Control-Allow-Origin'] = "*"
                        res.headers['Content-Type'] = 'application/json'
                        return res 


                else:
                    # print("not good")
                    cur.nextset()
                    mCon.rollback()
                    res = make_response({"workdata":"Cannot add 2"},201)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
            
            else:
                # return {"message":"No Data Found"}
                # print("good")
                cur.nextset()

                mCon.rollback()
                res = make_response({"workdata":"Cannot add"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            cur.nextset()

            traceback.print_exc()
            mCon.rollback()
            res = make_response({"workdata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()            
###########################   GET WORK DATA API   ##########################
    def getworkforoperator_model22(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            month = data.get('month')
            date = data.get('date')

            # Construct and execute the query
            query = f"SELECT * FROM work_f1 WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}'"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()

            cur.execute(query)
            result = cur.fetchall()
            print(result)
        
            if result is not None:



                for entry in result:
                    station_id = entry["station_id"]
                    split_items = station_id.split()
                    # print(split_items)
                    if len(split_items) == 3:
                        F1, L1, S1 = split_items

                # Further split each part
                        F1_part1, F1_part2 = F1[0], F1[1:]
                        L1_part1, L1_part2 = L1[0], L1[1:]
                        S1_part1, S1_part2 = S1[0], S1[1:]

                        # print("F1:", F1_part1, F1_part2)
                        # print("L1:", L1_part1, L1_part2)
                        # print("S1:", S1_part1, S1_part2)                
                    # station_num = "".join(filter(str.isdigit, station_id_parts[-1]))

                    entry["station_num"] = S1_part2
                # print(result)
                res = make_response({"processdata": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                # print(res)
                return res

            else:
                res = make_response({"processdata":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            traceback.print_exc()
            res = make_response({"processdata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()        
            
###########################   REJECTED_REASON API   ##########################
    def reason_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            process_id = data.get('process_id')

            # Construct and execute the query
            query = f"SELECT * FROM rejected_reason WHERE process_id = '{process_id}'"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
        
            cur.execute(query)
            result = cur.fetchone()
            cur.nextset()


            if result is not None:
                # return json.dumps(result)
                # return{"payload": result}
                res = make_response({"reasondata": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
            # return {"message":"No Data Found"}
                print("good")
                res = make_response({"reasondata":"No Data Found"},401)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            res = make_response({"reasondata":"Got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()
###########################   GET WORK DATA API   ##########################
    def getwork_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
           
            floor_id = data.get('floor_id')

            query = f"SELECT * FROM work_f1 WHERE floor_id='{floor_id}'"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
        
            cur.execute(query)
            result = cur.fetchall()
            # print("start")
            # print(result)
            if cur.rowcount > 0:
                    res = make_response({"workdata": result},200)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
            else:
                res = make_response({"workdata":"Cannot fetch"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            traceback.print_exc()
            res = make_response({"workdata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()        

            
###########################   ADD_STATION API   ##########################
    def add_station_model(self,data):
        mCon = self.pool.get_connection()
        print(data)
        try:
            cur = mCon.cursor(dictionary = True)
            qry = "INSERT INTO stations(station_id, e_one, e_one_name, e_one_skill, e_two, e_two_name, e_two_skill, process_id, process_name, process_skill) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = [
                (
                stationdata.get('station_id'),
                stationdata.get('station_num'),
                
                stationdata.get('e_one'),
                stationdata.get('e_one_name'),
                stationdata.get('e_one_skill'),
                stationdata.get('e_two'),
                stationdata.get('e_two_name'),
                stationdata.get('e_two_skill'),
                stationdata.get('process_id'),
                stationdata.get('process_name'),
                stationdata.get('process_skill')
                ) 
                for stationdata in data]
            
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
            cur.executemany(qry, values)
            result = cur.fetchone()
            cur.nextset()

            if cur.rowcount > 0:
                cur.nextset()
                res = make_response({"addStation": "added successfully"},201)
                # res = make_response({"addStation": result},200)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
                cur.nextset()
                res = make_response({"addStation":"cannot add"},202)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res

        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            traceback.print_exc()
            cur.nextset()
            res = make_response({"addStation":"Got error"},500)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

# demo projects
    def Station_model(self, data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry = "INSERT INTO stations(station_id, e_one, e_one_name, e_one_skill, e_two, e_two_name, e_two_skill, process_id, process_name, process_skill) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = [(stationdata.get('station_id'),
                    #    stationdata.get('station_num'),
                stationdata.get('e_one'),
                stationdata.get('e_one_name'),
                stationdata.get('e_one_skill'),
                stationdata.get('e_two_skill'),
                stationdata.get('e_two_name'),
                stationdata.get('e_two_skill'),
                stationdata.get('process_id'),
                stationdata.get('process_name'),
                stationdata.get('process_skill')
                ) for stationdata in data]
            cur.executemany(qry, values)
            if cur.rowcount > 0 :
                res= make_response({"message": "Stations(s) added successfully"}, 201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
            else:
                res= make_response({"message": "Stations(s) not successfully"}, 202)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res

        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()            
        
        # print(data)
        # qry="INSERT INTO stations(station_id, e_one, e_two, process_id) VALUES "
        # for stationdata in data:
        #     qry +=f"('{stationdata['station_id']}','{stationdata['e_one']}','{stationdata['e_two']}','{stationdata['process_id']}')"
        # finalqry = qry.rstrip(",")
        # cur.execute(finalqry)
        
        # # res.headers['Access-Control-Allow-Origin']="*"
        # # res.headers['Content-Type']="application/json"
        # return make_response({"message":"Station added successfully"},201)
    def get_process(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry = "SELECT process_id,process_name,prrocess_skill FROM processes WHERE part_id = %s"  
            values = [data.get('part_id')]
            cur.execute(qry,values)
            result = cur.fetchall()
            if len(result)>0:
                res = make_response({'payload':result},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()        

    def get_process_and_login_data(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry = "SELECT process_id,process_name,prrocess_skill FROM processes WHERE part_id = %s"  
            values = [data.get('part_id')]
            cur.execute(qry,values)
            process_result = cur.fetchall()

            qry_login_operators= "SELECT CONCAT(first_name, ' ', last_name) AS full_name, employee_code, skill FROM login_operator"
            cur.execute(qry_login_operators)
            employees_result=cur.fetchall()

            response_data={
                'process_data':process_result,
                'employess_data':employees_result
            }

            if len(process_result) > 0 or len(employees_result) > 0:
                res = make_response({'payload':response_data},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def task_assigned_model(self, data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            now_utc = datetime.now(pytz.utc)
            ist = pytz.timezone('Asia/Kolkata')
            now_ist = now_utc.astimezone(ist)
            assigned_for_date = now_ist.strftime('%Y-%m-%d')
            

            qry = "INSERT INTO task_assigned(floor_id, line_id, part_id, part_name, prev_quantity, quantity, assigned_for_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = [(taskassigned.get('floor_id'),
                taskassigned.get('line_id'),
                taskassigned.get('part_id'),
                taskassigned.get('part_name'),
                taskassigned.get('prev_quantity'),
                taskassigned.get('quantity'),
                assigned_for_date) for taskassigned in data]
           
            cur.executemany(qry, values)
            return make_response({"message": "task_assigned successfully"}, 201)
        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()    
    # def get_task_assigend_model(self):
    #     try:
    #         cur.execute("SELECT * FROM task_assigned WHERE floor_id = 1")
    #         result=cur.fetchall()
    #         if len(result)>0:
    #           res = make_response({'payload':result},200)
    #           res.headers['Access-Control-Allow-Origin']="*"
    #           return res
    #         else:
    #             return make_response({"message":"No Data found"},204)
    #     except mysql.connector.Error as err:
    #         print(f"MySQL Error: {err}")
    #         return make_response({"error": "Internal Server Error"}, 500)
    
    def get_asssigned_parts_model(self):

        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            # cur.execute("SELECT * FROM assigned_parts")
            cur.execute("SELECT * FROM assigned_parts")
            # result=cur.fetchall()
            result=cur.fetchall()
            if len(result)>0:
              res = make_response({'payload':result},200)
              res.headers['Access-Control-Allow-Origin']="*"
              return res
            else:
                return make_response({"message":"No Data found"},204)
        except Exception as err:
            print(f"Error: {err}")
            if cur:
                cur.close()
            if mCon:
                mCon.close()

            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_task_assigend_model(self,data):
        
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry = "SELECT * FROM task_assigned WHERE assigned_for_date = %s"  
            values = [data.get('assigned_for_date')]
            cur.execute(qry,values)
            # cur.execute(qry,values)
            # process_result = cur.fetchone()
            # cur.nextset()
            process_result = cur.fetchone()
            cur.nextset()


            # qry_login_operators= "SELECT CONCAT(first_name, ' ', last_name) AS full_name, employee_code, skill FROM login_operator"
            # cur.execute(qry_login_operators)
            # employees_result=cur.fetchall()

            # response_data={
            #     'process_data':process_result,
            #     'employess_data':employees_result
            # }

            if len(process_result) > 0 :
                res = make_response({'payload':process_result},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                cur.close()
            if mCon:
                mCon.close() 
        
    def update_assigned_parts_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            mCon.start_transaction()
            line_id = data.get('line_id')
            part_id = data.get('part_id')
            part_name = data.get('part_name')

        # Update assigned_parts table
            qry1 = """UPDATE assigned_parts SET part_id = %s, part_name = %s WHERE line_id = %s"""
            values1 = [part_id, part_name, line_id]
            cur.execute(qry1, values1)

        # Update stations table
            qry2 = """UPDATE stations SET process_id = NULL, process_name = NULL, process_skill = NULL WHERE station_id LIKE %s"""
            pattern = f'% L{line_id} S%'

            values2 = [pattern]
            # qry2="SELECT * FROM stations"
            # cur.execute(qry2)
            # result= cur.fetchall()
            # print(result)
            cur.execute(qry2,values2)

            mCon.commit()

            if cur.rowcount > 0:
                return make_response({"status": "Data updated successfully"}, 200)
            else:
                return make_response({"status": "No matching records found for update"}, 401)
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            mCon.rollback()
            return make_response({"status": "Rolled Back"}, 400)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()    
       
    
    def get_task_model(self):

        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            now_utc = datetime.now(pytz.utc)
            ist = pytz.timezone('Asia/Kolkata')
            now_ist = now_utc.astimezone(ist)
            assigned_for_date = now_ist.strftime('%Y-%m-%d')
            values = [assigned_for_date]
            qry = "SELECT * FROM task_assigned WHERE assigned_for_date = %s"
            cur.execute(qry,values)
            result=cur.fetchall()
            # cur.execute(qry,values)
            # result=cur.fetchall()
            if len(result)>0:
              res = make_response({'payload':result},200)
              res.headers['Access-Control-Allow-Origin']="*"
              return res
            else:
                return make_response({"message":"No Data found"},204)
        except Exception as err:
            print(f"Error error: {err}")
            # self.pool.reset()

            return make_response({"error": "Internal Server Error"}, 501)
        finally:
            if cur:
                cur.close()
            if mCon:
                mCon.close()
      
    def task_assigned_version_two_model(self, data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            now_utc = datetime.now(pytz.utc)
            ist = pytz.timezone('Asia/Kolkata')
            now_ist = now_utc.astimezone(ist)
            assigned_for_date = now_ist.strftime('%Y-%m-%d')
            values = []

            for taskassigned in data:
                floor_id=taskassigned.get('floor_id')
                line_id=taskassigned.get('line_id')
                is_task_completed = taskassigned.get('is_task_completed',0)
                parts_completed=taskassigned.get('parts_completed',0)
                parts_filled=taskassigned.get('parts_filled',0)
                parts_passed=taskassigned.get('parts_passed',0)
                parts_failed=taskassigned.get('parts_failed',0)
                approved=taskassigned.get('approved',0)

                check_query = "SELECT COUNT(*) FROM task_assigned WHERE floor_id = %s AND line_id = %s AND assigned_for_date = %s AND is_task_completed = 0"
                check_values = (floor_id, line_id, assigned_for_date)
                cur.execute(check_query, check_values)
                existing_task_count_result = cur.fetchone()
                cur.nextset()
                print(existing_task_count_result)
                # if existing_task_count_result and existing_task_count_result[0] > 0:
                #     # Task is already running
                #     return make_response({"message": "Task is already running"}, 200)
                # else:
                if existing_task_count_result and existing_task_count_result['COUNT(*)'] > 0:
                    return make_response({"message": "Task is already running"}, 200)
                
                else:

                    qry = "INSERT INTO task_assigned(floor_id, line_id, part_id, part_name, prev_quantity, quantity, assigned_for_date, is_task_completed, parts_completed, parts_filled, parts_passed, parts_failed, approved) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    
                    
                    values.append((taskassigned.get('floor_id'),
                              taskassigned.get('line_id'),
                              taskassigned.get('part_id'),
                              taskassigned.get('part_name'),
                              taskassigned.get('prev_quantity'),
                              taskassigned.get('quantity'),
                              assigned_for_date,
                              is_task_completed,
                              parts_completed,
                              parts_filled,
                              parts_passed,
                              parts_failed,
                              approved))
            if values:
                cur.executemany(qry, values)
                return make_response({"message": "Task assigned successfully"}, 201)
            else:
                return make_response({"message": "No data to insert"}, 200)

                

        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()        

    def savework_model_version_two(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)

            indian_timezone = pytz.timezone('Asia/Kolkata')
            # Get the current time in UTC
            current_time_utc = datetime.utcnow()
            # Convert UTC time to Indian time
            current_time_indian = current_time_utc.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
            # Print the formatted Indian time
            formatted_time = current_time_indian.strftime("%A, %B %d, %Y %H:%M:%S")
            # Format the datetime object as a string
            # formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print(formatted_time)

            month = data.get('month')
            date = data.get('date')
            station_id = data.get('station_id')
            process_id = data.get('process_id')
            part_id = data.get('part_id')
            timestamp = formatted_time
            floor_id = data.get('floor_id')
            line_id = data.get('line_id')
            status = data.get('status')
            reason = data.get('reason')
            remark = data.get('remark')
            isfilled = data.get('isfilled')
            
            p1 = data.get('p1')
            p2 = data.get('p2')
            p3 = data.get('p3')
            p4 = data.get('p4')
            p5 = data.get('p5')

            # EXECUTE TRANSACTION
            mCon.start_transaction()
            
            # Construct and execute the query
            # query = f"INSERT INTO work_f1 (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            query = "INSERT INTO work_f1 (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled)
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
    
            cur.execute(query,values)
            #Execute another query
            


            result = cur.fetchone()
            cur.nextset()

            # print("start")
            # print(result)
            if cur.rowcount > 0:
                cur.nextset()
                if isfilled == "0":
                    mCon.commit()
                    if result is not None:

                        myIsFilled = 0
                        myPass = 0
                        myFail = 0
                        mCount = 0

                        for entry in result:
                            mStation_id = entry["station_id"]
                            if(mStation_id == station_id):
                                mIsFilled = entry["isfilled"]
                                # floor_id = entry["floor_id"]
                                # line_id = entry["line_id"]
                                mStatus = entry["status"]
                                mCount = mCount + 1
                            
                                if(mIsFilled == "1"):
                                    myIsFilled = myIsFilled + 1
                                if(mStatus == "1"):
                                    myPass = myPass + 1
                                else:
                                    myFail = myFail + 1  

                        # Create a dictionary with the variables
                        response_dict = {
                            "myIsFilled": myIsFilled,
                            "myPass": myPass,
                            "myFail": myFail,
                            "mCount": mCount
                        }

                        # Use make_response and jsonify to create a response with the desired structure
                        res = make_response(jsonify({"workdata": response_dict}), 200)  
                        res.headers['Access-Control-Allow-Origin'] = "*"
                        res.headers['Content-Type'] = 'application/json'
                        return res
            
                query =  "INSERT INTO process_data (process_id, station_id, timestamp, p1, p2, p3, p4, p5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                values = (process_id, station_id, timestamp, p1, p2, p3, p4, p5)
                cur.execute(query, values)
            
                result = cur.fetchone()
                cur.nextset()

                # print("not null 1")

                if cur.rowcount > 0:
                    cur.nextset()
                    query = f"SELECT * FROM work_f1 WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}'"
                    cur.execute(query)
                    result = cur.fetchall()
                    mCon.commit()

                    if result is not None:

                        myIsFilled = 0
                        myPass = 0
                        myFail = 0
                        mCount = 0

                        for entry in result:
                            mStation_id = entry["station_id"]
                            if(mStation_id == station_id):
                                mIsFilled = entry["isfilled"]
                                # floor_id = entry["floor_id"]
                                # line_id = entry["line_id"]
                                mStatus = entry["status"]
                                mCount = mCount + 1
                            
                                if(mIsFilled == "1"):
                                    myIsFilled = myIsFilled + 1
                                if(mStatus == "1"):
                                    myPass = myPass + 1
                                else:
                                    myFail = myFail + 1  

                    # Create a dictionary with the variables
                        response_dict = {
                            "myIsFilled": myIsFilled,
                            "myPass": myPass,
                            "myFail": myFail,
                            "mCount": mCount
                        }
                        # Use make_response and jsonify to create a response with the desired structure
                        res = make_response(jsonify({"workdata": response_dict}), 200)            
                        # res = make_response({"workdata": result},200)
                        res.headers['Access-Control-Allow-Origin'] = "*"
                        res.headers['Content-Type'] = 'application/json'
                        return res   

                    else:
                        mCon.rollback()
                        res = make_response({"workdata":"Cannot fetch 3"},201)
                        res.headers['Access-Control-Allow-Origin'] = "*"
                        res.headers['Content-Type'] = 'application/json'
                        return res 


                else:
                    # print("not good")
                    cur.nextset()
                    mCon.rollback()
                    res = make_response({"workdata":"Cannot add 2"},201)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
                    return res
            
            else:
                # return {"message":"No Data Found"}
                # print("good")
                cur.nextset()

                mCon.rollback()
                res = make_response({"workdata":"Cannot add"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
                # message is not shown for 204    
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            cur.nextset()

            traceback.print_exc()
            mCon.rollback()
            res = make_response({"workdata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_max_station_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            station_id=data.get('station_id')
            indian_timezone = pytz.timezone('Asia/Kolkata')
            # # Get the current time in UTC
            current_time_utc = datetime.utcnow()
            # # Convert UTC time to Indian time
            current_time_indian = current_time_utc.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
            # # Print the formatted Indian time
            formatted_time = current_time_indian.strftime("%A, %B %d, %Y %H:%M:%S")
            parsed_time = datetime.strptime(formatted_time, "%A, %B %d, %Y %H:%M:%S")
            formatted_parsed_time = parsed_time.strftime("%Y-%m-%d")
            print(formatted_parsed_time)
            print(formatted_time)
                         
            floor_id, line_id, station_id_num = map(int, re.findall(r'\d+', station_id))
            print(floor_id)
            print(line_id)
            print(station_id_num)
            parts = station_id.split(' ')
            if len(parts) == 3:
                floor_id_num = parts[0]
                print(floor_id_num)
                
                line_id_num = parts[1]
                print(line_id_num)
                station_num = parts[2]
                print(station_num)
            else:
                # Handle incorrect format of station_id
                raise ValueError("Invalid station_id format")
            
            

            # EXECUTE TRANSACTION
            mCon.start_transaction()
            
            # Construct and execute the query
            # query = f"INSERT INTO work_f1 (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # query = "INSERT INTO work_f1 (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # values = (station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled)
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
       
            #     cur.execute(query,values)
            # newnew query_work_assigned = "SELECT * FROM work_f1 where date current"
            query_work_assigned = "SELECT * FROM work_f1 WHERE station_id = %s"
            values_work_assigned = (station_id,)
            # with mCon.cursor(dictionary=True) as cur:
            cur.execute(query_work_assigned, values_work_assigned)
            work_assigned_result = cur.fetchone()
            cur.nextset()
            print(work_assigned_result)

##################newnew on taskid basis
            query_task_assigned = "SELECT * FROM task_assigned WHERE floor_id = %s AND line_id = %s AND assigned_for_date = %s"
            values_task_assigned = (floor_id, line_id, formatted_parsed_time)
            # with mCon.cursor(dictionary=True) as cur:
            cur.execute(query_task_assigned, values_task_assigned)
            task_assigned_result = cur.fetchone()
            cur.nextset()
            print(task_assigned_result)
        
            if task_assigned_result and work_assigned_result:
                # Matching record found, check the status
                status_version_two = work_assigned_result['status']
                print(status_version_two)
                max_station_num=None
                if status_version_two == '0':
                    # Increment parts_failed in task_assigned table
                    query_update_failed = "UPDATE task_assigned SET parts_failed = parts_failed + 1 WHERE floor_id = %s AND line_id = %s AND assigned_for_date = %s"
                    print(task_assigned_result['parts_failed'])
                    values_update_failed = (floor_id, line_id, formatted_parsed_time)
                    # with mCon.cursor() as cur:
                    cur.execute(query_update_failed, values_update_failed)
                    print('failed updated succesfully')
                elif status_version_two == '1':
                     query = "SELECT MAX(CAST(SUBSTRING_INDEX(station_id, 'S', -1) AS UNSIGNED)) AS max_station_num FROM stations WHERE station_id LIKE %s"
                     values = (f"{floor_id_num} {line_id_num} S%",)
                    #  with mCon.cursor() as cur:
                     cur.execute(query, values)
                     result = cur.fetchone()
                     max_station_num = result[0] if result else None
                     print("max_station_num:", max_station_num)
                     print("station_num:", station_num)
                     if max_station_num is not None:
                         if station_id_num==max_station_num:
                             query_update_passed = "UPDATE task_assigned SET parts_passed = parts_passed + 1 WHERE floor_id = %s AND line_id = %s AND assigned_for_date = %s"
                             values_update_passed = (floor_id, line_id, formatted_parsed_time)
                             cur.execute(query_update_passed, values_update_passed)
                             print('passed updated succesfully')
                         else:
                             pass
                            
                                 
                    # Increment parts_passed in stations table
                    # query_update_passed = "UPDATE stations SET parts_passed = parts_passed + 1 WHERE floor_id = %s AND line_id = %s AND station_num = %s"
                    # values_update_passed = (floor_id, line_id, station_num)
                    # cur.execute(query_update_passed, values_update_passed)
                else:
                    # No matching record found in task_assigned table, handle accordingly
                    pass

                mCon.commit()

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(e)
            traceback.print_exc()
            mCon.rollback()
            return make_response({"workdata": "got error"}, 202)
        else:
            return make_response({"workdata": "completed"}, 200)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()        

        

            
    def task_assigned_version_three_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            now_utc = datetime.now(pytz.utc)
            ist = pytz.timezone('Asia/Kolkata')
            now_ist = now_utc.astimezone(ist)
            assigned_for_date = now_ist.strftime('%Y-%m-%d')
            values = []

            for taskassigned in data:
                floor_id = taskassigned.get('floor_id')
                line_id = taskassigned.get('line_id')
                is_task_completed = taskassigned.get('is_task_completed', 0)
                parts_completed = taskassigned.get('parts_completed', 0)
                parts_filled = taskassigned.get('parts_filled', 0)
                parts_passed = taskassigned.get('parts_passed', 0)
                parts_failed = taskassigned.get('parts_failed', 0)
                approved=taskassigned.get('approved',0)

                check_query = "SELECT COUNT(*) FROM task_assigned WHERE floor_id = %s AND line_id = %s AND assigned_for_date = %s AND is_task_completed = 0"
                check_values = (floor_id, line_id, assigned_for_date)
                cur.execute(check_query, check_values)
                existing_task_count_result = cur.fetchone()
                cur.nextset()
                print(existing_task_count_result)

                if existing_task_count_result and existing_task_count_result['COUNT(*)'] > 0:
                    continue
                else:
                    values.append((
                    floor_id,
                    line_id,
                    taskassigned.get('part_id'),
                    taskassigned.get('part_name'),
                    taskassigned.get('prev_quantity'),
                    taskassigned.get('quantity'),
                    assigned_for_date,
                    is_task_completed,
                    parts_completed,
                    parts_filled,
                    parts_passed,
                    parts_failed,
                    approved))
            
            if values:
                qry = "INSERT INTO task_assigned (floor_id, line_id, part_id, part_name, prev_quantity, quantity, assigned_for_date, is_task_completed, parts_completed, parts_filled, parts_passed, parts_failed, approved) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cur.executemany(qry, values)
                inserted_data_query = "SELECT * FROM task_assigned WHERE assigned_for_date = %s"
                cur.execute(inserted_data_query, (assigned_for_date,))
                inserted_data = cur.fetchall()
                return make_response({"message": "Task assigned successfully","data": inserted_data}, 201)
            else:
                return make_response({"message": "Task is already running"}, 200)

        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_assigned_parts_all_model(self):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry="SELECT * FROM assigned_parts"
            cur.execute(qry)
            result=cur.fetchall()
            if len(result)>0:
                res=make_response({"payload":result},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_taskassigned_all_model(self):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry="SELECT * FROM task_assigned"
            cur.execute(qry)
            result=cur.fetchall()
            if len(result)>0:
                res=make_response({"payload":result},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

# no. of lines and per line stations and part_names and part_id for each line api
    def get_line_no_station_no_assigned_parts_model(self):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            #no of lines count
            qry="SELECT COUNT(DISTINCT line_id) AS num_lines FROM assigned_parts"
            cur.execute(qry)
            count_line_result=cur.fetchall()
            qry2="SELECT * FROM assigned_parts"
            cur.execute(qry2)
            part_data=cur.fetchall()
            # qry3="SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(station_id, ' ', 2), ' ', -1) AS line_number,COUNT(*) AS number_of_stations FROM stations GROUP BY line_number"
            qry3="SELECT CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(station_id, 'L', -1), ' ', 1) AS UNSIGNED) AS line_number,COUNT(*) AS number_of_stations FROM stations GROUP BY line_number"
            cur.execute(qry3)
            stations_count=cur.fetchall()
            response_data={
                'count_line_result':count_line_result,
                'part_data':part_data,
                'stations_count':stations_count

            }
            
            if len(count_line_result)>0 or len(part_data)>0 or len(stations_count)>0:
                res=make_response({"payload":response_data},200)
                res.headers['Access-Control-Allow-Origin']="*"
                return res
            else:
             return make_response({"message":"No Data found"},204)
        
        except Exception as err:
            print(f"Error: {err}")
            return make_response({"error": "Internal Server Error"}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()        
#shift timing inserting data
    def add_shift_timings_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry = "INSERT INTO shift_timings (shift_name, shift_start_time, shift_end_time, tea_break_1_start, tea_break_1_end, lunch_start, lunch_end, tea_break_2_start, tea_break_2_end) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values=[]
            for timing_data in data:
                shift_name=timing_data.get('shift_name')
            # Parse and format time strings.
                shift_start_time = datetime.strptime(timing_data.get('shift_start_time'), '%I:%M%p').strftime('%H:%M:%S')
                shift_end_time = datetime.strptime(timing_data.get('shift_end_time'), '%I:%M%p').strftime('%H:%M:%S')
                tea_break_1_start = datetime.strptime(timing_data.get('tea_break_1_start'), '%I:%M%p').strftime('%H:%M:%S')
                tea_break_1_end = datetime.strptime(timing_data.get('tea_break_1_end'), '%I:%M%p').strftime('%H:%M:%S')
                lunch_start = datetime.strptime(timing_data.get('lunch_start'), '%I:%M%p').strftime('%H:%M:%S')
                lunch_end = datetime.strptime(timing_data.get('lunch_end'), '%I:%M%p').strftime('%H:%M:%S')
                tea_break_2_start = datetime.strptime(timing_data.get('tea_break_2_start'), '%I:%M%p').strftime('%H:%M:%S')
                tea_break_2_end = datetime.strptime(timing_data.get('tea_break_2_end'), '%I:%M%p').strftime('%H:%M:%S')
                
                
                values.append((shift_name,shift_start_time,shift_end_time,tea_break_1_start,tea_break_1_end,lunch_start,lunch_end,tea_break_2_start,tea_break_2_end))
            # shift_name = data.get('shift_name')
            # shift_start_time = data.get('shift_start_time')
            # shift_end_time = data.get('shift_end_time')
            # tea_break_1_start = data.get('tea_break_1_start')
            # tea_break_1_end = data.get('tea_break_1_end')
            # lunch_start = data.get('lunch_start')
            # lunch_end = data.get('lunch_end')
            # tea_break_2_start = data.get('tea_break_2_start')
            # tea_break_2_end = data.get('tea_break_2_end')
                
            
           
            cur.executemany(qry,values)
            return make_response({"message": "Shift timing added successfully"}, 201)
        except Exception as err:
            print(f"Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

#get shift timings
    def get_shift_timings_model(self):

        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            qry="SELECT * FROM shift_timings"

            cur.execute(qry)
            # cur.execute(qry)
            result=cur.fetchall()
            # result=cur.fetchall()
            print(result)
            
            
            # return make_response({'message': 'No shift timings found'}, 404)
            shift_timings = []
            for row in result:
                #  shift_timing = {
                    # "shift_name": row['shift_name'],
                    # "shift_start_time": row['shift_start_time'].strftime('%I:%M %p'),

                    # "shift_end_time": row['shift_end_time'].strftime('%I:%M %p'),
                    # "tea_break_1_start": row['tea_break_1_start'].strftime('%I:%M %p'),
                    # "tea_break_1_end": row['tea_break_1_end'].strftime('%I:%M %p'),
                    # "lunch_start": row['lunch_start'].strftime('%I:%M %p'),
                    # "lunch_end": row['lunch_end'].strftime('%I:%M %p'),
                    # "tea_break_2_start": row['tea_break_2_start'].strftime('%I:%M %p'),
                    # "tea_break_2_end": row['tea_break_2_end'].strftime('%I:%M %p')}
                # Convert timedelta to total seconds
                shift_start_seconds = row['shift_start_time'].total_seconds()
                shift_end_seconds = row['shift_end_time'].total_seconds()
                tea_break_1_start_seconds = row['tea_break_1_start'].total_seconds()
                tea_break_1_end_seconds = row['tea_break_1_end'].total_seconds()
                lunch_start_seconds = row['lunch_start'].total_seconds()
                lunch_end_seconds = row['lunch_end'].total_seconds()
                tea_break_2_start_seconds = row['tea_break_2_start'].total_seconds()
                tea_break_2_end_seconds = row['tea_break_2_end'].total_seconds()

                shift_timing = {
                    "shift_name": row['shift_name'],
                    "shift_start_time": "{:02}:{:02} {}".format(int(shift_start_seconds // 3600), int((shift_start_seconds % 3600) // 60), 'am' if shift_start_seconds < 43200 else 'pm'),
                    "shift_end_time": "{:02}:{:02} {}".format(int(shift_end_seconds // 3600), int((shift_end_seconds % 3600) // 60), 'am' if shift_end_seconds < 43200 else 'pm'),
                    "tea_break_1_start": "{:02}:{:02} {}".format(int(tea_break_1_start_seconds // 3600), int((tea_break_1_start_seconds % 3600) // 60), 'am' if tea_break_1_start_seconds < 43200 else 'pm'),
                    "tea_break_1_end": "{:02}:{:02} {}".format(int(tea_break_1_end_seconds // 3600), int((tea_break_1_end_seconds % 3600) // 60), 'am' if tea_break_1_end_seconds < 43200 else 'pm'),
                    "lunch_start": "{:02}:{:02} {}".format(int(lunch_start_seconds // 3600), int((lunch_start_seconds % 3600) // 60), 'am' if lunch_start_seconds < 43200 else 'pm'),
                    "lunch_end": "{:02}:{:02} {}".format(int(lunch_end_seconds // 3600), int((lunch_end_seconds % 3600) // 60), 'am' if lunch_end_seconds < 43200 else 'pm'),
                    "tea_break_2_start": "{:02}:{:02} {}".format(int(tea_break_2_start_seconds // 3600), int((tea_break_2_start_seconds % 3600) // 60), 'am' if tea_break_2_start_seconds < 43200 else 'pm'),
                    "tea_break_2_end": "{:02}:{:02} {}".format(int(tea_break_2_end_seconds // 3600), int((tea_break_2_end_seconds % 3600) // 60), 'am' if tea_break_2_end_seconds < 43200 else 'pm')}
                shift_timings.append(shift_timing)

            # shift_timings = []
            # for row in result:
            #     shift_start_seconds = row['shift_start_time'].seconds
            #     shift_end_seconds = row['shift_end_time'].seconds
            #     tea_break_1_start_seconds = row['tea_break_1_start'].seconds
            #     tea_break_1_end_seconds = row['tea_break_1_end'].seconds
            #     lunch_start_seconds = row['lunch_start'].seconds
            #     lunch_end_seconds = row['lunch_end'].seconds
            #     tea_break_2_start_seconds = row['tea_break_2_start'].seconds
            #     tea_break_2_end_seconds = row['tea_break_2_end'].seconds

            #     shift_timing = {
            #                "shift_name": row['shift_name'],
            #                "shift_start_time": f"{shift_start_seconds // 3600:02}:{(shift_start_seconds % 3600) // 60:02} {'am' if shift_start_seconds < 43200 else 'pm'}",
            #                "shift_end_time": f"{shift_end_seconds // 3600:02}:{(shift_end_seconds % 3600) // 60:02} {'am' if shift_end_seconds < 43200 else 'pm'}",
            #                "tea_break_1_start": f"{tea_break_1_start_seconds // 3600:02}:{(tea_break_1_start_seconds % 3600) // 60:02} {'am' if tea_break_1_start_seconds < 43200 else 'pm'}",
            #                "tea_break_1_end": f"{tea_break_1_end_seconds // 3600:02}:{(tea_break_1_end_seconds % 3600) // 60:02} {'am' if tea_break_1_end_seconds < 43200 else 'pm'}",
            #                "lunch_start": f"{lunch_start_seconds // 3600:02}:{(lunch_start_seconds % 3600) // 60:02} {'am' if lunch_start_seconds < 43200 else 'pm'}",
            #                "lunch_end": f"{lunch_end_seconds // 3600:02}:{(lunch_end_seconds % 3600) // 60:02} {'am' if lunch_end_seconds < 43200 else 'pm'}",
            #                "tea_break_2_start": f"{tea_break_2_start_seconds // 3600:02}:{(tea_break_2_start_seconds % 3600) // 60:02} {'am' if tea_break_2_start_seconds < 43200 else 'pm'}",
            #                "tea_break_2_end": f"{tea_break_2_end_seconds // 3600:02}:{(tea_break_2_end_seconds % 3600) // 60:02} {'am' if tea_break_2_end_seconds < 43200 else 'pm'}"
            #      }
            #     shift_timings.append(shift_timing)

            return make_response({'shift_timings':shift_timings},200)
        except Exception as err:
            print(f"Error: {err}")
            self.pool.reset()

            return make_response({'error': 'Internal Server Error'}, 201)

        finally:
            
            if cur:
                print("EXECUTIG CLOSE in shift timns")

                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")

                mCon.close()    
        
# get operator_task
    def get_operator_task_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            station_id=data.get('station_id')
            # task_id=data.get('task_id')
            month=data.get('month')
            date=data.get('date')
            print(station_id)
            print(date)
            print(month)
            floor_id, line_id, station_id_num = map(int, re.findall(r'\d+', station_id))
            now_utc = datetime.now(pytz.utc)
            ist = pytz.timezone('Asia/Kolkata')
            now_ist = now_utc.astimezone(ist)
            assigned_for_date = now_ist.strftime('%Y-%m-%d')
            print(floor_id)
            print(station_id)
            print(station_id_num)
            # fetching shift timings
            qry="SELECT * FROM shift_timings"
            cur.execute(qry)
            result=cur.fetchall()
            print(result)
            
            
            # return make_response({'message': 'No shift timings found'}, 404)
            shift_timings = []
            for row in result:
                #  shift_timing = {
                    # "shift_name": row['shift_name'],
                    # "shift_start_time": row['shift_start_time'].strftime('%I:%M %p'),

                    # "shift_end_time": row['shift_end_time'].strftime('%I:%M %p'),
                    # "tea_break_1_start": row['tea_break_1_start'].strftime('%I:%M %p'),
                    # "tea_break_1_end": row['tea_break_1_end'].strftime('%I:%M %p'),
                    # "lunch_start": row['lunch_start'].strftime('%I:%M %p'),
                    # "lunch_end": row['lunch_end'].strftime('%I:%M %p'),
                    # "tea_break_2_start": row['tea_break_2_start'].strftime('%I:%M %p'),
                    # "tea_break_2_end": row['tea_break_2_end'].strftime('%I:%M %p')}
                # Convert timedelta to total seconds
                shift_start_seconds = row['shift_start_time'].total_seconds()
                shift_end_seconds = row['shift_end_time'].total_seconds()
                tea_break_1_start_seconds = row['tea_break_1_start'].total_seconds()
                tea_break_1_end_seconds = row['tea_break_1_end'].total_seconds()
                lunch_start_seconds = row['lunch_start'].total_seconds()
                lunch_end_seconds = row['lunch_end'].total_seconds()
                tea_break_2_start_seconds = row['tea_break_2_start'].total_seconds()
                tea_break_2_end_seconds = row['tea_break_2_end'].total_seconds()

                shift_timing = {
                    "shift_name": row['shift_name'],
                    "shift_start_time": "{:02}:{:02} {}".format(int(shift_start_seconds // 3600), int((shift_start_seconds % 3600) // 60), 'am' if shift_start_seconds < 43200 else 'pm'),
                    "shift_end_time": "{:02}:{:02} {}".format(int(shift_end_seconds // 3600), int((shift_end_seconds % 3600) // 60), 'am' if shift_end_seconds < 43200 else 'pm'),
                    "tea_break_1_start": "{:02}:{:02} {}".format(int(tea_break_1_start_seconds // 3600), int((tea_break_1_start_seconds % 3600) // 60), 'am' if tea_break_1_start_seconds < 43200 else 'pm'),
                    "tea_break_1_end": "{:02}:{:02} {}".format(int(tea_break_1_end_seconds // 3600), int((tea_break_1_end_seconds % 3600) // 60), 'am' if tea_break_1_end_seconds < 43200 else 'pm'),
                    "lunch_start": "{:02}:{:02} {}".format(int(lunch_start_seconds // 3600), int((lunch_start_seconds % 3600) // 60), 'am' if lunch_start_seconds < 43200 else 'pm'),
                    "lunch_end": "{:02}:{:02} {}".format(int(lunch_end_seconds // 3600), int((lunch_end_seconds % 3600) // 60), 'am' if lunch_end_seconds < 43200 else 'pm'),
                    "tea_break_2_start": "{:02}:{:02} {}".format(int(tea_break_2_start_seconds // 3600), int((tea_break_2_start_seconds % 3600) // 60), 'am' if tea_break_2_start_seconds < 43200 else 'pm'),
                    "tea_break_2_end": "{:02}:{:02} {}".format(int(tea_break_2_end_seconds // 3600), int((tea_break_2_end_seconds % 3600) // 60), 'am' if tea_break_2_end_seconds < 43200 else 'pm')}
                shift_timings.append(shift_timing)


            # fetching task_assigned data accroding to current date and floor_id and line_id
            query_task_assigned_data = "SELECT * FROM task_assigned WHERE floor_id = %s AND line_id = %s AND assigned_for_date = %s"
            values_task_assigned_data = (floor_id, line_id, assigned_for_date)
            # with mCon.cursor(dictionary=True) as cur:
            cur.execute(query_task_assigned_data, values_task_assigned_data)
            task_assigned_result = cur.fetchone()
            task_id=task_assigned_result['task_id']
            print(task_id)
            cur.nextset()
            print(task_assigned_result)

            if task_assigned_result is None:
                return make_response({"payload":"no data found"},201)
                print(task_assigned_result)
            
            
        
                
            cur.nextset()

            
            # fetching data from stations table
            query_station_data = "SELECT * FROM stations WHERE station_id = %s"
            values_staion_data = [station_id]
            # with mCon.cursor(dictionary=True) as cur:
            cur.execute(query_station_data,values_staion_data)
            station_result = cur.fetchone()
            cur.nextset()
            print(station_result)
            
            # fetch data from parmeters table and image table according to process_id
            process_id=station_result['process_id']
            print(process_id)

            cur.execute("SELECT * FROM processes WHERE process_id = %s",(process_id,))
            process=cur.fetchone()
            cur.nextset()
            cur.execute("SELECT * FROM parameters WHERE process_id = %s", (process_id,))
            parameters_data = cur.fetchall()

            cur.execute("SELECT * FROM images WHERE process_id = %s",(process_id,))
            images_data = cur.fetchall()
            
            query_work_f1_Paas_fail = f"SELECT * FROM work_f1 WHERE task_id = '{task_id}' AND station_id ='{station_id}' AND MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}'"
            
            cur.execute(query_work_f1_Paas_fail)
            work_f1_Data = cur.fetchall()
            print(work_f1_Data)

            query_readings=f"SELECT reading_values FROM readings WHERE task_id ='{task_id}' AND process_id ='{process_id}' AND station_id = '{station_id}'"
            cur.execute(query_readings)
            readings_data_result = cur.fetchall()
            # unique_dates = set([datetime.strptime(row['timestamp'], "%A, %B %d, %Y %H:%M:%S").strftime('%d-%m-%Y') for row in readings_data_result])
            # print(readings_data_result)

            # print(unique_dates)
            # readings_data = {}

        # Iterate over unique dates and fetch readings
            # for date in unique_dates:
                # readings = [row['reading_values'] for row in readings_data_result if datetime.strptime(row['timestamp'], "%A, %B %d, %Y %H:%M:%S").strftime('%d-%m-%Y') == date]
                # readings_data[date] = readings
            # print(readings_data)
        
            response_dict = {
                "myIsFilled": 0,
                "myPass": 0,
                "myFail": 0,
                "mCount": 0
                }
            # print(work_f1_Data)
            if work_f1_Data is not None:
                myIsFilled = 0
                myPass = 0
                myFail = 0
                mCount = 0

                for entry in work_f1_Data:
                    mStation_id = entry["station_id"]
                    if mStation_id == station_id:
                        mIsFilled = entry["isfilled"]
                        mStatus = entry["status"]
                        mCount += 1

                        if mIsFilled == "1":
                            myIsFilled += 1
                        if mStatus == "1":
                            myPass += 1
                        else:
                            myFail += 1  

                response_dict = {
                  "myIsFilled": myIsFilled,
                   "myPass": myPass,
                   "myFail": myFail,
                   "mCount": mCount
                  }

                print(response_dict)
            
            cur.execute("SELECT * FROM checksheet")
            checksheet_data=cur.fetchall()
            response_result={
                'task_assigned_data':task_assigned_result,
                'staion_data':station_result,
                'parameters_data':parameters_data,
                'images_data':images_data,
                'checksheet_data':checksheet_data,
                'shift_timings':shift_timings,
                'process':process,
                'response_dict':response_dict,
                'reading_data':readings_data_result
                # 'work_f1_data':work_f1_Data
            }
            return make_response({"payload":response_result},200)

        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()    
  

    def task_approved_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            task_id=data.get('task_id')
            value=data.get('value')
            print(task_id)
            print(value)
            check_query = "SELECT COUNT(*) FROM task_assigned WHERE task_id = %s"
            cur.execute(check_query, (task_id,))
            task_exists = cur.fetchone()
            cur.nextset()
            if task_exists and task_exists['COUNT(*)'] > 0:
                if value=="1":
                    
                    qry ="UPDATE task_assigned SET approved=1 WHERE task_id=%s"
                    values=[task_id] 
                    if values:
                        cur.execute(qry,values)
                        return make_response({'message':"task aprroved 1 succesfully"},200)
                elif value=="2":
                    qry ="UPDATE task_assigned SET approved=2 WHERE task_id=%s"
                    values=[task_id] 
                    if values:
                        cur.execute(qry,values)
                        return make_response({'message':"task aprroved 2 succesfully"},200)
                else:
                    return make_response({'message':"task not approved"})
            else:
                return make_response({'message':"task not exists"})
        except Exception as err:
            print(f"Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)   
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_work_f1_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            station_id=data.get('station_id') 
            month=data.get('month')
            date=data.get('date') 
            
            query = f"SELECT * FROM work_f1 WHERE station_id = '{station_id}' AND MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}' LIMIT 2"
            query2=f"SELECT * FROM process_data WHERE station_id = '{station_id}' AND MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}' LIMIT 2"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
            cur.execute(query)
            work_f1_data = cur.fetchall()
            cur.execute(query2)
            process_data=cur.fetchall()
            if work_f1_data or process_data:
                #     transformed_data = []
                #     for row in result:
                #         transformed_row = {
                #          'work_id': row['work_id'],
                #         'station_id': row['station_id'],
                #         'process_id': row['process_id'],
                #         'part_id': row['part_id'],
                #         'timestamp': row['timestamp'],
                #         'floor_id': row['floor_id'],
                #         'line_id': row['line_id'],
                #         'status': row['status'],
                #         'reason': row['reason'],
                #         'remark': row['remark'],
                #         'isfilled': row['isfilled']
                #     }
                #     transformed_data.append(transformed_row)
                response_data={'work_f1_data':work_f1_data,
                                'process_data':process_data}
                response = make_response({'payload': response_data}, 200)
                response.headers['Access-Control-Allow-Origin'] = "*"
                response.headers['Content-Type'] = 'application/json'
                return response
            else:
                res = make_response({"message": "No Data Found"}, 404)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res = make_response({"stationdata": "Error"}, 500)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_work_f1_date_month_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            month=data.get('month')
            date=data.get('date') 
            
            query = f"SELECT * FROM work_f1 WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}' LIMIT 2"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
            cur.execute(query)
            result = cur.fetchall()
            if result:
                    response = make_response({'stationdata': result}, 200)
                    response.headers['Access-Control-Allow-Origin'] = "*"
                    response.headers['Content-Type'] = 'application/json'
                    return response
            else:
                res = make_response({"stationdata": "No Data Found"}, 404)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res = make_response({"stationdata": "Error"}, 500)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_stations_data_by_floor_id_version_two_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            floor_id=data.get('floor_id')
            query = f"SELECT * FROM stations WHERE station_id LIKE 'F{floor_id}%'"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
            cur.execute(query)
            result = cur.fetchall()
            if result:
                    response = make_response({'stationdata': result}, 200)
                    response.headers['Access-Control-Allow-Origin'] = "*"
                    response.headers['Content-Type'] = 'application/json'
                    return response
            else:
                res = make_response({"stationdata": "No Data Found"}, 404)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res = make_response({"stationdata": "Error"}, 500)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_process_data_month_date_version_two_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            month=data.get('month')
            date=data.get('date') 
            
            query = f"SELECT * FROM process_data WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}' LIMIT 2"
            # with mCon.cursor(dictionary=True) as cur:
            #     if not mCon.is_connected():
            #         mCon.reconnect()
            cur.execute(query)
            result = cur.fetchall()
            if result:
                    response = make_response({'stationdata': result}, 200)
                    response.headers['Access-Control-Allow-Origin'] = "*"
                    response.headers['Content-Type'] = 'application/json'
                    return response
            else:
                res = make_response({"stationdata": "No Data Found"}, 404)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res = make_response({"stationdata": "Error"}, 500)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_checksheet_data_month_date_version_two_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            month=data.get('month')
            date=data.get('date') 
            
            query = f"SELECT * FROM checksheet_data WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}' LIMIT 2"
            # if not mCon.is_connected():
            #     mCon.reconnect()
            cur.execute(query)
            result = cur.fetchall()
            if result:
                    response = make_response({'stationdata': result}, 200)
                    response.headers['Access-Control-Allow-Origin'] = "*"
                    response.headers['Content-Type'] = 'application/json'
                    return response
            else:
                res = make_response({"stationdata": "No Data Found"}, 404)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res = make_response({"stationdata": "Error"}, 500)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()              

    def save_work_updation_counter_save_process_data_model(self, data):
        mCon = self.pool.get_connection()

        ###implement transaction hewre
        try:
            cur = mCon.cursor(dictionary = True)
            indian_timezone = pytz.timezone('Asia/Kolkata')
            current_time_utc = datetime.utcnow()
            current_time_indian = current_time_utc.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
            formatted_time = current_time_indian.strftime("%A, %B %d, %Y %H:%M:%S")
            parsed_time = datetime.strptime(formatted_time, "%A, %B %d, %Y %H:%M:%S")
            formatted_parsed_time = parsed_time.strftime("%Y-%m-%d")
        
            task_id = data.get('task_id')
            station_id = data.get('station_id')
            process_id = data.get('process_id')
            part_id = data.get('part_id')
            timestamp = formatted_time
            floor_id = data.get('floor_id')
            line_id = data.get('line_id')
            status = data.get('status')
            reason = data.get('reason')
            remark = data.get('remark')
            isfilled = data.get('isfilled')
            p1 = data.get('p1')
            p2 = data.get('p2')
            # reading=data.get('reading')
            final_status = data.get('final_status')
            month = data.get('month')
            date = data.get('date')

            mCon.start_transaction()
            query = "INSERT INTO work_f1 (task_id, station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (task_id, station_id, process_id, part_id, timestamp, floor_id, line_id, status, reason, remark, isfilled)
            # if not mCon.is_connected():
            #     mCon.reconnect()
    
            cur.execute(query, values)
            if cur.rowcount > 0:
                query =  "INSERT INTO process_data (task_id, process_id, station_id, timestamp, p1, p2) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (task_id, process_id, station_id, timestamp, p1, p2)
                cur.execute(query, values)

                if final_status == 'fail':
                    query_update_failed = "UPDATE task_assigned SET parts_failed = parts_failed + 1, parts_completed = parts_completed + 1 WHERE task_id = %s AND floor_id = %s AND line_id = %s AND assigned_for_date = %s"
                    values_update_failed = (task_id,floor_id, line_id, formatted_parsed_time)
                    cur.execute(query_update_failed, values_update_failed)
                    print('failed updated successfully')
                elif final_status == 'pass':
                    query_update_passed = "UPDATE task_assigned SET parts_passed = parts_passed + 1, parts_completed = parts_completed + 1 WHERE task_id = %s AND floor_id = %s AND line_id = %s AND assigned_for_date = %s"
                    values_update_passed = (task_id,floor_id, line_id, formatted_parsed_time)
                    cur.execute(query_update_passed, values_update_passed)
                    print('passed updated successfully')
                elif final_status == 'none':
                    pass
                    print('nothing update')

                query_check_completed = "SELECT * FROM task_assigned WHERE task_id = %s AND floor_id = %s AND line_id = %s AND assigned_for_date = %s"
                values_check_completed = (task_id,floor_id, line_id, formatted_parsed_time)
                cur.execute(query_check_completed, values_check_completed)
                parts_completed_result = cur.fetchone()
                cur.nextset()
                parts_completed = parts_completed_result['parts_completed']
                quantity = parts_completed_result['quantity']
                
                if parts_completed == quantity:
                    query_update_is_task_complete = "UPDATE task_assigned SET is_task_completed = 1 WHERE task_id = %s AND floor_id = %s AND line_id = %s AND assigned_for_date = %s"
                    values_update_is_task_complete = (task_id,floor_id, line_id, formatted_parsed_time)
                    cur.execute(query_update_is_task_complete, values_update_is_task_complete)
                    print('is_task_complete updated successfully')
                
                query_task_assigned = "SELECT * FROM task_assigned WHERE task_id = %s"
                values_task_assigned = [task_id]
                cur.execute(query_task_assigned, values_task_assigned)
                task_assigned_result2 = cur.fetchone()
                cur.nextset()

                query_work_f1 = "SELECT * FROM work_f1 WHERE task_id = %s"
                values_work_f1 = [task_id]
                cur.execute(query_work_f1, values_work_f1)
                work_f1_result2 = cur.fetchall()

                query_work_f1_Paas_fail = f"SELECT * FROM work_f1 WHERE station_id ='{station_id}' AND MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}'"
                cur.execute(query_work_f1_Paas_fail)
                result = cur.fetchall()
                print(result)

                response_dict = {
                    "myIsFilled": 0,
                    "myPass": 0,
                    "myFail": 0,
                    "mCount": 0
                    }

                if result is not None:
                    myIsFilled = 0
                    myPass = 0
                    myFail = 0
                    mCount = 0

                    for entry in result:
                        mStation_id = entry["station_id"]
                        if mStation_id == station_id:
                            mIsFilled = entry["isfilled"]
                            mStatus = entry["status"]
                            mCount += 1

                            if mIsFilled == "1":
                                myIsFilled += 1
                            if mStatus == "1":
                                myPass += 1
                            else:
                                myFail += 1  

                    response_dict2 = {
                        "myIsFilled": myIsFilled,
                        "myPass": myPass,
                        "myFail": myFail,
                        "mCount": mCount
                        }

                response_result = {
                    'task_result2': task_assigned_result2,
                    'work_f1_result2': work_f1_result2,
                    'response_dict2': response_dict2
                    }
                
                print(response_dict2)
                print(task_assigned_result2)

                mCon.commit()
                return make_response({'payload2': response_result}, 200)
            else:
                mCon.rollback()
                res = make_response({"workdata": "Cannot add 2"}, 201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except mysql.connector.errors.OperationalError as e:
            self.reconnectItAgain(e)           
        except Exception as e:
            mCon.rollback()
            print(f"An error occurred: {e}")
            traceback.print_exc()
            res = make_response({"stationdata": "Error"}, 500)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'
            return res
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()
 
    def get_task_for_app_version_two_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            task_id=data.get('task_id')
            print(task_id)
            query="SELECT * FROM task_assigned WHERE task_id = %s"
            value=[task_id]
            cur.execute(query,value)
            result=cur.fetchone()
            cur.nextset()
            print(result)
            return make_response({'payload3':result},200)
        except Exception as err:
            print(f"Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        
    # def get_process_data_readings_timestamp_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            process_id=data.get('process_id')
            query="SELECT timestamp,reading FROM process_data WHERE process_id = %s"
            value=[process_id]
            cur.execute(query,value)
            result=cur.fetchall()
            unique_dates = set([datetime.strptime(row['timestamp'], "%A, %B %d, %Y %H:%M:%S").strftime('%d-%m-%Y') for row in result])
            

            print(unique_dates)
            data_by_date = {}

        # Iterate over unique dates and fetch readings
            for date in unique_dates:
                readings = [row['reading'] for row in result if datetime.strptime(row['timestamp'], "%A, %B %d, %Y %H:%M:%S").strftime('%d-%m-%Y') == date]
                data_by_date[date] = readings

            print(data_by_date)
            return make_response({'data_by_date': data_by_date}, 200)
        except mysql.connector.Error as err:
            print(f"MySQL Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        
    def get_work_data_process_data_version_two_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            month=data.get('month')
            date=data.get('date')
            query_work_f1_data = f"SELECT * FROM work_f1 WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}'"
            cur.execute(query_work_f1_data)
            result_1 = cur.fetchall()
            # work_data_station_ids = [row['station_id'] for row in result_work_data]
            
            # station_nums = [int(station_id.split(' ')[2][1:]) for station_id in work_data_station_ids]
            
            # print(station_nums)
            if result_1 is not None:
                    work_f1_data = []
                    for row in result_1:
                        floor_num, line_num, station_number = row['station_id'].split(' ')
                        transformed_row = {
                            'work_id': row['work_id'],
                            'task_id': row['task_id'],  # Extract numeric part and convert to int
                            'station_id': row['station_id'],
                            'station_num': int(station_number[1:]),
                            'process_id': row['process_id'],
                            'part_id': row['part_id'],
                            'timestamp': row['timestamp'],
                            'floor_id': row['floor_id'],
                            'line_id': row['line_id'],
                            'status': row['status'],
                            'reason': row['reason'],
                            'remark': row['remark'],
                            'isfilled': row['isfilled']
                        }
                        work_f1_data.append(transformed_row)
                        
            print(work_f1_data)
            # print(work_data_station_ids)
            # print(result_work_data)
            cur.nextset()
            query_process_data = f"SELECT * FROM process_data WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}' AND DAY(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{date}'"
            cur.execute(query_process_data)
            result_process_data = cur.fetchall()
            # print(result_process_data)
            response_result={
                'work_f1_data':work_f1_data,
                'process_data':result_process_data
            }
            return make_response({'payload4':response_result},200)
        except Exception as err:
            print(f"Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    # savereadings api
    def save_readings_version_two_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            indian_timezone = pytz.timezone('Asia/Kolkata')
            current_time_utc = datetime.utcnow()
            current_time_indian = current_time_utc.replace(tzinfo=pytz.utc).astimezone(indian_timezone)
            formatted_time = current_time_indian.strftime("%A, %B %d, %Y %H:%M:%S")
            parsed_time = datetime.strptime(formatted_time, "%A, %B %d, %Y %H:%M:%S")
            formatted_parsed_time = parsed_time.strftime("%Y-%m-%d")
        
            task_id = data.get('task_id')
            station_id = data.get('station_id')
            process_id = data.get('process_id')
            timestamp = formatted_time
            reading_values = data.get('reading_values')
           

            mCon.start_transaction()
            query = "INSERT INTO readings (task_id, station_id, process_id, timestamp, reading_values) VALUES (%s, %s, %s, %s, %s)"
            values = (task_id, station_id, process_id, timestamp, reading_values)
            if not mCon.is_connected():
                mCon.reconnect()
    
            cur.execute(query, values)
            if cur.rowcount >0:
                mCon.commit()
                return make_response({'message': 'reading data inserted successfully'}, 200)
            else:
                mCon.rollback()
                res = make_response({"readings": "Cannot added"}, 201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except Exception as err:
            print(f"Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()    
    # get readings_data
    def get_readings_data_version_two_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            task_id=data.get('task_id')
            process_id=data.get('process_id')
            station_id=data.get('station_id')
            query="SELECT timestamp,reading_values FROM readings WHERE task_id = %s AND process_id = %s AND station_id = %s"
            value=(task_id,process_id,station_id)
            cur.execute(query,value)
            # result=cur.fetchall()
            result=cur.fetchall()
            unique_dates = set([datetime.strptime(row['timestamp'], "%A, %B %d, %Y %H:%M:%S").strftime('%d-%m-%Y') for row in result])
            

            print(unique_dates)
            readings_data = {}

        # Iterate over unique dates and fetch readings
            for date in unique_dates:
                readings = [row['reading_values'] for row in result if datetime.strptime(row['timestamp'], "%A, %B %d, %Y %H:%M:%S").strftime('%d-%m-%Y') == date]
                readings_data[date] = readings
            return make_response({'readings_data': readings_data}, 200)
        except Exception as err:
            print(f"Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def get_readings_by_date_month_version_model(self,data):
        mCon = self.pool.get_connection()
        try:
            cur = mCon.cursor(dictionary = True)
            month=data.get('month')
            query_readings_data = f"SELECT timestamp, reading_values FROM readings WHERE MONTH(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = '{month}'"
            cur.execute(query_readings_data)
            result = cur.fetchall()

            readings_data = {}

            for row in result:
                timestamp = datetime.strptime(row['timestamp'], "%A, %B %d, %Y %H:%M:%S")
                date_str = timestamp.strftime('%Y-%m-%d')
                if date_str not in readings_data:
                    readings_data[date_str] = []
                readings_data[date_str].append(row['reading_values'])
            return make_response({'readings_data': readings_data}, 200)
        except Exception as err:
            print(f"Error: {err}")
            return make_response({'error': 'Internal Server Error'}, 500)
        finally:
            if cur:
                print("EXECUTIG CLOSE in shift timns")
                cur.close()
            if mCon:
                print("EXECUTIG con close in shift timns")
                mCon.close()

    def getworkforoperator_model(self):
        try:
            # month = data.get('month')
            # date = data.get('date')

            # current_date = datetime.now()

            # Extract the month and date
            # month = current_date.strftime('%m')
            # date = current_date.strftime('%d')

        # Construct and execute the query
            query = "SELECT * FROM work_f1 WHERE DATE(STR_TO_DATE(timestamp, '%W, %M %d, %Y %H:%i:%s')) = CURDATE()"

        # with self.con2.cursor(dictionary=True) as cur:
        #     if not self.con2.is_connected():
        #         self.con2.reconnect()

            self.cur2.execute(query)
            result = self.cur2.fetchall()
            print("result at first",result)
    
            if result is not None:
                for entry in result:
                    station_id = entry["station_id"]
                    split_items = station_id.split()
                # print(split_items)
                    if len(split_items) == 3:
                        F1, L1, S1 = split_items

            # Further split each part
                        F1_part1, F1_part2 = F1[0], F1[1:]
                        L1_part1, L1_part2 = L1[0], L1[1:]
                        S1_part1, S1_part2 = S1[0], S1[1:]

                    # print("F1:", F1_part1, F1_part2)
                    # print("L1:", L1_part1, L1_part2)
                    # print("S1:", S1_part1, S1_part2)                
                # station_num = "".join(filter(str.isdigit, station_id_parts[-1]))

                    entry["station_num"] = S1_part2
            # print(result)
                    res = make_response({"processdata": result},200)
                    res.headers['Access-Control-Allow-Origin'] = "*"
                    res.headers['Content-Type'] = 'application/json'
            # print(res)
                    return res
            else:
                res = make_response({"processdata":"No Data Found"},201)
                res.headers['Access-Control-Allow-Origin'] = "*"
                res.headers['Content-Type'] = 'application/json'
                return res
        except Exception as e:
            print(e)
            traceback.print_exc()
            res = make_response({"processdata":"got error"},202)
            res.headers['Access-Control-Allow-Origin'] = "*"
            res.headers['Content-Type'] = 'application/json'            
            return res
    

