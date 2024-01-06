from setting.config import *
import random


def return_output(data, message, status):
    return {"message": message, "data": data, "status": status}


def validate(request_data, validate_list):
    validation_list = []
    request_keys = []
    result = []
    valid_sub_key = []
    main_keys_only = []
    status_code = 200
    for key, value in validate_list.items():
        validation_list.append(key)  # to load given validation key

    for key, value in request_data.items():
        if key not in validation_list:
            main_keys_only.append(key)
        request_keys.append(key)  # to load request keys
        if type(value) is dict:
            for k, v in value.items():
                if k not in validation_list:
                    valid_sub_key.append(key + "." + k)
                request_keys.append(k)  # to load request sub keys
        else:
            if value is None or not value or value == " ":
                status_code = validate_list[key]

    keys_difference = list(set(validation_list) - set(request_keys))  # find difference

    if keys_difference:
        # if keys is invalid
        status_code = 1005
        if valid_sub_key:
            if len(valid_sub_key) == len(keys_difference) and len(valid_sub_key) == 1:
                output = {"request": valid_sub_key[0],
                          'actually': str(valid_sub_key[0]).split(".")[0] + "." + keys_difference[0]}
            elif len(valid_sub_key) == len(keys_difference):
                output = {"request": valid_sub_key, 'actuallySubKeys': keys_difference}
            else:
                output = {"request": {"mainKeys": main_keys_only, "subKeys": valid_sub_key},
                          "actually": keys_difference}
                # output=keys_difference+valid_sub_key
        else:
            if len(main_keys_only) > 0:
                if len(keys_difference) == 1:
                    print(main_keys_only)
                    output = {"request": main_keys_only[0], "actually": keys_difference[0]}
                else:
                    output = {"request": {"mainKeys": main_keys_only}, "actually": keys_difference}
            else:
                if len(keys_difference) == 1:
                    actually = keys_difference[0]
                else:
                    actually = keys_difference
                output = {"Request": "No such key", "actually": actually}
    else:
        # if key valid and no values
        for k_v, v_v in request_data.items():
            if type(v_v) is dict:
                for k, v in v_v.items():
                    if type(v_v[k]) is not bool and not v_v[k]:  # if value is not empty or not bool
                        result.append(k_v + "." + k)
                        status_code = validate_list[k]
                        break
            if not request_data[k_v]:
                result.append(k_v)
                status_code = validate_list[k_v]
        output = result

    return {"code": status_code, 'data': output}


def current_full_str_date():
    return strftime("%d.%m.%Y %H:%M:%S", localtime())


def current_str_date():
    today = date.today()
    return today.strftime("%d.%m.%Y")


def current_str_time():
    format_time = "%H:%M"
    return datetime.now().time().strftime(format_time)


def current_full_obj_date():
    full_format_date = "%d.%m.%Y %H:%M:%S"
    return datetime.today().strptime(current_full_str_date(), full_format_date)
