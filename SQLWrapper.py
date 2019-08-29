def sql_wrapper(func):
    def wrapper_sql_executor(*args, **kwargs):
        clazz = args[0]
        results = []

        for res in func(*args, **kwargs):
            if isinstance(res, str):
                sql_request, values = res, None
            else:
                sql_request, *values = res
                values = values[0]
            results.append(clazz.execute(sql_request, values))

        if len(results) == 1:
            return results[0]
        else:
            return results

    return wrapper_sql_executor
