import sqlite3
import logging
import settings
import time

class Database:

    def __init__(self):
        try:
            self.connection = sqlite3.connect(settings.DB_PATH + "/lunar.db",check_same_thread=False)
            logging.info("Connected to the DB.")
        except Exception as e:
            logging.error(f"Could not connect to the DB: {e}.")
            raise e

        #check if the table is created. If not create it
        self.cursor = self.connection.cursor()
    
    def write_lunar_cycle(self,input_dict):
        if 'date' not in input_dict or input_dict['date'] == None:
            logging.error("No date provided, could not write lunar phase.")
            raise Exception("No date provided, could not write lunar phase.")
        if 'jsonfile' not in input_dict or input_dict['jsonfile'] == None:
            logging.error("No json file path given, could not write lunar phase.")
            raise Exception("No json file path given, could not write lunar phase.")
        if 'phase' not in input_dict or input_dict['phase'] == None:
            logging.error("No lunar phase given, could not write lunar phase.")
            raise Exception("No lunar phase given, could not write lunar phase.")
        
        try:
            self.cursor.execute("INSERT OR REPLACE INTO LunarPhase (timestamp,jsonfile,phase) VALUES (?,?,?)",(input_dict['date'],input_dict['jsonfile'],input_dict['phase']))
            self.connection.commit()
            out = {'Phase': input_dict['phase'],'JSONfile':input_dict['jsonfile']}
        except Exception as e:
            print(e)
            logging.error(f'Could not write to the DB: {e}.')
        else:
            self.connection.rollback()
        
        return out

    def get_lunar_cycle(self,input_dict):
        if 'date' not in input_dict or input_dict['date'] == None:
            logging.error("No date provided, could not retrieve lunar phase.")
            raise Exception("No date provided, could not retrieve lunar phase.")
        
        try:
            self.cursor.execute(f"SELECT * FROM LunarDates where timestamp='{input_dict['date']}'")
            out = self.cursor.fetchone()
        except Exception as e:
            print(e)
            logging.error(f'Could retrieve the date {input_dict['date']} from LunarDates: {e}.')

        return out