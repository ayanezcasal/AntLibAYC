MESSAGE_TX_SYNC = 0xA4
MESSAGE_TX_SYNC_LEGACY = 0xA5

# Configuration messages
MESSAGE_CHANNEL_UNASSIGN = 0x41  # [Channel number]
MESSAGE_CHANNEL_ASSIGN = 0x42  # [Channel number, Channel type, Network number, Extended assign't (optional)]
MESSAGE_CHANNEL_ID = 0x51  # [Channel number, Device number (2bytes), Device type ID, Trans. type]
MESSAGE_CHANNEL_PERIOD = 0x43  # [Channel number, Channel period (2bytes)]
MESSAGE_CHANNEL_SEARCH_TIMEOUT = 0x44  # [Channel number, Search timeout]
MESSAGE_CHANNEL_FREQUENCY = 0x45  # [Channel number, RF frequency]
MESSAGE_NETWORK_KEY = 0x46  # [Network number, Network key (8bytes)]
MESSAGE_TX_POWER = 0x47  # [0, TX Power]
MESSAGE_SEARCH_WAVEFORM = 0x49  # [Channel number, Waveform (2bytes)]
MESSAGE_ADD_CHANNEL_ID_TO_LIST = 0x59  # [Channel number, Device number, Device type ID, Trans. type, List index]
MESSAGE_ADD_ENCRYPION_ID_TO_LIST = 0x59  # [Channel number, Encryption ID (4bytes), List index]
MESSAGE_CONFIG_ID_LIST = 0x5A  # [Channel number, List size, Exclude]
MESSAGE_CHANNEL_TX_POWER = 0x60  # [Channel number, Transmit power]
MESSAGE_LOW_PRIORITY_SEARCH_TIMEOUT = 0x63  # [Channel number, Search timeout]
MESSAGE_PROXIMITY_SEARCH = 0x71
MESSAGE_ENABLE_EXT_RX_MESSAGES = 0x66 # [0, enable]


# Notification messages
MESSAGE_STARTUP = 0x6F

# Control messages
MESSAGE_SYSTEM_RESET = 0x4A
MESSAGE_CHANNEL_OPEN = 0x4B
MESSAGE_CHANNEL_CLOSE = 0x4C
MESSAGE_CHANNEL_REQUEST = 0x4D

# Data messages
MESSAGE_CHANNEL_BROADCAST_DATA = 0x4E
MESSAGE_CHANNEL_ACKNOWLEDGED_DATA = 0x4F
MESSAGE_CHANNEL_BURST_DATA = 0x50

# Channel event messages
MESSAGE_CHANNEL_EVENT = 0x40

# Requested response messages
MESSAGE_CHANNEL_STATUS = 0x52
MESSAGE_VERSION = 0x3E
MESSAGE_CAPABILITIES = 0x54
MESSAGE_SERIAL_NUMBER = 0x61

# Message parameters
CHANNEL_TYPE_TWOWAY_RECEIVE = 0x00
CHANNEL_TYPE_TWOWAY_TRANSMIT = 0x10
CHANNEL_TYPE_SHARED_RECEIVE = 0x20
CHANNEL_TYPE_SHARED_TRANSMIT = 0x30
CHANNEL_TYPE_ONEWAY_RECEIVE = 0x40
CHANNEL_TYPE_ONEWAY_TRANSMIT = 0x50
RADIO_TX_POWER_MINUS20DB = 0x00
RADIO_TX_POWER_MINUS10DB = 0x01
RADIO_TX_POWER_0DB = 0x02
RADIO_TX_POWER_PLUS4DB = 0x03

# Message Codes
RESPONSE_NO_ERROR = 0x00
EVENT_RX_SEARCH_TIMEOUT = 0x01
EVENT_RX_FAIL = 0x02
EVENT_TX = 0x03
EVENT_TRANSFER_RX_FAILED = 0x04
EVENT_TRANSFER_TX_COMPLETED = 0x05
EVENT_TRANSFER_TX_FAILED = 0x06
EVENT_CHANNEL_CLOSED = 0x07
EVENT_RX_FAIL_GO_TO_SEARCH = 0x08
EVENT_CHANNEL_COLLISION = 0x09
EVENT_TRANSFER_TX_START = 0x0A
EVENT_TRANSFER_NEXT_DATA_BLOCK = 0x11
CHANNEL_IN_WRONG_STATE = 0x15
CHANNEL_NOT_OPENED = 0x16
CHANNEL_ID_NOT_SET = 0x18
CLOSE_ALL_CHANNELS = 0x19
TRANSFER_IN_PROGRESS = 0x1F
TRANSFER_SEQUENCE_NUMBER_ERROR = 0x20
TRANSFER_IN_ERROR = 0x21
MESSAGE_SIZE_EXCEEDS_LIMIT = 0x27
INVALID_MESSAGE = 0x28
INVALID_NETWORK_NUMBER = 0x29
INVALID_LIST_ID = 0x30
INVALID_SCAN_TX_CHANNEL = 0x31
INVALID_PARAMETER_PROVIDED = 0x33
EVENT_SERIAL_QUE_OVERFLOW = 0x34
EVENT_QUEUE_OVERFLOW = 0x35
ENCRYPT_NEGOTIATION_SUCCESS = 0x38
ENCRYPT_NEGOTIATION_FAIL = 0x39
NVM_FULL_ERROR = 0x40
NVM_WRITE_ERROR = 0x41
USB_STRING_WRITE_FAIL = 0x70
MESG_SERIAL_ERROR_ID = 0xAE

CHANNEL_STATE_UNASSIGNED = 0x00
CHANNEL_STATE_ASSIGNED = 0x01
CHANNEL_STATE_SEARCHING = 0x02
CHANNEL_STATE_TRACKING = 0x03
CAPABILITIES_NO_RECEIVE_CHANNELS = 0x01
CAPABILITIES_NO_TRANSMIT_CHANNELS = 0x02
CAPABILITIES_NO_RECEIVE_MESSAGES = 0x04
CAPABILITIES_NO_TRANSMIT_MESSAGES = 0x08
CAPABILITIES_NO_ACKNOWLEDGED_MESSAGES = 0x10
CAPABILITIES_NO_BURST_MESSAGES = 0x20
CAPABILITIES_NETWORK_ENABLED = 0x02
CAPABILITIES_SERIAL_NUMBER_ENABLED = 0x08
CAPABILITIES_PER_CHANNEL_TX_POWER_ENABLED = 0x10
CAPABILITIES_LOW_PRIORITY_SEARCH_ENABLED = 0x20
CAPABILITIES_SCRIPT_ENABLED = 0x40
CAPABILITIES_SEARCH_LIST_ENABLED = 0x80
CAPABILITIES_LED_ENABLED = 0x01
CAPABILITIES_EXT_MESSAGE_ENABLED = 0x02
CAPABILITIES_SCAN_MODE_ENABLED = 0x04
CAPABILITIES_PROX_SEARCH_ENABLED = 0x10
CAPABILITIES_EXT_ASSIGN_ENABLED = 0x20
CAPABILITIES_FS_ANTFS_ENABLED = 0x40
TIMEOUT_NEVER = 0xFF

OPEN_RX_SCAN_MODE = 0x5B


ANTPLUS_NETWORK_KEY = b'\xB9\xA5\x21\xFB\xBD\x72\xC3\x45'
ANTFS_KEY = b'\xA8\xA4\x23\xB9\xF5\x5E\x63\xC1'
PUBLIC_NETWORK_KEY = b'\xE8\xE4\x21\x3B\x55\x7A\x67\xC1'
