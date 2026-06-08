class MergeSort:
    @staticmethod
    def sort(items: list, key: str, reverse: bool = False) -> list:
        field = key.lstrip(":")
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = MergeSort.sort(items[:mid], key, reverse)
        right = MergeSort.sort(items[mid:], key, reverse)
        return MergeSort._merge(left, right, field, reverse)

    @staticmethod
    def _get_value(item, field):
        if isinstance(item, dict):
            return item[field]

        return getattr(item, field)

    @staticmethod
    def _compare_value(value):
        if isinstance(value, str):
            return value.casefold()

        return value

    @staticmethod
    def _merge(left, right, field, reverse=False):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            left_value = MergeSort._compare_value(MergeSort._get_value(left[i], field))
            right_value = MergeSort._compare_value(
                MergeSort._get_value(right[j], field)
            )
            if left_value >= right_value if reverse else left_value <= right_value:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
