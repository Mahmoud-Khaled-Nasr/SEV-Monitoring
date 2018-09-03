from database.database import Session
from actions.action import Action
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.lights_status_data_frame import LightsDataFrame
from models.data_frames.switches_status_data_frame import SwitchesDataFrame
from models.data_frames.battery_data_frame import BatteryDataFrame
from models.data_frames.driver_master_MC_data_frame import DriverMasterMCDataFrame
from models.data_frames.driver_slave_MC_data_frame import DriverSlaveMCDataFrame
from definitions import DatabaseTableTypes
from GUI.GUI_interface import GUIInterface


class CreateTableAction(Action):
    # Constructor
    def __init__(self, dispatcher, table_type: DatabaseTableTypes):
        super().__init__(dispatcher)
        self.table_type: DatabaseTableTypes = table_type
        self.table_data = None
        self.table_column_headers = None

    def execute(self):
        self.__get_table_data()
        if self.table_data:
            column_count = len(self.table_data[0])
        else:
            column_count = 0
        gui_interface: GUIInterface = self.dispatcher.gui_interface
        gui_interface.update_table_data(column_count=column_count,
                                        table_data=self.table_data,
                                        table_column_headers=self.table_column_headers)

    # Sets the table data and table column headers of the given table type as a 2D list
    def __get_table_data(self):
        # Open a session
        session = Session()
        # Check for table type
        table_type = self.table_type
        # Currents table
        if table_type is DatabaseTableTypes.CURRENTS_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(CurrentsDataFrame.time,
                                            CurrentsDataFrame.motors_current,
                                            CurrentsDataFrame.battery_current,
                                            CurrentsDataFrame.solar_panels_current).\
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            # Set table headers
            self.table_column_headers = ["Time", "Motors Current", "Battery Current", "Solar Panels Current"]
        # Bus Voltages table
        elif table_type is DatabaseTableTypes.BUS_VOLTAGES_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(BusVoltagesDataFrame.time,
                                            BusVoltagesDataFrame.DC_bus_voltage,
                                            BusVoltagesDataFrame.charge_rate). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            self.table_column_headers = ["Time", "DC Bus Voltage", "Charge Rate"]
        # Temperatures Table
        elif table_type is DatabaseTableTypes.TEMPERATURES_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(TemperaturesDataFrame.time,
                                            TemperaturesDataFrame.solar_panels_temperature). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            self.table_column_headers = ["Time", "Solar Panels Temperature"]
        # Batteries Table
        elif table_type is DatabaseTableTypes.BATTERIES_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(BatteryDataFrame.time,
                                            BatteryDataFrame.battery_id,
                                            BatteryDataFrame.voltage,
                                            BatteryDataFrame.temperature). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            self.table_column_headers = ["Time", "Battery Module ID", "Battery Module Volt",
                                         "Battery Module Temperature"]
        # Master Motor Table
        elif table_type is DatabaseTableTypes.MASTER_MOTOR_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(DriverMasterMCDataFrame.time,
                                            DriverMasterMCDataFrame.master_motor_speed,
                                            DriverMasterMCDataFrame.master_motor_current). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            self.table_column_headers = ["Time", "Master Motor Speed", "Master Motor Current"]
        # Slave Motor Table
        elif table_type is DatabaseTableTypes.SLAVE_MOTOR_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(DriverSlaveMCDataFrame.time,
                                            DriverSlaveMCDataFrame.slave_motor_speed,
                                            DriverSlaveMCDataFrame.slave_motor_current). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            self.table_column_headers = ["Time", "Slave Motor Speed", "Slave Motor Current"]
        # Lights Status Table
        elif table_type is DatabaseTableTypes.LIGHTS_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(LightsDataFrame.time,
                                            LightsDataFrame.head_lights,
                                            LightsDataFrame.tail_lights,
                                            LightsDataFrame.left_indicator,
                                            LightsDataFrame.right_indicator,
                                            LightsDataFrame.high_beam,
                                            LightsDataFrame.brake_light,
                                            LightsDataFrame.backing_light,
                                            LightsDataFrame.daytime_light). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            self.table_column_headers = ["Time", "Head Lights", "Tail Lights", "Left Indicator",
                                         "Right Indicator", "High Beam", "Brake Light",
                                         "Backing Light", "Daytime Light"]
        # Switches Status Table
        elif table_type is DatabaseTableTypes.SWITCHES_TABLE:
            # Return table data as a list of tuples
            self.table_data = session.query(SwitchesDataFrame.time,
                                            SwitchesDataFrame.motor_on,
                                            SwitchesDataFrame.forward,
                                            SwitchesDataFrame.reverse,
                                            SwitchesDataFrame.light_on,
                                            SwitchesDataFrame.warning,
                                            SwitchesDataFrame.daytime). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples to a list of lists
            self.table_data = [list(elem) for elem in self.table_data]
            self.table_column_headers = ["Time", "Motor On", "Forward", "Reverse",
                                         "Light On", "Warning", "Daytime"]
        # Close the session
        session.close()
