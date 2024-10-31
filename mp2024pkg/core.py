from collections.abc import Iterable

def show_nested(item, max_depth=2, max_items=5):
    """Displays type, length, and example values of nested items up to level 2."""
    
    # Level 1 정보 출력
    item_type = type(item).__name__
    try:
        item_len = len(item)
    except TypeError:
        item_len = None  # 길이를 구할 수 없는 경우
    
    item_str = repr(item)
    if len(item_str) > 50:
        example = f"{item_str[:25]} ... {item_str[-25:]}"
    else:
        example = item_str
    
    info = f"Level 1 - Type: {item_type}"
    if item_len is not None:
        info += f", Length: {item_len}"
    info += f", Example: {example}"
    print(info)

    # Level 2 정보 출력 (item이 Iterable일 경우에만)
    if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
        if item_len is None:
            return  # 길이를 구할 수 없는 객체는 반복하지 않음
        for idx, subitem in enumerate(item):
            if idx == max_items // 2 and item_len > max_items:
                print(f"     ...")
            elif idx >= max_items and idx < item_len - max_items // 2:
                continue

            subitem_type = type(subitem).__name__
            try:
                subitem_len = len(subitem)
            except TypeError:
                subitem_len = None
            
            subitem_str = repr(subitem)
            if len(subitem_str) > 50:
                sub_example = f"{subitem_str[:25]} ... {subitem_str[-25:]}"
            else:
                sub_example = subitem_str

            sub_info = f"     Level 2 - Type: {subitem_type}"
            if subitem_len is not None:
                sub_info += f", Length: {subitem_len}"
            sub_info += f", Example: {sub_example}"
            print(sub_info)

def show_dict(dct):
    print("Dictionary Overview:")
    print(f"Total keys: {len(dct.keys())}")
    print(f"Keys: {list(dct.keys())}\n")
    
    for i, (k, v) in enumerate(dct.items()):
        print(f"{i+1}. Key: '{k}'")
        print(f"   - Type: {type(v).__name__}")

        # 길이 확인이 가능한 타입인 경우 길이 정보 출력
        if hasattr(v, "__len__"):
            print(f"   - Length: {len(v)}")

        # Iterable 값의 길이를 제한해 출력
        if len(str(v)) > 100:
            display_values = str(v)[:100] + "..."  # 문자열 길이 제한 후 생략 표시
        else:
            display_values = str(v)

        # 값 출력
        print(f"   - Values: {display_values}")
        print()  # 공백 줄 추가