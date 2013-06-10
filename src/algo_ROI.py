# Brian Ward
# Principal Systems
# 11/10/2012
from collections import OrderedDict

"""
CLASS TO WORK OUT THE ROI FORMULA FOR A COMPANY
"""


class Algo_roi:
# Direct Labour Savings

    def __init__(self):
        # print('instaniated')
        self.shifts_per_day = 2
        self.pickers_per_shift = 10
        self.fork_drivers_per_shift = 3
        self.days_in_working_week = 6
        self.hours_per_shift = 8
        self.weeks_of_operation_per_year = 52
        self.productivity_improvement = .25
        self.Burdened_Labor_Cost_per_Hour = 1.00
        self.hours_of_operation_per_annum = 0.0
        self.number_of_hours_work_per_annum_per_operator = 0.0

        # we predict a 25% productivity saving
        self.productivity_saving = .25

        # cost of errors
        self.cost_per_pick_error = .02  # 2 cents
        self.pallet_error_rate_cost = 2  # 2 euros

        self.index_error_rate = .002
        self.current_picking_error_rate = .01
        self.full_pallet_error_rate = .01

# collection rate
        self.items_picked_per_Hour = 100
        self.pallets_collected_per_Hour = 10
        # in
        self.pick_saving = 0
        self.pallet_saving = 0
        self.total_labour_saving = 0
        # accuracy savings
        self.error_reduction_savings = 0
        self.reduced_error_rate_pick = 0
        self.reduced_error_rate_pallet = 0
        self.fill_pallet_error_reduction_potential = 0
        self.picking_error_reduction_potential = 0

    """
        number of hours worked by picker over the entire year
    """

    def hours_of_operation_per_year_picking(self):
        # total cost perp hour per worker per shift per year
        # print('here3')
        self.hours_of_operation_per_annum = (self.number_of_hours_work_per_annum_per_operator_function() * self.pickers_per_shift * self.Burdened_Labor_Cost_per_Hour)
        print('Hours of operation per annum = ', self.hours_of_operation_per_annum)
        # savings made by implementing our solution

    """
        number of work hours by operators
    """

    def number_of_hours_work_per_annum_per_operator_function(self):
        # print('here1')
        self.number_of_hours_work_per_annum_per_operator = self.shifts_per_day * self.days_in_working_week * self.hours_per_shift * self.weeks_of_operation_per_year
        return float(self.number_of_hours_work_per_annum_per_operator) 

    """
    Hours saved by producivity improvement
    """

    def producivity_saving(self):
        # call the functions on number of hours worked per year
        self.hours_operation_picking = self.hours_of_operation_per_year_picking()
        self.hours_annum_operator = self.number_of_hours_work_per_annum_per_operator_function()
        self.total_labour_saving = self.hours_of_operation_per_annum * self.productivity_saving
        print('Hours saved by producivity improvement= ',
               self.total_labour_saving)
        print('*' * 40)
        return self.total_labour_saving

    """
        Number of pallets moved in a year by forklift drivers
    """

    def picks_per_annum(self):
        self.picks_per_year = self.number_of_hours_work_per_annum_per_operator * self.items_picked_per_Hour * self.items_picked_per_Hour
        print('The number of picks in a year = ', self.picks_per_year)

    def full_pallets_per_year(self):
            # palletsd by hours by frivers by hours in the year
        self.pallets_moved_per_year = self.pallets_collected_per_Hour * self.fork_drivers_per_shift * self.number_of_hours_work_per_annum_per_operator_function()
        print('Number of Hours work per annum per operator = ',
               self.number_of_hours_work_per_annum_per_operator)
        print('The number of pallets moved in a year = '
              , self.pallets_moved_per_year)

    """
        The saving from reducing errors
    """

    def error_reduction_saving(self):
        # index's rate minus 100% accuracy minus customer error rate.
        self.reduced_error_rate_pick = self.current_picking_error_rate - self.index_error_rate
        # pick in a year
        self.picks_per_annum()
        # pallets per year
        self.full_pallets_per_year()
        # error reduction on pallets
        self.reduced_error_rate_pallet = self.full_pallet_error_rate - self.index_error_rate
        print('Reduced error rate for a PICK is', self.reduced_error_rate_pick)
        print('Reduced error rate for a PALLET is',
               self.reduced_error_rate_pallet)
        print('The cost per pick error is : ', self.cost_per_pick_error)
        print('The cost per pallet error is : ', self.pallet_error_rate_cost)
        # savings per pick and per pallet
        
        # error reduction by number of picking hours in a year by pick by hours
        self.picking_error_reduction_potential = self.reduced_error_rate_pick * self.hours_of_operation_per_annum * self.items_picked_per_Hour        
        print('Picking error reduction potential',
               self.picking_error_reduction_potential)
        # picking saving
        self.pick_saving = self.cost_per_pick_error * self.picking_error_reduction_potential
        self.fill_pallet_error_reduction_potential = self.reduced_error_rate_pallet * self.pallets_moved_per_year
        print ('Full Pallet error reduction potential',
                self.fill_pallet_error_reduction_potential)
        # pallet saving
        self.pallet_saving = self.fill_pallet_error_reduction_potential * self.pallet_error_rate_cost    
        print('\nPick saving : ',
               self.pick_saving)
        print('Pallet saving : ', self.pallet_saving)

        self.error_reduction_savings = self.pick_saving + self.pallet_saving

    """
        Print out the results of the roi
    """
    def total_roi(self):
        self.total_roi = self.total_labour_saving + self.error_reduction_savings
        return self.total_roi 

    def print_algo_roi(self):
        print('*' * 40)
        print('\nRwecurring annual Labour Savings = ',
               self.total_labour_saving)
        print('Recurring annual Accuracy savings = ',
               self.error_reduction_savings)
        print('The Total savings per annum are = ', self.total_roi)
        # use an ordered dictionary
        self.roi_data_dict = OrderedDict([
        ('hours_op_annum', self.hours_of_operation_per_annum),
        ('number_of_hours_work_per_annum_per_operator',
          self.number_of_hours_work_per_annum_per_operator),
        ('hours_operation_picking', self.hours_operation_picking),
        ('total_labour_saving', self.total_labour_saving),
        ('picks_per_year', self.picks_per_year),
        ('pallets_moved_per_year', self.pallets_moved_per_year),
        ('reduced_error_rate_pick', self.reduced_error_rate_pick),
        ('reduced_error_rate_pallet', self.reduced_error_rate_pallet),
        ('picking_error_reduction_potential',
          self.picking_error_reduction_potential),
        ('fill_pallet_error_reduction_potential',
          self.fill_pallet_error_reduction_potential),
        ('pallet_saving', self.pallet_saving),
        ('error_reduction_savings', self.error_reduction_savings),
        ('totalroi', self.total_roi)])

        return self.roi_data_dict

# print(Hours_of_operation_per_annum)
#
# algo1 = Algo_roi()
# algo1.producivity_saving()
# algo1.error_reduction_saving()
# algo1.total_roi()
# algo1.print_algo_roi()
