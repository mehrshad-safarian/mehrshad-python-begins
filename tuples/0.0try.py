employee_record = ("Sophie Turner", "Actress", 29, "Northampton, England", "salary: 175k USD")
data_components = (2025, 1, 10)

project_phases = ("planning", "development", "testing", "deployment")
print(len(project_phases))
combined_phases = project_phases + ("maintenance",) 
current_phase = project_phases[0]
print(combined_phases)
print(current_phase)

serve_status = ("active", "inactive", "active", "maintenance")
active_status = serve_status.count("active")
inactive_position = serve_status.index("inactive")
config_settings = ("debug_mode", "test_server", "logging_enable")
config_settings[0] = "release_mode" 