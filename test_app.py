import unittest

from app import process


class AppTestCase(unittest.TestCase):
    def test_process(self):
        expected_env = "SERVICE_JOBMANAGER_WEB_UI_PORT: 8081\n" \
                       "SERVICE_TASKMANAGER_RPC_PORT: 6122\n" \
                       "SERVICE_TASKMANAGER_TOTOTTO_DASDSA: dsadsad\n" \
                       "SERVICE_TASKMANAGER_TOTOTTO_DAD: dadsada\n" \
                       "SERVICE_TASKMANAGER_TOTOTTOA_DASDSA: dsadsad\n" \
                       "SERVICE_TASKMANAGER_TOTOTTOA_DAD: dadsada\n" \
                       "SERVICE_TASKMANAGER_QUERY_STATE_NAME: query-state\n" \
                       "SERVICE_TASKMANAGER_QUERY_STATE_PORT: 6125\n" \
                       "AUTOSCALER_REPLICA_MIN_COUNT: 1\n" \
                       "AUTOSCALER_REPLICA_MAX_COUNT: 10\n" \
                       "AUTOSCALER_CPU_AVG_UTILIZATION: 70\n"
        env = process('values.yaml')
        self.assertEqual(env, expected_env)


if __name__ == '__main__':
    unittest.main()
