from django.utils.html import format_html

def generate_readonly_fields_html(form, prefixes):
    """
    Generates HTML rows for readonly fields across prefixes like 'oc', 'cc', and 'hy'.
    Assumes that each profitability metric has the pattern: <prefix>_<field>
    """
    readonly_fields = ['mtr_cost', 'total_price', 'profit', 'margins', 'commission', 'profit_after_com']
    html_output = ''

    for field in readonly_fields:
        row = f'<tr><th>{field.replace("_", " ").title()}</th>'
        for prefix in prefixes:
            field_name = f'{prefix}_{field}'
            value = getattr(form.instance, field_name, '')
            row += f'<td>{value:.2f}</td>' if isinstance(value, (int, float)) else f'<td>{value}</td>'
        row += '</tr>'
        html_output += row

    return format_html(html_output)
