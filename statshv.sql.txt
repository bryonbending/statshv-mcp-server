-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.41 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.11.0.7065
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for view statshv.actual_protocol_testtime_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `actual_protocol_testtime_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`StartTime` TIMESTAMP NOT NULL,
	`FinishTime` DATETIME NULL,
	`YearMonth` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`Startup_Act` BIGINT NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests_Act` FLOAT NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`LowLevel_Rinse_Act` FLOAT NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1_Act` FLOAT NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ_Act` FLOAT NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data_Act` FLOAT NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal_Act` FLOAT NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver_Act` FLOAT NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal_Act` FLOAT NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver_Act` FLOAT NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity_Act` FLOAT NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision_Act` FLOAT NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2_Act` FLOAT NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL,
	`Constants_Act` FLOAT NULL,
	`Constants_Exp` FLOAT NULL
);

-- Dumping structure for table statshv.bay_status
CREATE TABLE IF NOT EXISTS `bay_status` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Row identifier',
  `Station` varchar(15) NOT NULL DEFAULT '' COMMENT 'Workstation Name',
  `Bay` varchar(15) NOT NULL DEFAULT '' COMMENT 'Bay identifier for status info',
  `SerialNo` varchar(15) NOT NULL DEFAULT '' COMMENT 'Instrument SerialNo in the Bay',
  `ShopOrder` varchar(15) NOT NULL DEFAULT '' COMMENT 'ShopOrder for the Instrument under test',
  `Series` varchar(10) NOT NULL DEFAULT '' COMMENT 'Series of the Instrument - M500, M500e',
  `Model` varchar(15) NOT NULL DEFAULT '' COMMENT 'Model of the Instrument - STD IOS, INLINE SAMPLER, SUPER IOS',
  `Options` varchar(6) NOT NULL DEFAULT '' COMMENT 'Options installed on the Instrument - Not Used',
  `StartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Starting time for the T&C process',
  `CurrentProtocol` varchar(45) NOT NULL DEFAULT '' COMMENT 'Name of the current Protocol being executed',
  `Step` int NOT NULL DEFAULT '0' COMMENT 'Step number for the current protocol',
  `TotalSteps` int NOT NULL DEFAULT '0' COMMENT 'Total number of Steps in the Test',
  `StepStatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'Step status - 0-Failure(Red), 1-Pass(Green), 2-Needs Attention(Yellow)',
  `LastProtocol` varchar(45) NOT NULL DEFAULT '0' COMMENT 'Name of the current Protocol being executed',
  `LastProtocolTime` float NOT NULL DEFAULT '0' COMMENT 'Last Protocol time in minutes',
  `LastProtocolExpectedTime` float NOT NULL DEFAULT '0' COMMENT 'Last Protocol expected time in minutes',
  `LastProtocolDelta` float NOT NULL DEFAULT '0',
  `TotalExpectedTime` float NOT NULL DEFAULT '0' COMMENT 'Total expected time in minutes for Instrument on the Bay',
  `ExpectedRemainingTime` float NOT NULL DEFAULT '0',
  `ActualRemainingTime` float NOT NULL DEFAULT '0',
  `ExpectedFinishDateTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `ActualFinishDateTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=latin1 COMMENT='Work cell and Bay status';

-- Data exporting was unselected.

-- Dumping structure for view statshv.bay_status_test_time_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `bay_status_test_time_90_day_view` (
	`RecNo` INT UNSIGNED NOT NULL COMMENT 'Row identifier',
	`Station` VARCHAR(1) NOT NULL COMMENT 'Workstation Name' COLLATE 'latin1_swedish_ci',
	`Bay` VARCHAR(1) NOT NULL COMMENT 'Bay identifier for status info' COLLATE 'latin1_swedish_ci',
	`SerialNo` VARCHAR(1) NOT NULL COMMENT 'Instrument SerialNo in the Bay' COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COMMENT 'ShopOrder for the Instrument under test' COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NOT NULL COMMENT 'Series of the Instrument - M500, M500e' COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NOT NULL COMMENT 'Model of the Instrument - STD IOS, INLINE SAMPLER, SUPER IOS' COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NOT NULL COMMENT 'Options installed on the Instrument - Not Used' COLLATE 'latin1_swedish_ci',
	`StartTime` DATETIME NOT NULL COMMENT 'Starting time for the T&C process',
	`CurrentProtocol` VARCHAR(1) NOT NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`Step` INT NOT NULL COMMENT 'Step number for the current protocol',
	`TotalSteps` INT NOT NULL COMMENT 'Total number of Steps in the Test',
	`StepStatus` TINYINT(1) NOT NULL COMMENT 'Step status - 0-Failure(Red), 1-Pass(Green), 2-Needs Attention(Yellow)',
	`LastProtocol` VARCHAR(1) NOT NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`LastProtocolTime` FLOAT NOT NULL COMMENT 'Last Protocol time in minutes',
	`LastProtocolExpectedTime` FLOAT NOT NULL COMMENT 'Last Protocol expected time in minutes',
	`LastProtocolDelta` FLOAT NOT NULL,
	`TotalExpectedTime` FLOAT NOT NULL COMMENT 'Total expected time in minutes for Instrument on the Bay',
	`ExpectedRemainingTime` FLOAT NOT NULL,
	`ActualRemainingTime` FLOAT NOT NULL,
	`ExpectedFinishDateTime` DATETIME NOT NULL,
	`ActualFinishDateTime` DATETIME NOT NULL,
	`Startup_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests_Act_90DayAvg` DECIMAL(24,4) NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`LowLevel_Rinse_Act_90DayAvg` DECIMAL(24,4) NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ_Act_90DayAvg` DECIMAL(24,4) NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data_Act_90DayAvg` DECIMAL(24,4) NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal_Act_90DayAvg` DECIMAL(24,4) NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver_Act_90DayAvg` DECIMAL(24,4) NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL
);

-- Dumping structure for view statshv.bay_status_test_time_90_day_view2
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `bay_status_test_time_90_day_view2` (
	`RecNo` INT UNSIGNED NOT NULL COMMENT 'Row identifier',
	`Station` VARCHAR(1) NOT NULL COMMENT 'Workstation Name' COLLATE 'latin1_swedish_ci',
	`Bay` VARCHAR(1) NOT NULL COMMENT 'Bay identifier for status info' COLLATE 'latin1_swedish_ci',
	`SerialNo` VARCHAR(1) NOT NULL COMMENT 'Instrument SerialNo in the Bay' COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COMMENT 'ShopOrder for the Instrument under test' COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NOT NULL COMMENT 'Series of the Instrument - M500, M500e' COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NOT NULL COMMENT 'Model of the Instrument - STD IOS, INLINE SAMPLER, SUPER IOS' COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NOT NULL COMMENT 'Options installed on the Instrument - Not Used' COLLATE 'latin1_swedish_ci',
	`StartTime` DATETIME NOT NULL COMMENT 'Starting time for the T&C process',
	`CurrentProtocol` VARCHAR(1) NOT NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`Step` INT NOT NULL COMMENT 'Step number for the current protocol',
	`TotalSteps` INT NOT NULL COMMENT 'Total number of Steps in the Test',
	`StepStatus` TINYINT(1) NOT NULL COMMENT 'Step status - 0-Failure(Red), 1-Pass(Green), 2-Needs Attention(Yellow)',
	`LastProtocol` VARCHAR(1) NOT NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`LastProtocolTime` FLOAT NOT NULL COMMENT 'Last Protocol time in minutes',
	`LastProtocolExpectedTime` FLOAT NOT NULL COMMENT 'Last Protocol expected time in minutes',
	`LastProtocolDelta` FLOAT NOT NULL,
	`TotalExpectedTime` FLOAT NOT NULL COMMENT 'Total expected time in minutes for Instrument on the Bay',
	`ExpectedRemainingTime` FLOAT NOT NULL,
	`ActualRemainingTime` FLOAT NOT NULL,
	`ExpectedFinishDateTime` DATETIME NOT NULL,
	`ActualFinishDateTime` DATETIME NOT NULL,
	`Startup_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests_Act_90DayAvg` DECIMAL(24,4) NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`LowLevel_Rinse_Act_90DayAvg` DECIMAL(24,4) NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1_Act_90DayAvg` DOUBLE NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ_Act_90DayAvg` DOUBLE NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data_Act_90DayAvg` DECIMAL(24,4) NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal_Act_90DayAvg` DECIMAL(24,4) NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver_Act_90DayAvg` DECIMAL(24,4) NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal_Act_90DayAvg` DOUBLE NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver_Act_90DayAvg` DOUBLE NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity_Act_90DayAvg` DOUBLE NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision_Act_90DayAvg` DOUBLE NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL
);

-- Dumping structure for function statshv.CatchZeroTimestamps
DELIMITER //
CREATE FUNCTION `CatchZeroTimestamps`(possibleZeroTimeStamp VARCHAR(30)) RETURNS datetime
    NO SQL
BEGIN
	
    DECLARE adjustedTime Datetime;
    

  
    
    
   IF (possibleZeroTimeStamp = '0000-00-00 00:00:00') THEN
		
		SET adjustedTime=NULL;
	
        
	
    

 
    else
		SET adjustedTime = possibleZeroTimeStamp;
    
	
	
	END IF;	
    
	RETURN adjustedTime;
    
END//
DELIMITER ;

-- Dumping structure for table statshv.component_build
CREATE TABLE IF NOT EXISTS `component_build` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `PartNo` varchar(20) NOT NULL DEFAULT '',
  `SerialNo` varchar(20) NOT NULL DEFAULT '',
  `Description` varchar(50) NOT NULL DEFAULT '',
  `ParentPartNo` varchar(20) NOT NULL DEFAULT '',
  `ParentSerialNo` varchar(20) NOT NULL DEFAULT '',
  `ItemNo` smallint NOT NULL DEFAULT '0',
  `Level` smallint NOT NULL DEFAULT '0',
  `HasChildren` tinyint(1) NOT NULL DEFAULT '0',
  `AutoSerialNo` tinyint(1) NOT NULL DEFAULT '0',
  `PrintLabel` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(5) NOT NULL DEFAULT '',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdateTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.component_template
CREATE TABLE IF NOT EXISTS `component_template` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `PartNo` varchar(20) NOT NULL DEFAULT '',
  `SerialNo` varchar(20) NOT NULL DEFAULT '',
  `Description` varchar(50) NOT NULL DEFAULT '',
  `ParentPartNo` varchar(20) NOT NULL DEFAULT '',
  `ParentSerialNo` varchar(20) NOT NULL DEFAULT '',
  `ItemNo` smallint NOT NULL DEFAULT '0',
  `Level` smallint NOT NULL DEFAULT '0',
  `HasChildren` tinyint(1) NOT NULL DEFAULT '0',
  `AutoSerialNo` tinyint(1) NOT NULL DEFAULT '0',
  `PrintLabel` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(5) NOT NULL DEFAULT '',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `UpdateTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.condaz
CREATE TABLE IF NOT EXISTS `condaz` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `ThornID` varchar(15) NOT NULL DEFAULT '',
  `ThornCal` date NOT NULL DEFAULT '0000-00-00',
  `RefCond` double NOT NULL DEFAULT '0',
  `OldCond` double NOT NULL DEFAULT '0',
  `NewCond` double NOT NULL DEFAULT '0',
  `CondPass` tinyint(1) NOT NULL DEFAULT '0',
  `ICold` double NOT NULL DEFAULT '0',
  `ICnew` double NOT NULL DEFAULT '0',
  `TCold` double NOT NULL DEFAULT '0',
  `TCnew` double NOT NULL DEFAULT '0',
  `ICTCpass` tinyint(1) NOT NULL DEFAULT '0',
  `LLICfnl` double NOT NULL DEFAULT '0',
  `LLTCfnl` double NOT NULL DEFAULT '0',
  `TempDiff` double NOT NULL DEFAULT '0',
  `TempIC` double NOT NULL DEFAULT '0',
  `TempTC` double NOT NULL DEFAULT '0',
  `TempC3` double NOT NULL DEFAULT '0',
  `TempFnl` double NOT NULL DEFAULT '0',
  `TempPass` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Sample_Cond_AZ_1_Time` datetime DEFAULT NULL,
  `IC_TC_Cond_AZ_Time` datetime DEFAULT NULL,
  `LowLevel_SL1_Data_Time` datetime DEFAULT NULL,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=8752 DEFAULT CHARSET=latin1 COMMENT='UPW_SAMPLE_COND_AUTOZERO_MODE = 25';

-- Data exporting was unselected.

-- Dumping structure for view statshv.condaz1_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `condaz1_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.condaz2
CREATE TABLE IF NOT EXISTS `condaz2` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `ThornID` varchar(10) NOT NULL DEFAULT '',
  `ThornCal` date NOT NULL DEFAULT '0000-00-00',
  `RefCond` double NOT NULL DEFAULT '0',
  `OldCond` double NOT NULL DEFAULT '0',
  `NewCond` double NOT NULL DEFAULT '0',
  `CondPass` tinyint(1) NOT NULL DEFAULT '0',
  `ICold` double NOT NULL DEFAULT '0',
  `ICnew` double NOT NULL DEFAULT '0',
  `TCold` double NOT NULL DEFAULT '0',
  `TCnew` double NOT NULL DEFAULT '0',
  `ICTCpass` tinyint(1) NOT NULL DEFAULT '0',
  `LLICfnl` double NOT NULL DEFAULT '0',
  `LLTCfnl` double NOT NULL DEFAULT '0',
  `TempDiff` double NOT NULL DEFAULT '0',
  `TempIC` double NOT NULL DEFAULT '0',
  `TempTC` double NOT NULL DEFAULT '0',
  `TempC3` double NOT NULL DEFAULT '0',
  `TempFnl` double NOT NULL DEFAULT '0',
  `TempPass` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='UPW_SAMPLE_COND_AUTOZERO_MODE = 25';

-- Data exporting was unselected.

-- Dumping structure for view statshv.condaz2_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `condaz2_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.condaz3_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `condaz3_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.condcalver
CREATE TABLE IF NOT EXISTS `condcalver` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `CalLot` varchar(15) NOT NULL DEFAULT '',
  `CalExp` date NOT NULL DEFAULT '0000-00-00',
  `CondGain` double NOT NULL DEFAULT '0',
  `GainDiff` double NOT NULL DEFAULT '0',
  `CondRSD` double NOT NULL DEFAULT '0',
  `CondAcc` double NOT NULL DEFAULT '0',
  `CondCalPass` tinyint(1) NOT NULL DEFAULT '0',
  `CondVerLot` varchar(15) NOT NULL DEFAULT '',
  `CondVerExp` date NOT NULL DEFAULT '0000-00-00',
  `CondRSD1` double NOT NULL DEFAULT '0',
  `CondACC1` double NOT NULL DEFAULT '0',
  `CondRSD2` double NOT NULL DEFAULT '0',
  `CondACC2` double NOT NULL DEFAULT '0',
  `CondRSD3` double NOT NULL DEFAULT '0',
  `CondACC3` double NOT NULL DEFAULT '0',
  `CondVerPass` tinyint(1) NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Cond_SP_Cal_Time` datetime DEFAULT NULL,
  `Cond_Cal_Ver_Time` datetime DEFAULT NULL,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=5224 DEFAULT CHARSET=latin1 COMMENT='SAMPLE_COND_SINGLE_POINT_CAL_MODE = 4, VER_MODE = 5 ';

-- Data exporting was unselected.

-- Dumping structure for view statshv.condcalver1_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `condcalver1_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.condcalver2_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `condcalver2_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.condcalvials
CREATE TABLE IF NOT EXISTS `condcalvials` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `STDrawAVG` double NOT NULL DEFAULT '0',
  `STDtcompAVG` double NOT NULL DEFAULT '0',
  `STDtempAVG` double NOT NULL DEFAULT '0',
  `STDrawSTD` double NOT NULL DEFAULT '0',
  `STDtcompSTD` double NOT NULL DEFAULT '0',
  `STDtempSTD` double NOT NULL DEFAULT '0',
  `STDrawRSD` double NOT NULL DEFAULT '0',
  `STDtcompRSD` double NOT NULL DEFAULT '0',
  `STDtempRSD` double NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='Generic inital cols';

-- Data exporting was unselected.

-- Dumping structure for table statshv.condvervials
CREATE TABLE IF NOT EXISTS `condvervials` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `RNSrawAVG` double NOT NULL DEFAULT '0',
  `RNStcompAVG` double NOT NULL DEFAULT '0',
  `RNStempAVG` double NOT NULL DEFAULT '0',
  `RNSrawSTD` double NOT NULL DEFAULT '0',
  `RNStcompSTD` double NOT NULL DEFAULT '0',
  `RNStempSTD` double NOT NULL DEFAULT '0',
  `RNSrawRSD` double NOT NULL DEFAULT '0',
  `RNStcompRSD` double NOT NULL DEFAULT '0',
  `RNStempRSD` double NOT NULL DEFAULT '0',
  `STDrawAVG` double NOT NULL DEFAULT '0',
  `STDtcompAVG` double NOT NULL DEFAULT '0',
  `STDtempAVG` double NOT NULL DEFAULT '0',
  `STDrawSTD` double NOT NULL DEFAULT '0',
  `STDtcompSTD` double NOT NULL DEFAULT '0',
  `STDtempSTD` double NOT NULL DEFAULT '0',
  `STDrawRSD` double NOT NULL DEFAULT '0',
  `STDtcompRSD` double NOT NULL DEFAULT '0',
  `STDtempRSD` double NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 COMMENT='Generic inital cols';

-- Data exporting was unselected.

-- Dumping structure for view statshv.cond_cal_ver_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `cond_cal_ver_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.cond_single_point_cal_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `cond_single_point_cal_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.constants
CREATE TABLE IF NOT EXISTS `constants` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `IC_CELL_NUMBER` varchar(15) NOT NULL DEFAULT '',
  `IC_CELL_CONSTANT` double NOT NULL DEFAULT '0',
  `IC_COND_A` double NOT NULL DEFAULT '0',
  `IC_COND_B` double NOT NULL DEFAULT '0',
  `IC_COND_C` double NOT NULL DEFAULT '0',
  `TC_CELL_NUMBER` varchar(15) NOT NULL DEFAULT '',
  `TC_CELL_CONSTANT` double NOT NULL DEFAULT '0',
  `TC_COND_A` double NOT NULL DEFAULT '0',
  `TC_COND_B` double NOT NULL DEFAULT '0',
  `TC_COND_C` double NOT NULL DEFAULT '0',
  `IC_CELL_OFFSET` double NOT NULL DEFAULT '0',
  `TC_CELL_OFFSET` double NOT NULL DEFAULT '0',
  `IC_PPT_SLOPE` double NOT NULL DEFAULT '0',
  `TC_PPT_SLOPE` double NOT NULL DEFAULT '0',
  `IC_PEAK_POINT` int NOT NULL DEFAULT '0',
  `TC_PEAK_POINT` int NOT NULL DEFAULT '0',
  `MULTIPOINT_TOC_SLOPE` double NOT NULL DEFAULT '0',
  `TOC_OFFSET` double NOT NULL DEFAULT '0',
  `USER_TOC_OFFSET` double NOT NULL DEFAULT '0',
  `SAMPLE_CELL_NUMBER` varchar(15) NOT NULL DEFAULT '',
  `SAMPLE_CELL_CONSTANT` double NOT NULL DEFAULT '0',
  `SAMPLE_COND_A` double NOT NULL DEFAULT '0',
  `SAMPLE_COND_B` double NOT NULL DEFAULT '0',
  `SAMPLE_COND_C` double NOT NULL DEFAULT '0',
  `SAMPLE_CELL_OFFSET` double NOT NULL DEFAULT '0',
  `MULTIPOINT_COND_SLOPE` double NOT NULL DEFAULT '0',
  `TEMP_COMP_ALG_INDEX` tinyint(1) NOT NULL DEFAULT '0',
  `TEMP_COMP_REF_TEMP` double NOT NULL DEFAULT '0',
  `TEMP_COMP_ONLINE_REF_TEMP` double NOT NULL DEFAULT '0',
  `TEMP_COMP_LINEAR_COEFF` double NOT NULL DEFAULT '0',
  `PRESSURE` double NOT NULL DEFAULT '0',
  `DIFR` double NOT NULL DEFAULT '0',
  `ICSFR` double NOT NULL DEFAULT '0',
  `TCSFR` double NOT NULL DEFAULT '0',
  `SAMPLE_MOTOR_SELECTION` tinyint(1) NOT NULL DEFAULT '0',
  `SERIAL_NUMBER` varchar(15) NOT NULL DEFAULT '',
  `BASE_MODEL` tinyint(1) NOT NULL DEFAULT '0',
  `SEMICONDUCTOR_TYPE` tinyint(1) NOT NULL DEFAULT '0',
  `DATAGUARD_ACTIVATED` tinyint(1) NOT NULL DEFAULT '0',
  `CONDUCTIVITY_ACTIVATED` tinyint(1) NOT NULL DEFAULT '0',
  `PQ_PROTOCOLS_ACTIVATED` tinyint(1) NOT NULL DEFAULT '0',
  `NO_ONBOARD_DATA_ACTIVATED` tinyint(1) NOT NULL DEFAULT '0',
  `THREE_MINUTE_ANALYSIS_ACTIVATED` tinyint(1) NOT NULL DEFAULT '0',
  `LIMIT_OF_DETECTION` double NOT NULL DEFAULT '0',
  `MAX_OPEN_MODBUS_CLIENTS` int NOT NULL DEFAULT '0',
  `MODBUS_IDLE_CONNECTIONS_TIMEOUT_IN_MIN` int NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(15) NOT NULL DEFAULT '',
  `Bay` int NOT NULL DEFAULT '0',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `Rectime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=4033 DEFAULT CHARSET=latin1 COMMENT='M500 system constants';

-- Data exporting was unselected.

-- Dumping structure for view statshv.constants_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `constants_90_day_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for view statshv.constants_all_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `constants_all_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Rectime` TIMESTAMP NOT NULL
);

-- Dumping structure for procedure statshv.CreateKpiSummaryRecord
DELIMITER //
CREATE PROCEDURE `CreateKpiSummaryRecord`(
	IN `kpiMonth` INT,
	IN `kpiYear` INT,
	OUT `totalProcessed` INT,
	OUT `totalFailed` INT,
	INOUT `fpy` FLOAT,
	OUT `failures` VARCHAR(128),
	OUT `components` VARCHAR(50),
	OUT `leadTime` FLOAT,
	OUT `sqlStmt1` VARCHAR(1024),
	OUT `sqlStmt2` VARCHAR(1024)
)
BEGIN

	DECLARE product VARCHAR(50);
    DECLARE nextKpiYear INT;
    DECLARE kpiProduct VARCHAR(50);
    DECLARE kpiProductYear VARCHAR(50);
    
	SET totalProcessed = 0;
	SET totalFailed = 0;
	SET fpy = 0;
	SET failures = "";
   SET components = "";
   SET leadTime = 0;
   SET product = "";
   SET sqlStmt1 = "";
   SET sqlStmt2 = "";
   SET kpiProduct = "M500";
   SET nextKpiYear = kpiYear + 1;
   SET kpiProductYear = CONCAT(kpiProduct, " ", kpiYear);
   
   SET sql_mode = REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', '');
   
	SET totalProcessed = (SELECT COUNT(SerialNo) FROM statshv.fnlprep_view WHERE MONTH(RecTime) = kpiMonth AND YEAR(RecTime) = kpiYear);
     
	IF totalProcessed IS NULL THEN
		SET totalProcessed = 0;
	END IF;
    
	SET totalFailed = (SELECT COUNT(c.SerialNo) FROM (SELECT SerialNo, Failure FROM statshv.repairdat2 AS r GROUP BY r.SerialNo HAVING r.SerialNo IN (SELECT SerialNo FROM statshv.fnlprep_view AS f WHERE MONTH(f.RecTime) = kpiMonth AND YEAR(f.RecTime) = kpiYear)) AS c);
	
    IF totalFailed IS NULL THEN
		SET totalFailed = 0;
	END IF;
    
   IF totalProcessed > 0 THEN
    	SET fpy = 1 - (totalFailed / totalProcessed);
   END IF;

	IF fpy IS NULL THEN
		SET fpy = 0;
	END IF;
    
	SET failures = (SELECT GROUP_CONCAT(d.Failure) FROM (SELECT c.RecTime, c.SerialNo, c.Failure, COUNT(*) FROM (SELECT Failure, RecTime, SerialNo FROM statshv.repairdat2 AS r WHERE r.SerialNo IN (SELECT SerialNo FROM statshv.fnlprep_view AS f WHERE MONTH(f.RecTime) = kpiMonth AND YEAR(f.RecTime) = kpiYear)) AS c GROUP BY Failure ORDER BY COUNT(*) DESC LIMIT 3) AS d);

	IF failures IS NULL THEN
		SET failures = '';
	END IF;
    
	SET components = (SELECT GROUP_CONCAT(d.Component) FROM (SELECT c.RecTime, c.SerialNo, c.Component, COUNT(*) FROM (SELECT Component, Failure, RecTime, SerialNo FROM statshv.repairdat2 AS r WHERE r.Failure = 'Replaced part(s)/component(s)' AND r.SerialNo IN (SELECT SerialNo FROM statshv.fnlprep_view AS f WHERE MONTH(f.RecTime) = kpiMonth AND YEAR(f.RecTime) = kpiYear)) AS c GROUP BY Component ORDER BY COUNT(*) DESC LIMIT 3) AS d);
    
	IF components IS NULL THEN
		SET components = '';
	END IF;
    
	SET leadTime = (SELECT AVG(TIMESTAMPDIFF(DAY, s.WizardStartTime, f.RecTime)) AS TestTime FROM statshv.fnlprep_view AS f 
					INNER JOIN statshv.startup AS s ON f.SerialNo = s.SerialNo WHERE MONTH(f.RecTime) = kpiMonth AND YEAR(f.RecTime) = kpiYear);
	
    IF leadTime IS NULL THEN
		SET leadTime = 0;
	END IF;
    
    
	SET @qry = CONCAT("SET @product = (SELECT ProductLine FROM report.instrument_kpi WHERE ProductLine = '", kpiProduct, "' AND  `Month` = '", kpiMonth, "' AND `Year` = '", kpiYear, "')");
	PREPARE qryStmt FROM @qry;
	EXECUTE qryStmt;
	DEALLOCATE PREPARE qryStmt;
 
	IF @product IS NULL THEN
		SET sqlStmt1 = CONCAT("INSERT INTO report.instrument_kpi (ProductLine, FPY, TotalFailure, TopFailures, TopComponents, ", 
							"`AverageLeadTime(Days)`, `Year`, `Month`, TotalProcessed) VALUES ('", kpiProduct, "', ", 
                            "'", fpy, "', '", totalFailed, "', '", failures, "', '", components, "', '", leadTime, "', '", 
                            kpiYear, "', '", kpiMonth, "', '", totalProcessed, "')");
		SET @insertSql = sqlStmt1;
        PREPARE insertStmt FROM @insertSql;
        EXECUTE insertStmt;
        DEALLOCATE PREPARE insertStmt;
    ELSE
		SET sqlStmt1 = CONCAT("UPDATE report.instrument_kpi SET ProductLine = '", kpiProduct, "', ", 
									"FPY = '", fpy, "', ", 
									"TotalFailure = '", totalFailed, "', ", 
									"TopFailures = '", failures, "', ", 
									"TopComponents = '", components, "', ", 
									"`AverageLeadTime(Days)` = '", leadTime, "', ", 
									"`Year` = '", kpiYear, "', ", 
									"`Month` = '", kpiMonth, "', ", 
									"TotalProcessed = '", totalProcessed, "' ", 
									"WHERE ProductLine = '", kpiProduct, "' ", 
									"AND `Month` = '", kpiMonth, "' ", 
									"AND `Year` = '", kpiYear, "' ");
		
        SET @updateSql = sqlStmt1;
		PREPARE updateStmt FROM @updateSql;
        EXECUTE updateStmt;
        DEALLOCATE PREPARE updateStmt;
    END IF;
    
    
    SET @qry = CONCAT("SET @product = (SELECT ProductLine FROM report.instrument_kpi WHERE ProductLine = '", kpiProductYear, "' AND  `Month` = '", kpiMonth, "' AND `Year` = '", nextKpiYear, "')");
	PREPARE qryStmt FROM @qry;
	EXECUTE qryStmt;
	DEALLOCATE PREPARE qryStmt;
    
	IF @product IS NULL THEN
		SET sqlStmt2 = CONCAT("INSERT INTO report.instrument_kpi (ProductLine, FPY, TotalFailure, TopFailures, TopComponents, ", 
							"`AverageLeadTime(Days)`, `Year`, `Month`, TotalProcessed) VALUES ('", kpiProductYear, "', ", 
                            "'", fpy, "', '", totalFailed, "', '", failures, "', '", components, "', '", leadTime, "', '", 
                            nextKpiYear, "', '", kpiMonth, "', '", totalProcessed, "')");
		SET @insertSql = sqlStmt2;
        PREPARE insertStmt FROM @insertSql;
        EXECUTE insertStmt;
        DEALLOCATE PREPARE insertStmt;
    ELSE
		SET sqlStmt2 = CONCAT("UPDATE report.instrument_kpi SET ProductLine = '", kpiProductYear, "', ", 
									"FPY = '", fpy, "', ", 
									"TotalFailure = '", totalFailed, "', ", 
									"TopFailures = '", failures, "', ", 
									"TopComponents = '", components, "', ", 
									"`AverageLeadTime(Days)` = '", leadTime, "', ", 
									"`Year` = '", nextKpiYear, "', ", 
									"`Month` = '", kpiMonth, "', ", 
									"TotalProcessed = '", totalProcessed, "' ", 
									"WHERE ProductLine = '", kpiProductYear, "' ", 
									"AND `Month` = '", kpiMonth, "' ", 
									"AND `Year` = '", nextKpiYear, "' ");
		
        SET @updateSql = sqlStmt2;
		PREPARE updateStmt FROM @updateSql;
        EXECUTE updateStmt;
        DEALLOCATE PREPARE updateStmt;
    END IF;
    
END//
DELIMITER ;

-- Dumping structure for procedure statshv.CreateKpiYtdSummaryRecord
DELIMITER //
CREATE PROCEDURE `CreateKpiYtdSummaryRecord`(
	IN `kpiMonth` INT,
	IN `kpiYear` INT,
	OUT `totalProcessed` INT,
	OUT `totalFailed` INT,
	INOUT `fpy` FLOAT,
	OUT `failures` VARCHAR(128),
	OUT `components` VARCHAR(50),
	OUT `leadTime` FLOAT,
	OUT `startDate` VARCHAR(25),
	OUT `stopDate` VARCHAR(25),
	OUT `sqlStmt` VARCHAR(1024)
)
BEGIN

	DECLARE product VARCHAR(50);
    
	SET totalProcessed = 0;
	SET totalFailed = 0;
	SET fpy = 0;
	SET failures = "";
   SET components = "";
   SET leadTime = 0;
   SET product = "";
   SET sqlStmt = "";
    
   SET sql_mode = REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', '');
   
	SET startDate = CONCAT(kpiYear, '-01-01');
    
    IF kpiMonth = 12 THEN
		SET @nextMonth = 1;
        SET @nextYear = kpiYear + 1;
	ELSE
		SET @nextMonth = kpiMonth + 1;
        SET @nextYear = kpiYear;
	END IF;
    
	SET stopDate = CONCAT(@nextYear, '-', @nextMonth, '-1');
	
	SET totalProcessed = (SELECT COUNT(SerialNo) FROM statshv.fnlprep_view WHERE RecTime BETWEEN startDate AND stopDate);
     
	IF totalProcessed IS NULL THEN
		SET totalProcessed = 0;
	END IF;
    
	SET totalFailed = (SELECT COUNT(c.SerialNo) FROM (SELECT SerialNo, Failure FROM statshv.repairdat2 AS r GROUP BY r.SerialNo HAVING r.SerialNo IN (SELECT SerialNo FROM statshv.fnlprep_view AS f WHERE f.RecTime BETWEEN startDate AND stopDate)) AS c);
    
	IF totalFailed IS NULL THEN
		SET totalFailed = 0;
	END IF;
    
   IF totalProcessed > 0 THEN
    	SET fpy = 1 - (totalFailed / totalProcessed);
   END IF;

	IF fpy IS NULL THEN
		SET fpy = 0;
	END IF;
    
	SET failures = (SELECT GROUP_CONCAT(d.Failure) FROM (SELECT c.RecTime, c.SerialNo, c.Failure, COUNT(*) FROM (SELECT Failure, RecTime, SerialNo FROM statshv.repairdat2 AS r WHERE r.SerialNo IN (SELECT SerialNo FROM statshv.fnlprep_view AS f WHERE f.RecTime BETWEEN startDate AND stopDate)) AS c GROUP BY Failure ORDER BY COUNT(*) DESC LIMIT 3) AS d);

	IF failures IS NULL THEN
		SET failures = '';
	END IF;
    
	SET components = (SELECT GROUP_CONCAT(d.Component) FROM (SELECT c.RecTime, c.SerialNo, c.Component, COUNT(*) FROM (SELECT Component, Failure, RecTime, SerialNo FROM statshv.repairdat2 AS r WHERE r.Failure = 'Replaced part(s)/component(s)' AND r.SerialNo IN (SELECT SerialNo FROM statshv.fnlprep_view AS f WHERE f.RecTime BETWEEN startDate AND stopDate)) AS c GROUP BY Component ORDER BY COUNT(*) DESC LIMIT 3) AS d);

	IF components IS NULL THEN
		SET components = '';
	END IF;
    
	SET leadTime = (SELECT AVG(TIMESTAMPDIFF(DAY, s.WizardStartTime, f.RecTime)) AS TestTime FROM statshv.fnlprep_view AS f 
					INNER JOIN statshv.startup AS s ON f.SerialNo = s.SerialNo WHERE f.RecTime BETWEEN startDate AND stopDate);
	
    IF leadTime IS NULL THEN
		SET leadTime = 0;
	END IF;
    
    SET @product = (SELECT ProductLine FROM report.instrument_kpi WHERE ProductLine = 'M500 YTD' AND `Month` = kpiMonth AND `Year` = kpiYear);
 
	IF @product IS NULL THEN
		SET sqlStmt = CONCAT("INSERT INTO report.instrument_kpi (ProductLine, FPY, TotalFailure, TopFailures, TopComponents, ", 
							"`AverageLeadTime(Days)`, `Year`, `Month`, TotalProcessed) VALUES ('M500 YTD', ", 
                            "'", fpy, "', '", totalFailed, "', '", failures, "', '", components, "', '", leadTime, "', '", 
                            kpiYear, "', '", kpiMonth, "', '", totalProcessed, "')");
		SET @insertSql = sqlStmt;
	   PREPARE insertStmt FROM @insertSql;
        EXECUTE insertStmt;
        DEALLOCATE PREPARE insertStmt;
    ELSE
		SET sqlStmt = CONCAT("UPDATE report.instrument_kpi SET ProductLine = 'M500 YTD', ", 
									"FPY = '", fpy, "', ", 
									"TotalFailure = '", totalFailed, "', ", 
									"TopFailures = '", failures, "', ", 
									"TopComponents = '", components, "', ", 
									"`AverageLeadTime(Days)` = '", leadTime, "', ", 
									"`Year` = '", kpiYear, "', ", 
									"`Month` = '", kpiMonth, "', ", 
									"TotalProcessed = '", totalProcessed, "' ", 
									"WHERE ProductLine = 'M500 YTD' AND ", 
									"`Month` = '", kpiMonth, "' ", 
									"AND `Year` = '", kpiYear, "' ");
		
		SET @updateSql = sqlStmt;
		PREPARE updateStmt FROM @updateSql;
        EXECUTE updateStmt;
        DEALLOCATE PREPARE updateStmt;
    END IF;
    
END//
DELIMITER ;

-- Dumping structure for table statshv.expected_testtime
CREATE TABLE IF NOT EXISTS `expected_testtime` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `Series` varchar(10) NOT NULL DEFAULT '',
  `Model` varchar(15) NOT NULL DEFAULT '',
  `Options` varchar(6) NOT NULL DEFAULT '',
  `TotalTests` int NOT NULL DEFAULT '0',
  `Startup_Exp` float NOT NULL DEFAULT '0',
  `IO_Tests_Exp` float NOT NULL DEFAULT '0',
  `LowLevel_Rinse_Exp` float NOT NULL DEFAULT '0',
  `Sample_Cond_AZ_1_Exp` float NOT NULL DEFAULT '0',
  `IC_TC_Cond_AZ_Exp` float NOT NULL DEFAULT '0',
  `LowLevel_SL1_Data_Exp` float NOT NULL DEFAULT '0',
  `TOC_Single_Point_Cal_Exp` float NOT NULL DEFAULT '0',
  `TOC_Ver_Exp` float NOT NULL DEFAULT '0',
  `Cond_Single_Point_Cal_Exp` float NOT NULL DEFAULT '0',
  `Cond_Cal_Ver_Exp` float NOT NULL DEFAULT '0',
  `Specificity_Exp` float NOT NULL DEFAULT '0',
  `Online_Precision_Exp` float NOT NULL DEFAULT '0',
  `Sample_Cond_AZ_2_Exp` float NOT NULL DEFAULT '0',
  `Constants_Exp` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view statshv.expected_testtime_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `expected_testtime_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`Series` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`TotalTests` INT NOT NULL,
	`Startup_Exp` FLOAT NOT NULL,
	`IO_Tests_Exp` FLOAT NOT NULL,
	`LowLevel_Rinse_Exp` FLOAT NOT NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NOT NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NOT NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NOT NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NOT NULL,
	`TOC_Ver_Exp` FLOAT NOT NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NOT NULL,
	`Cond_Cal_Ver_Exp` FLOAT NOT NULL,
	`Specificity_Exp` FLOAT NOT NULL,
	`Online_Precision_Exp` FLOAT NOT NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NOT NULL,
	`Constants_Exp` FLOAT NOT NULL
);

-- Dumping structure for table statshv.failures_lookup
CREATE TABLE IF NOT EXISTS `failures_lookup` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.fluidics
CREATE TABLE IF NOT EXISTS `fluidics` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '0',
  `SeqNo` int NOT NULL DEFAULT '0',
  `Bay` int NOT NULL DEFAULT '0',
  `RunNo` int NOT NULL DEFAULT '0',
  `ICCell` varchar(15) NOT NULL DEFAULT '',
  `TCCell` varchar(15) NOT NULL DEFAULT '',
  `SCCell` varchar(15) NOT NULL DEFAULT '' COMMENT 'Single Conductivity Cell ID (Also known as the C4 Cell)',
  `ConstantsChkd` tinyint(1) NOT NULL DEFAULT '0',
  `ConstantsPass` tinyint(1) NOT NULL DEFAULT '0',
  `ICCurr` double NOT NULL DEFAULT '0' COMMENT 'Current IC reading',
  `ICAvg` double NOT NULL DEFAULT '0',
  `ICStd` double NOT NULL DEFAULT '0',
  `ICTempCorrAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Temperature Corrected calculation for the IC Cell',
  `ICTempCorrStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation Temperature Corrected calculation for the IC Cell',
  `TCCurr` double NOT NULL DEFAULT '0' COMMENT 'Current TC reading',
  `TCAvg` double NOT NULL DEFAULT '0',
  `TCStd` double NOT NULL DEFAULT '0',
  `TCTempCorrAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Temperature Corrected calculation for the TC Cell',
  `TCTempCorrStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation Temperature Corrected calculation for the TC Cell',
  `SCCond` double NOT NULL DEFAULT '0' COMMENT 'Current SC reading',
  `SCCondAvg` double NOT NULL DEFAULT '0' COMMENT 'Average reading for the Sample Conductivity Cell (C4 Cell)',
  `SCCondStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation reading of the Sample Cell (C4 Cell)',
  `SCTempCorrAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Temperature Corrected calculation for the Sample Conductivity Cell (C4 Cell)',
  `SCTempCorrStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation for Temperature Corrected calculation for the Sample Conductivity Cell (C4 Cell)',
  `MFTempAvg` double NOT NULL DEFAULT '0' COMMENT 'Average for Manifold Temperature readings',
  `MFTempStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation for Manifold Temperature readings',
  `ICTempAvg` double NOT NULL DEFAULT '0' COMMENT 'Average IC Cell Temperature',
  `TCTempAvg` double NOT NULL DEFAULT '0' COMMENT 'Average TC Cell Temperature',
  `SCTempAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Sample Cell Temperature (C4 Cell)',
  `DeltaT` double NOT NULL DEFAULT '0',
  `EmptyChkd` tinyint(1) NOT NULL DEFAULT '0',
  `LvlSnsEmpty` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Level Sensor Empty pass result. This field stores the output from the Level Status sensor from command GDS,4 compared to the expected Reservoir Empty.  Values 0 - Fail, 1 - Pass',
  `FullChkd` tinyint(1) NOT NULL DEFAULT '0',
  `LvlSnsFull` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Level Sensor Full pass result. This field stores the output from the Level Status sensor from command GDS,4 compared to the expected Reservoir Full.  Values 0 - Fail, 1 - Pass',
  `FlowRateChkd` tinyint(1) NOT NULL DEFAULT '0',
  `FlowRate` float NOT NULL DEFAULT '0',
  `FlowRatePass` tinyint(1) NOT NULL DEFAULT '0',
  `Pass` tinyint(1) NOT NULL DEFAULT '0',
  `Readings` int unsigned NOT NULL DEFAULT '0',
  `PrimeStart` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `PrimeEnd` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `PrimeTime` time NOT NULL DEFAULT '00:00:00',
  `TotalPrimeMinutes` int NOT NULL DEFAULT '0',
  `RinseStart` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `RinseEnd` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `TotalRinseMinutes` int NOT NULL DEFAULT '0',
  `LastRecTm` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Operator` varchar(30) NOT NULL DEFAULT '',
  `SWVersion` varchar(20) NOT NULL DEFAULT '',
  `Station` varchar(15) NOT NULL DEFAULT '',
  `Repair` tinyint NOT NULL DEFAULT '0',
  `TcIcAutoZeroStart` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `TcIcAutoZeroEnd` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `TcIcAutoZeroTotalMinutes` int NOT NULL DEFAULT '0',
  `TcIcAutoZeroOldTcOffset` double NOT NULL DEFAULT '0',
  `TcIcAutoZeroNewTcOffset` double NOT NULL DEFAULT '0',
  `TcIcAutoZeroOldIcOffset` double NOT NULL DEFAULT '0',
  `TcIcAutoZeroNewIcOffset` double NOT NULL DEFAULT '0',
  `TcIcAutoZeroChkd` tinyint(1) NOT NULL DEFAULT '0',
  `TcIcAutoZeroPass` tinyint(1) NOT NULL DEFAULT '0',
  `TocAutoZeroStart` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `TocAutoZeroEnd` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `TocAutoZeroTotalMinutes` int NOT NULL DEFAULT '0',
  `TocAutoZeroNewTocOffset` double NOT NULL DEFAULT '0',
  `TocAutoZeroOldTocOffset` double NOT NULL DEFAULT '0',
  `TocAutoZeroFileName` varchar(255) NOT NULL DEFAULT '',
  `TocAutoZeroMaxTc1` double NOT NULL DEFAULT '0',
  `TocAutoZeroMaxIc1` double NOT NULL DEFAULT '0',
  `TocAutoZeroMaxTc2` double NOT NULL DEFAULT '0',
  `TocAutoZeroMaxIc2` double NOT NULL DEFAULT '0',
  `TocAutoZeroAvgTc2` double NOT NULL DEFAULT '0',
  `TocAutoZeroAvgIc2` double NOT NULL DEFAULT '0',
  `TocAutoZeroDiffTc2` double NOT NULL DEFAULT '0',
  `TocAutoZeroDiffIc2` double NOT NULL DEFAULT '0',
  `TocAutoZeroChkd` tinyint(1) NOT NULL DEFAULT '0',
  `TocAutoZeroPass` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=4247 DEFAULT CHARSET=latin1 COMMENT='From HVCellCal';

-- Data exporting was unselected.

-- Dumping structure for table statshv.fluidics_bay_status
CREATE TABLE IF NOT EXISTS `fluidics_bay_status` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `Station` varchar(15) NOT NULL DEFAULT '',
  `Bay` int NOT NULL DEFAULT '0',
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `ShopOrder` varchar(15) NOT NULL DEFAULT '',
  `PartNo` varchar(15) NOT NULL DEFAULT '',
  `PartDescription` varchar(45) NOT NULL DEFAULT '',
  `Protocol` varchar(45) NOT NULL DEFAULT '',
  `LastProtocol` varchar(45) NOT NULL DEFAULT '',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view statshv.fluidics_passing_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `fluidics_passing_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SeqNo` INT NOT NULL,
	`Bay` INT NOT NULL,
	`ICCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`TCCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SCCell` VARCHAR(1) NOT NULL COMMENT 'Single Conductivity Cell ID (Also known as the C4 Cell)' COLLATE 'latin1_swedish_ci',
	`ConstantsChkd` TINYINT(1) NOT NULL,
	`ConstantsPass` TINYINT(1) NOT NULL,
	`ICAvg` DOUBLE NOT NULL,
	`ICStd` DOUBLE NOT NULL,
	`ICTempCorrAvg` DOUBLE NOT NULL COMMENT 'Average Temperature Corrected calculation for the IC Cell',
	`ICTempCorrStd` DOUBLE NOT NULL COMMENT 'Standard Deviation Temperature Corrected calculation for the IC Cell',
	`TCAvg` DOUBLE NOT NULL,
	`TCStd` DOUBLE NOT NULL,
	`TCTempCorrAvg` DOUBLE NOT NULL COMMENT 'Average Temperature Corrected calculation for the TC Cell',
	`TCTempCorrStd` DOUBLE NOT NULL COMMENT 'Standard Deviation Temperature Corrected calculation for the TC Cell',
	`SCCondAvg` DOUBLE NOT NULL COMMENT 'Average reading for the Sample Conductivity Cell (C4 Cell)',
	`SCCondStd` DOUBLE NOT NULL COMMENT 'Standard Deviation reading of the Sample Cell (C4 Cell)',
	`SCTempCorrAvg` DOUBLE NOT NULL COMMENT 'Average Temperature Corrected calculation for the Sample Conductivity Cell (C4 Cell)',
	`SCTempCorrStd` DOUBLE NOT NULL COMMENT 'Standard Deviation for Temperature Corrected calculation for the Sample Conductivity Cell (C4 Cell)',
	`MFTempAvg` DOUBLE NOT NULL COMMENT 'Average for Manifold Temperature readings',
	`MFTempStd` DOUBLE NOT NULL COMMENT 'Standard Deviation for Manifold Temperature readings',
	`ICTempAvg` DOUBLE NOT NULL COMMENT 'Average IC Cell Temperature',
	`TCTempAvg` DOUBLE NOT NULL COMMENT 'Average TC Cell Temperature',
	`SCTempAvg` DOUBLE NOT NULL COMMENT 'Average Sample Cell Temperature (C4 Cell)',
	`DeltaT` DOUBLE NOT NULL,
	`EmptyChkd` TINYINT(1) NOT NULL,
	`LvlSnsEmpty` TINYINT(1) NOT NULL COMMENT 'Level Sensor Empty pass result. This field stores the output from the Level Status sensor from command GDS,4 compared to the expected Reservoir Empty.  Values 0 - Fail, 1 - Pass',
	`FullChkd` TINYINT(1) NOT NULL,
	`LvlSnsFull` TINYINT(1) NOT NULL COMMENT 'Level Sensor Full pass result. This field stores the output from the Level Status sensor from command GDS,4 compared to the expected Reservoir Full.  Values 0 - Fail, 1 - Pass',
	`FlowRateChkd` TINYINT(1) NOT NULL,
	`FlowRate` FLOAT NOT NULL,
	`Pass` TINYINT(1) NOT NULL,
	`Readings` INT UNSIGNED NOT NULL,
	`PrimeStart` DATETIME NOT NULL,
	`PrimeEnd` DATETIME NOT NULL,
	`PrimeTime` TIME NOT NULL,
	`TotalPrimeMinutes` INT NOT NULL,
	`RinseStart` DATETIME NOT NULL,
	`RinseEnd` DATETIME NOT NULL,
	`TotalRinseMinutes` INT NOT NULL,
	`LastRecTm` DATETIME NOT NULL,
	`UpdateTime` TIMESTAMP NOT NULL,
	`Operator` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SWVersion` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for table statshv.fluidics_repair
CREATE TABLE IF NOT EXISTS `fluidics_repair` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `ShopOrder` varchar(15) NOT NULL DEFAULT '',
  `TestName` varchar(45) NOT NULL DEFAULT '',
  `Technician` varchar(30) NOT NULL DEFAULT '',
  `PartNo` varchar(15) NOT NULL DEFAULT '',
  `PartDescription` varchar(60) NOT NULL DEFAULT '',
  `Failure` varchar(40) NOT NULL DEFAULT '',
  `Notes` varchar(255) NOT NULL DEFAULT '',
  `RepairTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=293 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.fluidics_rinse_log
CREATE TABLE IF NOT EXISTS `fluidics_rinse_log` (
  `RecNo` int NOT NULL DEFAULT '0',
  `SerialNo` varchar(15) NOT NULL DEFAULT '0',
  `Bay` int NOT NULL DEFAULT '0',
  `RunNo` int NOT NULL DEFAULT '0',
  `ICCell` varchar(15) NOT NULL DEFAULT '',
  `TCCell` varchar(15) NOT NULL DEFAULT '',
  `SCCell` varchar(15) NOT NULL DEFAULT '' COMMENT 'Single Conductivity Cell ID (Also known as the C4 Cell)',
  `ICAvg` double NOT NULL DEFAULT '0',
  `TCAvg` double NOT NULL DEFAULT '0',
  `SCAvg` double NOT NULL DEFAULT '0' COMMENT 'Average reading for the Sample Conductivity Cell (C4 Cell)',
  `ICCurr` double NOT NULL DEFAULT '0',
  `TCCurr` double NOT NULL DEFAULT '0',
  `SCCurr` double NOT NULL DEFAULT '0' COMMENT 'Average reading for the Sample Conductivity Cell (C4 Cell)',
  `ICStd` double NOT NULL DEFAULT '0',
  `TCStd` double NOT NULL DEFAULT '0',
  `SCStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation reading of the Sample Cell (C4 Cell)',
  `ICTempCorr` double NOT NULL DEFAULT '0' COMMENT ' ICTempCorr value',
  `TCTempCorr` double NOT NULL DEFAULT '0' COMMENT ' TC TempCorr value',
  `SCTempCorr` double NOT NULL DEFAULT '0' COMMENT ' SC TempCorr value',
  `ICTempCorrAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Temperature Corrected calculation for the IC Cell',
  `TCTempCorrAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Temperature Corrected calculation for the TC Cell',
  `SCTempCorrAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Temperature Corrected calculation for the Sample Conductivity Cell (C4 Cell)',
  `ICTempCorrStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation Temperature Corrected calculation for the IC Cell',
  `TCTempCorrStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation Temperature Corrected calculation for the TC Cell',
  `SCTempCorrStd` double NOT NULL DEFAULT '0' COMMENT 'Standard Deviation for Temperature Corrected calculation for the Sample Conductivity Cell (C4 Cell)',
  `ICTemp` double NOT NULL DEFAULT '0' COMMENT ' IC Temp column value',
  `TCTemp` double NOT NULL DEFAULT '0' COMMENT 'TC Temp COlumn value',
  `SCTemp` double NOT NULL DEFAULT '0' COMMENT 'SC temp column value',
  `ICTempAvg` double NOT NULL DEFAULT '0' COMMENT 'Average IC Cell Temperature',
  `TCTempAvg` double NOT NULL DEFAULT '0' COMMENT 'Average TC Cell Temperature',
  `SCTempAvg` double NOT NULL DEFAULT '0' COMMENT 'Average Sample Cell Temperature (C4 Cell)',
  `ICTempStd` double NOT NULL DEFAULT '0' COMMENT 'IC Cell Temperature std',
  `TCTempStd` double NOT NULL DEFAULT '0' COMMENT 'TC Cell Temperature std',
  `SCTempStd` double NOT NULL DEFAULT '0' COMMENT 'Sample Cell Temperature (C4 Cell) std',
  `Readings` int NOT NULL DEFAULT '0',
  `ReadTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`RecNo`,`Readings`,`ReadTime`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.fluidics_workcell_bay
CREATE TABLE IF NOT EXISTS `fluidics_workcell_bay` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Row unique identifier',
  `WorkCell` varchar(25) NOT NULL DEFAULT '' COMMENT 'Description of the Work Cell - ie. Cell 1',
  `Station` varchar(15) NOT NULL DEFAULT '' COMMENT 'Name of the Workstation. ie. W0360000JV881T2',
  `Bay` varchar(15) NOT NULL DEFAULT '' COMMENT 'Description of the Bay. ie. 1',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1 COMMENT='Table to store the bays in a given Work Cell';

-- Data exporting was unselected.

-- Dumping structure for table statshv.fnlprep
CREATE TABLE IF NOT EXISTS `fnlprep` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `ErrsClrd` tinyint(1) NOT NULL DEFAULT '0',
  `ErrsRvwd` tinyint(1) NOT NULL DEFAULT '0',
  `ClockVer` tinyint(1) NOT NULL DEFAULT '0',
  `DoorIntrfr` tinyint(1) NOT NULL DEFAULT '0',
  `CellsMatch` tinyint(1) NOT NULL DEFAULT '0',
  `PumpsTight` tinyint(1) NOT NULL DEFAULT '0',
  `WiFiTest` tinyint(1) NOT NULL DEFAULT '0',
  `ConnsCheck` tinyint(1) NOT NULL DEFAULT '0',
  `BackScrwTght` tinyint(1) NOT NULL DEFAULT '0',
  `DoorScrwTght` tinyint(1) NOT NULL DEFAULT '0',
  `AutoRstrtOn` tinyint(1) NOT NULL DEFAULT '0',
  `OnlnBckup` tinyint(1) NOT NULL DEFAULT '0',
  `PrtclBckup` tinyint(1) NOT NULL DEFAULT '0',
  `FilesSvd` tinyint(1) NOT NULL DEFAULT '0',
  `SvcDataBckup` tinyint(1) NOT NULL DEFAULT '0',
  `HorizCvr` tinyint(1) NOT NULL DEFAULT '0',
  `VertCvr` tinyint(1) NOT NULL DEFAULT '0',
  `ActCode` varchar(30) NOT NULL DEFAULT '',
  `OptCond` tinyint(1) NOT NULL DEFAULT '0',
  `OptPQ` tinyint(1) NOT NULL DEFAULT '0',
  `Opt3min` tinyint(1) NOT NULL DEFAULT '0',
  `OptDatGrd` tinyint(1) NOT NULL DEFAULT '0',
  `OptNoDatStrg` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Activated` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Flag to indicate the Instrument was programmed with the Activation Options',
  `ChassisChckd` tinyint(1) NOT NULL DEFAULT '0',
  `PlasticCoverChckd` tinyint(1) NOT NULL DEFAULT '0',
  `SilkScreenChckd` tinyint(1) NOT NULL DEFAULT '0',
  `StickersChckd` tinyint(1) NOT NULL DEFAULT '0',
  `SettingsBckup` tinyint(1) NOT NULL DEFAULT '0',
  `SettingsRestored` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=3792 DEFAULT CHARSET=latin1 COMMENT='CheckList';

-- Data exporting was unselected.

-- Dumping structure for table statshv.fnlprep2
CREATE TABLE IF NOT EXISTS `fnlprep2` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `FilesRmvd` tinyint(1) NOT NULL DEFAULT '0',
  `NdlVlvClsd` tinyint(1) NOT NULL DEFAULT '0',
  `LoopDrnd` tinyint(1) NOT NULL DEFAULT '0',
  `SmplDrnd` tinyint(1) NOT NULL DEFAULT '0',
  `DisConUPW` tinyint(1) NOT NULL DEFAULT '0',
  `DisConWaste` tinyint(1) NOT NULL DEFAULT '0',
  `AZoff` tinyint(1) NOT NULL DEFAULT '0',
  `KeysInDr` tinyint(1) NOT NULL DEFAULT '0',
  `IOcapsOn` tinyint(1) NOT NULL DEFAULT '0',
  `TestRecChckd` tinyint(1) NOT NULL DEFAULT '0',
  `CalDays` int NOT NULL DEFAULT '0',
  `ConsumReset` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `VerInstrModelType` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Verification programmed Instrument Model and Type match AQC No',
  `CablesChckd` tinyint(1) NOT NULL DEFAULT '0',
  `GasketsChckd` tinyint(1) NOT NULL DEFAULT '0',
  `TubesChckd` tinyint(1) NOT NULL DEFAULT '0',
  `WaterLeaksChckd` tinyint(1) NOT NULL DEFAULT '0',
  `SettingsRestored` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=3780 DEFAULT CHARSET=latin1 COMMENT='Checklist';

-- Data exporting was unselected.

-- Dumping structure for view statshv.fnlprep_all_desc_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `fnlprep_all_desc_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NOT NULL
);

-- Dumping structure for view statshv.fnlprep_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `fnlprep_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for function statshv.GetActual_Cond_Cal_Ver_Time
DELIMITER //
CREATE FUNCTION `GetActual_Cond_Cal_Ver_Time`(series VARCHAR(20), condCalVer FLOAT, 
	condSinglePtCal FLOAT, tocVer FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    DECLARE previousProtocol FLOAT;
    
    SET actualTime = NULL;
    SET previousProtocol = condSinglePtCal;
    
    IF series = 'M500e' THEN
		SET previousProtocol = tocVer;
	END IF;
		
	IF NOT ISNULL(condCalVer) THEN
		IF NOT ISNULL(previousProtocol) THEN 
			SET actualTime = ABS(condCalVer - previousProtocol);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Cond_Single_Point_Cal_Time
DELIMITER //
CREATE FUNCTION `GetActual_Cond_Single_Point_Cal_Time`(series VARCHAR(20), condSinglePtCal FLOAT, tocVer FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF series = 'M500' THEN
		IF NOT ISNULL(condSinglePtCal) THEN
			IF NOT ISNULL(tocVer) THEN 
				SET actualTime = ABS(condSinglePtCal - tocVer);
			ELSE
				SET actualTime = NULL;
			END IF;
		END IF;
    END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Constants_Time
DELIMITER //
CREATE FUNCTION `GetActual_Constants_Time`(series VARCHAR(20), constants FLOAT, 
	condAZ2 FLOAT, onlinePrecision FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    DECLARE previousProtocol FLOAT;
    
    SET actualTime = NULL;
    SET previousProtocol = condAZ2;
    
    IF series = 'M500e' THEN
		SET previousProtocol = onlinePrecision;
	END IF;
		
	IF NOT ISNULL(constants) THEN
		IF NOT ISNULL(previousProtocol) THEN 
			SET actualTime = ABS(constants - previousProtocol);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_IC_TC_Cond_AZ_Time
DELIMITER //
CREATE FUNCTION `GetActual_IC_TC_Cond_AZ_Time`(series VARCHAR(20), itTcCondAZ FLOAT, 
	sampleCondAZ1 FLOAT, lowLevelRinse FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    DECLARE previousProtocol FLOAT;
    
    SET actualTime = NULL;
    SET previousProtocol = sampleCondAZ1;
    
    IF series = 'M500e' THEN
		SET previousProtocol = lowLevelRinse;
	END IF;
		
	IF NOT ISNULL(itTcCondAZ) THEN
		IF NOT ISNULL(previousProtocol) THEN 
			SET actualTime = ABS(itTcCondAZ - previousProtocol);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_IOTests_Time
DELIMITER //
CREATE FUNCTION `GetActual_IOTests_Time`(ioTests FLOAT, startupTime FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF NOT ISNULL(ioTests) THEN
		IF NOT ISNULL(startupTime) THEN 
			SET actualTime = ABS(ioTests - startupTime);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_LowLevel_Rinse_Time
DELIMITER //
CREATE FUNCTION `GetActual_LowLevel_Rinse_Time`(lowLevelRinse FLOAT, ioTests FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF NOT ISNULL(lowLevelRinse) THEN
		IF NOT ISNULL(ioTests) THEN 
			SET actualTime = ABS(lowLevelRinse - ioTests);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_LowLevel_SL1_Data_Time
DELIMITER //
CREATE FUNCTION `GetActual_LowLevel_SL1_Data_Time`(lowLevelSL1Data FLOAT, icTcCondAZ FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF NOT ISNULL(lowLevelSL1Data) THEN
		IF NOT ISNULL(icTcCondAZ) THEN 
			SET actualTime = ABS(lowLevelSL1Data - icTcCondAZ);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Online_Precision_Time
DELIMITER //
CREATE FUNCTION `GetActual_Online_Precision_Time`(series VARCHAR(20), model VARCHAR(20),
	onlinePrecision FLOAT, specificity FLOAT, condCalVer FLOAT, tocVer FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    DECLARE previousProtocol FLOAT;
    
    SET actualTime = NULL;
    
    
    IF series = 'M500e' THEN
		SET previousProtocol = tocVer;
    ELSEIF series = 'M500' AND model = 'SUPER' THEN
		SET previousProtocol = specificity;
	ELSE
		SET previousProtocol = condCalVer;
	END IF;
		
	IF NOT ISNULL(onlinePrecision) THEN
		IF NOT ISNULL(previousProtocol) THEN 
			SET actualTime = ABS(onlinePrecision - previousProtocol);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Protocol_Series_Precision_Time
DELIMITER //
CREATE FUNCTION `GetActual_Protocol_Series_Precision_Time`(series VARCHAR(20),
	model VARCHAR(20), time1 DATETIME, time2 DATETIME, time3 DATETIME, time4 DATETIME) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF series = 'M500e' THEN
		IF NOT ISNULL(time1) AND NOT ISNULL(time4) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time1, time4);
		END IF;
	ELSEIF series = 'M500' AND model <> 'SUPER' THEN
		IF NOT ISNULL(time2) AND NOT ISNULL(time4) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time2, time4);
		END IF;
    ELSEIF series = 'M500' AND model = 'SUPER' THEN
		IF NOT ISNULL(time3) AND NOT ISNULL(time4) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time3, time4);
		END IF;
	ELSE
		SET actualTime = NULL;
    END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Protocol_Series_Time
DELIMITER //
CREATE FUNCTION `GetActual_Protocol_Series_Time`(series VARCHAR(20), time1 DATETIME, time2 DATETIME, time3 DATETIME) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF series = 'M500e' AND ISNULL(time1) THEN
		SET actualTime = NULL;
	ELSEIF series = 'M500' AND ISNULL(time1) THEN
		IF NOT ISNULL(time2) AND NOT ISNULL(time3) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time2, time3);
		END IF;
	ELSEIF series = 'M500e' AND NOT ISNULL(time1) THEN
		IF NOT ISNULL(time3) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time1, time3);
		END IF;
    ELSEIF series = 'M500' AND NOT ISNULL(time1) THEN
		IF NOT ISNULL(time2) AND NOT ISNULL(time3) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time2, time3);
		END IF;
	ELSE
		SET actualTime = NULL;
    END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Protocol_Time
DELIMITER //
CREATE FUNCTION `GetActual_Protocol_Time`(series VARCHAR(20), time1 DATETIME, time2 DATETIME, time3 DATETIME) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF series = 'M500e' AND ISNULL(time1) THEN
		SET actualTime = NULL;
	ELSEIF series = 'M500' AND ISNULL(time1) THEN
		IF NOT ISNULL(time2) AND NOT ISNULL(time3) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time2, time3);
		END IF;
	ELSEIF series = 'M500e' AND NOT ISNULL(time1) THEN
		IF NOT ISNULL(time3) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time1, time3);
		END IF;
    ELSEIF series = 'M500' AND NOT ISNULL(time1) THEN
		IF NOT ISNULL(time2) AND NOT ISNULL(time3) THEN 
			SET actualTime = TIMESTAMPDIFF(MINUTE, time2, time3);
		END IF;
	ELSE
		SET actualTime = NULL;
    END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Sample_Cond_AZ_1_Time
DELIMITER //
CREATE FUNCTION `GetActual_Sample_Cond_AZ_1_Time`(series VARCHAR(20), sampleCondAZ1 FLOAT, lowLevelRinse FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF series = 'M500' THEN
		IF NOT ISNULL(sampleCondAZ1) THEN
			IF NOT ISNULL(lowLevelRinse) THEN 
				SET actualTime = ABS(sampleCondAZ1 - lowLevelRinse);
			ELSE
				SET actualTime = NULL;
			END IF;
		END IF;
    END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Sample_Cond_AZ_2_Time
DELIMITER //
CREATE FUNCTION `GetActual_Sample_Cond_AZ_2_Time`(sampleCondAZ2 FLOAT, onlinePrecision FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF NOT ISNULL(sampleCondAZ2) THEN
		IF NOT ISNULL(onlinePrecision) THEN 
			SET actualTime = ABS(sampleCondAZ2 - onlinePrecision);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_Specificity_Time
DELIMITER //
CREATE FUNCTION `GetActual_Specificity_Time`(series VARCHAR(20), specificity FLOAT, 
	condCalVer FLOAT, tocVer FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    DECLARE previousProtocol FLOAT;
    
    SET actualTime = NULL;
    SET previousProtocol = condCalVer;
    
    IF series = 'M500e' THEN
		SET previousProtocol = tocVer;
	END IF;
		
	IF NOT ISNULL(specificity) THEN
		IF NOT ISNULL(previousProtocol) THEN 
			SET actualTime = ABS(specificity - previousProtocol);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_TOC_Single_Point_Cal_Time
DELIMITER //
CREATE FUNCTION `GetActual_TOC_Single_Point_Cal_Time`(tocSinglePtCal FLOAT, lowLevelSL1Data FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF NOT ISNULL(tocSinglePtCal) THEN
		IF NOT ISNULL(lowLevelSL1Data) THEN 
			SET actualTime = ABS(tocSinglePtCal - lowLevelSL1Data);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetActual_TOC_Ver_Time
DELIMITER //
CREATE FUNCTION `GetActual_TOC_Ver_Time`(tocVer FLOAT, tocSinglePtCal FLOAT) RETURNS float
    NO SQL
BEGIN

    DECLARE actualTime FLOAT;
    
    SET actualTime = NULL;
    
    IF NOT ISNULL(tocVer) THEN
		IF NOT ISNULL(tocSinglePtCal) THEN 
			SET actualTime = ABS(tocVer - tocSinglePtCal);
		ELSE
			SET actualTime = NULL;
		END IF;
	END IF;
    
	RETURN actualTime;

END//
DELIMITER ;

-- Dumping structure for function statshv.GetBaseModelFilter
DELIMITER //
CREATE FUNCTION `GetBaseModelFilter`(filter VARCHAR(15)) RETURNS varchar(50) CHARSET latin1
    NO SQL
BEGIN
	 DECLARE model_in_filter VARCHAR(50);
     
     IF filter = 'BASE' OR filter = '(All)' THEN
		SET model_in_filter = 'BASE';
	 ELSE
		SET model_in_filter = 'NULL';
     END IF;
     
RETURN model_in_filter;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetCurrentProtocol90DayAvg
DELIMITER //
CREATE FUNCTION `GetCurrentProtocol90DayAvg`(protocol VARCHAR(40), series VARCHAR(7), model VARCHAR(17)) RETURNS int
    READS SQL DATA
    DETERMINISTIC
BEGIN
	DECLARE LastThreeMonthAvg INT;
    
    IF protocol = 'Startup' THEN
		SET LastThreeMonthAvg = (SELECT Startup_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'IO Tests' THEN
		SET LastThreeMonthAvg = (SELECT IO_Tests_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Low Level Rinse' THEN
		SET LastThreeMonthAvg = (SELECT LowLevel_Rinse_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Sample Conductivity AutoZero 1' THEN
		SET LastThreeMonthAvg = (SELECT Sample_Cond_AZ_1_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'IC/TC Conductivity AutoZero' THEN
		SET LastThreeMonthAvg = (SELECT IC_TC_Cond_AZ_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Low Level SL1 Data' THEN
		SET LastThreeMonthAvg = (SELECT LowLevel_SL1_Data_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'TOC Single Point Calibration' THEN
		SET LastThreeMonthAvg = (SELECT TOC_Single_Point_Cal_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'TOC_Verification' THEN
		SET LastThreeMonthAvg = (SELECT TOC_Ver_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Conductivity Single Point Calibration' THEN
		SET LastThreeMonthAvg = (SELECT Cond_Single_Point_Cal_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Conductivity Calibration Verification' THEN
		SET LastThreeMonthAvg = (SELECT Cond_Cal_Ver_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Specificity' THEN
		SET LastThreeMonthAvg = (SELECT Specificity_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Online Precision' THEN
		SET LastThreeMonthAvg = (SELECT Online_Precision_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	ELSEIF protocol = 'Sample Conductivity AutoZero 2' THEN
		SET LastThreeMonthAvg = (SELECT Sample_Cond_AZ_2_Act_90DayAvg FROM statshv.bay_status_test_time_90_day_view2 WHERE (bay_status_test_time_90_day_view2.Series = series) AND (bay_status_test_time_90_day_view2.Model = model)   LIMIT 1 );
	else	
		SET LastThreeMonthAvg = NULL;
		
    END IF;
    
    
	RETURN LastThreeMonthAvg;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetCurrentProtocolExpectedTime
DELIMITER //
CREATE FUNCTION `GetCurrentProtocolExpectedTime`(protocol VARCHAR(40)) RETURNS int
    NO SQL
BEGIN
	DECLARE expectedTime INT;
    
    IF protocol = 'Startup' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'IO Tests' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Low Level Rinse' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Sample Conductivity AutoZero 1' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'IC/TC Conductivity AutoZero' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Low Level SL1 Data' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'TOC Single Point Calibration' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'TOC_Verification' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Conductivity Single Point Calibration' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Conductivity Calibration Verification' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Specificity' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Online Precision' THEN
		SET expectedTime = 60;
	ELSEIF protocol = 'Sample Conductivity AutoZero 2' THEN
		SET expectedTime = 60;
	else	
		SET expectedTime = NULL;
		
    END IF;
    
    
	RETURN expectedTime;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetCurrentProtocolTime
DELIMITER //
CREATE FUNCTION `GetCurrentProtocolTime`(protocolFinishTime DATETIME, currentProtocol VARCHAR(45), matchProtocol VARCHAR(45)) RETURNS datetime
    NO SQL
BEGIN
	DECLARE protocolTime DATETIME;
    
    IF (protocolFinishTime = '0000-00-00 00:00:00') THEN
		SET protocolTime = NULL;
	ELSE
		SET protocolTime = protocolFinishTime;
    END IF;
    IF NOT ISNULL(currentProtocol) AND INSTR(currentProtocol, matchProtocol) > 0 THEN
		SET protocolTime = NOW();
    END IF;
    
	RETURN protocolTime;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetInitialRinseTime
DELIMITER //
CREATE FUNCTION `GetInitialRinseTime`(RecNoStr VARCHAR(15)) RETURNS datetime
    READS SQL DATA
    DETERMINISTIC
BEGIN
	DECLARE InitialRinseTime Datetime;
    
   
	SET InitialRinseTime = (SELECT ICReadTime FROM statshv.diloopdatainitial WHERE diloopdatainitial.RecordNo = RecNoStr);
	
    
    
	RETURN InitialRinseTime;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetLastProtocolEndTime
DELIMITER //
CREATE FUNCTION `GetLastProtocolEndTime`(lastProtocol VARCHAR(40), serialNo VARCHAR(15)) RETURNS datetime
    READS SQL DATA
    DETERMINISTIC
BEGIN
	
    DECLARE lastProtocolEndTime DATETIME;
   
    IF lastProtocol = 'Startup' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.startup_view WHERE startup_view.SerialNo = serialNo);
	
    ELSEIF lastProtocol = 'IO Tests' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.iotests_view WHERE iotests_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'Low Level Rinse' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.llrinse_view WHERE llrinse_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'Sample Conductivity AutoZero 1' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.condaz1_view WHERE condaz1_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'IC/TC Conductivity AutoZero' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.condaz2_view WHERE condaz2_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'Low Level SL1 Data' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.condaz3_view WHERE condaz3_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'TOC Single Point Calibration' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.spcal1_view WHERE spcal1_view.SerialNo = serialNo);
	
    ELSEIF lastProtocol = 'TOC_Verification' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.spcal2_view WHERE spcal2_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'Conductivity Single Point Calibration' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.condcalver1_view WHERE condcalver1_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'Conductivity Calibration Verification' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.condcalver2_view WHERE condcalver2_view.SerialNo = serialNo) ;
	
    ELSEIF lastProtocol = 'Specificity' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.tocaz1_view WHERE tocaz1_view.SerialNo = serialNo) ;
	
    
    ELSEIF lastProtocol = 'Online Precision' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.tocaz2_view WHERE tocaz2_view.SerialNo = serialNo);
	
    
    ELSEIF lastProtocol = 'Sample Conductivity AutoZero 2' THEN
		SET lastProtocolEndTime = (SELECT RecTime FROM statshv.tocaz3_view WHERE tocaz3_view.SerialNo = serialNo) ;
	
	ELSE
		SET lastProtocolEndTime = NULL;
	END IF;
    
    IF lastProtocolEndTime = '0000-00-00 00:00:00' THEN
		SET lastProtocolEndTime = NULL;
    END IF;
    
	RETURN lastProtocolEndTime;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetM500eSeriesFilter
DELIMITER //
CREATE FUNCTION `GetM500eSeriesFilter`(filter VARCHAR(15)) RETURNS varchar(50) CHARSET latin1
    NO SQL
BEGIN
	 DECLARE series_in_filter VARCHAR(50);
     
     IF filter = 'M500e' OR filter = '(All)' THEN
		SET series_in_filter = 'M500e';
	 ELSE
		SET series_in_filter = 'NULL';
     END IF;
     
RETURN series_in_filter;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetM500SeriesFilter
DELIMITER //
CREATE FUNCTION `GetM500SeriesFilter`(filter VARCHAR(15)) RETURNS varchar(50) CHARSET latin1
    NO SQL
BEGIN
	 DECLARE series_in_filter VARCHAR(50);
     
     IF filter = 'M500' OR filter = '(All)' THEN
		SET series_in_filter = 'M500';
	 ELSE
		SET series_in_filter = 'NULL';
     END IF;
     
RETURN series_in_filter;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetModelName
DELIMITER //
CREATE FUNCTION `GetModelName`(acqNo VARCHAR(15)) RETURNS varchar(15) CHARSET latin1
    NO SQL
BEGIN
	DECLARE model VARCHAR(15);
    DECLARE partNo VARCHAR(10);
    
    SET partNo = LEFT(acqNo, 9);
    
    IF partNo = 'AQC 78100' OR partNo = 'AQC 78130' THEN
		SET model = 'STD';
	ELSEIF partNo = 'AQC 78200' THEN
		SET model = 'BASE';
	ELSEIF partNo = 'AQC 78230' THEN
		SET model = 'SS';
	ELSEIF partNo = 'AQC 78300' THEN
		SET model = 'SUPER';
	ELSE
		SET model = '';
	END IF;
    
	RETURN model;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetNoneOptionFilter
DELIMITER //
CREATE FUNCTION `GetNoneOptionFilter`(filter VARCHAR(30)) RETURNS varchar(50) CHARSET latin1
    NO SQL
BEGIN
	 DECLARE option_in_filter VARCHAR(50);
     
     IF filter = 'NONE' OR filter = '(All)' THEN
		SET option_in_filter = 'NONE';
	 ELSE
		SET option_in_filter = 'NULL';
     END IF;
     
RETURN option_in_filter;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetRecTime
DELIMITER //
CREATE FUNCTION `GetRecTime`(serialNo varchar(15)) RETURNS datetime
    READS SQL DATA
    DETERMINISTIC
BEGIN
	DECLARE rec2Time DATETIME;
	
	SET rec2Time = (SELECT RecTime FROM statshv.instlocn WHERE instlocn.SerialNo = serialNo);
	RETURN rec2Time;
    
END//
DELIMITER ;

-- Dumping structure for function statshv.GetRecTime-Ok-to-Delete
DELIMITER //
CREATE FUNCTION `GetRecTime-Ok-to-Delete`(serialNo varchar(15)) RETURNS datetime
    READS SQL DATA
    DETERMINISTIC
BEGIN
	DECLARE rec2Time DATETIME;
	
	SET rec2Time = (SELECT RecTime FROM statshv.instlocn WHERE instlocn.SerialNo = serialNo);
	RETURN rec2Time;
    
END//
DELIMITER ;

-- Dumping structure for function statshv.GetSeriesName
DELIMITER //
CREATE FUNCTION `GetSeriesName`(acqNo VARCHAR(15)) RETURNS varchar(15) CHARSET latin1
    NO SQL
BEGIN
	DECLARE series VARCHAR(15);
    DECLARE partNo VARCHAR(10);
    
    SET partNo = LEFT(acqNo, 9);
    
    IF partNo = 'AQC 78100' OR partNo = 'AQC 78200' OR partNo = 'AQC 78300' THEN
		SET series = 'M500';
	ELSEIF partNo = 'AQC 78130' OR partNo = 'AQC 78230' THEN
		SET series = 'M500e';
	ELSE
		SET series = '';
	END IF;
    
	RETURN series;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetSsModelFilter
DELIMITER //
CREATE FUNCTION `GetSsModelFilter`(filter VARCHAR(15)) RETURNS varchar(50) CHARSET latin1
    NO SQL
BEGIN
	 DECLARE model_in_filter VARCHAR(50);
     
     IF filter = 'SS' OR filter = '(All)' THEN
		SET model_in_filter = 'SS';
	 ELSE
		SET model_in_filter = 'NULL';
     END IF;
     
RETURN model_in_filter;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetStdModelFilter
DELIMITER //
CREATE FUNCTION `GetStdModelFilter`(filter VARCHAR(15)) RETURNS varchar(50) CHARSET latin1
    NO SQL
BEGIN
	 DECLARE model_in_filter VARCHAR(50);
     
     IF filter = 'STD' OR filter = '(All)' THEN
		SET model_in_filter = 'STD';
	 ELSE
		SET model_in_filter = 'NULL';
     END IF;
     
RETURN model_in_filter;
END//
DELIMITER ;

-- Dumping structure for function statshv.GetSuperModelFilter
DELIMITER //
CREATE FUNCTION `GetSuperModelFilter`(filter VARCHAR(15)) RETURNS varchar(50) CHARSET latin1
    NO SQL
BEGIN
	 DECLARE model_in_filter VARCHAR(50);
     
     IF filter = 'SUPER' OR filter = '(All)' THEN
		SET model_in_filter = 'SUPER';
	 ELSE
		SET model_in_filter = 'NULL';
     END IF;
     
RETURN model_in_filter;
END//
DELIMITER ;

-- Dumping structure for table statshv.hipottest
CREATE TABLE IF NOT EXISTS `hipottest` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `StationID` varchar(5) NOT NULL DEFAULT '',
  `PartNo` varchar(15) NOT NULL DEFAULT '',
  `Model` varchar(75) NOT NULL DEFAULT '',
  `ShopOrd` varchar(15) NOT NULL DEFAULT '',
  `SerialNo` varchar(10) NOT NULL DEFAULT '',
  `Operator` varchar(5) NOT NULL DEFAULT '',
  `PassRef` tinyint(1) NOT NULL DEFAULT '0',
  `PassProd` tinyint(1) NOT NULL DEFAULT '0',
  `comment1` varchar(45) NOT NULL DEFAULT '',
  `comment2` varchar(45) NOT NULL DEFAULT '',
  `refID` varchar(15) NOT NULL DEFAULT '',
  `caldate` date NOT NULL,
  `Rectime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=3944 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.ictcaz
CREATE TABLE IF NOT EXISTS `ictcaz` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `LOD` double NOT NULL DEFAULT '0',
  `TOCoffs` double NOT NULL DEFAULT '0',
  `Spikes` int NOT NULL DEFAULT '0',
  `TOCAZpass` tinyint(1) NOT NULL DEFAULT '0',
  `TOCpass` tinyint(1) NOT NULL DEFAULT '0',
  `ICCpass` tinyint(1) NOT NULL DEFAULT '0',
  `TMFno` varchar(15) NOT NULL DEFAULT '',
  `TCalDue` date NOT NULL DEFAULT '0000-00-00',
  `CondRef` double NOT NULL DEFAULT '0',
  `CondOffs` double NOT NULL DEFAULT '0',
  `Prcsn` double NOT NULL DEFAULT '0',
  `ResRSD` double NOT NULL DEFAULT '0',
  `CondAZpass` tinyint(1) NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='TC_IC_COND_AUTOZERO_MODE = 22';

-- Data exporting was unselected.

-- Dumping structure for view statshv.ic_tc_cond_az_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `ic_tc_cond_az_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.inicnfg
CREATE TABLE IF NOT EXISTS `inicnfg` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `caption` varchar(15) NOT NULL DEFAULT 'BOM list',
  `hdrcnt` int NOT NULL DEFAULT '5',
  `hdr00` varchar(15) NOT NULL DEFAULT 'partno',
  `hdr00w` int NOT NULL DEFAULT '100',
  `hdr01` varchar(15) NOT NULL DEFAULT 'item',
  `hdr01w` int NOT NULL DEFAULT '40',
  `hdr02` varchar(15) NOT NULL DEFAULT 'description',
  `hdr02w` int NOT NULL DEFAULT '230',
  `hdr03` varchar(15) NOT NULL DEFAULT 'QTY',
  `hdr03w` int NOT NULL DEFAULT '40',
  `hdr04` varchar(15) NOT NULL DEFAULT 'UOM',
  `hdr04w` int NOT NULL DEFAULT '40',
  `hdr05` varchar(15) NOT NULL DEFAULT '',
  `hdr05w` int NOT NULL DEFAULT '0',
  `hdr06` varchar(15) NOT NULL DEFAULT '',
  `hdr06w` int NOT NULL DEFAULT '0',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COMMENT='replaces .ini file entries (later)';

-- Data exporting was unselected.

-- Dumping structure for table statshv.instlocn
CREATE TABLE IF NOT EXISTS `instlocn` (
  `Recno` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '' COMMENT 'SerialNo for the Instrument',
  `Location` varchar(15) NOT NULL DEFAULT '' COMMENT 'Location State - Assembly, EndAssembly, TestAndCal, EndCal, OBA, PreShip, Shipped, PGI',
  `Starttm` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Start time in the current Location',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Row timestamp',
  `DeliveryNo` varchar(15) NOT NULL DEFAULT '' COMMENT 'Delivery Number - Value from SER01-LIEF_NR in SAP.',
  `LineNo` varchar(5) NOT NULL DEFAULT '',
  `Material` varchar(15) NOT NULL DEFAULT '' COMMENT 'Material issued on Goods Pick Date.  The Material is the PRD number of the Instrument.  Value from OBJK-MATNR in SAP.',
  `GoodsPickDate` date NOT NULL DEFAULT '0000-00-00' COMMENT 'Goods Pick Date - Date Material was picked for shipment.  Value from OBJK-DATUM in SAP.',
  `PlannedGoodsIssueDate` date NOT NULL DEFAULT '0000-00-00' COMMENT 'Planned Goods Movement Date - Value from LIKP-WADAT in SAP.  ',
  `ActualGoodsIssueDate` date NOT NULL DEFAULT '0000-00-00' COMMENT 'Actual Goods Issue Date - Date goods are issued when the Goods Issue Status is Completed.  Value from LIKP-WADAT_IST in SAP. ',
  `GoodsIssueStatus` varchar(2) NOT NULL DEFAULT '' COMMENT 'Total Goods Movement from VBUK-WBSTK in SAP.  A - Not Started, C - Completed',
  `SalesOrg` varchar(5) NOT NULL DEFAULT '',
  `AssemblyStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Time the Instrument was started in Assembly',
  `EndAssemblyStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Time the Instrument was finished Assembly and waiting for Test and Cal',
  `TestAndCalStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Time the Instrument started Test and Cal',
  `OBAStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Time the Instrument started OBA',
  `EndCalStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Time the Instrument was finished in Test and Cal and is waiting for Breakdown',
  `PreShipStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Time the Instrument entered into Pre Shipment and is waiting for shipment',
  `ShippedStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT 'Time the Instrument entered into Warehouse',
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=4143 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view statshv.instlocn_all_desc_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `instlocn_all_desc_view` (
	`Recno` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COMMENT 'SerialNo for the Instrument' COLLATE 'latin1_swedish_ci',
	`Location` VARCHAR(1) NOT NULL COMMENT 'Location State - Assembly, EndAssembly, TestAndCal, EndCal, OBA, PreShip, Shipped, PGI' COLLATE 'latin1_swedish_ci',
	`Starttm` DATETIME NOT NULL COMMENT 'Start time in the current Location',
	`RecTime` TIMESTAMP NOT NULL COMMENT 'Row timestamp'
);

-- Dumping structure for view statshv.instlocn_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `instlocn_view` (
	`Recno` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COMMENT 'SerialNo for the Instrument' COLLATE 'latin1_swedish_ci',
	`PartNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Location` VARCHAR(1) NOT NULL COMMENT 'Location State - Assembly, EndAssembly, TestAndCal, EndCal, OBA, PreShip, Shipped, PGI' COLLATE 'latin1_swedish_ci',
	`Material` VARCHAR(1) NOT NULL COMMENT 'Material issued on Goods Pick Date.  The Material is the PRD number of the Instrument.  Value from OBJK-MATNR in SAP.' COLLATE 'latin1_swedish_ci',
	`Starttm` DATETIME NOT NULL COMMENT 'Start time in the current Location',
	`RecTime` TIMESTAMP NOT NULL COMMENT 'Row timestamp'
);

-- Dumping structure for table statshv.iotests
CREATE TABLE IF NOT EXISTS `iotests` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `StrtsFlowOn` tinyint(1) NOT NULL DEFAULT '0',
  `PauseFlowOff` tinyint(1) NOT NULL DEFAULT '0',
  `ResumeFlowOn` tinyint(1) NOT NULL DEFAULT '0',
  `StopsLvlOn` tinyint(1) NOT NULL DEFAULT '0',
  `ResumeLvlOff` tinyint(1) NOT NULL DEFAULT '0',
  `StartsBinOn` tinyint(1) NOT NULL DEFAULT '0',
  `StopsBinOff` tinyint(1) NOT NULL DEFAULT '0',
  `BinOffAtEnd` tinyint(1) NOT NULL DEFAULT '0',
  `AnalogMeter` varchar(15) NOT NULL DEFAULT '',
  `MeterCalDue` date NOT NULL DEFAULT '0000-00-00',
  `Anal14Ma` double NOT NULL DEFAULT '0',
  `Anal18Ma` double NOT NULL DEFAULT '0',
  `Anal116mA` double NOT NULL DEFAULT '0',
  `Anal120mA` double NOT NULL DEFAULT '0',
  `Anal24mA` double NOT NULL DEFAULT '0',
  `Anal28mA` double NOT NULL DEFAULT '0',
  `Anal216mA` double NOT NULL DEFAULT '0',
  `Anal220mA` double NOT NULL DEFAULT '0',
  `Anal34mA` double NOT NULL DEFAULT '0',
  `Anal38mA` double NOT NULL DEFAULT '0',
  `Anal316mA` double NOT NULL DEFAULT '0',
  `Anal320mA` double NOT NULL DEFAULT '0',
  `AnalPass` tinyint(1) NOT NULL DEFAULT '0',
  `Alm1PriorRed` tinyint(1) NOT NULL DEFAULT '0',
  `Alm1AftGrn` tinyint(1) NOT NULL DEFAULT '0',
  `Alm2PriorRed` tinyint(1) NOT NULL DEFAULT '0',
  `Alm2AftGrn` tinyint(1) NOT NULL DEFAULT '0',
  `Alm3PriorRed` tinyint(1) NOT NULL DEFAULT '0',
  `Alm3AftGrn` tinyint(1) NOT NULL DEFAULT '0',
  `Alm4PriorRed` tinyint(1) NOT NULL DEFAULT '0',
  `Alm4AftGrn` tinyint(1) NOT NULL DEFAULT '0',
  `AlmPass` tinyint(1) NOT NULL DEFAULT '0',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Site` varchar(5) NOT NULL DEFAULT '',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=4167 DEFAULT CHARSET=latin1 COMMENT='Checklist (start)';

-- Data exporting was unselected.

-- Dumping structure for view statshv.iotests_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `iotests_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for view statshv.io_tests_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `io_tests_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for table statshv.llrinse
CREATE TABLE IF NOT EXISTS `llrinse` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `CondRes` double NOT NULL DEFAULT '0',
  `CondPass` tinyint(1) NOT NULL DEFAULT '0',
  `HART` tinyint(1) NOT NULL DEFAULT '0',
  `WiFi` tinyint(1) NOT NULL DEFAULT '0',
  `MdBus` tinyint(1) NOT NULL DEFAULT '0',
  `ProfiBus` tinyint(1) NOT NULL DEFAULT '0',
  `PrtClPass` tinyint(1) NOT NULL DEFAULT '0',
  `TempTMF` varchar(15) NOT NULL DEFAULT '',
  `TempCalDate` date NOT NULL DEFAULT '0000-00-00',
  `TempC3` double NOT NULL DEFAULT '0',
  `TempRdr` double NOT NULL DEFAULT '0',
  `TempDiff` double NOT NULL DEFAULT '0',
  `TempPass` tinyint(1) NOT NULL DEFAULT '0',
  `FlowRate` double NOT NULL DEFAULT '0',
  `FlowPass` tinyint(1) NOT NULL DEFAULT '0',
  `ICavg` double NOT NULL DEFAULT '0',
  `ICrsd` double NOT NULL DEFAULT '0',
  `TCavg` double NOT NULL DEFAULT '0',
  `TCrsd` double NOT NULL DEFAULT '0',
  `TOCavg` double NOT NULL DEFAULT '0',
  `TOCrsd` double NOT NULL DEFAULT '0',
  `RnsPass` tinyint(1) NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1 COMMENT='Start of cal checklists';

-- Data exporting was unselected.

-- Dumping structure for view statshv.llrinse_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `llrinse_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for table statshv.location
CREATE TABLE IF NOT EXISTS `location` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SequenceNo` tinyint NOT NULL DEFAULT '0' COMMENT 'Location sequence order',
  `Location` varchar(15) NOT NULL DEFAULT '' COMMENT 'Location code - TestAndCal, EndCal, OBA, Preship, Shipped',
  `Description` varchar(25) NOT NULL DEFAULT '' COMMENT 'Description of the Location',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COMMENT='Location area for Instrument to be located in during Manufac';

-- Data exporting was unselected.

-- Dumping structure for view statshv.low_level_rinse_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `low_level_rinse_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for view statshv.low_level_sl1_data_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `low_level_sl1_data_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.obanotes
CREATE TABLE IF NOT EXISTS `obanotes` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `Result` varchar(15) NOT NULL DEFAULT '',
  `FinishedDate` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Notes` varchar(5000) NOT NULL DEFAULT '',
  `Operator` varchar(25) DEFAULT NULL,
  `Station` varchar(15) NOT NULL DEFAULT '',
  `Bay` int NOT NULL DEFAULT '0',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `Rectime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=143 DEFAULT CHARSET=latin1 COMMENT='M500 OBA Notes';

-- Data exporting was unselected.

-- Dumping structure for view statshv.online_precision_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `online_precision_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.planning_instruments_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `planning_instruments_view` (
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`PartNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.prd_goods_issue_bldr_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `prd_goods_issue_bldr_view` (
	`SerialNo` VARCHAR(1) NOT NULL COMMENT 'SerialNo for the Instrument' COLLATE 'latin1_swedish_ci',
	`Location` VARCHAR(1) NOT NULL COMMENT 'Location State - Assembly, EndAssembly, TestAndCal, EndCal, OBA, PreShip, Shipped, PGI' COLLATE 'latin1_swedish_ci',
	`DeliveryNo` VARCHAR(1) NOT NULL COMMENT 'Delivery Number - Value from SER01-LIEF_NR in SAP.' COLLATE 'latin1_swedish_ci',
	`LineNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Material` VARCHAR(1) NOT NULL COMMENT 'Material issued on Goods Pick Date.  The Material is the PRD number of the Instrument.  Value from OBJK-MATNR in SAP.' COLLATE 'latin1_swedish_ci',
	`GoodsPickDate` DATE NOT NULL COMMENT 'Goods Pick Date - Date Material was picked for shipment.  Value from OBJK-DATUM in SAP.',
	`GoodsIssueStatus` VARCHAR(1) NOT NULL COMMENT 'Total Goods Movement from VBUK-WBSTK in SAP.  A - Not Started, C - Completed' COLLATE 'latin1_swedish_ci',
	`SalesOrg` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`VendorSerialNo` VARCHAR(1) NULL COMMENT 'SerialNo for the Instrument' COLLATE 'latin1_swedish_ci',
	`VendorLocation` VARCHAR(1) NULL COMMENT 'Location State - Assembly, EndAssembly, TestAndCal, EndCal, OBA, PreShip, Shipped, PGI' COLLATE 'latin1_swedish_ci',
	`VendorDeliveryNo` VARCHAR(1) NULL COMMENT 'Delivery Number - Value from SER01-LIEF_NR in SAP.' COLLATE 'latin1_swedish_ci',
	`VendorLineNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorMaterial` VARCHAR(1) NULL COMMENT 'Material issued on Goods Pick Date.  The Material is the PRD number of the Instrument.  Value from OBJK-MATNR in SAP.' COLLATE 'latin1_swedish_ci',
	`VendorGoodsPickDate` DATE NULL COMMENT 'Goods Pick Date - Date Material was picked for shipment.  Value from OBJK-DATUM in SAP.',
	`VendorGoodsIssueStatus` VARCHAR(1) NULL COMMENT 'Total Goods Movement from VBUK-WBSTK in SAP.  A - Not Started, C - Completed' COLLATE 'latin1_swedish_ci',
	`VendorSalesOrg` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.prd_goods_issue_sales_org_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `prd_goods_issue_sales_org_view` (
	`SerialNo` VARCHAR(1) NULL COMMENT 'SerialNo for the Instrument' COLLATE 'latin1_swedish_ci',
	`Location` VARCHAR(1) NULL COMMENT 'Location State - Assembly, EndAssembly, TestAndCal, EndCal, OBA, PreShip, Shipped, PGI' COLLATE 'latin1_swedish_ci',
	`DeliveryNo` VARCHAR(1) NULL COMMENT 'Delivery Number - Value from SER01-LIEF_NR in SAP.' COLLATE 'latin1_swedish_ci',
	`LineNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Material` VARCHAR(1) NULL COMMENT 'Material issued on Goods Pick Date.  The Material is the PRD number of the Instrument.  Value from OBJK-MATNR in SAP.' COLLATE 'latin1_swedish_ci',
	`GoodsPickDate` DATE NULL COMMENT 'Goods Pick Date - Date Material was picked for shipment.  Value from OBJK-DATUM in SAP.',
	`GoodsIssueStatus` VARCHAR(1) NULL COMMENT 'Total Goods Movement from VBUK-WBSTK in SAP.  A - Not Started, C - Completed' COLLATE 'latin1_swedish_ci',
	`SalesOrg` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorSerialNo` VARCHAR(1) NOT NULL COMMENT 'SerialNo for the Instrument' COLLATE 'latin1_swedish_ci',
	`VendorLocation` VARCHAR(1) NOT NULL COMMENT 'Location State - Assembly, EndAssembly, TestAndCal, EndCal, OBA, PreShip, Shipped, PGI' COLLATE 'latin1_swedish_ci',
	`VendorDeliveryNo` VARCHAR(1) NOT NULL COMMENT 'Delivery Number - Value from SER01-LIEF_NR in SAP.' COLLATE 'latin1_swedish_ci',
	`VendorLineNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorMaterial` VARCHAR(1) NOT NULL COMMENT 'Material issued on Goods Pick Date.  The Material is the PRD number of the Instrument.  Value from OBJK-MATNR in SAP.' COLLATE 'latin1_swedish_ci',
	`VendorGoodsPickDate` DATE NOT NULL COMMENT 'Goods Pick Date - Date Material was picked for shipment.  Value from OBJK-DATUM in SAP.',
	`VendorGoodsIssueStatus` VARCHAR(1) NOT NULL COMMENT 'Total Goods Movement from VBUK-WBSTK in SAP.  A - Not Started, C - Completed' COLLATE 'latin1_swedish_ci',
	`VendorSalesOrg` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.prd_goods_issue_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `prd_goods_issue_view` (
	`SerialNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Location` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`DeliveryNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`LineNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Material` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`GoodsPickDate` DATE NULL,
	`GoodsIssueStatus` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`SalesOrg` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorSerialNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorLocation` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorDeliveryNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorLineNo` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorMaterial` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorGoodsPickDate` DATE NULL,
	`VendorGoodsIssueStatus` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`VendorSalesOrg` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for table statshv.preship
CREATE TABLE IF NOT EXISTS `preship` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Unique identifer for the record.',
  `SerialNo` varchar(15) NOT NULL DEFAULT '' COMMENT 'Serial No for the M500 instrument.',
  `AccPN1` varchar(15) NOT NULL DEFAULT '' COMMENT '1st PartNo checked during Final Ship operation.  This PartNo originates from the planning.partdesc table for the associated PRD number.',
  `AccPN2` varchar(15) NOT NULL DEFAULT '' COMMENT '2nd PartNo checked during Final Ship operation.  This PartNo originates from the planning.partdesc table for the associated PRD number.',
  `AccPN3` varchar(15) NOT NULL DEFAULT '' COMMENT '3rd PartNo checked during Final Ship operation.  This PartNo originates from the planning.partdesc table for the associated PRD number.',
  `AccPN4` varchar(15) NOT NULL DEFAULT '' COMMENT '4th PartNo checked during Final Ship operation.  This PartNo originates from the planning.partdesc table for the associated PRD number.',
  `AccPN5` varchar(15) NOT NULL DEFAULT '' COMMENT '5th PartNo checked during Final Ship operation.  This PartNo originates from the planning.partdesc table for the associated PRD number.',
  `CertGenerated` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Certificate was generated.  Value: 0 - No,  1 - Yes',
  `Site` varchar(5) NOT NULL DEFAULT '' COMMENT 'Site for the Preship Checklist.',
  `Operator` varchar(25) NOT NULL DEFAULT '' COMMENT 'Operator performing the Final Ship operation.',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Update time for the record.',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=3762 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.protocol_expected_testtime
CREATE TABLE IF NOT EXISTS `protocol_expected_testtime` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `Series` varchar(10) NOT NULL DEFAULT '',
  `Model` varchar(15) NOT NULL DEFAULT '',
  `Options` varchar(6) NOT NULL DEFAULT '',
  `TotalTests` int NOT NULL DEFAULT '0',
  `Startup_Exp` float DEFAULT NULL,
  `IO_Tests_Exp` float DEFAULT NULL,
  `LowLevel_Rinse_Exp` float DEFAULT NULL,
  `Sample_Cond_AZ_1_Exp` float DEFAULT NULL,
  `IC_TC_Cond_AZ_Exp` float DEFAULT NULL,
  `LowLevel_SL1_Data_Exp` float DEFAULT NULL,
  `TOC_Single_Point_Cal_Exp` float DEFAULT NULL,
  `TOC_Ver_Exp` float DEFAULT NULL,
  `Cond_Single_Point_Cal_Exp` float DEFAULT NULL,
  `Cond_Cal_Ver_Exp` float DEFAULT NULL,
  `Specificity_Exp` float DEFAULT NULL,
  `Online_Precision_Exp` float DEFAULT NULL,
  `Sample_Cond_AZ_2_Exp` float DEFAULT NULL,
  `Constants_Exp` float DEFAULT NULL,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.protocol_expected_testtime2
CREATE TABLE IF NOT EXISTS `protocol_expected_testtime2` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `Series` varchar(10) NOT NULL DEFAULT '',
  `Model` varchar(15) NOT NULL DEFAULT '',
  `Options` varchar(6) NOT NULL DEFAULT '',
  `TotalTests` int NOT NULL DEFAULT '0',
  `Startup_Exp` float DEFAULT NULL,
  `IO_Tests_Exp` float DEFAULT NULL,
  `LowLevel_Rinse_Exp` float DEFAULT NULL,
  `Sample_Cond_AZ_1_Exp` float DEFAULT NULL,
  `IC_TC_Cond_AZ_Exp` float DEFAULT NULL,
  `LowLevel_SL1_Data_Exp` float DEFAULT NULL,
  `TOC_Single_Point_Cal_Exp` float DEFAULT NULL,
  `TOC_Ver_Exp` float DEFAULT NULL,
  `Cond_Single_Point_Cal_Exp` float DEFAULT NULL,
  `Cond_Cal_Ver_Exp` float DEFAULT NULL,
  `Specificity_Exp` float DEFAULT NULL,
  `Online_Precision_Exp` float DEFAULT NULL,
  `Sample_Cond_AZ_2_Exp` float DEFAULT NULL,
  `Constants_Exp` float DEFAULT NULL,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view statshv.protocol_expected_testtime_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `protocol_expected_testtime_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`Series` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`TotalTests` INT NOT NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL,
	`Constants_Exp` FLOAT NULL
);

-- Dumping structure for view statshv.protocol_testtime_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `protocol_testtime_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`StartTime` TIMESTAMP NOT NULL,
	`FinishTime` DATETIME NULL,
	`CurrentProtocol` VARCHAR(1) NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`Startup` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`Startup_Act` BIGINT NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`IO_Tests_Act` BIGINT NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`Low_Level_Rinse_Down` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`LowLevel_Rinse_Act` BIGINT NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`Sample_Cond_AZ_1_Act` BIGINT NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`IC_TC_Cond_AZ_Act` BIGINT NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`LowLevel_SL1_Data_Act` BIGINT NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`TOC_Single_Point_Cal_Act` BIGINT NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`TOC_Ver_Act` BIGINT NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`Cond_Single_Point_Cal_Act` BIGINT NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`Cond_Cal_Ver_Act` BIGINT NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`Specificity_Act` BIGINT NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`Online_Precision_Act` BIGINT NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2` VARCHAR(1) NOT NULL COLLATE 'utf8mb3_general_ci',
	`Sample_Cond_AZ_2_Act` BIGINT NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL,
	`Constants_Act` BIGINT NULL,
	`Constants_Exp` FLOAT NULL
);

-- Dumping structure for function statshv.RealTimeCalculator
DELIMITER //
CREATE FUNCTION `RealTimeCalculator`(lastProtocolEndTime DATETIME, timeInCurrentProtocol INT) RETURNS int
    NO SQL
BEGIN
	
    DECLARE adjustedTime INT;
    DECLARE weeknights INT;
    DECLARE currentProtDayOfWeek INT;
    DECLARE lastProtDayOfWeek INT;
    DECLARE currentTime DATETIME;
    SET currentTime = NOW();
    SET currentProtDayOfWeek = DAYOFWEEK(currentTime);
    SET lastProtDayOfWeek = DAYOFWEEK(lastProtocolEndTime);
    
    
   
	
     
	
    
    
    
    
   IF (lastProtDayOfWeek = currentProtDayOfWeek) THEN
		
        IF timeInCurrentProtocol < 540 THEN
			SET adjustedTime = timeInCurrentProtocol;
		
        ELSEIF (timeInCurrentProtocol > 9540) & (timeInCurrentProtocol < 20160)  THEN 
			SET adjustedTime = timeInCurrentProtocol-3840;
			SET weeknights = FLOOR(adjustedTime/1440);
			SET adjustedTime = adjustedTime - (weeknights*960);
		
        else	
			SET adjustedTime=timeInCurrentProtocol;
        END IF;
    
    
    
    
	
	ELSEIF  (lastProtDayOfWeek < currentProtDayOfWeek) & (timeInCurrentProtocol > 9540) THEN
		SET adjustedTime = timeInCurrentProtocol-3840;
			SET weeknights = FLOOR(adjustedTime/1440);
			SET adjustedTime = adjustedTime - (weeknights*960);
	
	ELSEIF lastProtDayOfWeek > currentProtDayOfWeek THEN 
			 
		IF (timeInCurrentProtocol > 3840) & (timeInCurrentProtocol < 5280) THEN
			SET adjustedTime = timeInCurrentProtocol - 3840;
		
		ELSEIF timeInCurrentProtocol > 5280   THEN
			SET adjustedTime = timeInCurrentProtocol-3840;
			SET weeknights = FLOOR(adjustedTime/1440);
			SET adjustedTime = adjustedTime - (weeknights*960);
		END IF;
	
    
	ELSEIF lastProtDayOfWeek < currentProtDayOfWeek & (timeInCurrentProtocol < 9540) THEN 
		
		IF timeInCurrentProtocol < 540 THEN
			SET adjustedTime = timeInCurrentProtocol;
		
		ELSEIF (timeInCurrentProtocol > 540) & (timeInCurrentProtocol < 1440)   THEN
			SET adjustedTime = timeInCurrentProtocol-960;
		
		ELSEIF (timeInCurrentProtocol > 1440) & (timeInCurrentProtocol < 3840)   THEN
			SET weeknights = FLOOR(timeInCurrentProtocol/1440);
			SET adjustedTime = timeInCurrentProtocol-(weeknights*960);
		END IF;
	
	
	ELSE
		SET adjustedTime = NULL;
	END IF;	
    
	RETURN adjustedTime;
    
END//
DELIMITER ;

-- Dumping structure for table statshv.repairdat
CREATE TABLE IF NOT EXISTS `repairdat` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `PageName` varchar(100) NOT NULL DEFAULT '',
  `FailedPartNo` varchar(20) NOT NULL DEFAULT '',
  `Description` varchar(45) NOT NULL DEFAULT '',
  `Comments` varchar(1000) NOT NULL DEFAULT '',
  `Func` varchar(10) NOT NULL DEFAULT 'OPS',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COMMENT='Record fails for QC';

-- Data exporting was unselected.

-- Dumping structure for table statshv.repairdat2
CREATE TABLE IF NOT EXISTS `repairdat2` (
  `RecordNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `ShopOrder` varchar(10) NOT NULL DEFAULT '',
  `PageName` varchar(90) NOT NULL DEFAULT '',
  `Operator` varchar(15) NOT NULL DEFAULT '',
  `Assy` varchar(45) NOT NULL DEFAULT '',
  `Component` varchar(45) NOT NULL DEFAULT '',
  `Failure` varchar(40) NOT NULL DEFAULT '',
  `Func` varchar(10) NOT NULL DEFAULT 'OPS',
  `Site` varchar(5) NOT NULL DEFAULT '',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `StrtTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `notes` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`RecordNo`)
) ENGINE=InnoDB AUTO_INCREMENT=2271 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.rnsdown
CREATE TABLE IF NOT EXISTS `rnsdown` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `CondRes` double NOT NULL DEFAULT '0',
  `CondPass` tinyint(1) NOT NULL DEFAULT '0',
  `HART` tinyint(1) NOT NULL DEFAULT '0',
  `WiFi` tinyint(1) NOT NULL DEFAULT '0',
  `MdBus` tinyint(1) NOT NULL DEFAULT '0',
  `ProfiBus` tinyint(1) NOT NULL DEFAULT '0',
  `PrtClPass` tinyint(1) NOT NULL DEFAULT '0',
  `TempTMF` varchar(15) NOT NULL DEFAULT '',
  `TempCalDate` date NOT NULL DEFAULT '0000-00-00',
  `TempC3` double NOT NULL DEFAULT '0',
  `TempRdr` double NOT NULL DEFAULT '0',
  `TempDiff` double NOT NULL DEFAULT '0',
  `TempPass` tinyint(1) NOT NULL DEFAULT '0',
  `FlowRate` double NOT NULL DEFAULT '0',
  `FlowPass` tinyint(1) NOT NULL DEFAULT '0',
  `ICavg` double NOT NULL DEFAULT '0',
  `ICrsd` double NOT NULL DEFAULT '0',
  `TCavg` double NOT NULL DEFAULT '0',
  `TCrsd` double NOT NULL DEFAULT '0',
  `TOCavg` double NOT NULL DEFAULT '0',
  `TOCrsd` double NOT NULL DEFAULT '0',
  `RnsPass` tinyint(1) NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `DoorSwitchPass` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=4189 DEFAULT CHARSET=latin1 COMMENT='Start of cal checklists';

-- Data exporting was unselected.

-- Dumping structure for view statshv.rnsdown_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `rnsdown_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for table statshv.samplcellcal
CREATE TABLE IF NOT EXISTS `samplcellcal` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `calconst` double NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Generic inital cols';

-- Data exporting was unselected.

-- Dumping structure for view statshv.sample_cond_az_1_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `sample_cond_az_1_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.sample_cond_az_2_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `sample_cond_az_2_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.spcal
CREATE TABLE IF NOT EXISTS `spcal` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `SPcalLot` varchar(15) NOT NULL DEFAULT '',
  `SPcalExp` date NOT NULL DEFAULT '0000-00-00',
  `ICslope` double NOT NULL DEFAULT '0',
  `TCslope` double NOT NULL DEFAULT '0',
  `SLPratio` double NOT NULL DEFAULT '0',
  `spICpeak` double NOT NULL DEFAULT '0',
  `spTCpeak` double NOT NULL DEFAULT '0',
  `spPkRatio` double NOT NULL DEFAULT '0',
  `SPpass` tinyint(1) NOT NULL DEFAULT '0',
  `SPaccLot` varchar(15) NOT NULL DEFAULT '',
  `SPaccExp` date NOT NULL DEFAULT '0000-00-00',
  `TOCacc` double NOT NULL DEFAULT '0',
  `TOCrsd` double NOT NULL DEFAULT '0',
  `SPaccpass` tinyint(1) NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `TOC_SP_Cal_Time` datetime DEFAULT NULL,
  `TOC_Ver_Time` datetime DEFAULT NULL,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=8392 DEFAULT CHARSET=latin1 COMMENT='TOC_SINGLE_POINT_CAL_MODE = 6';

-- Data exporting was unselected.

-- Dumping structure for view statshv.spcal1_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `spcal1_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.spcal2_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `spcal2_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.spcalvials
CREATE TABLE IF NOT EXISTS `spcalvials` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `CalBlnkTocAVG` double NOT NULL DEFAULT '0',
  `CalBlnkIcAVG` double NOT NULL DEFAULT '0',
  `CalBlnkTcAVG` double NOT NULL DEFAULT '0',
  `CalBlnkTocSTD` double NOT NULL DEFAULT '0',
  `CalBlnkIcSTD` double NOT NULL DEFAULT '0',
  `CalBlnkTcSTD` double NOT NULL DEFAULT '0',
  `CalBlnkTocRSD` double NOT NULL DEFAULT '0',
  `CalBlnkIcRSD` double NOT NULL DEFAULT '0',
  `CalBlnkTcRSD` double NOT NULL DEFAULT '0',
  `RWBlnkTocAVG` double NOT NULL DEFAULT '0',
  `RWBlnkIcAVG` double NOT NULL DEFAULT '0',
  `RWBlnkTcAVG` double NOT NULL DEFAULT '0',
  `RWBlnkTocSTD` double NOT NULL DEFAULT '0',
  `RWBlnkIcSTD` double NOT NULL DEFAULT '0',
  `RWBlnkTcSTD` double NOT NULL DEFAULT '0',
  `RWBlnkTocRSD` double NOT NULL DEFAULT '0',
  `RWBlnkIcRSD` double NOT NULL DEFAULT '0',
  `RWBlnkTcRSD` double NOT NULL DEFAULT '0',
  `STDTocAVG` double NOT NULL DEFAULT '0',
  `STDIcAVG` double NOT NULL DEFAULT '0',
  `STDTcAVG` double NOT NULL DEFAULT '0',
  `STDTocSTD` double NOT NULL DEFAULT '0',
  `STDIcSTD` double NOT NULL DEFAULT '0',
  `STDTcSTD` double NOT NULL DEFAULT '0',
  `STDTocRSD` double NOT NULL DEFAULT '0',
  `STDIcRSD` double NOT NULL DEFAULT '0',
  `STDTcRSD` double NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COMMENT='Generic inital cols';

-- Data exporting was unselected.

-- Dumping structure for table statshv.speccal
CREATE TABLE IF NOT EXISTS `speccal` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `MethRec` double NOT NULL DEFAULT '0',
  `NicRec` double NOT NULL DEFAULT '0',
  `KHPRec` double NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='TOC_SINGLE_POINT_CAL_MODE = 6';

-- Data exporting was unselected.

-- Dumping structure for view statshv.specificity_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `specificity_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for table statshv.specvials
CREATE TABLE IF NOT EXISTS `specvials` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `RWBlnkTocAVG` double NOT NULL DEFAULT '0',
  `RWBlnkIcAVG` double NOT NULL DEFAULT '0',
  `RWBlnkTcAVG` double NOT NULL DEFAULT '0',
  `RWBlnkTocSTD` double NOT NULL DEFAULT '0',
  `RWBlnkIcSTD` double NOT NULL DEFAULT '0',
  `RWBlnkTcSTD` double NOT NULL DEFAULT '0',
  `RWBlnkTocRSD` double NOT NULL DEFAULT '0',
  `RWBlnkIcRSD` double NOT NULL DEFAULT '0',
  `RWBlnkTcRSD` double NOT NULL DEFAULT '0',
  `NICTocAVG` double NOT NULL DEFAULT '0',
  `NICIcAVG` double NOT NULL DEFAULT '0',
  `NICTcAVG` double NOT NULL DEFAULT '0',
  `NICTocSTD` double NOT NULL DEFAULT '0',
  `NICIcSTD` double NOT NULL DEFAULT '0',
  `NICTcSTD` double NOT NULL DEFAULT '0',
  `NICTocRSD` double NOT NULL DEFAULT '0',
  `NICIcRSD` double NOT NULL DEFAULT '0',
  `NICTcRSD` double NOT NULL DEFAULT '0',
  `MeOHTocAVG` double NOT NULL DEFAULT '0',
  `MeOHIcAVG` double NOT NULL DEFAULT '0',
  `MeOHTcAVG` double NOT NULL DEFAULT '0',
  `MeOHTocSTD` double NOT NULL DEFAULT '0',
  `MeOHIcSTD` double NOT NULL DEFAULT '0',
  `MeOHTcSTD` double NOT NULL DEFAULT '0',
  `MeOHTocRSD` double NOT NULL DEFAULT '0',
  `MeOHIcRSD` double NOT NULL DEFAULT '0',
  `MeOHTcRSD` double NOT NULL DEFAULT '0',
  `TOCTocAVG` double NOT NULL DEFAULT '0',
  `TOCIcAVG` double NOT NULL DEFAULT '0',
  `TOCTcAVG` double NOT NULL DEFAULT '0',
  `TOCTocSTD` double NOT NULL DEFAULT '0',
  `TOCIcSTD` double NOT NULL DEFAULT '0',
  `TOCTcSTD` double NOT NULL DEFAULT '0',
  `TOCTocRSD` double NOT NULL DEFAULT '0',
  `TOCIcRSD` double NOT NULL DEFAULT '0',
  `TOCTcRSD` double NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COMMENT='Generic inital cols';

-- Data exporting was unselected.

-- Dumping structure for table statshv.spvervials
CREATE TABLE IF NOT EXISTS `spvervials` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `RWBlnkTocAVG` double NOT NULL DEFAULT '0',
  `RWBlnkIcAVG` double NOT NULL DEFAULT '0',
  `RWBlnkTcAVG` double NOT NULL DEFAULT '0',
  `RWBlnkTocSTD` double NOT NULL DEFAULT '0',
  `RWBlnkIcSTD` double NOT NULL DEFAULT '0',
  `RWBlnkTcSTD` double NOT NULL DEFAULT '0',
  `RWBlnkTocRSD` double NOT NULL DEFAULT '0',
  `RWBlnkIcRSD` double NOT NULL DEFAULT '0',
  `RWBlnkTcRSD` double NOT NULL DEFAULT '0',
  `STDTocAVG` double NOT NULL DEFAULT '0',
  `STDIcAVG` double NOT NULL DEFAULT '0',
  `STDTcAVG` double NOT NULL DEFAULT '0',
  `STDTocSTD` double NOT NULL DEFAULT '0',
  `STDIcSTD` double NOT NULL DEFAULT '0',
  `STDTcSTD` double NOT NULL DEFAULT '0',
  `STDTocRSD` double NOT NULL DEFAULT '0',
  `STDIcRSD` double NOT NULL DEFAULT '0',
  `STDTcRSD` double NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Generic inital cols';

-- Data exporting was unselected.

-- Dumping structure for table statshv.startup
CREATE TABLE IF NOT EXISTS `startup` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `AQCNo` varchar(15) NOT NULL DEFAULT '',
  `RLE` tinyint(1) NOT NULL DEFAULT '0',
  `FWrev` varchar(10) NOT NULL DEFAULT '',
  `IPAddr` varchar(15) NOT NULL DEFAULT '',
  `ICCell` varchar(10) NOT NULL DEFAULT '',
  `TCCell` varchar(10) NOT NULL DEFAULT '',
  `C3Cell` varchar(10) NOT NULL DEFAULT '',
  `ShopOrder` varchar(15) NOT NULL DEFAULT '',
  `SIOSOrder` varchar(10) NOT NULL DEFAULT '',
  `SmplCondres` varchar(10) NOT NULL DEFAULT '',
  `ThermsChkd` tinyint(1) NOT NULL DEFAULT '0',
  `SysChkd` tinyint(1) NOT NULL DEFAULT '0',
  `GainsChkd` tinyint(1) NOT NULL DEFAULT '0',
  `TdsChkd` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) DEFAULT NULL,
  `Mods` varchar(256) NOT NULL DEFAULT '',
  `CalDone` tinyint unsigned NOT NULL DEFAULT '0',
  `LastProtocol` int unsigned NOT NULL DEFAULT '100',
  `Station` varchar(15) NOT NULL DEFAULT '',
  `Bay` int NOT NULL DEFAULT '0',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `Rectime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `SWversion` varchar(30) NOT NULL DEFAULT '',
  `SNChecked` tinyint(1) NOT NULL DEFAULT '0',
  `WizardStartTime` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `Series` varchar(26) DEFAULT '',
  `Model` varchar(26) DEFAULT '',
  `Options` varchar(10) DEFAULT 'NONE',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=5866 DEFAULT CHARSET=latin1 COMMENT='General Data';

-- Data exporting was unselected.

-- Dumping structure for view statshv.startup_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `startup_90_day_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`IPAddr` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`AQCNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL,
	`Station` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Bay` INT NOT NULL,
	`WizardStartTime` DATETIME NOT NULL
);

-- Dumping structure for view statshv.startup_all_desc_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `startup_all_desc_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`AQCno` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RLE` TINYINT(1) NOT NULL,
	`IPAddr` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ICCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`TCCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`C3Cell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SIOSOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SmplCondres` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ThermsChkd` TINYINT(1) NOT NULL,
	`SysChkd` TINYINT(1) NOT NULL,
	`GainsChkd` TINYINT(1) NOT NULL,
	`TdsChkd` TINYINT(1) NOT NULL,
	`Operator` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Mods` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`CalDone` TINYINT UNSIGNED NOT NULL,
	`LastProtocol` INT UNSIGNED NOT NULL,
	`Station` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Bay` INT NOT NULL,
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL
);

-- Dumping structure for view statshv.startup_all_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `startup_all_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`AQCno` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RLE` TINYINT(1) NOT NULL,
	`IPAddr` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ICCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`TCCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`C3Cell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SIOSOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SmplCondres` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ThermsChkd` TINYINT(1) NOT NULL,
	`SysChkd` TINYINT(1) NOT NULL,
	`GainsChkd` TINYINT(1) NOT NULL,
	`TdsChkd` TINYINT(1) NOT NULL,
	`Operator` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Mods` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`CalDone` TINYINT UNSIGNED NOT NULL,
	`LastProtocol` INT UNSIGNED NOT NULL,
	`Station` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Bay` INT NOT NULL,
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NOT NULL
);

-- Dumping structure for view statshv.startup_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `startup_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`AQCNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RLE` TINYINT(1) NOT NULL,
	`FWrev` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`IpAddr` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ICCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`TCCell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`C3Cell` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SIOSOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SmplCondres` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ThermsChkd` TINYINT(1) NOT NULL,
	`SysChkd` TINYINT(1) NOT NULL,
	`GainsChkd` TINYINT(1) NOT NULL,
	`TdsChkd` TINYINT(1) NOT NULL,
	`RecTime` TIMESTAMP NOT NULL,
	`Operator` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Mods` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`CalDone` TINYINT UNSIGNED NOT NULL,
	`LastProtocol` INT UNSIGNED NOT NULL,
	`Station` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Bay` INT NOT NULL,
	`Site` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`UpdateTime` TIMESTAMP NOT NULL,
	`SWversion` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SNChecked` TINYINT(1) NOT NULL,
	`WizardStartTime` DATETIME NOT NULL
);

-- Dumping structure for table statshv.table_all_actions
CREATE TABLE IF NOT EXISTS `table_all_actions` (
  `RecordNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `PageName` varchar(25) NOT NULL DEFAULT '',
  `SymptomID` varchar(4) NOT NULL DEFAULT '',
  `Symptom` varchar(255) NOT NULL DEFAULT '',
  `Cause` varchar(255) DEFAULT '',
  `Resolutions` varchar(600) NOT NULL DEFAULT '',
  PRIMARY KEY (`RecordNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.table_causes
CREATE TABLE IF NOT EXISTS `table_causes` (
  `RecordNo` int unsigned NOT NULL AUTO_INCREMENT,
  `StepName` varchar(55) NOT NULL DEFAULT '',
  `PageName` varchar(24) NOT NULL DEFAULT '',
  `SymptomID` varchar(4) NOT NULL DEFAULT '',
  `Cause` varchar(255) NOT NULL DEFAULT '',
  `Troubleshooting Level Count` varchar(7) DEFAULT '',
  `Level_1_Instruction` varchar(700) NOT NULL DEFAULT '',
  `Level_2_Instruction` varchar(600) NOT NULL DEFAULT '',
  `Level_3_Instruction` varchar(500) NOT NULL DEFAULT '',
  PRIMARY KEY (`RecordNo`)
) ENGINE=InnoDB AUTO_INCREMENT=1734 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.table_causes_old
CREATE TABLE IF NOT EXISTS `table_causes_old` (
  `RecordNo` int NOT NULL,
  `SymptomID` double DEFAULT NULL,
  `Cause` text,
  `Troubleshooting Level Count` int DEFAULT NULL,
  `Level_1_Instruction` text,
  `Level_2_Instruction` text,
  `Level_3_Instruction` text,
  PRIMARY KEY (`RecordNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.table_resolution
CREATE TABLE IF NOT EXISTS `table_resolution` (
  `RecordNo` int unsigned NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `PageName` varchar(25) NOT NULL DEFAULT '',
  `SymptomID` varchar(5) NOT NULL DEFAULT '',
  `Symptom` varchar(255) NOT NULL DEFAULT '',
  `Cause` varchar(255) DEFAULT '',
  `Resolution` varchar(600) NOT NULL DEFAULT '',
  PRIMARY KEY (`RecordNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.table_resolution2
CREATE TABLE IF NOT EXISTS `table_resolution2` (
  `RecordNo` int unsigned NOT NULL,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `Operator` varchar(15) DEFAULT '',
  `PageName` varchar(55) NOT NULL DEFAULT '',
  `SymptomID` varchar(6) NOT NULL DEFAULT '',
  `Symptom` varchar(255) NOT NULL DEFAULT '',
  `Cause` varchar(255) DEFAULT '',
  `Instruction_Level_1` varchar(600) NOT NULL DEFAULT '',
  `Instruction_Level_2` varchar(600) NOT NULL DEFAULT '',
  `Resolution` varchar(600) NOT NULL DEFAULT '',
  `CaseNo` int DEFAULT NULL,
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Symptom_copy` varchar(255) NOT NULL DEFAULT '',
  `SerialNo_copy` varchar(15) NOT NULL DEFAULT '',
  `PageName_copy` varchar(55) NOT NULL DEFAULT '',
  `Operator_copy` varchar(15) DEFAULT '',
  `MFE_Level_Used` varchar(5) DEFAULT '',
  `Instruction_Level_Technology` varchar(600) NOT NULL DEFAULT '',
  PRIMARY KEY (`RecordNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view statshv.table_resolution2_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `table_resolution2_view` (
	`RecordNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Operator` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`PageName` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Symptom` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Cause` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Instruction_Level_1` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Instruction_Level_2` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Resolution` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`CaseNo` INT NULL,
	`UpdateTime` TIMESTAMP NOT NULL,
	`Symptom_copy` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`SerialNo_copy` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`PageName_copy` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Operator_copy` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`MFE_Level_Used` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Technology_Instructions` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for table statshv.table_symptoms
CREATE TABLE IF NOT EXISTS `table_symptoms` (
  `RecordNo` int NOT NULL,
  `StepName` varchar(55) NOT NULL DEFAULT '',
  `PageName` varchar(25) NOT NULL DEFAULT '',
  `SymptomID` varchar(4) NOT NULL DEFAULT '',
  `Symptom` varchar(255) NOT NULL DEFAULT '',
  `Cause Count` varchar(2) DEFAULT '',
  `Cause1` varchar(255) NOT NULL DEFAULT '',
  `Cause2` varchar(255) NOT NULL DEFAULT '',
  `Cause3` varchar(255) NOT NULL DEFAULT '',
  `Cause4` varchar(255) NOT NULL DEFAULT '',
  `Cause5` varchar(255) NOT NULL DEFAULT '',
  `Cause6` varchar(255) NOT NULL DEFAULT '',
  `Cause7` varchar(255) NOT NULL DEFAULT '',
  `Cause8` varchar(255) NOT NULL DEFAULT '',
  `Cause9` varchar(255) NOT NULL DEFAULT '',
  `Cause10` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`RecordNo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table statshv.technician
CREATE TABLE IF NOT EXISTS `technician` (
  `Recno` bigint unsigned NOT NULL AUTO_INCREMENT,
  `First` varchar(10) NOT NULL DEFAULT '',
  `Last` varchar(25) NOT NULL DEFAULT '',
  `Title` varchar(25) NOT NULL DEFAULT '',
  `RecTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `PIN` int NOT NULL DEFAULT '0',
  `Active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=latin1 COMMENT='PINs for data integrity';

-- Data exporting was unselected.

-- Dumping structure for table statshv.template
CREATE TABLE IF NOT EXISTS `template` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='Generic inital cols';

-- Data exporting was unselected.

-- Dumping structure for table statshv.tests_lookup
CREATE TABLE IF NOT EXISTS `tests_lookup` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL DEFAULT '',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for view statshv.test_time_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `test_time_90_day_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`WizardStartTime` DATETIME NOT NULL,
	`StartTime` TIMESTAMP NULL,
	`FinishTime` DATETIME NULL,
	`Startup_Act` BIGINT NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests_Act` BIGINT NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`LowLevel_Rinse_Act` BIGINT NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1_Act` BIGINT NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ_Act` BIGINT NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data_Act` BIGINT NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal_Act` BIGINT NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver_Act` BIGINT NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal_Act` BIGINT NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver_Act` BIGINT NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity_Act` BIGINT NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision_Act` BIGINT NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2_Act` BIGINT NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL
);

-- Dumping structure for view statshv.test_time_90_day_view2
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `test_time_90_day_view2` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`WizardStartTime` DATETIME NOT NULL,
	`StartTime` TIMESTAMP NULL,
	`FinishTime` DATETIME NULL,
	`Startup_Act` BIGINT NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests_Act` BIGINT NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`LowLevel_Rinse_Act` BIGINT NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1_Act` FLOAT NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ_Act` FLOAT NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data_Act` BIGINT NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal_Act` BIGINT NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver_Act` BIGINT NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal_Act` FLOAT NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver_Act` FLOAT NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity_Act` FLOAT NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision_Act` FLOAT NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2_Act` BIGINT NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL
);

-- Dumping structure for view statshv.test_time_expected_test_time_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `test_time_expected_test_time_view` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NULL,
	`RecTime (fnlprep)` TIMESTAMP NOT NULL,
	`TestTime` BIGINT NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL
);

-- Dumping structure for view statshv.test_time_expected_test_time_view_2
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `test_time_expected_test_time_view_2` (
	`RecNo` INT UNSIGNED NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NOT NULL,
	`RecTime (fnlprep)` TIMESTAMP NOT NULL,
	`YearMonth` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`YearMonthDay` VARCHAR(1) NULL COLLATE 'utf8mb4_0900_ai_ci',
	`TestTime` BIGINT NULL,
	`Constants_Exp` FLOAT NULL
);

-- Dumping structure for table statshv.tocaz
CREATE TABLE IF NOT EXISTS `tocaz` (
  `Recno` int NOT NULL AUTO_INCREMENT,
  `SerialNo` varchar(15) NOT NULL DEFAULT '',
  `LOD` double NOT NULL DEFAULT '0',
  `TOCoffs` double NOT NULL DEFAULT '0',
  `Spikes` int NOT NULL DEFAULT '0',
  `TOCAZpass` tinyint(1) NOT NULL DEFAULT '0',
  `TOCpass` tinyint(1) NOT NULL DEFAULT '0',
  `ICCpass` tinyint(1) NOT NULL DEFAULT '0',
  `TMFno` varchar(15) NOT NULL DEFAULT '',
  `TCalDue` date NOT NULL DEFAULT '0000-00-00',
  `CondRef` double NOT NULL DEFAULT '0',
  `CondOffs` double NOT NULL DEFAULT '0',
  `Prcsn` double NOT NULL DEFAULT '0',
  `ResRSD` double NOT NULL DEFAULT '0',
  `CondAZpass` tinyint(1) NOT NULL DEFAULT '0',
  `MethRec` double NOT NULL DEFAULT '0',
  `NicRec` double NOT NULL DEFAULT '0',
  `KHPrec` double NOT NULL DEFAULT '0',
  `PrecPass` tinyint(1) NOT NULL DEFAULT '0',
  `Automated` tinyint(1) NOT NULL DEFAULT '0',
  `OldCondOffs` double NOT NULL DEFAULT '0',
  `Spikes2` int NOT NULL DEFAULT '0',
  `StdLot` varchar(30) NOT NULL DEFAULT '',
  `StdExp` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `LOD70Pct` double NOT NULL DEFAULT '0',
  `Operator` varchar(25) NOT NULL DEFAULT '',
  `Station` varchar(5) NOT NULL DEFAULT '',
  `Bay` varchar(5) NOT NULL DEFAULT '',
  `System` varchar(25) NOT NULL DEFAULT '',
  `Site` varchar(5) NOT NULL DEFAULT 'BLDR',
  `RecTime` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `UpdateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Specificity_Time` datetime DEFAULT NULL,
  `Online_Precision_Time` datetime DEFAULT NULL,
  `Sample_Cond_AZ_2_Time` datetime DEFAULT NULL,
  PRIMARY KEY (`Recno`)
) ENGINE=InnoDB AUTO_INCREMENT=7887 DEFAULT CHARSET=latin1 COMMENT='TOC_AUTOZERO_MODE = 23,';

-- Data exporting was unselected.

-- Dumping structure for view statshv.tocaz1_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `tocaz1_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.tocaz2_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `tocaz2_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.tocaz3_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `tocaz3_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.toc_single_point_cal_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `toc_single_point_cal_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.toc_ver_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `toc_ver_90_day_view` (
	`RecNo` INT NOT NULL,
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` DATETIME NULL
);

-- Dumping structure for view statshv.troubleshoot_all_levels
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `troubleshoot_all_levels` (
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Protocol` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Symptom` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Cause` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NOT NULL,
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.troubleshoot_final_resolutions
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `troubleshoot_final_resolutions` (
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Protocol` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Symptom` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Cause` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Resolution` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.troubleshoot_level_1
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `troubleshoot_level_1` (
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Protocol` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Symptom` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Cause` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NOT NULL,
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.troubleshoot_level_1_only2
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `troubleshoot_level_1_only2` (
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NOT NULL,
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.troubleshoot_level_technology
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `troubleshoot_level_technology` (
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Protocol` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Symptom` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Cause` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`RecTime` TIMESTAMP NOT NULL,
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for view statshv.troubleshoot_potential_causes_investigated
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `troubleshoot_potential_causes_investigated` (
	`SerialNo` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Protocol` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Symptom` VARCHAR(1) NOT NULL COLLATE 'latin1_swedish_ci',
	`Cause` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci',
	`Options` VARCHAR(1) NULL COLLATE 'latin1_swedish_ci'
);

-- Dumping structure for procedure statshv.UpdateKpi
DELIMITER //
CREATE PROCEDURE `UpdateKpi`(IN kpiMonth INT, IN kpiYear INT)
BEGIN

set @totalProcessed = 0;
set @totalFailed = 0;
set @fpy = 0;
set @failures = '';
set @components = '';
set @leadTime = 0;
set @sqlStmt1 = '';
set @sqlStmt2 = '';

call statshv.CreateKpiSummaryRecord(kpiMonth, kpiYear, @totalProcessed, @totalFailed, @fpy, @failures, @components, @leadTime, @sqlStmt1, @sqlStmt2);

SELECT @totalProcessed, @totalFailed, @fpy, @failures, @components, @leadTime, @sqlStmt1, @sqlStmt2;

END//
DELIMITER ;

-- Dumping structure for procedure statshv.UpdateYtdKpi
DELIMITER //
CREATE PROCEDURE `UpdateYtdKpi`(IN kpiMonth INT, IN kpiYear INT)
BEGIN

set @totalProcessed = 0;
set @totalFailed = 0;
set @fpy = 0;
set @failures = '';
set @components = '';
set @leadTime = 0;
SET @startDate = '';
SET @stopDate = '';
set @sqlStmt = '';

call statshv.CreateKpiYtdSummaryRecord(kpiMonth, kpiYear, @totalProcessed, @totalFailed, @fpy, @failures, @components, @leadTime, @startDate, @stopDate, @sqlStmt);

SELECT @totalProcessed, @totalFailed, @fpy, @failures, @components, @leadTime, @startDate, @stopDate, @sqlStmt;

END//
DELIMITER ;

-- Dumping structure for table statshv.workcell_bay
CREATE TABLE IF NOT EXISTS `workcell_bay` (
  `RecNo` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'Row unique identifier',
  `WorkCell` varchar(25) NOT NULL DEFAULT '' COMMENT 'Description of the Work Cell - ie. Cell 1',
  `Station` varchar(15) NOT NULL DEFAULT '' COMMENT 'Name of the Workstation. ie. W0360000JV881T2',
  `Bay` varchar(15) NOT NULL DEFAULT '' COMMENT 'Description of the Bay. ie. 1',
  PRIMARY KEY (`RecNo`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1 COMMENT='Table to store the bays in a given Work Cell';

-- Data exporting was unselected.

-- Dumping structure for view statshv.workcell_bay_status_expected_testtime_90_day_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `workcell_bay_status_expected_testtime_90_day_view` (
	`Workcell_Act` VARCHAR(1) NOT NULL COMMENT 'Description of the Work Cell - ie. Cell 1' COLLATE 'latin1_swedish_ci',
	`WorkcellStation_Act` VARCHAR(1) NOT NULL COMMENT 'Name of the Workstation. ie. W0360000JV881T2' COLLATE 'latin1_swedish_ci',
	`WorkcellBay_Act` VARCHAR(1) NOT NULL COMMENT 'Description of the Bay. ie. 1' COLLATE 'latin1_swedish_ci',
	`Station_Act` VARCHAR(1) NULL COMMENT 'Workstation Name' COLLATE 'latin1_swedish_ci',
	`Bay_Act` VARCHAR(1) NULL COMMENT 'Bay identifier for status info' COLLATE 'latin1_swedish_ci',
	`SerialNo_Act` VARCHAR(1) NULL COMMENT 'Instrument SerialNo in the Bay' COLLATE 'latin1_swedish_ci',
	`ShopOrder_Act` VARCHAR(1) NULL COMMENT 'ShopOrder for the Instrument under test' COLLATE 'latin1_swedish_ci',
	`Series_Act` VARCHAR(1) NULL COMMENT 'Series of the Instrument - M500, M500e' COLLATE 'latin1_swedish_ci',
	`Model_Act` VARCHAR(1) NULL COMMENT 'Model of the Instrument - STD IOS, INLINE SAMPLER, SUPER IOS' COLLATE 'latin1_swedish_ci',
	`OptionsID_Act` VARCHAR(1) NULL COMMENT 'Options installed on the Instrument - Not Used' COLLATE 'latin1_swedish_ci',
	`OptionsName_Act` CHAR(0) NOT NULL COLLATE 'utf8mb3_general_ci',
	`StartTime_Act` DATETIME NULL COMMENT 'Starting time for the T&C process',
	`CurrentProtocol_Act` VARCHAR(1) NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`CurrentProtocol_Exp_Time` INT NULL,
	`CurrentProtocol_90DayAvg` INT NULL,
	`Curr_Prot_Tm` BIGINT NULL,
	`Step_Act` INT NULL COMMENT 'Step number for the current protocol',
	`TotalSteps_Act` INT NULL COMMENT 'Total number of Steps in the Test',
	`TimeInTestAndCal_Act` BIGINT NULL,
	`LastProtocol_Act` VARCHAR(1) NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`LastProtocolTime_Act` FLOAT NULL COMMENT 'Last Protocol time in minutes',
	`LastProtocolExpectedTime_Act` FLOAT NULL COMMENT 'Last Protocol expected time in minutes',
	`TotalExpectedTime_Act` FLOAT NULL COMMENT 'Total expected time in minutes for Instrument on the Bay',
	`ExpectedRemainingTimeInTestAndCal_Act` DOUBLE NULL,
	`LastProtocolDelta_Act` DOUBLE NULL,
	`ExpectedFinishDateTime_Act` DATETIME NULL,
	`ActualExpectedFinishDateTime_Act` DATETIME NULL,
	`Startup_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Startup_Exp` FLOAT NULL,
	`IO_Tests_Act_90DayAvg` DECIMAL(24,4) NULL,
	`IO_Tests_Exp` FLOAT NULL,
	`LowLevel_Rinse_Act_90DayAvg` DECIMAL(24,4) NULL,
	`LowLevel_Rinse_Exp` FLOAT NULL,
	`Sample_Cond_AZ_1_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Sample_Cond_AZ_1_Exp` FLOAT NULL,
	`IC_TC_Cond_AZ_Act_90DayAvg` DECIMAL(24,4) NULL,
	`IC_TC_Cond_AZ_Exp` FLOAT NULL,
	`LowLevel_SL1_Data_Act_90DayAvg` DECIMAL(24,4) NULL,
	`LowLevel_SL1_Data_Exp` FLOAT NULL,
	`TOC_Single_Point_Cal_Act_90DayAvg` DECIMAL(24,4) NULL,
	`TOC_Single_Point_Cal_Exp` FLOAT NULL,
	`TOC_Ver_Act_90DayAvg` DECIMAL(24,4) NULL,
	`TOC_Ver_Exp` FLOAT NULL,
	`Cond_Single_Point_Cal_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Cond_Single_Point_Cal_Exp` FLOAT NULL,
	`Cond_Cal_Ver_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Cond_Cal_Ver_Exp` FLOAT NULL,
	`Specificity_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Specificity_Exp` FLOAT NULL,
	`Online_Precision_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Online_Precision_Exp` FLOAT NULL,
	`Sample_Cond_AZ_2_Act_90DayAvg` DECIMAL(24,4) NULL,
	`Sample_Cond_AZ_2_Exp` FLOAT NULL
);

-- Dumping structure for view statshv.workcell_bay_status_expected_testtime_view
-- Creating temporary table to overcome VIEW dependency errors
CREATE TABLE `workcell_bay_status_expected_testtime_view` (
	`Workcell` VARCHAR(1) NOT NULL COMMENT 'Description of the Work Cell - ie. Cell 1' COLLATE 'latin1_swedish_ci',
	`WorkcellStation` VARCHAR(1) NOT NULL COMMENT 'Name of the Workstation. ie. W0360000JV881T2' COLLATE 'latin1_swedish_ci',
	`WorkcellBay` VARCHAR(1) NOT NULL COMMENT 'Description of the Bay. ie. 1' COLLATE 'latin1_swedish_ci',
	`Station` VARCHAR(1) NULL COMMENT 'Workstation Name' COLLATE 'latin1_swedish_ci',
	`Bay` VARCHAR(1) NULL COMMENT 'Bay identifier for status info' COLLATE 'latin1_swedish_ci',
	`SerialNo` VARCHAR(1) NULL COMMENT 'Instrument SerialNo in the Bay' COLLATE 'latin1_swedish_ci',
	`ShopOrder` VARCHAR(1) NULL COMMENT 'ShopOrder for the Instrument under test' COLLATE 'latin1_swedish_ci',
	`Series` VARCHAR(1) NULL COMMENT 'Series of the Instrument - M500, M500e' COLLATE 'latin1_swedish_ci',
	`Model` VARCHAR(1) NULL COMMENT 'Model of the Instrument - STD IOS, INLINE SAMPLER, SUPER IOS' COLLATE 'latin1_swedish_ci',
	`OptionsID` VARCHAR(1) NULL COMMENT 'Options installed on the Instrument - Not Used' COLLATE 'latin1_swedish_ci',
	`OptionsName` CHAR(0) NOT NULL COLLATE 'utf8mb3_general_ci',
	`StartTime` DATETIME NULL COMMENT 'Starting time for the T&C process',
	`CurrentProtocol` VARCHAR(1) NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`Step` INT NULL COMMENT 'Step number for the current protocol',
	`TotalSteps` INT NULL COMMENT 'Total number of Steps in the Test',
	`TimeInTestAndCal` BIGINT NULL,
	`LastProtocol` VARCHAR(1) NULL COMMENT 'Name of the current Protocol being executed' COLLATE 'latin1_swedish_ci',
	`LastProtocolTime` FLOAT NULL COMMENT 'Last Protocol time in minutes',
	`LastProtocolExpectedTime` FLOAT NULL COMMENT 'Last Protocol expected time in minutes',
	`TotalExpectedTime` FLOAT NULL COMMENT 'Total expected time in minutes for Instrument on the Bay',
	`ExpectedRemainingTimeInTestAndCal` DOUBLE NULL,
	`LastProtocolDelta` DOUBLE NULL,
	`ExpectedFinishDateTime` DATETIME NULL,
	`ActualExpectedFinishDateTime` DATETIME NULL
);

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `actual_protocol_testtime_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `actual_protocol_testtime_view` AS select `protocol`.`RecNo` AS `RecNo`,`protocol`.`SerialNo` AS `SerialNo`,`protocol`.`ShopOrder` AS `ShopOrder`,`protocol`.`Series` AS `Series`,`protocol`.`Model` AS `Model`,`protocol`.`Options` AS `Options`,`protocol`.`StartTime` AS `StartTime`,`protocol`.`FinishTime` AS `FinishTime`,date_format(`protocol`.`StartTime`,'%Y%m') AS `YearMonth`,`protocol`.`Startup_Act` AS `Startup_Act`,`protocol`.`Startup_Exp` AS `Startup_Exp`,`statshv`.`GetActual_IOTests_Time`(`protocol`.`IO_Tests_Act`,`protocol`.`Startup_Act`) AS `IO_Tests_Act`,`protocol`.`IO_Tests_Exp` AS `IO_Tests_Exp`,`statshv`.`GetActual_LowLevel_Rinse_Time`(`protocol`.`LowLevel_Rinse_Act`,`protocol`.`IO_Tests_Act`) AS `LowLevel_Rinse_Act`,`protocol`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,`statshv`.`GetActual_Sample_Cond_AZ_1_Time`(`protocol`.`Series`,`protocol`.`Sample_Cond_AZ_1_Act`,`protocol`.`LowLevel_Rinse_Act`) AS `Sample_Cond_AZ_1_Act`,`protocol`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,`statshv`.`GetActual_IC_TC_Cond_AZ_Time`(`protocol`.`Series`,`protocol`.`IC_TC_Cond_AZ_Act`,`protocol`.`Sample_Cond_AZ_1_Act`,`protocol`.`LowLevel_Rinse_Act`) AS `IC_TC_Cond_AZ_Act`,`protocol`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,`statshv`.`GetActual_LowLevel_SL1_Data_Time`(`protocol`.`LowLevel_SL1_Data_Act`,`protocol`.`IC_TC_Cond_AZ_Act`) AS `LowLevel_SL1_Data_Act`,`protocol`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,`statshv`.`GetActual_TOC_Single_Point_Cal_Time`(`protocol`.`TOC_Single_Point_Cal_Act`,`protocol`.`LowLevel_SL1_Data_Act`) AS `TOC_Single_Point_Cal_Act`,`protocol`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,`statshv`.`GetActual_TOC_Ver_Time`(`protocol`.`TOC_Ver_Act`,`protocol`.`TOC_Single_Point_Cal_Act`) AS `TOC_Ver_Act`,`protocol`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,`statshv`.`GetActual_Cond_Single_Point_Cal_Time`(`protocol`.`Series`,`protocol`.`Cond_Single_Point_Cal_Act`,`protocol`.`TOC_Ver_Act`) AS `Cond_Single_Point_Cal_Act`,`protocol`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,`statshv`.`GetActual_Cond_Cal_Ver_Time`(`protocol`.`Series`,`protocol`.`Cond_Cal_Ver_Act`,`protocol`.`Cond_Single_Point_Cal_Act`,`protocol`.`TOC_Ver_Act`) AS `Cond_Cal_Ver_Act`,`protocol`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,`statshv`.`GetActual_Specificity_Time`(`protocol`.`Series`,`protocol`.`Specificity_Act`,`protocol`.`Cond_Cal_Ver_Act`,`protocol`.`TOC_Ver_Act`) AS `Specificity_Act`,`protocol`.`Specificity_Exp` AS `Specificity_Exp`,`statshv`.`GetActual_Online_Precision_Time`(`protocol`.`Series`,`protocol`.`Model`,`protocol`.`Online_Precision_Act`,`protocol`.`Specificity_Act`,`protocol`.`Cond_Cal_Ver_Act`,`protocol`.`TOC_Ver_Act`) AS `Online_Precision_Act`,`protocol`.`Online_Precision_Exp` AS `Online_Precision_Exp`,`statshv`.`GetActual_Sample_Cond_AZ_2_Time`(`protocol`.`Sample_Cond_AZ_2_Act`,`protocol`.`Online_Precision_Act`) AS `Sample_Cond_AZ_2_Act`,`protocol`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp`,`statshv`.`GetActual_Constants_Time`(`protocol`.`Series`,`protocol`.`Constants_Act`,`protocol`.`Sample_Cond_AZ_2_Act`,`protocol`.`Online_Precision_Act`) AS `Constants_Act`,`protocol`.`Constants_Exp` AS `Constants_Exp` from `protocol_testtime_view` `protocol`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `bay_status_test_time_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `bay_status_test_time_90_day_view` AS select `b`.`RecNo` AS `RecNo`,`b`.`Station` AS `Station`,`b`.`Bay` AS `Bay`,`b`.`SerialNo` AS `SerialNo`,`b`.`ShopOrder` AS `ShopOrder`,`b`.`Series` AS `Series`,`b`.`Model` AS `Model`,`b`.`Options` AS `Options`,`b`.`StartTime` AS `StartTime`,`b`.`CurrentProtocol` AS `CurrentProtocol`,`b`.`Step` AS `Step`,`b`.`TotalSteps` AS `TotalSteps`,`b`.`StepStatus` AS `StepStatus`,`b`.`LastProtocol` AS `LastProtocol`,`b`.`LastProtocolTime` AS `LastProtocolTime`,`b`.`LastProtocolExpectedTime` AS `LastProtocolExpectedTime`,`b`.`LastProtocolDelta` AS `LastProtocolDelta`,`b`.`TotalExpectedTime` AS `TotalExpectedTime`,`b`.`ExpectedRemainingTime` AS `ExpectedRemainingTime`,`b`.`ActualRemainingTime` AS `ActualRemainingTime`,`b`.`ExpectedFinishDateTime` AS `ExpectedFinishDateTime`,`b`.`ActualFinishDateTime` AS `ActualFinishDateTime`,avg(`v`.`Startup_Act`) AS `Startup_Act_90DayAvg`,`v`.`Startup_Exp` AS `Startup_Exp`,avg(`v`.`IO_Tests_Act`) AS `IO_Tests_Act_90DayAvg`,`v`.`IO_Tests_Exp` AS `IO_Tests_Exp`,avg(`v`.`LowLevel_Rinse_Act`) AS `LowLevel_Rinse_Act_90DayAvg`,`v`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,avg(`v`.`Sample_Cond_AZ_1_Act`) AS `Sample_Cond_AZ_1_Act_90DayAvg`,`v`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,avg(`v`.`IC_TC_Cond_AZ_Act`) AS `IC_TC_Cond_AZ_Act_90DayAvg`,`v`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,avg(`v`.`LowLevel_SL1_Data_Act`) AS `LowLevel_SL1_Data_Act_90DayAvg`,`v`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,avg(`v`.`TOC_Single_Point_Cal_Act`) AS `TOC_Single_Point_Cal_Act_90DayAvg`,`v`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,avg(`v`.`TOC_Ver_Act`) AS `TOC_Ver_Act_90DayAvg`,`v`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,avg(`v`.`Cond_Single_Point_Cal_Act`) AS `Cond_Single_Point_Cal_Act_90DayAvg`,`v`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,avg(`v`.`Cond_Cal_Ver_Act`) AS `Cond_Cal_Ver_Act_90DayAvg`,`v`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,avg(`v`.`Specificity_Act`) AS `Specificity_Act_90DayAvg`,`v`.`Specificity_Exp` AS `Specificity_Exp`,avg(`v`.`Online_Precision_Act`) AS `Online_Precision_Act_90DayAvg`,`v`.`Online_Precision_Exp` AS `Online_Precision_Exp`,avg(`v`.`Sample_Cond_AZ_2_Act`) AS `Sample_Cond_AZ_2_Act_90DayAvg`,`v`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp` from (`bay_status` `b` join `test_time_90_day_view` `v` on(((`b`.`Series` = `v`.`Series`) and (`b`.`Model` = `v`.`Model`) and (`b`.`Options` = `v`.`Options`)))) group by `b`.`Series`,`b`.`Model`,`b`.`Options`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `bay_status_test_time_90_day_view2`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `bay_status_test_time_90_day_view2` AS select `b`.`RecNo` AS `RecNo`,`b`.`Station` AS `Station`,`b`.`Bay` AS `Bay`,`b`.`SerialNo` AS `SerialNo`,`b`.`ShopOrder` AS `ShopOrder`,`b`.`Series` AS `Series`,`b`.`Model` AS `Model`,`b`.`Options` AS `Options`,`b`.`StartTime` AS `StartTime`,`b`.`CurrentProtocol` AS `CurrentProtocol`,`b`.`Step` AS `Step`,`b`.`TotalSteps` AS `TotalSteps`,`b`.`StepStatus` AS `StepStatus`,`b`.`LastProtocol` AS `LastProtocol`,`b`.`LastProtocolTime` AS `LastProtocolTime`,`b`.`LastProtocolExpectedTime` AS `LastProtocolExpectedTime`,`b`.`LastProtocolDelta` AS `LastProtocolDelta`,`b`.`TotalExpectedTime` AS `TotalExpectedTime`,`b`.`ExpectedRemainingTime` AS `ExpectedRemainingTime`,`b`.`ActualRemainingTime` AS `ActualRemainingTime`,`b`.`ExpectedFinishDateTime` AS `ExpectedFinishDateTime`,`b`.`ActualFinishDateTime` AS `ActualFinishDateTime`,avg(`v`.`Startup_Act`) AS `Startup_Act_90DayAvg`,`v`.`Startup_Exp` AS `Startup_Exp`,avg(`v`.`IO_Tests_Act`) AS `IO_Tests_Act_90DayAvg`,`v`.`IO_Tests_Exp` AS `IO_Tests_Exp`,avg(`v`.`LowLevel_Rinse_Act`) AS `LowLevel_Rinse_Act_90DayAvg`,`v`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,avg(`v`.`Sample_Cond_AZ_1_Act`) AS `Sample_Cond_AZ_1_Act_90DayAvg`,`v`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,avg(`v`.`IC_TC_Cond_AZ_Act`) AS `IC_TC_Cond_AZ_Act_90DayAvg`,`v`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,avg(`v`.`LowLevel_SL1_Data_Act`) AS `LowLevel_SL1_Data_Act_90DayAvg`,`v`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,avg(`v`.`TOC_Single_Point_Cal_Act`) AS `TOC_Single_Point_Cal_Act_90DayAvg`,`v`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,avg(`v`.`TOC_Ver_Act`) AS `TOC_Ver_Act_90DayAvg`,`v`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,avg(`v`.`Cond_Single_Point_Cal_Act`) AS `Cond_Single_Point_Cal_Act_90DayAvg`,`v`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,avg(`v`.`Cond_Cal_Ver_Act`) AS `Cond_Cal_Ver_Act_90DayAvg`,`v`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,avg(`v`.`Specificity_Act`) AS `Specificity_Act_90DayAvg`,`v`.`Specificity_Exp` AS `Specificity_Exp`,avg(`v`.`Online_Precision_Act`) AS `Online_Precision_Act_90DayAvg`,`v`.`Online_Precision_Exp` AS `Online_Precision_Exp`,avg(`v`.`Sample_Cond_AZ_2_Act`) AS `Sample_Cond_AZ_2_Act_90DayAvg`,`v`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp` from (`bay_status` `b` join `test_time_90_day_view2` `v` on(((`b`.`Series` = `v`.`Series`) and (`b`.`Model` = `v`.`Model`) and (`b`.`Options` = `v`.`Options`)))) group by `b`.`Series`,`b`.`Model`,`b`.`Options`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `condaz1_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `condaz1_view` AS select `condaz`.`Recno` AS `RecNo`,`condaz`.`SerialNo` AS `SerialNo`,max(`condaz`.`Sample_Cond_AZ_1_Time`) AS `RecTime` from `condaz` group by `condaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `condaz2_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `condaz2_view` AS select `condaz`.`Recno` AS `RecNo`,`condaz`.`SerialNo` AS `SerialNo`,max(`condaz`.`IC_TC_Cond_AZ_Time`) AS `RecTime` from `condaz` group by `condaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `condaz3_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `condaz3_view` AS select `condaz`.`Recno` AS `RecNo`,`condaz`.`SerialNo` AS `SerialNo`,max(`condaz`.`LowLevel_SL1_Data_Time`) AS `RecTime` from `condaz` group by `condaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `condcalver1_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `condcalver1_view` AS select `condcalver`.`Recno` AS `RecNo`,`condcalver`.`SerialNo` AS `SerialNo`,max(`condcalver`.`Cond_SP_Cal_Time`) AS `RecTime` from `condcalver` group by `condcalver`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `condcalver2_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `condcalver2_view` AS select `condcalver`.`Recno` AS `RecNo`,`condcalver`.`SerialNo` AS `SerialNo`,max(`condcalver`.`Cond_Cal_Ver_Time`) AS `RecTime` from `condcalver` group by `condcalver`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `cond_cal_ver_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `cond_cal_ver_90_day_view` AS select `condcalver`.`Recno` AS `RecNo`,`condcalver`.`SerialNo` AS `SerialNo`,max(`condcalver`.`Cond_Cal_Ver_Time`) AS `RecTime` from `condcalver` where (`condcalver`.`Cond_Cal_Ver_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `condcalver`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `cond_single_point_cal_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `cond_single_point_cal_90_day_view` AS select `condcalver`.`Recno` AS `RecNo`,`condcalver`.`SerialNo` AS `SerialNo`,max(`condcalver`.`Cond_SP_Cal_Time`) AS `RecTime` from `condcalver` where (`condcalver`.`Cond_SP_Cal_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `condcalver`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `constants_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `constants_90_day_view` AS select `constants`.`RecNo` AS `RecNo`,`constants`.`SerialNo` AS `SerialNo`,max(`constants`.`Rectime`) AS `RecTime` from `constants` where (`constants`.`Rectime` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `constants`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `constants_all_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `constants_all_view` AS select `a`.`RecNo` AS `RecNo`,`a`.`SerialNo` AS `SerialNo`,`a`.`Rectime` AS `Rectime` from (`constants` `a` left join `constants` `b` on(((`a`.`SerialNo` = `b`.`SerialNo`) and (`a`.`RecNo` < `b`.`RecNo`)))) where (`b`.`RecNo` is null) order by `a`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `expected_testtime_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `expected_testtime_view` AS select `e`.`RecNo` AS `RecNo`,`e`.`Series` AS `Series`,`e`.`Model` AS `Model`,`e`.`Options` AS `Options`,`e`.`TotalTests` AS `TotalTests`,`e`.`Startup_Exp` AS `Startup_Exp`,`e`.`IO_Tests_Exp` AS `IO_Tests_Exp`,`e`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,`e`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,`e`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,`e`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,`e`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,`e`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,`e`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,`e`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,`e`.`Specificity_Exp` AS `Specificity_Exp`,`e`.`Online_Precision_Exp` AS `Online_Precision_Exp`,`e`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp`,`e`.`Constants_Exp` AS `Constants_Exp` from `expected_testtime` `e`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `fluidics_passing_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `fluidics_passing_view` AS select `fluidics`.`RecNo` AS `RecNo`,`fluidics`.`SerialNo` AS `SerialNo`,`fluidics`.`SeqNo` AS `SeqNo`,`fluidics`.`Bay` AS `Bay`,`fluidics`.`ICCell` AS `ICCell`,`fluidics`.`TCCell` AS `TCCell`,`fluidics`.`SCCell` AS `SCCell`,`fluidics`.`ConstantsChkd` AS `ConstantsChkd`,`fluidics`.`ConstantsPass` AS `ConstantsPass`,`fluidics`.`ICAvg` AS `ICAvg`,`fluidics`.`ICStd` AS `ICStd`,`fluidics`.`ICTempCorrAvg` AS `ICTempCorrAvg`,`fluidics`.`ICTempCorrStd` AS `ICTempCorrStd`,`fluidics`.`TCAvg` AS `TCAvg`,`fluidics`.`TCStd` AS `TCStd`,`fluidics`.`TCTempCorrAvg` AS `TCTempCorrAvg`,`fluidics`.`TCTempCorrStd` AS `TCTempCorrStd`,`fluidics`.`SCCondAvg` AS `SCCondAvg`,`fluidics`.`SCCondStd` AS `SCCondStd`,`fluidics`.`SCTempCorrAvg` AS `SCTempCorrAvg`,`fluidics`.`SCTempCorrStd` AS `SCTempCorrStd`,`fluidics`.`MFTempAvg` AS `MFTempAvg`,`fluidics`.`MFTempStd` AS `MFTempStd`,`fluidics`.`ICTempAvg` AS `ICTempAvg`,`fluidics`.`TCTempAvg` AS `TCTempAvg`,`fluidics`.`SCTempAvg` AS `SCTempAvg`,`fluidics`.`DeltaT` AS `DeltaT`,`fluidics`.`EmptyChkd` AS `EmptyChkd`,`fluidics`.`LvlSnsEmpty` AS `LvlSnsEmpty`,`fluidics`.`FullChkd` AS `FullChkd`,`fluidics`.`LvlSnsFull` AS `LvlSnsFull`,`fluidics`.`FlowRateChkd` AS `FlowRateChkd`,`fluidics`.`FlowRate` AS `FlowRate`,`fluidics`.`Pass` AS `Pass`,`fluidics`.`Readings` AS `Readings`,`fluidics`.`PrimeStart` AS `PrimeStart`,`fluidics`.`PrimeEnd` AS `PrimeEnd`,`fluidics`.`PrimeTime` AS `PrimeTime`,`fluidics`.`TotalPrimeMinutes` AS `TotalPrimeMinutes`,`fluidics`.`RinseStart` AS `RinseStart`,`fluidics`.`RinseEnd` AS `RinseEnd`,`fluidics`.`TotalRinseMinutes` AS `TotalRinseMinutes`,`fluidics`.`LastRecTm` AS `LastRecTm`,`fluidics`.`UpdateTime` AS `UpdateTime`,`fluidics`.`Operator` AS `Operator`,`fluidics`.`SWVersion` AS `SWVersion` from `fluidics` where ((`fluidics`.`ICAvg` < 12) and (`fluidics`.`TCAvg` < 12) and (`fluidics`.`ICStd` < 0.75) and (`fluidics`.`TCStd` < 0.75))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `fnlprep_all_desc_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `fnlprep_all_desc_view` AS select `fnlprep`.`Recno` AS `RecNo`,`fnlprep`.`SerialNo` AS `SerialNo`,`fnlprep`.`RecTime` AS `RecTime` from `fnlprep` order by `fnlprep`.`RecTime` desc
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `fnlprep_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `fnlprep_view` AS select `fnlprep`.`Recno` AS `RecNo`,`fnlprep`.`SerialNo` AS `SerialNo`,max(`fnlprep`.`RecTime`) AS `RecTime` from `fnlprep` group by `fnlprep`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `ic_tc_cond_az_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `ic_tc_cond_az_90_day_view` AS select `condaz`.`Recno` AS `RecNo`,`condaz`.`SerialNo` AS `SerialNo`,max(`condaz`.`IC_TC_Cond_AZ_Time`) AS `RecTime` from `condaz` where (`condaz`.`IC_TC_Cond_AZ_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `condaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `instlocn_all_desc_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `instlocn_all_desc_view` AS select `instlocn`.`Recno` AS `Recno`,`instlocn`.`SerialNo` AS `SerialNo`,`instlocn`.`Location` AS `Location`,`instlocn`.`Starttm` AS `Starttm`,`instlocn`.`RecTime` AS `RecTime` from `instlocn` order by `instlocn`.`RecTime` desc
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `instlocn_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `instlocn_view` AS select `l`.`Recno` AS `Recno`,`l`.`SerialNo` AS `SerialNo`,`p`.`PartNo` AS `PartNo`,`p`.`ShopOrder` AS `ShopOrder`,`p`.`Series` AS `Series`,`p`.`Model` AS `Model`,`p`.`Options` AS `Options`,`l`.`Location` AS `Location`,`l`.`Material` AS `Material`,`l`.`Starttm` AS `Starttm`,`l`.`RecTime` AS `RecTime` from (`planning_instruments_view` `p` join `instlocn` `l` on((`p`.`SerialNo` = `l`.`SerialNo`))) order by `l`.`Location`,`l`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `iotests_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `iotests_view` AS select `iotests`.`Recno` AS `RecNo`,`iotests`.`SerialNo` AS `SerialNo`,max(`iotests`.`RecTime`) AS `RecTime` from `iotests` group by `iotests`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `io_tests_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `io_tests_90_day_view` AS select `iotests`.`Recno` AS `RecNo`,`iotests`.`SerialNo` AS `SerialNo`,max(`iotests`.`RecTime`) AS `RecTime` from `iotests` where (`iotests`.`RecTime` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `iotests`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `llrinse_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `llrinse_view` AS select `llrinse`.`Recno` AS `RecNo`,`llrinse`.`SerialNo` AS `SerialNo`,max(`llrinse`.`RecTime`) AS `RecTime` from `llrinse` group by `llrinse`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `low_level_rinse_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `low_level_rinse_90_day_view` AS select `rnsdown`.`Recno` AS `RecNo`,`rnsdown`.`SerialNo` AS `SerialNo`,max(`rnsdown`.`RecTime`) AS `RecTime` from `rnsdown` where (`rnsdown`.`RecTime` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `rnsdown`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `low_level_sl1_data_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `low_level_sl1_data_90_day_view` AS select `condaz`.`Recno` AS `RecNo`,`condaz`.`SerialNo` AS `SerialNo`,max(`condaz`.`LowLevel_SL1_Data_Time`) AS `RecTime` from `condaz` where (`condaz`.`LowLevel_SL1_Data_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `condaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `online_precision_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `online_precision_90_day_view` AS select `tocaz`.`Recno` AS `RecNo`,`tocaz`.`SerialNo` AS `SerialNo`,max(`tocaz`.`Online_Precision_Time`) AS `RecTime` from `tocaz` where (`tocaz`.`Online_Precision_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `tocaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `planning_instruments_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `planning_instruments_view` AS select `p`.`SerialNo` AS `SerialNo`,`p`.`PartNo` AS `PartNo`,`p`.`ShopOrder` AS `ShopOrder`,`planning`.`GetM500SeriesName`(`p`.`PartNo`) AS `Series`,`planning`.`GetM500ModelName`(`p`.`PartNo`) AS `Model`,convert('NONE' using latin1) AS `Options` from `planning`.`m500` `p` where (`p`.`PartNo` like '%AQC%') order by `p`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `prd_goods_issue_bldr_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `prd_goods_issue_bldr_view` AS select `b`.`SerialNo` AS `SerialNo`,`b`.`Location` AS `Location`,`b`.`DeliveryNo` AS `DeliveryNo`,`b`.`LineNo` AS `LineNo`,`b`.`Material` AS `Material`,`b`.`GoodsPickDate` AS `GoodsPickDate`,`b`.`GoodsIssueStatus` AS `GoodsIssueStatus`,`b`.`SalesOrg` AS `SalesOrg`,`v`.`SerialNo` AS `VendorSerialNo`,`v`.`Location` AS `VendorLocation`,`v`.`DeliveryNo` AS `VendorDeliveryNo`,`v`.`LineNo` AS `VendorLineNo`,`v`.`Material` AS `VendorMaterial`,`v`.`GoodsPickDate` AS `VendorGoodsPickDate`,`v`.`GoodsIssueStatus` AS `VendorGoodsIssueStatus`,`v`.`SalesOrg` AS `VendorSalesOrg` from (`instlocn` `b` left join `instlocn` `v` on(((`b`.`SerialNo` = `v`.`SerialNo`) and (`b`.`SalesOrg` <> `v`.`SalesOrg`)))) where ((`b`.`Location` = 'PGI') and (`b`.`Starttm` >= '2021-01-01')) group by `b`.`SerialNo` having (count(`b`.`SerialNo`) = 1) order by `b`.`GoodsPickDate`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `prd_goods_issue_sales_org_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `prd_goods_issue_sales_org_view` AS select `b`.`SerialNo` AS `SerialNo`,`b`.`Location` AS `Location`,`b`.`DeliveryNo` AS `DeliveryNo`,`b`.`LineNo` AS `LineNo`,`b`.`Material` AS `Material`,`b`.`GoodsPickDate` AS `GoodsPickDate`,`b`.`GoodsIssueStatus` AS `GoodsIssueStatus`,`b`.`SalesOrg` AS `SalesOrg`,`v`.`SerialNo` AS `VendorSerialNo`,`v`.`Location` AS `VendorLocation`,`v`.`DeliveryNo` AS `VendorDeliveryNo`,`b`.`LineNo` AS `VendorLineNo`,`v`.`Material` AS `VendorMaterial`,`v`.`GoodsPickDate` AS `VendorGoodsPickDate`,`v`.`GoodsIssueStatus` AS `VendorGoodsIssueStatus`,`v`.`SalesOrg` AS `VendorSalesOrg` from (`instlocn` `v` left join `instlocn` `b` on(((`b`.`SerialNo` = `v`.`SerialNo`) and (`b`.`SalesOrg` <> `v`.`SalesOrg`)))) where ((`b`.`Location` = 'PGI') and (`b`.`SalesOrg` in ('B494','B370')) and (`b`.`Starttm` >= '2021-01-01')) group by `b`.`SerialNo` order by `b`.`GoodsPickDate`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `prd_goods_issue_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `prd_goods_issue_view` AS select `prd_goods_issue_bldr_view`.`SerialNo` AS `SerialNo`,`prd_goods_issue_bldr_view`.`Location` AS `Location`,`prd_goods_issue_bldr_view`.`DeliveryNo` AS `DeliveryNo`,`prd_goods_issue_bldr_view`.`LineNo` AS `LineNo`,`prd_goods_issue_bldr_view`.`Material` AS `Material`,`prd_goods_issue_bldr_view`.`GoodsPickDate` AS `GoodsPickDate`,`prd_goods_issue_bldr_view`.`GoodsIssueStatus` AS `GoodsIssueStatus`,`prd_goods_issue_bldr_view`.`SalesOrg` AS `SalesOrg`,`prd_goods_issue_bldr_view`.`VendorSerialNo` AS `VendorSerialNo`,`prd_goods_issue_bldr_view`.`VendorLocation` AS `VendorLocation`,`prd_goods_issue_bldr_view`.`VendorDeliveryNo` AS `VendorDeliveryNo`,`prd_goods_issue_bldr_view`.`VendorLineNo` AS `VendorLineNo`,`prd_goods_issue_bldr_view`.`VendorMaterial` AS `VendorMaterial`,`prd_goods_issue_bldr_view`.`VendorGoodsPickDate` AS `VendorGoodsPickDate`,`prd_goods_issue_bldr_view`.`VendorGoodsIssueStatus` AS `VendorGoodsIssueStatus`,`prd_goods_issue_bldr_view`.`VendorSalesOrg` AS `VendorSalesOrg` from `prd_goods_issue_bldr_view` union all select `prd_goods_issue_sales_org_view`.`SerialNo` AS `SerialNo`,`prd_goods_issue_sales_org_view`.`Location` AS `Location`,`prd_goods_issue_sales_org_view`.`DeliveryNo` AS `DeliveryNo`,`prd_goods_issue_sales_org_view`.`LineNo` AS `LineNo`,`prd_goods_issue_sales_org_view`.`Material` AS `Material`,`prd_goods_issue_sales_org_view`.`GoodsPickDate` AS `GoodsPickDate`,`prd_goods_issue_sales_org_view`.`GoodsIssueStatus` AS `GoodsIssueStatus`,`prd_goods_issue_sales_org_view`.`SalesOrg` AS `SalesOrg`,`prd_goods_issue_sales_org_view`.`VendorSerialNo` AS `VendorSerialNo`,`prd_goods_issue_sales_org_view`.`VendorLocation` AS `VendorLocation`,`prd_goods_issue_sales_org_view`.`VendorDeliveryNo` AS `VendorDeliveryNo`,`prd_goods_issue_sales_org_view`.`VendorLineNo` AS `VendorLineNo`,`prd_goods_issue_sales_org_view`.`VendorMaterial` AS `VendorMaterial`,`prd_goods_issue_sales_org_view`.`VendorGoodsPickDate` AS `VendorGoodsPickDate`,`prd_goods_issue_sales_org_view`.`VendorGoodsIssueStatus` AS `VendorGoodsIssueStatus`,`prd_goods_issue_sales_org_view`.`VendorSalesOrg` AS `VendorSalesOrg` from `prd_goods_issue_sales_org_view`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `protocol_expected_testtime_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `protocol_expected_testtime_view` AS select `e`.`RecNo` AS `RecNo`,`e`.`Series` AS `Series`,`e`.`Model` AS `Model`,`e`.`Options` AS `Options`,`e`.`TotalTests` AS `TotalTests`,`e`.`Startup_Exp` AS `Startup_Exp`,`e`.`IO_Tests_Exp` AS `IO_Tests_Exp`,`e`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,`e`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,`e`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,`e`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,`e`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,`e`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,`e`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,`e`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,`e`.`Specificity_Exp` AS `Specificity_Exp`,`e`.`Online_Precision_Exp` AS `Online_Precision_Exp`,`e`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp`,`e`.`Constants_Exp` AS `Constants_Exp` from `protocol_expected_testtime` `e`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `protocol_testtime_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `protocol_testtime_view` AS select `startup`.`RecNo` AS `RecNo`,`startup`.`SerialNo` AS `SerialNo`,`startup`.`ShopOrder` AS `ShopOrder`,`startup`.`Series` AS `Series`,`startup`.`Model` AS `Model`,`startup`.`Options` AS `Options`,`startup`.`RecTime` AS `StartTime`,`tocaz3`.`RecTime` AS `FinishTime`,`bay_status`.`CurrentProtocol` AS `CurrentProtocol`,'Startup' AS `Startup`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`statshv`.`GetCurrentProtocolTime`(`startup`.`RecTime`,`bay_status`.`CurrentProtocol`,'Startup')) AS `Startup_Act`,`expected`.`Startup_Exp` AS `Startup_Exp`,'IO Tests' AS `IO_Tests`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`iotests`.`RecTime`,`bay_status`.`CurrentProtocol`,'IO Tests')) AS `IO_Tests_Act`,`expected`.`IO_Tests_Exp` AS `IO_Tests_Exp`,'Low Level Rinse Down' AS `Low_Level_Rinse_Down`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`rnsdown`.`RecTime`,`bay_status`.`CurrentProtocol`,'Low Level Rinse')) AS `LowLevel_Rinse_Act`,`expected`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,'Sample Cond AZ 1' AS `Sample_Cond_AZ_1`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`condaz1`.`RecTime`,`bay_status`.`CurrentProtocol`,'Sample Conductivity AutoZero 1')) AS `Sample_Cond_AZ_1_Act`,`expected`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,'IC TC Cond AZ' AS `IC_TC_Cond_AZ`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`condaz2`.`RecTime`,`bay_status`.`CurrentProtocol`,'IC/TC Conductivity AutoZero')) AS `IC_TC_Cond_AZ_Act`,`expected`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,'LowLevel SL1 Data' AS `LowLevel_SL1_Data`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`condaz3`.`RecTime`,`bay_status`.`CurrentProtocol`,'Low Level SL1 Data')) AS `LowLevel_SL1_Data_Act`,`expected`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,'TOC Single Point Cal' AS `TOC_Single_Point_Cal`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`spcal1`.`RecTime`,`bay_status`.`CurrentProtocol`,'TOC Single Point Calibration')) AS `TOC_Single_Point_Cal_Act`,`expected`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,'TOC Ver' AS `TOC_Ver`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`spcal2`.`RecTime`,`bay_status`.`CurrentProtocol`,'TOC_Verification')) AS `TOC_Ver_Act`,`expected`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,'Cond Single Point Cal' AS `Cond_Single_Point_Cal`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`condcalver1`.`RecTime`,`bay_status`.`CurrentProtocol`,'Conductivity Single Point Calibration')) AS `Cond_Single_Point_Cal_Act`,`expected`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,'Cond Cal Ver' AS `Cond_Cal_Ver`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`condcalver2`.`RecTime`,`bay_status`.`CurrentProtocol`,'Conductivity Calibration Verification')) AS `Cond_Cal_Ver_Act`,`expected`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,'Specificity' AS `Specificity`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`tocaz1`.`RecTime`,`bay_status`.`CurrentProtocol`,'Specificity')) AS `Specificity_Act`,`expected`.`Specificity_Exp` AS `Specificity_Exp`,'Online Precision' AS `Online_Precision`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`tocaz2`.`RecTime`,`bay_status`.`CurrentProtocol`,'Online Precision')) AS `Online_Precision_Act`,`expected`.`Online_Precision_Exp` AS `Online_Precision_Exp`,'Sample Cond AZ 2' AS `Sample_Cond_AZ_2`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`tocaz3`.`RecTime`,`bay_status`.`CurrentProtocol`,'Sample Conductivity AutoZero 2')) AS `Sample_Cond_AZ_2_Act`,`expected`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp`,timestampdiff(MINUTE,`startup`.`RecTime`,`statshv`.`GetCurrentProtocolTime`(`constants`.`Rectime`,`bay_status`.`CurrentProtocol`,'Constants')) AS `Constants_Act`,`expected`.`Constants_Exp` AS `Constants_Exp` from (((((((((((((((`startup_view` `startup` left join `iotests_view` `iotests` on((`iotests`.`SerialNo` = `startup`.`SerialNo`))) left join `rnsdown_view` `rnsdown` on((`rnsdown`.`SerialNo` = `startup`.`SerialNo`))) left join `condaz1_view` `condaz1` on((`condaz1`.`SerialNo` = `startup`.`SerialNo`))) left join `condaz2_view` `condaz2` on((`condaz2`.`SerialNo` = `startup`.`SerialNo`))) left join `condaz3_view` `condaz3` on((`condaz3`.`SerialNo` = `startup`.`SerialNo`))) left join `spcal1_view` `spcal1` on((`spcal1`.`SerialNo` = `startup`.`SerialNo`))) left join `spcal2_view` `spcal2` on((`spcal2`.`SerialNo` = `startup`.`SerialNo`))) left join `condcalver1_view` `condcalver1` on((`condcalver1`.`SerialNo` = `startup`.`SerialNo`))) left join `condcalver2_view` `condcalver2` on((`condcalver2`.`SerialNo` = `startup`.`SerialNo`))) left join `tocaz1_view` `tocaz1` on((`tocaz1`.`SerialNo` = `startup`.`SerialNo`))) left join `tocaz2_view` `tocaz2` on((`tocaz2`.`SerialNo` = `startup`.`SerialNo`))) left join `tocaz3_view` `tocaz3` on((`tocaz3`.`SerialNo` = `startup`.`SerialNo`))) left join `constants_all_view` `constants` on((`constants`.`SerialNo` = `startup`.`SerialNo`))) left join `workcell_bay_status_expected_testtime_view` `bay_status` on((`bay_status`.`SerialNo` = `startup`.`SerialNo`))) left join `protocol_expected_testtime_view` `expected` on(((`startup`.`Series` = `expected`.`Series`) and (`startup`.`Model` = `expected`.`Model`))))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `rnsdown_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `rnsdown_view` AS select `rnsdown`.`Recno` AS `RecNo`,`rnsdown`.`SerialNo` AS `SerialNo`,max(`rnsdown`.`RecTime`) AS `RecTime` from `rnsdown` group by `rnsdown`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `sample_cond_az_1_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `sample_cond_az_1_90_day_view` AS select `condaz`.`Recno` AS `RecNo`,`condaz`.`SerialNo` AS `SerialNo`,max(`condaz`.`Sample_Cond_AZ_1_Time`) AS `RecTime` from `condaz` where (`condaz`.`Sample_Cond_AZ_1_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `condaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `sample_cond_az_2_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `sample_cond_az_2_90_day_view` AS select `tocaz`.`Recno` AS `RecNo`,`tocaz`.`SerialNo` AS `SerialNo`,max(`tocaz`.`Sample_Cond_AZ_2_Time`) AS `RecTime` from `tocaz` where (`tocaz`.`Sample_Cond_AZ_2_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `tocaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `spcal1_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `spcal1_view` AS select `spcal`.`Recno` AS `RecNo`,`spcal`.`SerialNo` AS `SerialNo`,max(`spcal`.`TOC_SP_Cal_Time`) AS `RecTime` from `spcal` group by `spcal`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `spcal2_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `spcal2_view` AS select `spcal`.`Recno` AS `RecNo`,`spcal`.`SerialNo` AS `SerialNo`,max(`spcal`.`TOC_Ver_Time`) AS `RecTime` from `spcal` group by `spcal`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `specificity_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `specificity_90_day_view` AS select `tocaz`.`Recno` AS `RecNo`,`tocaz`.`SerialNo` AS `SerialNo`,max(`tocaz`.`Specificity_Time`) AS `RecTime` from `tocaz` where (`tocaz`.`Specificity_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `tocaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `startup_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `startup_90_day_view` AS select `startup`.`RecNo` AS `RecNo`,`startup`.`SerialNo` AS `SerialNo`,`startup`.`IPAddr` AS `IPAddr`,`startup`.`ShopOrder` AS `ShopOrder`,`startup`.`AQCNo` AS `AQCNo`,`statshv`.`GetSeriesName`(`startup`.`AQCNo`) AS `Series`,`statshv`.`GetModelName`(`startup`.`AQCNo`) AS `Model`,`startup`.`Options` AS `Options`,max(`startup`.`Rectime`) AS `RecTime`,`startup`.`Station` AS `Station`,`startup`.`Bay` AS `Bay`,`startup`.`WizardStartTime` AS `WizardStartTime` from `startup` where (`startup`.`Rectime` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `startup`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `startup_all_desc_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `startup_all_desc_view` AS select `startup`.`RecNo` AS `RecNo`,`startup`.`SerialNo` AS `SerialNo`,`startup`.`AQCNo` AS `AQCno`,`startup`.`RLE` AS `RLE`,`startup`.`IPAddr` AS `IPAddr`,`startup`.`ICCell` AS `ICCell`,`startup`.`TCCell` AS `TCCell`,`startup`.`C3Cell` AS `C3Cell`,`startup`.`SIOSOrder` AS `SIOSOrder`,`startup`.`ShopOrder` AS `ShopOrder`,`startup`.`SmplCondres` AS `SmplCondres`,`startup`.`ThermsChkd` AS `ThermsChkd`,`startup`.`SysChkd` AS `SysChkd`,`startup`.`GainsChkd` AS `GainsChkd`,`startup`.`TdsChkd` AS `TdsChkd`,`startup`.`Operator` AS `Operator`,`startup`.`Mods` AS `Mods`,`startup`.`CalDone` AS `CalDone`,`startup`.`LastProtocol` AS `LastProtocol`,`startup`.`Station` AS `Station`,`startup`.`Bay` AS `Bay`,`startup`.`Series` AS `Series`,`startup`.`Model` AS `Model`,`startup`.`Options` AS `Options`,max(`startup`.`Rectime`) AS `RecTime` from `startup` group by `startup`.`SerialNo` order by `startup`.`Rectime` desc
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `startup_all_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `startup_all_view` AS select `startup`.`RecNo` AS `RecNo`,`startup`.`SerialNo` AS `SerialNo`,`startup`.`AQCNo` AS `AQCno`,`startup`.`RLE` AS `RLE`,`startup`.`IPAddr` AS `IPAddr`,`startup`.`ICCell` AS `ICCell`,`startup`.`TCCell` AS `TCCell`,`startup`.`C3Cell` AS `C3Cell`,`startup`.`SIOSOrder` AS `SIOSOrder`,`startup`.`ShopOrder` AS `ShopOrder`,`startup`.`SmplCondres` AS `SmplCondres`,`startup`.`ThermsChkd` AS `ThermsChkd`,`startup`.`SysChkd` AS `SysChkd`,`startup`.`GainsChkd` AS `GainsChkd`,`startup`.`TdsChkd` AS `TdsChkd`,`startup`.`Operator` AS `Operator`,`startup`.`Mods` AS `Mods`,`startup`.`CalDone` AS `CalDone`,`startup`.`LastProtocol` AS `LastProtocol`,`startup`.`Station` AS `Station`,`startup`.`Bay` AS `Bay`,`startup`.`Series` AS `Series`,`startup`.`Model` AS `Model`,`startup`.`Options` AS `Options`,`startup`.`Rectime` AS `RecTime` from `startup` group by `startup`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `startup_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `startup_view` AS select `startup`.`RecNo` AS `RecNo`,`startup`.`SerialNo` AS `SerialNo`,`startup`.`AQCNo` AS `AQCNo`,`startup`.`Options` AS `Options`,`planning`.`GetM500SeriesName`(`startup`.`AQCNo`) AS `Series`,`planning`.`GetM500ModelName`(`startup`.`AQCNo`) AS `Model`,`startup`.`RLE` AS `RLE`,`startup`.`FWrev` AS `FWrev`,`startup`.`IPAddr` AS `IpAddr`,`startup`.`ICCell` AS `ICCell`,`startup`.`TCCell` AS `TCCell`,`startup`.`C3Cell` AS `C3Cell`,`startup`.`ShopOrder` AS `ShopOrder`,`startup`.`SIOSOrder` AS `SIOSOrder`,`startup`.`SmplCondres` AS `SmplCondres`,`startup`.`ThermsChkd` AS `ThermsChkd`,`startup`.`SysChkd` AS `SysChkd`,`startup`.`GainsChkd` AS `GainsChkd`,`startup`.`TdsChkd` AS `TdsChkd`,`startup`.`Rectime` AS `RecTime`,`startup`.`Operator` AS `Operator`,`startup`.`Mods` AS `Mods`,`startup`.`CalDone` AS `CalDone`,`startup`.`LastProtocol` AS `LastProtocol`,`startup`.`Station` AS `Station`,`startup`.`Bay` AS `Bay`,`startup`.`Site` AS `Site`,`startup`.`UpdateTime` AS `UpdateTime`,`startup`.`SWversion` AS `SWversion`,`startup`.`SNChecked` AS `SNChecked`,`startup`.`WizardStartTime` AS `WizardStartTime` from `startup` group by `startup`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `table_resolution2_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `table_resolution2_view` AS select `r`.`RecordNo` AS `RecordNo`,`r`.`SerialNo` AS `SerialNo`,`r`.`Operator` AS `Operator`,`r`.`PageName` AS `PageName`,`r`.`Symptom` AS `Symptom`,`r`.`Cause` AS `Cause`,`r`.`Instruction_Level_1` AS `Instruction_Level_1`,`r`.`Instruction_Level_2` AS `Instruction_Level_2`,`r`.`Resolution` AS `Resolution`,`r`.`CaseNo` AS `CaseNo`,`r`.`UpdateTime` AS `UpdateTime`,`r`.`Symptom_copy` AS `Symptom_copy`,`r`.`SerialNo_copy` AS `SerialNo_copy`,`r`.`PageName_copy` AS `PageName_copy`,`r`.`Operator_copy` AS `Operator_copy`,`r`.`MFE_Level_Used` AS `MFE_Level_Used`,`r`.`Instruction_Level_Technology` AS `Technology_Instructions`,`s`.`Series` AS `Series`,`s`.`Model` AS `Model`,`s`.`Options` AS `Options` from (`table_resolution2` `r` left join `startup` `s` on((`r`.`SerialNo_copy` = `s`.`SerialNo`)))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `test_time_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `test_time_90_day_view` AS select `startup`.`RecNo` AS `RecNo`,`startup`.`SerialNo` AS `SerialNo`,`startup`.`ShopOrder` AS `ShopOrder`,`startup`.`Series` AS `Series`,`startup`.`Model` AS `Model`,`startup`.`Options` AS `Options`,`startup`.`WizardStartTime` AS `WizardStartTime`,`startup`.`RecTime` AS `StartTime`,`tocaz`.`RecTime` AS `FinishTime`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`startup`.`RecTime`) AS `Startup_Act`,`expected`.`Startup_Exp` AS `Startup_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`iotests`.`RecTime`) AS `IO_Tests_Act`,`expected`.`IO_Tests_Exp` AS `IO_Tests_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`rnsdown`.`RecTime`) AS `LowLevel_Rinse_Act`,`expected`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`condaz`.`RecTime`) AS `Sample_Cond_AZ_1_Act`,`expected`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`ictc_condaz`.`RecTime`) AS `IC_TC_Cond_AZ_Act`,`expected`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`sl1data`.`RecTime`) AS `LowLevel_SL1_Data_Act`,`expected`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`spcal`.`RecTime`) AS `TOC_Single_Point_Cal_Act`,`expected`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`spver`.`RecTime`) AS `TOC_Ver_Act`,`expected`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`condcal`.`RecTime`) AS `Cond_Single_Point_Cal_Act`,`expected`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`condver`.`RecTime`) AS `Cond_Cal_Ver_Act`,`expected`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`specificity`.`RecTime`) AS `Specificity_Act`,`expected`.`Specificity_Exp` AS `Specificity_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`precision`.`RecTime`) AS `Online_Precision_Act`,`expected`.`Online_Precision_Exp` AS `Online_Precision_Exp`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`tocaz`.`RecTime`) AS `Sample_Cond_AZ_2_Act`,`expected`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp` from (((((((((((((`startup_90_day_view` `startup` left join `io_tests_90_day_view` `iotests` on((`iotests`.`SerialNo` = `startup`.`SerialNo`))) left join `low_level_rinse_90_day_view` `rnsdown` on((`rnsdown`.`SerialNo` = `startup`.`SerialNo`))) left join `sample_cond_az_1_90_day_view` `condaz` on((`condaz`.`SerialNo` = `startup`.`SerialNo`))) left join `ic_tc_cond_az_90_day_view` `ictc_condaz` on((`ictc_condaz`.`SerialNo` = `startup`.`SerialNo`))) left join `low_level_sl1_data_90_day_view` `sl1data` on((`sl1data`.`SerialNo` = `startup`.`SerialNo`))) left join `toc_single_point_cal_90_day_view` `spcal` on((`spcal`.`SerialNo` = `startup`.`SerialNo`))) left join `toc_ver_90_day_view` `spver` on((`spver`.`SerialNo` = `startup`.`SerialNo`))) left join `cond_single_point_cal_90_day_view` `condcal` on((`condcal`.`SerialNo` = `startup`.`SerialNo`))) left join `cond_cal_ver_90_day_view` `condver` on((`condver`.`SerialNo` = `startup`.`SerialNo`))) left join `specificity_90_day_view` `specificity` on((`specificity`.`SerialNo` = `startup`.`SerialNo`))) left join `online_precision_90_day_view` `precision` on((`precision`.`SerialNo` = `startup`.`SerialNo`))) left join `sample_cond_az_2_90_day_view` `tocaz` on((`tocaz`.`SerialNo` = `startup`.`SerialNo`))) left join `expected_testtime_view` `expected` on(((`startup`.`Series` = `expected`.`Series`) and (`startup`.`Model` = `expected`.`Model`) and (`startup`.`Options` = `expected`.`Options`))))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `test_time_90_day_view2`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `test_time_90_day_view2` AS select `startup`.`RecNo` AS `RecNo`,`startup`.`SerialNo` AS `SerialNo`,`startup`.`ShopOrder` AS `ShopOrder`,`startup`.`Series` AS `Series`,`startup`.`Model` AS `Model`,`startup`.`Options` AS `Options`,`startup`.`WizardStartTime` AS `WizardStartTime`,`startup`.`RecTime` AS `StartTime`,`tocaz`.`RecTime` AS `FinishTime`,timestampdiff(MINUTE,`startup`.`WizardStartTime`,`startup`.`RecTime`) AS `Startup_Act`,`expected`.`Startup_Exp` AS `Startup_Exp`,timestampdiff(MINUTE,`startup`.`RecTime`,`iotests`.`RecTime`) AS `IO_Tests_Act`,`expected`.`IO_Tests_Exp` AS `IO_Tests_Exp`,timestampdiff(MINUTE,`iotests`.`RecTime`,`rnsdown`.`RecTime`) AS `LowLevel_Rinse_Act`,`expected`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,`statshv`.`GetActual_Protocol_Series_Time`(`startup`.`Series`,NULL,`rnsdown`.`RecTime`,`condaz`.`RecTime`) AS `Sample_Cond_AZ_1_Act`,`expected`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,`statshv`.`GetActual_Protocol_Series_Time`(`startup`.`Series`,`rnsdown`.`RecTime`,`condaz`.`RecTime`,`ictc_condaz`.`RecTime`) AS `IC_TC_Cond_AZ_Act`,`expected`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,timestampdiff(MINUTE,`ictc_condaz`.`RecTime`,`sl1data`.`RecTime`) AS `LowLevel_SL1_Data_Act`,`expected`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,timestampdiff(MINUTE,`sl1data`.`RecTime`,`spcal`.`RecTime`) AS `TOC_Single_Point_Cal_Act`,`expected`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,timestampdiff(MINUTE,`spcal`.`RecTime`,`spver`.`RecTime`) AS `TOC_Ver_Act`,`expected`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,`statshv`.`GetActual_Protocol_Series_Time`(`startup`.`Series`,NULL,`spver`.`RecTime`,`condcal`.`RecTime`) AS `Cond_Single_Point_Cal_Act`,`expected`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,`statshv`.`GetActual_Protocol_Series_Time`(`startup`.`Series`,NULL,`condcal`.`RecTime`,`condver`.`RecTime`) AS `Cond_Cal_Ver_Act`,`expected`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,`statshv`.`GetActual_Protocol_Series_Time`(`startup`.`Series`,NULL,`condver`.`RecTime`,`specificity`.`RecTime`) AS `Specificity_Act`,`expected`.`Specificity_Exp` AS `Specificity_Exp`,`statshv`.`GetActual_Protocol_Series_Precision_Time`(`startup`.`Series`,`startup`.`Model`,`spver`.`RecTime`,`condver`.`RecTime`,`specificity`.`RecTime`,`precision`.`RecTime`) AS `Online_Precision_Act`,`expected`.`Online_Precision_Exp` AS `Online_Precision_Exp`,timestampdiff(MINUTE,`precision`.`RecTime`,`tocaz`.`RecTime`) AS `Sample_Cond_AZ_2_Act`,`expected`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp` from (((((((((((((`startup_90_day_view` `startup` left join `io_tests_90_day_view` `iotests` on((`iotests`.`SerialNo` = `startup`.`SerialNo`))) left join `low_level_rinse_90_day_view` `rnsdown` on((`rnsdown`.`SerialNo` = `startup`.`SerialNo`))) left join `sample_cond_az_1_90_day_view` `condaz` on((`condaz`.`SerialNo` = `startup`.`SerialNo`))) left join `ic_tc_cond_az_90_day_view` `ictc_condaz` on((`ictc_condaz`.`SerialNo` = `startup`.`SerialNo`))) left join `low_level_sl1_data_90_day_view` `sl1data` on((`sl1data`.`SerialNo` = `startup`.`SerialNo`))) left join `toc_single_point_cal_90_day_view` `spcal` on((`spcal`.`SerialNo` = `startup`.`SerialNo`))) left join `toc_ver_90_day_view` `spver` on((`spver`.`SerialNo` = `startup`.`SerialNo`))) left join `cond_single_point_cal_90_day_view` `condcal` on((`condcal`.`SerialNo` = `startup`.`SerialNo`))) left join `cond_cal_ver_90_day_view` `condver` on((`condver`.`SerialNo` = `startup`.`SerialNo`))) left join `specificity_90_day_view` `specificity` on((`specificity`.`SerialNo` = `startup`.`SerialNo`))) left join `online_precision_90_day_view` `precision` on((`precision`.`SerialNo` = `startup`.`SerialNo`))) left join `sample_cond_az_2_90_day_view` `tocaz` on((`tocaz`.`SerialNo` = `startup`.`SerialNo`))) left join `protocol_expected_testtime2` `expected` on(((`startup`.`Series` = `expected`.`Series`) and (`startup`.`Model` = `expected`.`Model`) and (`startup`.`Options` = `expected`.`Options`))))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `test_time_expected_test_time_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `test_time_expected_test_time_view` AS select `s`.`RecNo` AS `RecNo`,`s`.`SerialNo` AS `SerialNo`,`s`.`ShopOrder` AS `ShopOrder`,`s`.`Series` AS `Series`,`s`.`Model` AS `Model`,`s`.`Options` AS `Options`,`s`.`RecTime` AS `RecTime`,`f`.`RecTime` AS `RecTime (fnlprep)`,timestampdiff(MINUTE,`s`.`RecTime`,`f`.`RecTime`) AS `TestTime`,`e`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp` from ((`startup_all_desc_view` `s` join `fnlprep_all_desc_view` `f` on((`s`.`SerialNo` = `f`.`SerialNo`))) left join `expected_testtime_view` `e` on(((`s`.`Series` = `e`.`Series`) and (`s`.`Model` = `e`.`Model`) and (`s`.`Options` = `e`.`Options`))))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `test_time_expected_test_time_view_2`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `test_time_expected_test_time_view_2` AS select `s`.`RecNo` AS `RecNo`,`s`.`SerialNo` AS `SerialNo`,`s`.`ShopOrder` AS `ShopOrder`,`s`.`Series` AS `Series`,`s`.`Model` AS `Model`,`s`.`Options` AS `Options`,`s`.`RecTime` AS `RecTime`,`f`.`Rectime` AS `RecTime (fnlprep)`,date_format(`f`.`Rectime`,'%Y%m') AS `YearMonth`,date_format(`f`.`Rectime`,'%Y-%m-01') AS `YearMonthDay`,timestampdiff(MINUTE,`s`.`RecTime`,`f`.`Rectime`) AS `TestTime`,`e`.`Constants_Exp` AS `Constants_Exp` from ((`startup_all_view` `s` join `constants_all_view` `f` on((`s`.`SerialNo` = `f`.`SerialNo`))) left join `expected_testtime_view` `e` on(((`s`.`Series` = `e`.`Series`) and (`s`.`Model` = `e`.`Model`) and (`s`.`Options` = `e`.`Options`))))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `tocaz1_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `tocaz1_view` AS select `tocaz`.`Recno` AS `RecNo`,`tocaz`.`SerialNo` AS `SerialNo`,`statshv`.`CatchZeroTimestamps`(max(`tocaz`.`Specificity_Time`)) AS `RecTime` from `tocaz` group by `tocaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `tocaz2_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `tocaz2_view` AS select `tocaz`.`Recno` AS `RecNo`,`tocaz`.`SerialNo` AS `SerialNo`,`statshv`.`CatchZeroTimestamps`(max(`tocaz`.`Online_Precision_Time`)) AS `RecTime` from `tocaz` group by `tocaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `tocaz3_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `tocaz3_view` AS select `tocaz`.`Recno` AS `RecNo`,`tocaz`.`SerialNo` AS `SerialNo`,max(`tocaz`.`Sample_Cond_AZ_2_Time`) AS `RecTime` from `tocaz` group by `tocaz`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `toc_single_point_cal_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `toc_single_point_cal_90_day_view` AS select `spcal`.`Recno` AS `RecNo`,`spcal`.`SerialNo` AS `SerialNo`,max(`spcal`.`TOC_SP_Cal_Time`) AS `RecTime` from `spcal` where (`spcal`.`TOC_SP_Cal_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `spcal`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `toc_ver_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `toc_ver_90_day_view` AS select `spcal`.`Recno` AS `RecNo`,`spcal`.`SerialNo` AS `SerialNo`,max(`spcal`.`TOC_Ver_Time`) AS `RecTime` from `spcal` where (`spcal`.`TOC_Ver_Time` >= (date_format(curdate(),'%y-%m-01') - interval 2 month)) group by `spcal`.`SerialNo`
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `troubleshoot_all_levels`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `troubleshoot_all_levels` AS select `table_resolution2_view`.`SerialNo` AS `SerialNo`,`table_resolution2_view`.`PageName` AS `Protocol`,`table_resolution2_view`.`Symptom` AS `Symptom`,`table_resolution2_view`.`Cause` AS `Cause`,`table_resolution2_view`.`UpdateTime` AS `RecTime`,`s`.`Series` AS `Series`,`s`.`Model` AS `Model`,`s`.`Options` AS `Options` from (`table_resolution2_view` left join `startup` `s` on((`table_resolution2_view`.`SerialNo_copy` = `s`.`SerialNo`))) where (`table_resolution2_view`.`MFE_Level_Used` = 'TRUE')
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `troubleshoot_final_resolutions`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `troubleshoot_final_resolutions` AS select `table_resolution2_view`.`SerialNo` AS `SerialNo`,`table_resolution2_view`.`PageName` AS `Protocol`,`table_resolution2_view`.`Symptom` AS `Symptom`,`table_resolution2_view`.`Cause` AS `Cause`,`table_resolution2_view`.`Resolution` AS `Resolution`,`table_resolution2_view`.`Series` AS `Series`,`table_resolution2_view`.`Model` AS `Model`,`table_resolution2_view`.`Options` AS `Options` from `table_resolution2_view` where (`table_resolution2_view`.`PageName` <> '')
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `troubleshoot_level_1`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `troubleshoot_level_1` AS select `table_resolution2_view`.`SerialNo` AS `SerialNo`,`table_resolution2_view`.`PageName` AS `Protocol`,`table_resolution2_view`.`Symptom` AS `Symptom`,`table_resolution2_view`.`Cause` AS `Cause`,`table_resolution2_view`.`UpdateTime` AS `RecTime`,`s`.`Series` AS `Series`,`s`.`Model` AS `Model`,`s`.`Options` AS `Options` from (`table_resolution2_view` left join `startup` `s` on((`table_resolution2_view`.`SerialNo_copy` = `s`.`SerialNo`))) where (`table_resolution2_view`.`MFE_Level_Used` = 'FALSE')
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `troubleshoot_level_1_only2`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `troubleshoot_level_1_only2` AS select `troubleshoot_level_1`.`SerialNo` AS `SerialNo`,`troubleshoot_level_1`.`RecTime` AS `RecTime`,`troubleshoot_level_1`.`Series` AS `Series`,`troubleshoot_level_1`.`Model` AS `Model`,`troubleshoot_level_1`.`Options` AS `Options` from `troubleshoot_level_1` where `troubleshoot_level_1`.`SerialNo` in (select `troubleshoot_all_levels`.`SerialNo` AS `SerialNo` from `troubleshoot_all_levels`) is false
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `troubleshoot_level_technology`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `troubleshoot_level_technology` AS select `table_resolution2_view`.`SerialNo` AS `SerialNo`,`table_resolution2_view`.`PageName` AS `Protocol`,`table_resolution2_view`.`Symptom` AS `Symptom`,`table_resolution2_view`.`Cause` AS `Cause`,`table_resolution2_view`.`UpdateTime` AS `RecTime`,`s`.`Series` AS `Series`,`s`.`Model` AS `Model`,`s`.`Options` AS `Options` from (`table_resolution2_view` left join `startup` `s` on((`table_resolution2_view`.`SerialNo_copy` = `s`.`SerialNo`))) where (`table_resolution2_view`.`Technology_Instructions` <> '')
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `troubleshoot_potential_causes_investigated`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `troubleshoot_potential_causes_investigated` AS select `table_resolution2_view`.`SerialNo_copy` AS `SerialNo`,`table_resolution2_view`.`PageName_copy` AS `Protocol`,`table_resolution2_view`.`Symptom_copy` AS `Symptom`,`table_resolution2_view`.`Cause` AS `Cause`,`table_resolution2_view`.`Series` AS `Series`,`table_resolution2_view`.`Model` AS `Model`,`table_resolution2_view`.`Options` AS `Options` from `table_resolution2_view` where (`table_resolution2_view`.`PageName` = '')
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `workcell_bay_status_expected_testtime_90_day_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `workcell_bay_status_expected_testtime_90_day_view` AS select `b`.`Workcell` AS `Workcell_Act`,`b`.`WorkcellStation` AS `WorkcellStation_Act`,`b`.`WorkcellBay` AS `WorkcellBay_Act`,`b`.`Station` AS `Station_Act`,`b`.`Bay` AS `Bay_Act`,`b`.`SerialNo` AS `SerialNo_Act`,`b`.`ShopOrder` AS `ShopOrder_Act`,`b`.`Series` AS `Series_Act`,`b`.`Model` AS `Model_Act`,`b`.`OptionsID` AS `OptionsID_Act`,`b`.`OptionsName` AS `OptionsName_Act`,`b`.`StartTime` AS `StartTime_Act`,`b`.`CurrentProtocol` AS `CurrentProtocol_Act`,`statshv`.`GetCurrentProtocolExpectedTime`(`b`.`CurrentProtocol`) AS `CurrentProtocol_Exp_Time`,`statshv`.`GetCurrentProtocol90DayAvg`(`b`.`CurrentProtocol`,`b`.`Series`,`b`.`Model`) AS `CurrentProtocol_90DayAvg`,timestampdiff(MINUTE,`statshv`.`GetLastProtocolEndTime`(`b`.`LastProtocol`,`b`.`SerialNo`),now()) AS `Curr_Prot_Tm`,`b`.`Step` AS `Step_Act`,`b`.`TotalSteps` AS `TotalSteps_Act`,`b`.`TimeInTestAndCal` AS `TimeInTestAndCal_Act`,`b`.`LastProtocol` AS `LastProtocol_Act`,`b`.`LastProtocolTime` AS `LastProtocolTime_Act`,`b`.`LastProtocolExpectedTime` AS `LastProtocolExpectedTime_Act`,`b`.`TotalExpectedTime` AS `TotalExpectedTime_Act`,`b`.`ExpectedRemainingTimeInTestAndCal` AS `ExpectedRemainingTimeInTestAndCal_Act`,`b`.`LastProtocolDelta` AS `LastProtocolDelta_Act`,`b`.`ExpectedFinishDateTime` AS `ExpectedFinishDateTime_Act`,`b`.`ActualExpectedFinishDateTime` AS `ActualExpectedFinishDateTime_Act`,`v`.`Startup_Act_90DayAvg` AS `Startup_Act_90DayAvg`,`v`.`Startup_Exp` AS `Startup_Exp`,`v`.`IO_Tests_Act_90DayAvg` AS `IO_Tests_Act_90DayAvg`,`v`.`IO_Tests_Exp` AS `IO_Tests_Exp`,`v`.`LowLevel_Rinse_Act_90DayAvg` AS `LowLevel_Rinse_Act_90DayAvg`,`v`.`LowLevel_Rinse_Exp` AS `LowLevel_Rinse_Exp`,`v`.`Sample_Cond_AZ_1_Act_90DayAvg` AS `Sample_Cond_AZ_1_Act_90DayAvg`,`v`.`Sample_Cond_AZ_1_Exp` AS `Sample_Cond_AZ_1_Exp`,`v`.`IC_TC_Cond_AZ_Act_90DayAvg` AS `IC_TC_Cond_AZ_Act_90DayAvg`,`v`.`IC_TC_Cond_AZ_Exp` AS `IC_TC_Cond_AZ_Exp`,`v`.`LowLevel_SL1_Data_Act_90DayAvg` AS `LowLevel_SL1_Data_Act_90DayAvg`,`v`.`LowLevel_SL1_Data_Exp` AS `LowLevel_SL1_Data_Exp`,`v`.`TOC_Single_Point_Cal_Act_90DayAvg` AS `TOC_Single_Point_Cal_Act_90DayAvg`,`v`.`TOC_Single_Point_Cal_Exp` AS `TOC_Single_Point_Cal_Exp`,`v`.`TOC_Ver_Act_90DayAvg` AS `TOC_Ver_Act_90DayAvg`,`v`.`TOC_Ver_Exp` AS `TOC_Ver_Exp`,`v`.`Cond_Single_Point_Cal_Act_90DayAvg` AS `Cond_Single_Point_Cal_Act_90DayAvg`,`v`.`Cond_Single_Point_Cal_Exp` AS `Cond_Single_Point_Cal_Exp`,`v`.`Cond_Cal_Ver_Act_90DayAvg` AS `Cond_Cal_Ver_Act_90DayAvg`,`v`.`Cond_Cal_Ver_Exp` AS `Cond_Cal_Ver_Exp`,`v`.`Specificity_Act_90DayAvg` AS `Specificity_Act_90DayAvg`,`v`.`Specificity_Exp` AS `Specificity_Exp`,`v`.`Online_Precision_Act_90DayAvg` AS `Online_Precision_Act_90DayAvg`,`v`.`Online_Precision_Exp` AS `Online_Precision_Exp`,`v`.`Sample_Cond_AZ_2_Act_90DayAvg` AS `Sample_Cond_AZ_2_Act_90DayAvg`,`v`.`Sample_Cond_AZ_2_Exp` AS `Sample_Cond_AZ_2_Exp` from (`workcell_bay_status_expected_testtime_view` `b` left join `bay_status_test_time_90_day_view` `v` on(((`b`.`Series` = `v`.`Series`) and (`b`.`Model` = `v`.`Model`) and (`b`.`OptionsID` = `v`.`Options`))))
;

-- Removing temporary table and create final VIEW structure
DROP TABLE IF EXISTS `workcell_bay_status_expected_testtime_view`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `workcell_bay_status_expected_testtime_view` AS select `w`.`WorkCell` AS `Workcell`,`w`.`Station` AS `WorkcellStation`,`w`.`Bay` AS `WorkcellBay`,`b`.`Station` AS `Station`,`b`.`Bay` AS `Bay`,`b`.`SerialNo` AS `SerialNo`,`b`.`ShopOrder` AS `ShopOrder`,`b`.`Series` AS `Series`,`b`.`Model` AS `Model`,`b`.`Options` AS `OptionsID`,'' AS `OptionsName`,`b`.`StartTime` AS `StartTime`,`b`.`CurrentProtocol` AS `CurrentProtocol`,`b`.`Step` AS `Step`,`b`.`TotalSteps` AS `TotalSteps`,timestampdiff(MINUTE,`b`.`StartTime`,now()) AS `TimeInTestAndCal`,`b`.`LastProtocol` AS `LastProtocol`,`b`.`LastProtocolTime` AS `LastProtocolTime`,`b`.`LastProtocolExpectedTime` AS `LastProtocolExpectedTime`,`b`.`TotalExpectedTime` AS `TotalExpectedTime`,(`b`.`TotalExpectedTime` - `b`.`LastProtocolExpectedTime`) AS `ExpectedRemainingTimeInTestAndCal`,(`b`.`LastProtocolTime` - `b`.`LastProtocolExpectedTime`) AS `LastProtocolDelta`,(`b`.`StartTime` + interval `b`.`TotalExpectedTime` minute) AS `ExpectedFinishDateTime`,(`b`.`StartTime` + interval (`b`.`TotalExpectedTime` + (`b`.`LastProtocolTime` - `b`.`LastProtocolExpectedTime`)) minute) AS `ActualExpectedFinishDateTime` from (`workcell_bay` `w` left join `bay_status` `b` on(((`w`.`Station` = `b`.`Station`) and (`w`.`Bay` = `b`.`Bay`))))
;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
