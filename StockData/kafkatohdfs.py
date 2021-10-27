import subprocess

def run_cmd(args_list):
    """
    Description: Run linux commands
    Parameter: It takes args_list as parameter
    Return: It returns s_return, s_output, e_err
    """
    print('Running system command: {0}',format(''. join(args_list)))
    proc = subprocess.Popen(args_list,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    s_output, s_err = proc.communicate()
    s_return = proc.returncode
    return s_return,s_output,s_err

if __name__== "__main__":
    
    #create a directory in HDFS
    mkdir = run_cmd(['hdfs','dfs','-mkdir','/Kafka_Stock_Data'])

    # copy StockData.txt data from local system to hdfs  
    copy = run_cmd(['hdfs','dfs','-copyFromLocal', '/home/namratha/Documents/Kafka/StockData/StockData.txt', '/Kafka_Stock_Data'])     