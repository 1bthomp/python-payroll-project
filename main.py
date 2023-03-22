from prettytable import PrettyTable

payroll_list = []

while len(payroll_list) < 10:
    emp_name = input("Employee name: ")
    t_hours = float(input("Hours worked: "))
    pay_rate = float(input("Pay rate: "))

    if t_hours > 40.0:
        ot_pay = (t_hours - 40) * round(pay_rate * 1.5)
        reg_pay = round(40 * pay_rate, 2)
        gross = round(reg_pay + ot_pay, 2)
    else:
        reg_pay = round(t_hours * pay_rate, 2)
        ot_pay = 0.0
        gross = reg_pay

    fed = round(gross * .10, 2)
    state = round(gross *.06, 2)
    fica = round(gross * .03, 2)
    tax = fed + state + fica

    payroll_dict = {'Employee Name': emp_name,
                    'Hours Worked': t_hours,
                    'Pay Rate': pay_rate,
                    'OT Pay': ot_pay,
                    'Gross Pay': gross,
                    'Federal Tax': fed,
                    'State Tax': state,
                    'FICA': fica,
                    'Total Tax': tax}

    payroll_list.append(payroll_dict)

table = PrettyTable()
table.field_names = payroll_list[0].keys()
for payroll in payroll_list:
    table.add_row(payroll.values())

print(table)