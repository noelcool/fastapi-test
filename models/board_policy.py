class BoardCommentPolicy:
    def __init__(self, has_per_comment_limit, has_daily_user_limit, max_per_comment, max_daily_per_user):
        self.has_per_comment_limit = has_per_comment_limit
        self.has_daily_user_limit = has_daily_user_limit
        self.max_per_comment = max_per_comment
        self.max_daily_per_user = max_daily_per_user


class BoardPolicy:
    def __init__(self, is_reply_enabled, is_comment_enabled, comment_policy: BoardCommentPolicy):
        self._validate_bool(is_reply_enabled)
        self._validate_bool(is_comment_enabled)
        self._validate_obj(comment_policy)

        self.is_reply_enabled = is_reply_enabled
        self.is_comment_enabled = is_comment_enabled
        self.comment_policy = comment_policy

    def _validate_bool(self, test: bool):
        if not isinstance(test, bool):
            raise ValueError("only bool")

    def _validate_obj(self, test: object):
        if not isinstance(test, BoardCommentPolicy):
            raise ValueError("only obj")
