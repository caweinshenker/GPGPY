###############################
# Colin Weinshenker
# caweinshenker@email.wm.edu
#
# 12/2016
#
#
######################################


"""
Hold configuration constants and a wrapper class for sets that 
hold their variable names
"""

###########################
#Named Set

class NamedSet(set):
        """Wrapper class adds variable name to set built-in
           Eliminates to search call stack for name
           when writing metadata to file
        """
        def __init__(self, s=(), name = None):
                super(NamedSet, self).__init__(s)
                self.name = name
###########################




###########################
#Config options


simulation_run_config_options = NamedSet(set(["-gpgpu_max_cycle", "-gpgpu_max_insn",\
                        "-gpgpu_ptx_sim_mode", "-gpgpu_deadlock_detect",\
                        "-gpgpu_max_cta", "-gpgpu_max_concurrent_kernel"]),\
                         "simulation_run_config_options")

stat_collection_options = NamedSet(set(["-gpgpu_ptx_instruction_classification", "-gpgpu_runtime_stat",\
		"-gpgpu_memlatency_stat", "-visualizer_enabled",\
		"-visualizer_outputfile", "-visualizer_zlevel",\
		"-save_embedded_ptx", "-enable_ptx_file_line_stats",\
		"-ptx_line_stats_filename", "-gpgpu_warpdistro_shader",\
		"-gpgpu_cflog_interval", "-keep"]), "stat_collection_options")

high_level_architecture_configuration_options = NamedSet(set(["-gpgpu_n_mem", "-gpgpu_clock_domains",\
		"-gpgpu_n_clusters", "-gpgpu_n_cores_per_cluster"]),\
		 "high_level_architecture_configuration_options")


additional_architecture_configuration_options= NamedSet(set(["-gpgpu_num_sched_per_core", "-gpgpu_max_insn_issue_per_warp"]),\
		"additional_architecture_configuration_options")

scheduler_options=NamedSet(set(["-gpgpu_num_sched_per_core", "-gpgpu_max_insn_issue_per_warp"]),"scheduler_options")

shader_core_pipeline_configuration_options= NamedSet(set(["-gpgpu_shader_core_pipeline", "-gpgpu_shader_registers",\
		"-gpgpu_shader_cta", "-gpgpu_simd_model",\
		"-ptx_opcode_latency_int", "-ptx_opcode_latency_fp",\
		"-ptx_opcode_latency_dp", "-ptx_opcode_initiation_int", "-ptx_opcode_initiation_fp",\
		"-ptx_opcode_initiation_dp"]), "shader_core_pipeline_configuration_options")

memory_sub_system_configuration_options= NamedSet(set(["-gpgpu_perfect_mem", "-gpgpu_tex_cache:l1", \
		"-gpgpu_const_cache:l1", "-gpgpu_cache:il1",\
		"-gpgpu_cache:dl1", "-gpgpu_cache:dl2",\
		 "-gpgpu_shmem_size", "-gpgpu_flush_cache",\
		"-gpgpu_local_mem_map", "-gpgpu_num_reg_banks",\
		 "-gpgpu_reg_bank_use_warp_id", "-gpgpu_cache:dl2_texture_only",\
		"-gpgpu_shmem_warp_parts"]), "memory_sub_system_configuration_options")


operand_collector_configuration_options = NamedSet(set(["-gpgpu_operand_collector_num_units_sp", "-gpgpu_operand_collector_num_units_sfu",\
		"-gpgpu_operand_collector_num_units_mem", "-gpgpu_operand_collector_num_gen",\
		"-gpgpu_operand_collector_num_in_ports_sp",  "-gpgpu_operand_collector_num_in_ports_sfu",\
		"-gpgpu_operand_collector_num_in_ports_mem", "-gpgpu_operand_collector_num_in_ports_gen",\
		"-gpgpu_operand_collector_num_out_ports_sp", "-gpgpu_operand_collector_num_out_ports_sfu",\
		"-gpgpu_operand_collector_num_out_ports_mem", "-gpgpu_operand_collector_num_out_ports_gen"]), "operand_collector_configuration_options")

dram_controller_configuration_options= NamedSet(set(["-gpgpu_dram_scheduler", "-gpgpu_frfcfs_dram_sched_queue_size", \
		"-gpgpu_dram_return_queue_size", "-gpgpu_dram_buswidth",\
		"-gpgpu_dram_burst_length", "-gpgpu_dram_timing_opt",\
		"-gpgpu_mem_address_mask", "-gpgpu_mem_addr_mapping",\
		"-gpgpu_n_mem_per_ctrlr", "-gpgpu_dram_partition_queues",\
		 "-rop_latency", "-dram_latency"]),\
		"dram_controller_configuration_options")

interconnection_configuration_options = NamedSet(set(["-inter_config_file", "-network_mode"]),\
		 "interconnection_configuration_options")

ptx_configuration_options = NamedSet(set(["-gpgpu_ptx_use_cuobjdump", "-gpgpu_ptx_convert_to_ptxplus",\
		 "-gpgpu_ptx_save_converted_ptxplus",\
		 "-gpgpu_ptx_force_max_capability", "-gpgpu_ptx_inst_debug_to_file",\
		 "-gpgpu_ptx_inst_debug_thread_uid"]),\
		 "ptx_configuration_options")

unrecognized_configuration_options = NamedSet(set([]), "unrecognized_configuration_options")


default_configs = [simulation_run_config_options, stat_collection_options,\
		high_level_architecture_configuration_options,\
		additional_architecture_configuration_options,\
		scheduler_options, shader_core_pipeline_configuration_options,\
		memory_sub_system_configuration_options, operand_collector_configuration_options,\
		dram_controller_configuration_options, interconnection_configuration_options,\
		ptx_configuration_options, unrecognized_configuration_options]

###########################



