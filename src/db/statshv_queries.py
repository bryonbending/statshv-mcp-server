from src.db.connection import DatabaseManager


class StatshvQueries:
    """Pre-built query helpers for the statshv instrument test & calibration database."""

    # ── Bay Status ────────────────────────────────────────────────────────────

    @staticmethod
    def get_bay_status(station: str = None) -> list[dict]:
        if station:
            query = """
                SELECT RecNo, Station, Bay, SerialNo, ShopOrder, Series, Model, Options,
                       StartTime, CurrentProtocol, Step, TotalSteps, StepStatus,
                       LastProtocol, LastProtocolTime, LastProtocolExpectedTime,
                       LastProtocolDelta, TotalExpectedTime,
                       ExpectedRemainingTime, ActualRemainingTime,
                       ExpectedFinishDateTime, ActualFinishDateTime
                FROM bay_status
                WHERE Station = %s
                ORDER BY Station, Bay
            """
            return DatabaseManager.execute_safe_query(query, (station,))
        query = """
            SELECT RecNo, Station, Bay, SerialNo, ShopOrder, Series, Model, Options,
                   StartTime, CurrentProtocol, Step, TotalSteps, StepStatus,
                   LastProtocol, LastProtocolTime, LastProtocolExpectedTime,
                   LastProtocolDelta, TotalExpectedTime,
                   ExpectedRemainingTime, ActualRemainingTime,
                   ExpectedFinishDateTime, ActualFinishDateTime
            FROM bay_status
            ORDER BY Station, Bay
        """
        return DatabaseManager.execute_safe_query(query)

    @staticmethod
    def get_active_instruments() -> list[dict]:
        query = """
            SELECT Station, Bay, SerialNo, ShopOrder, Series, Model,
                   StartTime, CurrentProtocol, Step, TotalSteps,
                   StepStatus, ExpectedRemainingTime, ActualRemainingTime,
                   ExpectedFinishDateTime
            FROM bay_status
            WHERE SerialNo != '' AND CurrentProtocol != ''
            ORDER BY Station, Bay
        """
        return DatabaseManager.execute_safe_query(query)

    # ── Startup / Instrument Initialization ───────────────────────────────────

    @staticmethod
    def get_startup_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT RecNo, SerialNo, AQCNo, Series, Model, Options,
                   FWrev, SWversion, IPAddr, ICCell, TCCell, C3Cell,
                   ShopOrder, Station, Bay, Site, Operator,
                   WizardStartTime, Rectime
            FROM startup
            WHERE SerialNo LIKE %s
            ORDER BY Rectime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_recent_startups(days: int = 7, limit: int = 50) -> list[dict]:
        query = """
            SELECT SerialNo, AQCNo, Series, Model, Options,
                   ShopOrder, Station, Bay, Site, Operator,
                   WizardStartTime, Rectime
            FROM startup
            WHERE Rectime >= DATE_SUB(NOW(), INTERVAL %s DAY)
            ORDER BY Rectime DESC
            LIMIT %s
        """
        return DatabaseManager.execute_safe_query(query, (days, limit))

    # ── Conductivity Auto-Zero (condaz) ───────────────────────────────────────

    @staticmethod
    def get_condaz_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, ThornID, ThornCal,
                   RefCond, OldCond, NewCond, CondPass,
                   ICold, ICnew, TCold, TCnew, ICTCpass,
                   LLICfnl, LLTCfnl, TempDiff, TempPass,
                   Operator, Station, Bay, Site, RecTime
            FROM condaz
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_condaz_pass_rate(days: int = 90) -> list[dict]:
        query = """
            SELECT
                COUNT(*) AS total,
                SUM(CondPass) AS cond_pass,
                SUM(ICTCpass) AS ictc_pass,
                SUM(TempPass) AS temp_pass,
                ROUND(AVG(CondPass) * 100, 1) AS cond_pass_pct,
                ROUND(AVG(ICTCpass) * 100, 1) AS ictc_pass_pct,
                ROUND(AVG(TempPass) * 100, 1) AS temp_pass_pct
            FROM condaz
            WHERE RecTime >= DATE_SUB(NOW(), INTERVAL %s DAY)
        """
        return DatabaseManager.execute_safe_query(query, (days,))

    # ── Conductivity Calibration & Verification (condcalver) ──────────────────

    @staticmethod
    def get_condcalver_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, CalLot, CalExp,
                   CondGain, GainDiff, CondRSD, CondAcc, CondCalPass,
                   CondVerLot, CondVerExp,
                   CondRSD1, CondACC1, CondRSD2, CondACC2,
                   CondVerPass, Operator, Station, Bay, Site, RecTime
            FROM condcalver
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_condcalver_pass_rate(days: int = 90) -> list[dict]:
        query = """
            SELECT
                COUNT(*) AS total,
                SUM(CondCalPass) AS cal_pass,
                SUM(CondVerPass) AS ver_pass,
                ROUND(AVG(CondCalPass) * 100, 1) AS cal_pass_pct,
                ROUND(AVG(CondVerPass) * 100, 1) AS ver_pass_pct
            FROM condcalver
            WHERE RecTime >= DATE_SUB(NOW(), INTERVAL %s DAY)
        """
        return DatabaseManager.execute_safe_query(query, (days,))

    # ── TOC Single-Point Calibration (spcal) ─────────────────────────────────

    @staticmethod
    def get_spcal_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, SPcalLot, SPcalExp,
                   ICslope, TCslope, SLPratio,
                   spICpeak, spTCpeak, spPkRatio, SPpass,
                   SPaccLot, SPaccExp, TOCacc, TOCrsd, SPaccpass,
                   Operator, Station, Bay, Site, RecTime
            FROM spcal
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_spcal_pass_rate(days: int = 90) -> list[dict]:
        query = """
            SELECT
                COUNT(*) AS total,
                SUM(SPpass) AS sp_cal_pass,
                SUM(SPaccpass) AS sp_acc_pass,
                ROUND(AVG(SPpass) * 100, 1) AS sp_cal_pass_pct,
                ROUND(AVG(SPaccpass) * 100, 1) AS sp_acc_pass_pct
            FROM spcal
            WHERE RecTime >= DATE_SUB(NOW(), INTERVAL %s DAY)
        """
        return DatabaseManager.execute_safe_query(query, (days,))

    # ── Specificity Calibration (speccal) ─────────────────────────────────────

    @staticmethod
    def get_speccal_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, MethRec, NicRec, KHPRec,
                   Operator, Station, Bay, Site, RecTime
            FROM speccal
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    # ── I/O Tests (iotests) ───────────────────────────────────────────────────

    @staticmethod
    def get_iotests_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, AnalPass, AlmPass,
                   StrtsFlowOn, PauseFlowOff, ResumeFlowOn,
                   StopsLvlOn, ResumeLvlOff,
                   StartsBinOn, StopsBinOff, BinOffAtEnd,
                   AnalogMeter, Operator, Station, Bay, Site, RecTime
            FROM iotests
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_iotests_pass_rate(days: int = 90) -> list[dict]:
        query = """
            SELECT
                COUNT(*) AS total,
                SUM(AnalPass) AS analog_pass,
                SUM(AlmPass) AS alarm_pass,
                ROUND(AVG(AnalPass) * 100, 1) AS analog_pass_pct,
                ROUND(AVG(AlmPass) * 100, 1) AS alarm_pass_pct
            FROM iotests
            WHERE RecTime >= DATE_SUB(NOW(), INTERVAL %s DAY)
        """
        return DatabaseManager.execute_safe_query(query, (days,))

    # ── Low-Level Rinse (llrinse) ─────────────────────────────────────────────

    @staticmethod
    def get_llrinse_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, CondRes, CondPass,
                   TempC3, TempRdr, TempDiff, TempPass,
                   FlowRate, FlowPass, RnsPass,
                   ICavg, ICrsd, TCavg, TCrsd, TOCavg, TOCrsd,
                   Operator, Station, Bay, Site, RecTime
            FROM llrinse
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    # ── Fluidics Calibration ──────────────────────────────────────────────────

    @staticmethod
    def get_fluidics_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT RecNo, SerialNo, ICCell, TCCell, SCCell,
                   ICAvg, ICStd, TCAvg, TCStd,
                   SCCondAvg, SCCondStd,
                   DeltaT, FlowRate, FlowRatePass,
                   LvlSnsEmpty, LvlSnsFull,
                   ConstantsPass, Pass,
                   PrimeStart, PrimeEnd, TotalPrimeMinutes,
                   RinseStart, RinseEnd, TotalRinseMinutes,
                   Operator, SWVersion, Station, UpdateTime
            FROM fluidics
            WHERE SerialNo LIKE %s
            ORDER BY UpdateTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_fluidics_repairs_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT RecNo, SerialNo, ShopOrder, TestName,
                   Technician, PartNo, PartDescription,
                   Failure, Notes, RepairTime
            FROM fluidics_repair
            WHERE SerialNo LIKE %s
            ORDER BY RepairTime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    # ── Repair Data (repairdat2) ───────────────────────────────────────────────

    @staticmethod
    def get_repair_history(serial_no: str) -> list[dict]:
        query = """
            SELECT RecordNo, SerialNo, ShopOrder, PageName,
                   Operator, Assy, Component, Failure,
                   Func, Site, StrtTime, RecTime, notes
            FROM repairdat2
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 50
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_top_failures(days: int = 90, limit: int = 10) -> list[dict]:
        query = """
            SELECT Failure, Component, COUNT(*) AS occurrence_count,
                   COUNT(DISTINCT SerialNo) AS affected_instruments
            FROM repairdat2
            WHERE RecTime >= DATE_SUB(NOW(), INTERVAL %s DAY)
            GROUP BY Failure, Component
            ORDER BY occurrence_count DESC
            LIMIT %s
        """
        return DatabaseManager.execute_safe_query(query, (days, limit))

    @staticmethod
    def get_fpy_stats(days: int = 30) -> list[dict]:
        query = """
            SELECT
                COUNT(DISTINCT s.SerialNo) AS total_instruments,
                COUNT(DISTINCT r.SerialNo) AS instruments_with_failures,
                COUNT(DISTINCT s.SerialNo) - COUNT(DISTINCT r.SerialNo) AS first_pass,
                ROUND(
                    (COUNT(DISTINCT s.SerialNo) - COUNT(DISTINCT r.SerialNo))
                    / NULLIF(COUNT(DISTINCT s.SerialNo), 0) * 100, 1
                ) AS fpy_pct
            FROM startup s
            LEFT JOIN repairdat2 r ON s.SerialNo = r.SerialNo
            WHERE s.Rectime >= DATE_SUB(NOW(), INTERVAL %s DAY)
        """
        return DatabaseManager.execute_safe_query(query, (days,))

    # ── Final Prep Checklists ─────────────────────────────────────────────────

    @staticmethod
    def get_fnlprep_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, ErrsClrd, ErrsRvwd,
                   FilesSvd, SvcDataBckup, Activated,
                   Operator, Station, Bay, Site, RecTime
            FROM fnlprep
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 10
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_fnlprep2_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT Recno, SerialNo, FilesRmvd, NdlVlvClsd,
                   LoopDrnd, SmplDrnd, DisConUPW, DisConWaste,
                   KeysInDr, IOcapsOn, TestRecChckd, CalDays,
                   Operator, Station, Bay, Site, RecTime
            FROM fnlprep2
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 10
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    # ── OBA Notes ─────────────────────────────────────────────────────────────

    @staticmethod
    def get_oba_notes(serial_no: str) -> list[dict]:
        query = """
            SELECT RecNo, SerialNo, Result, FinishedDate,
                   Notes, Operator, Station, Bay, Site, Rectime
            FROM obanotes
            WHERE SerialNo LIKE %s
            ORDER BY Rectime DESC
            LIMIT 20
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    @staticmethod
    def get_oba_summary(days: int = 30) -> list[dict]:
        query = """
            SELECT Result, COUNT(*) AS count
            FROM obanotes
            WHERE Rectime >= DATE_SUB(NOW(), INTERVAL %s DAY)
            GROUP BY Result
            ORDER BY count DESC
        """
        return DatabaseManager.execute_safe_query(query, (days,))

    # ── Pre-Ship Checklist ────────────────────────────────────────────────────

    @staticmethod
    def get_preship_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT RecNo, SerialNo, CertGenerated,
                   AccPN1, AccPN2, AccPN3, AccPN4, AccPN5,
                   Site, Operator, RecTime
            FROM preship
            WHERE SerialNo LIKE %s
            ORDER BY RecTime DESC
            LIMIT 10
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    # ── System Constants ──────────────────────────────────────────────────────

    @staticmethod
    def get_constants_by_serial(serial_no: str) -> list[dict]:
        query = """
            SELECT RecNo, SerialNo,
                   IC_CELL_NUMBER, IC_CELL_CONSTANT,
                   TC_CELL_NUMBER, TC_CELL_CONSTANT,
                   SAMPLE_CELL_NUMBER, SAMPLE_CELL_CONSTANT,
                   MULTIPOINT_TOC_SLOPE, TOC_OFFSET,
                   MULTIPOINT_COND_SLOPE,
                   BASE_MODEL, Series,
                   Operator, Station, Bay, Site, Rectime
            FROM constants
            WHERE SerialNo LIKE %s
            ORDER BY Rectime DESC
            LIMIT 10
        """
        return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%",))

    # ── Test Time Analysis ────────────────────────────────────────────────────

    @staticmethod
    def get_actual_protocol_test_times(serial_no: str = None, limit: int = 50) -> list[dict]:
        if serial_no:
            query = """
                SELECT RecNo, SerialNo, ShopOrder, Series, Model, Options,
                       StartTime, FinishTime, YearMonth,
                       Startup_Act, Startup_Exp,
                       IO_Tests_Act, IO_Tests_Exp,
                       LowLevel_Rinse_Act, LowLevel_Rinse_Exp,
                       Sample_Cond_AZ_1_Act, Sample_Cond_AZ_1_Exp,
                       TOC_Single_Point_Cal_Act, TOC_Single_Point_Cal_Exp,
                       TOC_Ver_Act, TOC_Ver_Exp,
                       Cond_Single_Point_Cal_Act, Cond_Single_Point_Cal_Exp,
                       Cond_Cal_Ver_Act, Cond_Cal_Ver_Exp,
                       Specificity_Act, Specificity_Exp,
                       Online_Precision_Act, Online_Precision_Exp
                FROM actual_protocol_testtime_view
                WHERE SerialNo LIKE %s
                ORDER BY StartTime DESC
                LIMIT %s
            """
            return DatabaseManager.execute_safe_query(query, (f"%{serial_no}%", limit))
        query = """
            SELECT RecNo, SerialNo, ShopOrder, Series, Model, Options,
                   StartTime, FinishTime, YearMonth,
                   Startup_Act, Startup_Exp,
                   IO_Tests_Act, IO_Tests_Exp,
                   LowLevel_Rinse_Act, LowLevel_Rinse_Exp,
                   Sample_Cond_AZ_1_Act, Sample_Cond_AZ_1_Exp,
                   TOC_Single_Point_Cal_Act, TOC_Single_Point_Cal_Exp,
                   TOC_Ver_Act, TOC_Ver_Exp,
                   Cond_Single_Point_Cal_Act, Cond_Single_Point_Cal_Exp,
                   Cond_Cal_Ver_Act, Cond_Cal_Ver_Exp,
                   Specificity_Act, Specificity_Exp,
                   Online_Precision_Act, Online_Precision_Exp
            FROM actual_protocol_testtime_view
            ORDER BY StartTime DESC
            LIMIT %s
        """
        return DatabaseManager.execute_safe_query(query, (limit,))

    @staticmethod
    def get_expected_test_times(series: str = None, model: str = None) -> list[dict]:
        if series and model:
            query = """
                SELECT RecNo, Series, Model, Options, TotalTests,
                       Startup_Exp, IO_Tests_Exp, LowLevel_Rinse_Exp,
                       Sample_Cond_AZ_1_Exp, IC_TC_Cond_AZ_Exp,
                       LowLevel_SL1_Data_Exp, TOC_Single_Point_Cal_Exp,
                       TOC_Ver_Exp, Cond_Single_Point_Cal_Exp, Cond_Cal_Ver_Exp,
                       Specificity_Exp, Online_Precision_Exp,
                       Sample_Cond_AZ_2_Exp, Constants_Exp
                FROM expected_testtime
                WHERE Series = %s AND Model = %s
            """
            return DatabaseManager.execute_safe_query(query, (series, model))
        query = """
            SELECT RecNo, Series, Model, Options, TotalTests,
                   Startup_Exp, IO_Tests_Exp, LowLevel_Rinse_Exp,
                   Sample_Cond_AZ_1_Exp, IC_TC_Cond_AZ_Exp,
                   LowLevel_SL1_Data_Exp, TOC_Single_Point_Cal_Exp,
                   TOC_Ver_Exp, Cond_Single_Point_Cal_Exp, Cond_Cal_Ver_Exp,
                   Specificity_Exp, Online_Precision_Exp,
                   Sample_Cond_AZ_2_Exp, Constants_Exp
            FROM expected_testtime
            ORDER BY Series, Model
        """
        return DatabaseManager.execute_safe_query(query)

    @staticmethod
    def get_test_time_90day_summary() -> list[dict]:
        query = """
            SELECT Series, Model, Options,
                   COUNT(*) AS instrument_count,
                   ROUND(AVG(Startup_Act), 2) AS avg_startup,
                   ROUND(AVG(IO_Tests_Act), 2) AS avg_io_tests,
                   ROUND(AVG(TOC_Single_Point_Cal_Act), 2) AS avg_toc_spcal,
                   ROUND(AVG(TOC_Ver_Act), 2) AS avg_toc_ver,
                   ROUND(AVG(Cond_Single_Point_Cal_Act), 2) AS avg_cond_spcal,
                   ROUND(AVG(Cond_Cal_Ver_Act), 2) AS avg_cond_calver,
                   ROUND(AVG(Specificity_Act), 2) AS avg_specificity,
                   ROUND(AVG(Online_Precision_Act), 2) AS avg_online_precision
            FROM actual_protocol_testtime_view
            WHERE StartTime >= DATE_SUB(NOW(), INTERVAL 90 DAY)
            GROUP BY Series, Model, Options
            ORDER BY Series, Model
        """
        return DatabaseManager.execute_safe_query(query)

    # ── Instrument Full History ───────────────────────────────────────────────

    @staticmethod
    def get_instrument_summary(serial_no: str) -> list[dict]:
        query = """
            SELECT s.SerialNo, s.AQCNo, s.Series, s.Model, s.Options,
                   s.ShopOrder, s.FWrev, s.SWversion,
                   s.ICCell, s.TCCell, s.C3Cell,
                   s.Station, s.Bay, s.Site,
                   s.WizardStartTime, s.Rectime AS startup_time,
                   (SELECT COUNT(*) FROM repairdat2 r WHERE r.SerialNo = s.SerialNo) AS total_repairs,
                   (SELECT MAX(RecTime) FROM repairdat2 r WHERE r.SerialNo = s.SerialNo) AS last_repair_time,
                   (SELECT COUNT(*) FROM condaz c WHERE c.SerialNo = s.SerialNo) AS condaz_tests,
                   (SELECT COUNT(*) FROM spcal sp WHERE sp.SerialNo = s.SerialNo) AS spcal_tests
            FROM startup s
            WHERE s.SerialNo = %s
            ORDER BY s.Rectime DESC
            LIMIT 1
        """
        return DatabaseManager.execute_safe_query(query, (serial_no,))

    # ── Custom SQL ────────────────────────────────────────────────────────────

    @staticmethod
    def run_custom_query(sql: str, params: tuple = None) -> list[dict]:
        return DatabaseManager.execute_safe_query(sql, params)
