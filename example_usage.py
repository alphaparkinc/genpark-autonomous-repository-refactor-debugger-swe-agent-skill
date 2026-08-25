from client import AutonomousRepositoryRefactorDebuggerSweAgentClient

def main():
    client = AutonomousRepositoryRefactorDebuggerSweAgentClient()
    res = client.execute_swe_bench_task('Migrate auth service from session tokens to JWT RS256 with key rotation')
    print('SWE Task: ' + res['task_session_id'] + ' on ' + res['target_repository'])
    print('Files Modified: ' + str(res['files_modified_count']) + ' | Tests Passed: ' + str(res['sandbox_unit_tests_passed']) + ' unit / ' + str(res['sandbox_regression_tests_passed']) + ' regression')
    print('PR Branch: ' + res['pull_request_branch'] + ' (SWE-Bench Resolved: ' + str(res['swe_bench_resolved_pct']) + '%)')

if __name__ == '__main__':
    main()
