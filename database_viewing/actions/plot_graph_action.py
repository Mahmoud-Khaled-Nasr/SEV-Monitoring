from database.database import Session
from database_viewing.actions.action import Action
from models.data_frames.currents_data_frame import CurrentsDataFrame
from models.data_frames.bus_voltages_data_frame import BusVoltagesDataFrame
from models.data_frames.tempratures_data_frame import TemperaturesDataFrame
from models.data_frames.battery_data_frame import BatteryDataFrame
from models.data_frames.driver_master_MC_data_frame import DriverMasterMCDataFrame
from models.data_frames.driver_slave_MC_data_frame import DriverSlaveMCDataFrame
from definitions import MonitoredItems
from database_viewing.GUI.GUI_interface import GUIInterface
from typing import Dict


class PlotGraphAction(Action):
    # Constructor
    def __init__(self, dispatcher, items_to_plot: Dict[MonitoredItems, bool]):
        super().__init__(dispatcher)
        self.items_to_plot = items_to_plot

    def execute(self):
        all_graphs_data = self.__get_all_graphs_data()
        gui_interface: GUIInterface = self.dispatcher.gui_interface
        gui_interface.plot(all_graphs_data=all_graphs_data)

    # Private method: Gets all data that needs to be plotted as a list of tuples, each tuple is a graph
    # Each tuple contains 2 lists, one for X values and one for Y values
    def __get_all_graphs_data(self):
        # Open a session
        session = Session()

        all_graphs_data = []

        # Check which graphs to get their data
        # Battery Current
        if self.items_to_plot[MonitoredItems.BATTERY_CURRENT]:
            # Return table data as a list of tuples
            graph_data = session.query(CurrentsDataFrame.time,
                                       CurrentsDataFrame.battery_current). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # Motors Current
        if self.items_to_plot[MonitoredItems.MOTORS_CURRENT]:
            # Return table data as a list of tuples
            graph_data = session.query(CurrentsDataFrame.time,
                                       CurrentsDataFrame.motors_current). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # Solar Panels Current
        if self.items_to_plot[MonitoredItems.SOLAR_PANELS_CURRENT]:
            # Return table data as a list of tuples
            graph_data = session.query(CurrentsDataFrame.time,
                                       CurrentsDataFrame.solar_panels_current). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # DC Bus Voltage
        if self.items_to_plot[MonitoredItems.DC_BUS_VOLT]:
            # Return table data as a list of tuples
            graph_data = session.query(BusVoltagesDataFrame.time,
                                       BusVoltagesDataFrame.DC_bus_voltage). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # Charge Rate
        if self.items_to_plot[MonitoredItems.CHARGE_RATE]:
            # Return table data as a list of tuples
            graph_data = session.query(BusVoltagesDataFrame.time,
                                       BusVoltagesDataFrame.charge_rate). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # Solar Panels Temperature
        if self.items_to_plot[MonitoredItems.SOLAR_PANELS_TEMPERATURE]:
            # Return table data as a list of tuples
            graph_data = session.query(TemperaturesDataFrame.time,
                                       TemperaturesDataFrame.solar_panels_temperature). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # TODO implement batteries highlights graphs
        # Min Battery Voltage
        if self.items_to_plot[MonitoredItems.MIN_BATTERY_VOLT]:
            pass
        # Max Battery Voltage
        if self.items_to_plot[MonitoredItems.MAX_BATTERY_VOLT]:
            pass
        # Max Battery Temperature
        if self.items_to_plot[MonitoredItems.MAX_BATTERY_TEMPERATURE]:
            pass
        # Master Motor Current
        if self.items_to_plot[MonitoredItems.MASTER_MOTOR_CURRENT]:
            # Return table data as a list of tuples
            graph_data = session.query(DriverMasterMCDataFrame.time,
                                       DriverMasterMCDataFrame.master_motor_current). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # Master Motor Speed
        if self.items_to_plot[MonitoredItems.MASTER_MOTOR_SPEED]:
            # Return table data as a list of tuples
            graph_data = session.query(DriverMasterMCDataFrame.time,
                                       DriverMasterMCDataFrame.master_motor_speed). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # Slave Motor Current
        if self.items_to_plot[MonitoredItems.SLAVE_MOTOR_CURRENT]:
            # Return table data as a list of tuples
            graph_data = session.query(DriverSlaveMCDataFrame.time,
                                       DriverSlaveMCDataFrame.slave_motor_current). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))
        # Slave Motor Speed
        if self.items_to_plot[MonitoredItems.SLAVE_MOTOR_SPEED]:
            # Return table data as a list of tuples
            graph_data = session.query(DriverSlaveMCDataFrame.time,
                                       DriverSlaveMCDataFrame.slave_motor_speed). \
                filter_by(lap_id=self.dispatcher.current_lap.id).all()
            # Convert list of tuples into two lists
            [x, y] = map(list, zip(*graph_data))
            # Form a tuple of the 2 lists and add it to all_graphs_data
            all_graphs_data.append((x, y))

        # Close the session
        session.close()

        return all_graphs_data
