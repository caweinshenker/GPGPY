create table BP(
	input_dim INT NOT NULL,
	output_dim INT NOT NULL,
	num_layers INT NOT NULL,
	train_samples INT NOT NULL,
	topology VARCHAR(1000) NOT NULL,
	IPC FLOAT
);

create table MBP(
	input_dim INT NOT NULL,
	output_dim INT NOT NULL,
	num_layers INT NOT NULL,
	train_samples INT NOT NULL,
	topology VARCHAR(1000) NOT NULL,
	IPC FLOAT
);

create table ATS(
	input_dim INT NOT NULL,
	output_dim INT NOT NULL,
	num_layers INT NOT NULL,
	topology VARCHAR(1000) NOT NULL,
	max_epochs INT DEFAULT 0,
	rms_stop FLOAT DEFAULT 0.01,
	robust BOOL DEFAULT true,
	num_networks INT DEFAULT 1,
	train_samples INT NOT NULL,
	algorithms VARCHAR(3) DEFAULT "MBP" NOT NULL,
	IPC FLOAT NOT NULL
);


create table DBN(
	input_dim INT NOT NULL,
	output_dim INT NOT NULL,
	num_layers INT NOT NULL,
	topology VARCHAR(1000) NOT NULL,
	max_epochs INT DEFAULT 0,
	rms_stop FLOAT DEFAULT 0.01,
	train_samples INT NOT NULL,
	mini_batch INT DEFAULT 0 NOT NULL,
	momentum  FLOAT DEFAULT 0 NOT NULL,
	num_networks INT DEFAULT 1,
	algorithms VARCHAR(3) DEFAULT "MBP" NOT NULL,
	IPC FLOAT NOT NULL
);
	
