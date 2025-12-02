# Complex authentication with proper group checks and conditions
is_admin = True
has_full_access = True
is_special_case = False 

# Clear grouping with parentheses
can_modify = (is_admin and has_full_access) or is_special_case

# multiple conditions with line breaks
is_valid = (
    is_admin
    and has_full_access
    and not is_special_case
)