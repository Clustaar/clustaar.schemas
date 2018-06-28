from enum import Enum

WAIT_ACTION_DEFAULT_DURATION = 2
WAIT_ACTION_MAX_DURATION = 7
WAIT_ACTION_MIN_DURATION = 0.5

SEND_EMAIL_ACTION_SUBJECT_MAX_LENGTH = 150
SEND_EMAIL_ACTION_CONTENT_MAX_LENGTH = 1500
SEND_EMAIL_ACTION_RECIPIENT_MAX_LENGTH = 150

EXTERNAL_URL_MAX_LENGTH = 500

SEND_TEXT_ACTION_MESSAGE_MAX_LENGTH = 500
SEND_TEXT_ACTION_MAX_MESSAGES_COUNT = 10

SEND_QUICK_REPLIES_ACTION_MAX_BUTTONS_COUNT = 11
QUICK_REPLY_TITLE_MAX_LENGTH = 20

BUTTON_TITLE_MAX_LENGTH = 20

CARD_MAX_BUTTONS_COUNT = 3
CARD_TITLE_MAX_LENGTH = 80
CARD_SUBTITLE_MAX_LENGTH = 80
SEND_CARDS_ACTION_MAX_CARDS_COUNT = 10

STORE_SESSION_VALUE_ACTION_KEY_MAX_LENGTH = 100
STORE_SESSION_VALUE_ACTION_VALUE_MAX_LENGTH = 200

GOOGLE_CUSTOM_SEARCH_ACTION_QUERY_MAX_LENGTH = 2048
GOOGLE_CUSTOM_SEARCH_ACTION_MAX_LIMIT = 10

ASSIGN_INTERCOM_CONVERSATION_ACTION_ASSIGNEE_ID_MAX_LENGTH = 100

ZENDESK_TAG_MAX_LENGTH = 80
ZENDESK_TAGS_MAX_COUNT = 10
ZENDESK_NAME_MAX_LENGTH = 100
ZENDESK_EMAIL_MAX_LENGTH = 100
ZENDESK_SUBJECT_MAX_LENGTH = 100
ZENDESK_GROUP_ID_MAX_LENGTH = 20
ZENDESK_ASSIGNEE_ID_MAX_LENGTH = 20
ZENDESK_DESCRIPTION_MAX_LENGTH = 1500
ZENDESK_TICKET_TYPES = frozenset(["question", "incident", "problem", "task"])
