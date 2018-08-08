
error_names = {
	0x80010001: "Core::Unknown",
	0x80010002: "Core::NotImplemented",
	0x80010003: "Core::InvalidPointer",
	0x80010004: "Core::OperationAborted",
	0x80010005: "Core::Exception",
	0x80010006: "Core::AccessDenied",
	0x80010007: "Core::InvalidHandle",
	0x80010008: "Core::InvalidIndex",
	0x80010009: "Core::OutOfMemory",
	0x8001000A: "Core::InvalidArgument",
	0x8001000B: "Core::Timeout",
	0x8001000C: "Core::InitializationFailure",
	0x8001000D: "Core::CallInitiationFailure",
	0x8001000E: "Core::RegistrationError",
	0x8001000F: "Core::BufferOverflow",
	0x80010010: "Core::InvalidLockState",
	0x80010011: "Core::InvalidSequence",
	0x80010012: "Core::SystemError",
	
	0x80020001: "DDL::InvalidSignature",
	0x80020002: "DDL::IncorrectVersion",
	
	0x80030001: "RendezVous::ConnectionFailure",
	0x80030002: "RendezVous::NotAuthenticated",

	0x80030064: "RendezVous::InvalidUsername",
	0x80030065: "RendezVous::InvalidPassword",
	0x80030066: "RendezVous::UsernameAlreadyExists",
	0x80030067: "RendezVous::AccountDisabled",
	0x80030068: "RendezVous::AccountExpired",
	0x80030069: "RendezVous::ConcurrentLoginDenied",
	0x8003006A: "RendezVous::EncryptionFailure",
	0x8003006B: "RendezVous::InvalidPID",
	0x8003006C: "RendezVous::MaxConnectionsReached",
	0x8003006D: "RendezVous::InvalidGID",
	0x8003006E: "RendezVous::InvalidControlScriptID",
	0x8003006F: "RendezVous::InvalidOperationInLiveEnvironment",
	0x80030070: "RendezVous::DuplicateEntry",
	0x80030071: "RendezVous::ControlScriptFailure",
	0x80030072: "RendezVous::ClassNotFound",
	0x80030073: "RendezVous::SessionVoid",
	0x80030075: "RendezVous::DDLMismatch",
	0x80030076: "RendezVous::InvalidConfiguration",
	
	0x800300C8: "RendezVous::SessionFull",
	0x800300C9: "RendezVous::InvalidGatheringPassword",
	0x800300CA: "RendezVous::WithoutParticipationPeriod",
	0x800300CB: "RendezVous::PersistentGatheringCreationMax",
	0x800300CC: "RendezVous::PersistentGatheringParticipationMax",
	0x800300CD: "RendezVous::DeniedByParticipants",
	0x800300CE: "RendezVous::ParticipantInBlackList",
	0x800300CF: "RendezVous::GameServerMaintenance",
	0x800300D0: "RendezVous::OperationPostpone",
	0x800300D1: "RendezVous::OutOfRatingRange",
	0x800300D2: "RendezVous::ConnectionDisconnected",
	0x800300D3: "RendezVous::InvalidOperation",
	0x800300D4: "RendezVous::NotParticipatedGathering",
	0x800300D5: "RendezVous::MatchmakeSessionUserPasswordUnmatch",
	0x800300D6: "RendezVous::MatchmakeSessionSystemPasswordUnmatch",
	0x800300D7: "RendezVous::UserIsOffline",
	0x800300D8: "RendezVous::AlreadyParticipatedGathering",
	0x800300D9: "RendezVous::PermissionDenied",
	0x800300DA: "RendezVous::NotFriend",
	0x800300DB: "RendezVous::SessionClosed",
	0x800300DC: "RendezVous::DatabaseTemporarilyUnavailable",
	0x800300DD: "RendezVous::InvalidUniqueId",
	0x800300DE: "RendezVous::MatchmakingWithdrawn",
	0x800300DF: "RendezVous::LimitExceeded",
	0x800300E0: "RendezVous::AccountTemporarilyDisabled",
	
	0x80040001: "PythonCore::Exception",
	0x80040002: "PythonCore::TypeError",
	0x80040003: "PythonCore::IndexError",
	0x80040004: "PythonCore::InvalidReference",
	0x80040005: "PythonCore::CallFailure",
	0x80040006: "PythonCore::MemoryError",
	0x80040007: "PythonCore::KeyError",
	0x80040008: "PythonCore::OperationError",
	0x80040009: "PythonCore::ConversionError",
	0x8004000A: "PythonCore::ValidationError",
	
	0x80050001: "Transport::Unknown",
	0x80050002: "Transport::ConnectionFailure",
	0x80050003: "Transport::InvalidUrl",
	0x80050004: "Transport::InvalidKey",
	0x80050005: "Transport::InvalidURLType",
	0x80050006: "Transport::DuplicateEndpoint",
	0x80050007: "Transport::IOError",
	0x80050008: "Transport::Timeout",
	0x80050009: "Transport::ConnectionReset",
	0x8005000A: "Transport::IncorrectRemoteAuthentication",
	0x8005000B: "Transport::ServerRequestError",
	0x8005000C: "Transport::DecompressionFailure",
	0x8005000D: "Transport::ReliableSendBufferFullFatal",
	0x8005000E: "Transport::UPnPCannotInit",
	0x8005000F: "Transport::UPnPCannotAddMapping",
	0x80050010: "Transport::NatPMPCannotInit",
	0x80050011: "Transport::NatPMPCannotAddMapping",
	0x80050013: "Transport::UnsupportedNAT",
	0x80050014: "Transport::DnsError",
	0x80050015: "Transport::ProxyError",
	0x80050016: "Transport::DataRemaining",
	0x80050017: "Transport::NoBuffer",
	0x80050018: "Transport::NotFound",
	0x80050019: "Transport::TemporaryServerError",
	0x8005001A: "Transport::PermanentServerError",
	0x8005001B: "Transport::ServiceUnavailable",
	0x8005001C: "Transport::ReliableSendBufferFull",
	0x8005001D: "Transport::InvalidStation",
	0x8005001E: "Transport::InvalidSubStreamID",
	0x8005001F: "Transport::PacketBufferFull",
	0x80050020: "Transport::NatTraversalError",
	0x80050021: "Transport::NatCheckError",
	
	0x80060001: "DOCore::StationNotReached",
	0x80060002: "DOCore::TargetStationDisconnect",
	0x80060003: "DOCore::LocalStationLeaving",
	0x80060004: "DOCore::ObjectNotFound",
	0x80060005: "DOCore::InvalidRole",
	0x80060006: "DOCore::CallTimeout",
	0x80060007: "DOCore::RMCDispatchFailed",
	0x80060008: "DOCore::MigrationInProgress",
	0x80060009: "DOCore::NoAuthority",
	0x8006000A: "DOCore::NoTargetStationSpecified",
	0x8006000B: "DOCore::JoinFailed",
	0x8006000C: "DOCore::JoinDenied",
	0x8006000D: "DOCore::ConnectivityTestFailed",
	0x8006000E: "DOCore::Unknown",
	0x8006000F: "DOCore::UnfreedReferences",
	0x80060010: "DOCore::JobTerminationFailed",
	0x80060011: "DOCore::InvalidState",
	0x80060012: "DOCore::FaultRecoveryFatal",
	0x80060013: "DOCore::FaultRecoveryJobProcessFailed",
	0x80060014: "DOCore::StationInconsitency",
	0x80060015: "DOCore::AbnormalMasterState",
	0x80060016: "DOCore::VersionMismatch",
	
	0x80650000: "FPD::NotInitialized",
	0x80650001: "FPD::AlreadyInitialized",
	0x80650002: "FPD::NotConnected",
	0x80650003: "FPD::Connected",
	0x80650004: "FPD::InitializationFailure",
	0x80650005: "FPD::OutOfMemory",
	0x80650006: "FPD::RmcFailed",
	0x80650007: "FPD::InvalidArgument",
	0x80650008: "FPD::InvalidLocalAccountID",
	0x80650009: "FPD::InvalidPrincipalID",
	0x8065000A: "FPD::InvalidLocalFriendCode",
	0x8065000B: "FPD::LocalAccountNotExists",
	0x8065000C: "FPD::LocalAccountNotLoaded",
	0x8065000D: "FPD::LocalAccountAlreadyLoaded",
	0x8065000E: "FPD::FriendAlreadyExists",
	0x8065000F: "FPD::FriendNotExists",
	0x80650010: "FPD::FriendNumMax",
	0x80650011: "FPD::NotFriend",
	0x80650012: "FPD::FileIO",
	0x80650013: "FPD::P2PInternetProhibited",
	0x80650014: "FPD::Unknown",
	0x80650015: "FPD::InvalidState",
	0x80650017: "FPD::AddFriendProhibited",
	0x80650019: "FPD::InvalidAccount",
	0x8065001A: "FPD::BlacklistedByMe",
	0x8065001C: "FPD::FriendAlreadyAdded",
	0x8065001D: "FPD::MyFriendListLimitExceed",
	0x8065001E: "FPD::RequestLimitExceed",
	0x8065001F: "FPD::InvalidMessageID",
	0x80650020: "FPD::MessageIsNotMine",
	0x80650021: "FPD::MessageIsNotForMe",
	0x80650022: "FPD::FriendRequestBlocked",
	0x80650023: "FPD::NotInMyFriendList",
	0x80650024: "FPD::FriendListedByMe",
	0x80650025: "FPD::NotInMyBlacklist",
	0x80650026: "FPD::IncompatibleAccount",
	0x80650027: "FPD::BlockSettingChangeNotAllowed",
	0x80650028: "FPD::SizeLimitExceeded",
	0x80650029: "FPD::OperationNotAllowed",
	0x8065002A: "FPD::NotNetworkAccount",
	0x8065002B: "FPD::NotificationNotFound",
	0x8065002C: "FPD::PreferenceNotInitialized",
	0x8065002D: "FPD::FriendRequestNotAllowed",
	
	0x80670001: "Ranking::NotInitialized",
	0x80670002: "Ranking::InvalidArgument",
	0x80670003: "Ranking::RegistrationError",
	0x80670005: "Ranking::NotFound",
	0x80670006: "Ranking::InvalidScore",
	0x80670007: "Ranking::InvalidDataSize",
	0x80670009: "Ranking::PermissionDenied",
	0x8067000A: "Ranking::Unknown",
	0x8067000B: "Ranking::NotImplemented",
	
	0x80680001: "Authentication::NASAuthenticateError",
	0x80680002: "Authentication::TokenParseError",
	0x80680003: "Authentication::HttpConnectionError",
	0x80680004: "Authentication::HttpDNSError",
	0x80680005: "Authentication::HttpGetProxySetting",
	0x80680006: "Authentication::TokenExpired",
	0x80680007: "Authentication::ValidationFailed",
	0x80680008: "Authentication::InvalidParam",
	0x80680009: "Authentication::PrincipalIdUnmatched",
	0x8068000A: "Authentication::MoveCountUnmatch",
	0x8068000B: "Authentication::UnderMaintenance",
	0x8068000C: "Authentication::UnsupportedVersion",
	0x8068000D: "Authentication::ServerVersionIsOld",
	0x8068000E: "Authentication::Unknown",
	0x8068000F: "Authentication::ClientVersionIsOld",
	0x80680010: "Authentication::AccountLibraryError",
	0x80680011: "Authentication::ServiceNoLongerAvailable",
	0x80680012: "Authentication::UnknownApplication",
	0x80680013: "Authentication::ApplicationVersionIsOld",
	
	0x80690001: "DataStore::Unknown",
	0x80690002: "DataStore::InvalidArgument",
	0x80690003: "DataStore::PermissionDenied",
	0x80690004: "DataStore::NotFound",
	0x80690005: "DataStore::AlreadyLocked",
	0x80690006: "DataStore::UnderReviewing",
	0x80690007: "DataStore::Expired",
	0x80690008: "DataStore::InvalidCheckToken",
	0x80690009: "DataStore::SystemFileError",
	0x8069000A: "DataStore::OverCapacity",
	0x8069000B: "DataStore::OperationNotAllowed",
	0x8069000C: "DataStore::InvalidPassword",
	0x8069000D: "DataStore::ValueNotEqual",
	
	0x806C0001: "ServiceItem::Unknown",
	0x806C0002: "ServiceItem::InvalidArgument",
	0x806C0003: "ServiceItem::EShopUnknownHttpError",
	0x806C0004: "ServiceItem::EShopResponseParseError",
	0x806C0005: "ServiceItem::NotOwned",
	0x806C0006: "ServiceItem::InvalidLimitationType",
	0x806C0007: "ServiceItem::ConsumptionRightShortage",
	
	0x806F0001: "MatchmakeReferee::Unknown",
	0x806F0002: "MatchmakeReferee::InvalidArgument",
	0x806F0003: "MatchmakeReferee::AlreadyExists",
	0x806F0004: "MatchmakeReferee::NotParticipatedGathering",
	0x806F0005: "MatchmakeReferee::NotParticipatedRound",
	0x806F0006: "MatchmakeReferee::StatsNotFound",
	0x806F0007: "MatchmakeReferee::RoundNotFound",
	0x806F0008: "MatchmakeReferee::RoundArbitrated",
	
	0x80700001: "Subscriber::Unknown",
	0x80700002: "Subscriber::InvalidArgument",
	0x80700003: "Subscriber::OverLimit",
	0x80700004: "Subscriber::PermissionDenied",
	
	0x80710001: "Ranking2::Unknown",
	0x80710002: "Ranking2::InvalidArgument",
	0x80710003: "Ranking2::InvalidScore"
}

error_codes = {name: code for code, name in error_names.items()}
