def solution(record):
    commands = []
    id_name = {}
    
    for each_record in record:
        command = each_record.split(' ')[0]
        id_ = each_record.split(' ')[1]
        if len(each_record.split(' ')) > 2:
            name = each_record.split(' ')[2]
            id_name[id_] = name
        commands.append((command, id_))
        
    answer = []
    for command in commands:
        if command[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(id_name[command[1]]))
        elif command[0] == 'Leave':
            answer.append('{}님이 나갔습니다.'.format(id_name[command[1]]))
    
    return answer