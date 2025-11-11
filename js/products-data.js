// Complete GATEMAN Product Database - 70+ Models
const productsData = [
    // Premium Series
    {
        id: 'GM-1000L',
        name: 'GM-1000L',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '1,280,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-gm-1000l.png',
        description: '게이트맨 최초 커스터마이징 도어락. 모터락 기술과 IoT 통합 기능을 갖춘 프리미엄 정맥인식 스마트도어락',
        features: ['정맥인식', '지문인식 (QuickPass)', '비밀번호', '카드', '0초 즉시 잠김', '이중 잠금 후크 메커니즘', '허위번호 입력', '지문흔적 방지', '내부강제잠금', '침입/파손 알람', '모터락 푸시풀', '배터리 교체 알림', '에티켓 모드', '음성안내', '비상전원단자', 'IoT 원격제어', '실시간 알림', '가족 출입 알림', '일회용 비밀번호'],
        specs: {
            auth: '정맥, 지문 (100개), 비밀번호, 카드 (100개), 기계식열쇠',
            color: '블랙, 메탈릭 스톤 그레이 (핸들바: 메탈그레이/실버/블랙/브라운)',
            battery: 'AA 4개 (약 1년)',
            dimensions: '전면: 385.5 x 117.7 x 45.1mm / 본체: 385.5 x 117.7 x 56.8mm',
            material: '알루미늄 DC/ABS',
            iot: '지원 (Gateman Access - DOT/Dual Communication Pack 필요)'
        },
        popular: true
    },
    {
        id: 'GM-900S',
        name: 'GM-900S',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '980,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/GM-900S_1.png',
        description: '우아한 곡선 디자인의 프리미엄 스마트도어락. 고급 보안 기술과 편리한 모터락 기능 결합',
        features: ['QuickPass 지문인식 (100개)', '터치키패드', '카드 (100개)', '비밀번호 (100개)', '0초 즉시 잠김', '이중 잠금 후크 메커니즘', '내화재질 (1000℃)', '화재 갭 밀폐', '내부강제잠금 (5초)', '파손감지 알람', '허위번호 입력', '타임락 (5회 실패시)', '모터락 푸시풀', '배터리 교체 알림', '에티켓 모드', '다국어 음성안내', '비상전원단자', 'Gateman Dot NFC', 'IoT 원격제어', '실시간 알림', '임시 비밀번호'],
        specs: {
            auth: '지문 (100개), 비밀번호 (100개), 카드 (100개), 기계식열쇠',
            color: '실버',
            battery: 'AA 4개 (1일 10회 사용시 약 1년)',
            dimensions: '전면: 102 x 383.4 x 50mm / 본체: 86.9 x 384.9 x 49.2mm',
            material: 'PC, AIDC 폴리머',
            waterproof: 'IPX4 (0.8bar 10L/min 스프레이)',
            durability: '버튼 60,000회, UV 72시간, 염수분무 96시간 테스트',
            iot: '지원 (Gateman Access - DOT/Dual Communication Pack 필요)'
        },
        popular: true
    },
    {
        id: 'GM-500S',
        name: 'GM-500S',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '780,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/GM-500S_1.png',
        description: '세련된 미니멀 디자인의 프리미엄 스마트도어락. 모터락 푸시풀 기능과 고급 보안 기술 탑재',
        features: ['터치키패드', '카드 (100개)', '비밀번호 (100개)', '즉시 잠김', '내화재질 (1000℃)', '허위번호 입력', '내부강제잠금 (5초)', '파손감지 알람', '타임락 (5회 실패시)', '지문흔적 방지', '모터락 푸시풀', '배터리 교체 알림', '에티켓 모드 (5초)', '비상전원단자', 'IoT 원격제어', '실시간 알림', '임시 비밀번호', '가족 출입 알림', '침입 경보'],
        specs: {
            auth: '비밀번호 (100개), 카드 (100개), 기계식열쇠',
            color: '블랙',
            battery: 'AA 4개 (1일 10회 사용시 약 1년)',
            dimensions: '전면: 102 x 383.4 x 50mm / 본체: 86.9 x 384.9 x 49.2mm',
            material: 'PC, AIDC 폴리머',
            iot: '지원 (Gateman Access 필요)'
        },
        popular: false
    },
    {
        id: 'GP-900D',
        name: 'GP-900D',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '1,180,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/gp900d.png',
        description: '지문인식과 푸시풀 동작을 결합한 프리미엄 도어락. 1초 빠른 잠금 해제 및 10배 강력한 후크 메커니즘 적용',
        features: ['QuickPass 지문인식 (100개)', '숫자키패드', '카드 (100개)', '후크 메커니즘 (SUS재질)', '1초 자동잠금', '허위지문 방지', '내부강제잠금 (5초)', '침입 알람', '허위번호 입력', '3분 잠금 (5회 실패시)', '배터리 교체 알림', '푸시형 배터리 커버', '에티켓 모드', '음성안내', '비상전원단자', 'IoT 원격제어', '실시간 알림', '출입 이력', '일회용 비밀번호'],
        specs: {
            auth: '지문 (100개), 비밀번호, 카드 (100개), 기계식열쇠',
            color: '다크실버, 블랙',
            battery: 'AA 4개 (1일 10회 사용시 약 1년)',
            dimensions: '전면: 74 x 380 x 80mm / 본체: 74 x 380 x 79mm',
            material: '알루미늄 다이캐스트 / 폴리카보네이트 (V0등급)',
            waterproof: 'IPX4 (0.8bar 10L/min 스프레이)',
            durability: '버튼 60,000회, UV 72시간, 염수분무 96시간 테스트',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: false
    },
    {
        id: 'GP-700D',
        name: 'GP-700D',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '880,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/GP-700D-240730.png',
        description: '편리한 당기고 밀어 잠금 해제 푸시풀 도어락. 1초 즉시 잠김과 강화된 후크 메커니즘으로 보안 강화',
        features: ['터치키패드', '카드 (100개)', '1초 즉시 잠김 (1-5초 설정 가능)', '이중 잠금 후크 메커니즘 (SUS재질)', '허위번호 입력', '지문흔적 소거', '내부강제잠금 (5초)', '파손방지 알람', '3분 잠금 (5회 실패시)', '배터리 교체 알림', '푸시형 배터리 커버', '에티켓 모드 (5초)', '음성안내', '비상전원단자', 'IoT 원격제어', '실시간 알림', '가족 출입 알림', '일회용 비밀번호', '무단 출입 알람'],
        specs: {
            auth: '비밀번호, 카드 (100개), 기계식열쇠',
            color: '다크실버, 블랙',
            battery: 'AA 4개 (1일 10회 사용시 약 1년)',
            dimensions: '전면: 74 x 380 x 80mm / 본체: 74 x 380 x 79mm',
            material: '알루미늄 다이캐스트 / 폴리카보네이트 (V0등급)',
            waterproof: 'IPX4 (0.8bar 10L/min 스프레이)',
            durability: '버튼 60,000회, UV 72시간, 염수분무 96시간 테스트',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: true
    },
    {
        id: 'GP-500R',
        name: 'GP-500R',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '680,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-gp-500r_new.png',
        description: '초슬림 17mm 두께의 세련된 디자인. 아름다운 타이포그래피와 푸시풀 편의성을 갖춘 실용형 프리미엄 도어락',
        features: ['터치키패드', '카드 (100개)', '허위번호 입력', '지문흔적 방지', '내부강제잠금 (5초)', '파손 알람', '3분 잠금 (5회 실패시)', '배터리 교체 알림', '푸시형 배터리 커버', '에티켓 모드 (5초)', '비상전원단자', '푸시풀 (핸들 회전 불필요)', '1초 즉시 잠김', 'IoT 원격제어', '가족 출입 알림', '실시간 알림', '일회용 비밀번호'],
        specs: {
            auth: '비밀번호, 카드 (100개), 기계식열쇠',
            color: '모던골드, 블랙',
            battery: 'AA 4개 (1일 10회 사용시 약 1년)',
            dimensions: '전면: 64.5 x 380 x 80mm / 본체: 84 x 380 x 77mm',
            material: '알루미늄 다이캐스트 / 폴리카보네이트 V0',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: false
    },
    {
        id: 'GP-500RC',
        name: 'GP-500RC',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '720,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/240925_gp_500rc.png',
        description: 'LG화학 협업 크림 컬러 옵션 제공. 초슬림 17mm 디자인과 1000℃ 내화 기술을 갖춘 카드형 프리미엄 도어락',
        features: ['터치키패드', '카드 (100개)', '국내 KS 기준 초과 안전성', '내화기술 (1000℃ 60분+)', '60℃ 자동 잠금해제', '허위번호 입력', '지문흔적 방지', '내부강제잠금', '침입/파손 알람', '1초 자동잠금', '3분 잠금 (5회 실패시)', '비상전원단자 (9V)', '배터리 교체 알림', '푸시형 배터리 커버', '에티켓/무음 모드 (3초)', 'IoT 원격제어', '실시간 알림', '일회용 비밀번호', '출입 이력'],
        specs: {
            auth: '비밀번호, 카드 (100개), 기계식열쇠',
            color: '크림, 모던골드&블랙',
            battery: 'AA 4개 (1일 10회 사용시 약 1년)',
            dimensions: '전면: 64.5 x 380 x 80mm / 본체: 84 x 380 x 77mm',
            material: '알루미늄 다이캐스트, V0 PC',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: true
    },
    {
        id: 'GP-300R',
        name: 'GP-300R',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '580,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/GP-300R-2.png',
        description: '실속형 푸시풀 도어락',
        features: ['지문인식', '비밀번호', '푸시풀', '자동잠금'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'GP-300UN',
        name: 'GP-300UN',
        category: 'premium',
        type: 'pushpull',
        series: 'Premium',
        price: '520,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/gp_300un.png',
        description: '유니버설 디자인 도어락',
        features: ['지문인식', '비밀번호', '푸시풀'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },

    // G-SUIT Series
    {
        id: 'GSUIT-SCAN-PLUS',
        name: 'G-SUIT scan+',
        category: 'gsuit',
        type: 'pushpull',
        series: 'G-SUIT',
        price: '920,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-g-suit-scan_new2.png',
        description: '시장에서 가장 빠르고 편리한 도어락. QuickPass 지문인식과 푸시풀 동작을 동시에 수행하는 프리미엄 스마트도어락',
        features: ['QuickPass 지문인식 (Goodix, 100개)', '카드', '터치패드', '이중 후크 메커니즘 (10배 강력)', '3분 잠금 (5회 실패시)', '허위번호 입력 (무제한)', '내화기술', '논스톱 푸시풀', '스마트패드 (개별 LED)', '고급 음성안내', '무음 모드 (3초)', 'IPX4 방수', 'IoT 통합 (Gateman Access)', '가족 출입 알림', '원격 제어', '실시간 알림', '임시 비밀번호'],
        specs: {
            auth: '지문 (100개), 비밀번호, 카드, 기계식열쇠',
            color: '모던골드',
            battery: 'AAA 4개',
            material: '풀메탈 바디',
            waterproof: 'IPX4',
            durability: '버튼 60,000회, UV 72시간, 염수분무 96시간 테스트',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: false
    },
    {
        id: 'GSUIT-TOUCH-PLUS',
        name: 'G-SUIT touch+',
        category: 'gsuit',
        type: 'pushpull',
        series: 'G-SUIT',
        price: '820,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-g-suit-touch_new.png',
        description: '깊이감 있는 디자인과 완벽한 품질의 네오클래식 스타일. 시간이 지날수록 가치가 높아지는 프리미엄 푸시풀 도어락',
        features: ['카드 (4개 포함)', '논스톱 푸시풀', '이중 잠금 후크 (5배 강력)', 'IPX4 방수', '3분 잠금 (5회 실패시)', '허위번호 입력', '스마트패드 (개별 LED)', '고급 음성안내', '스마트 에티켓 모드 (3초)', '푸시풀 (핸들 불필요)', '배터리 4개 포함', 'IoT 통합 (Gateman Access)', '가족 출입 알림', '실시간 알림', '원격 비밀번호 변경', '일회용 비밀번호'],
        specs: {
            auth: '비밀번호, 카드, 기계식열쇠',
            color: '메트로 브론즈',
            battery: 'AA 4개',
            waterproof: 'IPX4',
            durability: '버튼 60,000회, UV 72시간, 염수분무 96시간 테스트',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: true
    },
    {
        id: 'GSUIT-SIMPLE-PLUS',
        name: 'G-SUIT simple+',
        category: 'gsuit',
        type: 'pushpull',
        series: 'G-SUIT',
        price: '680,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-g-suit-simple.png',
        description: '압도적인 디자인과 최첨단 기술의 조화. 다양한 문 스타일에 어울리는 미니멀리스트 디자인의 스마트도어락',
        features: ['IPX4 방수', '버튼 60,000회 내구성', '염수분무 96시간 테스트', 'UV 72시간 노출 저항', '3분 잠금 (5회 실패시)', '허위번호 입력', '푸시풀 메커니즘', '스마트패드 (개별 LED)', '다중 인증 방식', 'IoT 호환 (Gateman Access)', '원격 앱 제어', '가족 출입 알림', '실시간 알림', '임시 게스트 비밀번호', '원격 비밀번호 변경', '도어락 상태 모니터링'],
        specs: {
            auth: '비밀번호, 카드, 기계식열쇠',
            color: '모던골드',
            battery: 'AA 4개',
            waterproof: 'IPX4',
            durability: '버튼 60,000회, UV 72시간, 염수분무 96시간 테스트',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: false
    },

    // G-CLICK Series
    {
        id: 'GCLICK-SCAN-PLUS',
        name: 'G-CLICK scan+',
        category: 'gclick',
        type: 'pushpull',
        series: 'G-CLICK',
        price: '880,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/fh.png',
        description: '무타공 설치 가능한 지문인식 푸시풀 도어락. 접촉 시 지문인식으로 즉시 개방되는 QuickPass 기술 탑재',
        features: ['QuickPass 지문인식', '카드', '이중 후크 잠금', 'IPX4 방수', '3분 잠금 (5회 실패시)', '허위번호 입력', '무타공 설치', '푸시풀 핸들 (밀고/당기기)', '스마트패드 (개별 LED)', '고급 음성안내', 'IoT 연결 (Gateman Access)', '가족 출입 알림', '원격 제어', '실시간 알림', '임시 게스트 비밀번호', '원격 잠금/해제'],
        specs: {
            auth: '지문, 비밀번호, 카드, 기계식열쇠',
            color: '다크그레이',
            battery: 'AA 4개',
            waterproof: 'IPX4',
            durability: '버튼 60,000회, 염수분무 96시간, UV 72시간 테스트',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: false
    },
    {
        id: 'GCLICK-TOUCH-PLUS',
        name: 'G-CLICK touch+',
        category: 'gclick',
        type: 'pushpull',
        series: 'G-CLICK',
        price: '780,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/c1.png',
        description: '무타공 설치로 기존 문 손상 없이 설치. 원클릭 동작으로 현대 생활에 최적화된 터치패드 스마트도어락',
        features: ['4자리 비밀번호', '카드 (4개 포함)', '이중 후크 메커니즘 (5배 강력)', '3분 자동잠금 (5회 실패시)', '엿보기 방지 (무제한 허위번호)', '후크 (10배 강력 저항)', '무타공 설치', '논스톱 푸시풀 (밀고/당기기)', '개별 LED 스마트패드', '고급 음성안내', 'IoT 통합 (Gateman Access)', '가족 출입 알림', '원격 제어', '실시간 알림', '일회용 비밀번호'],
        specs: {
            auth: '비밀번호, 카드, 세이프티키',
            color: '다크그레이',
            battery: 'AA 4개',
            waterproof: 'IPX4 (0.8bar 10L/min)',
            durability: '버튼 60,000회 (99%+ 성공률), UV 72시간, 염수분무 96시간 테스트',
            iot: '지원 (Gateman Access - Dual Communication Pack/Connect 필요)'
        },
        popular: false
    },

    // G-GRAB Series
    {
        id: 'GGRAB-SCAN-PLUS',
        name: 'G-GRAB scan+',
        category: 'ggrab',
        type: 'pushpull',
        series: 'G-GRAB',
        price: '850,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-grab100-fh.png',
        description: '한층 업그레이드된 국내 최초 레버형 QuickPass 지문인식 도어락. 레버를 잡는 동시에 지문 스캔으로 매끄러운 출입',
        features: ['QuickPass 지문인식 (레버 잡으면서)', '이중 잠금 후크 (5배 강력)', '세이프 핸들 메커니즘', '3분 잠금 (5회 실패시)', '내화기술 (1000℃)', '허위번호 입력 (무제한)', '스마트 음성안내', '디지털 스마트패드 (개별 조명)', 'IPX4 방수', '이중 통신 모듈 슬롯', 'Smart Living 3.0 앱', '원격 잠금/해제', '가족 출입 이력', '실시간 침입/화재 알림', '접근시 자동 잠금해제'],
        specs: {
            auth: '지문, 비밀번호, 카드, 기계식열쇠',
            color: '모던골드',
            battery: 'AA 4개',
            waterproof: 'IPX4',
            durability: 'UV 72시간, 버튼 60,000회, 염수분무 96시간 테스트',
            iot: '지원 (Smart Living / Gateman Access)'
        },
        popular: false
    },
    {
        id: 'GGRAB-TOUCH',
        name: 'G-GRAB touch',
        category: 'ggrab',
        type: 'pushpull',
        series: 'G-GRAB',
        price: '750,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-grabtouch.png',
        description: '최상의 그립감과 프리미엄 디자인의 레버형 도어락. QuickPass 지문인식과 다중 인증 방식 지원',
        features: ['QuickPass 지문인식 (국내 최초 레버형)', '비밀번호', '카드', '이중 후크 메커니즘', '세이프 핸들 (버튼 누르며 조작)', '3분 잠금 (5회 실패시)', '멀티 모듈 이중 통신 슬롯', '고급 음성안내', '허위번호 기능', 'Smart Living 통합', 'IPX4 방수 (0.8bar 10L/min)', '내화재질 및 기술', '앱 기반 제어', '출입 이력', '실시간 알림'],
        specs: {
            auth: '지문, 비밀번호, 카드, 기계식열쇠',
            color: '모던골드',
            battery: 'AA 4개',
            waterproof: 'IPX4',
            durability: 'UV 72시간, 버튼 60,000회, 염수분무 96시간 테스트',
            iot: '지원 (Smart Living / Gateman Access)'
        },
        popular: false
    },

    // Other Push-Pull Types
    {
        id: 'G-SWIPE',
        name: 'G-SWIPE',
        category: 'pushpull',
        type: 'pushpull',
        series: 'G Series',
        price: '650,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-g-swipe.png',
        description: '압도적인 디자인과 기술력의 푸시풀 도어락. 빠르고 편리한 출입과 5배 강화된 후크 메커니즘 적용',
        features: ['비밀번호', '지문인식', '5배 강화 후크 메커니즘', '내화기술 (1000℃)', '실시간 화재/침입/파손 알람', '출입 이력 추적', '푸시풀 조작', '위치기반 스마트키', '원격 잠금/해제', '앱 기반 설정', 'GATEMAN Access 서비스', '가족 출입 알림', '실시간 상태 모니터링', '종합 출입 기록'],
        specs: {
            auth: '비밀번호, 지문, 스마트키 (모바일앱), 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 4개',
            iot: '지원 (Gateman Access)'
        },
        popular: false
    },
    {
        id: 'G-TOUCH',
        name: 'G-TOUCH',
        category: 'pushpull',
        type: 'pushpull',
        series: 'G Series',
        price: '620,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-g-touch.png',
        description: '터치스크린 도어락',
        features: ['지문인식', '비밀번호', '푸시풀', '터치스크린'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'G-SLIDE',
        name: 'G-SLIDE',
        category: 'pushpull',
        type: 'pushpull',
        series: 'G Series',
        price: '590,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-g-slide.png',
        description: '슬라이드 방식 도어락',
        features: ['지문인식', '비밀번호', '푸시풀'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },

    // Mortise Type (Handle Integrated)
    {
        id: 'GL-200H',
        name: 'GL-200H',
        category: 'mortise',
        type: 'mortise',
        series: 'GL Series',
        price: '480,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-gl-200h.png',
        description: '핸들일체형 도어락',
        features: ['지문인식', '비밀번호', '핸들일체형', '자동잠금'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'GR-20',
        name: 'GR-20',
        category: 'mortise',
        type: 'mortise',
        series: 'GR Series',
        price: '420,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-gr-20.png',
        description: '레버형 도어락',
        features: ['지문인식', '비밀번호', '레버핸들'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버, 골드',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'GR-SASH',
        name: 'GR-SASH',
        category: 'mortise',
        type: 'mortise',
        series: 'GR Series',
        price: '380,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-gr-sash.png',
        description: '새시형 도어락',
        features: ['지문인식', '비밀번호', '새시형'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'GR-CLIP',
        name: 'GR-CLIP',
        category: 'mortise',
        type: 'mortise',
        series: 'GR Series',
        price: '350,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-gr-clip.png',
        description: '클립형 도어락',
        features: ['지문인식', '비밀번호'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'GR-FRAME',
        name: 'GR-FRAME',
        category: 'mortise',
        type: 'mortise',
        series: 'GR Series',
        price: '320,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-gr-flame.png',
        description: '프레임형 도어락',
        features: ['지문인식', '비밀번호'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },

    // Rim Type (Handle Separate)
    {
        id: 'A330-FH',
        name: 'A330-FH',
        category: 'rim',
        type: 'rim',
        series: 'A Series',
        price: '520,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb1.png',
        description: '세계에서 가장 빠르고 편리한 지문인식 푸시풀 도어락. 복제 불가능한 스캔형 지문인식과 후크 메커니즘 적용',
        features: ['지문인식 (스캔형, 복제불가)', '숫자키패드', '후크 메커니즘 (이중 잠금)', '내화기술 (국내최초 1000℃)', '논스톱 푸시풀', '곡선형 키패드', '스마트 에티켓 무음모드 (3초)', '풀메탈 바디', '고급 인서트 필름', '배터리 4개 포함'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 4개',
            material: '풀메탈 바디',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'X300-FH',
        name: 'X300-FH',
        category: 'rim',
        type: 'rim',
        series: 'X Series',
        price: '480,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb2.png',
        description: '세계에서 가장 빠르고 편리한 푸시풀 도어락. 약 1.8초 빠른 문 개방과 핸들 조작을 결합한 지문인식 도어락',
        features: ['QuickPass 지문인식', '카드 (등록된 카드만)', '터치패드 비밀번호', '허위번호 기능', '후크 메커니즘 (이중 잠금)', '3분 잠금 (5회 실패시)', '내화기술 (1000℃, 국내최초)', '푸시바 화재 탈출', '논스톱 푸시풀', '스마트패드 (개별 LED)', '앱 원격 접근', '위치기반 스마트키', '가족 출입 이력', '원격 잠금/해제', '초슬림 일체형 핸들', '풀메탈 바디'],
        specs: {
            auth: '지문, 비밀번호, 카드, 기계식열쇠',
            color: '모던골드',
            battery: 'AA 4개',
            material: '풀메탈 바디',
            iot: '지원 (앱 연동)'
        },
        popular: false
    },
    {
        id: 'F300-FH',
        name: 'F300-FH',
        category: 'rim',
        type: 'rim',
        series: 'F Series',
        price: '450,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-f300-fh.png',
        description: '5배 강화된 체결강도의 후크 메커니즘 적용. 국내 최초 1000℃ 내화 기술을 갖춘 핸들일체형 도어락',
        features: ['후크 메커니즘 (5배 강화)', '내화기술 (국내최초 1000℃)', '화재대응 기술', '핸들일체형 디자인', '글로벌 엔지니어링 인정', '배터리 4개 포함'],
        specs: {
            auth: '비밀번호, 카드, 기계식열쇠',
            color: '실버',
            battery: 'AA 4개',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'E300-FH',
        name: 'E300-FH',
        category: 'rim',
        type: 'rim',
        series: 'E Series',
        price: '420,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb3.png',
        description: '림형 실용 도어락',
        features: ['지문인식', '비밀번호', '림형'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'R200-CH',
        name: 'R200-CH',
        category: 'rim',
        type: 'rim',
        series: 'R Series',
        price: '380,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb4.png',
        description: '림형 카드 도어락',
        features: ['비밀번호', '카드', '림형'],
        specs: {
            auth: '비밀번호, 카드, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'P380-FH',
        name: 'P380-FH',
        category: 'rim',
        type: 'rim',
        series: 'P Series',
        price: '490,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-p380-fh.png',
        description: '림형 프리미엄',
        features: ['지문인식', '비밀번호', '카드', '림형'],
        specs: {
            auth: '지문, 비밀번호, 카드, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'M180-FH',
        name: 'M180-FH',
        category: 'rim',
        type: 'rim',
        series: 'M Series',
        price: '360,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-m180-fh.png',
        description: '림형 기본형',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'J20-IH',
        name: 'J20-IH',
        category: 'rim',
        type: 'rim',
        series: 'J Series',
        price: '340,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-j20-ih.png',
        description: '림형 인터폰연동',
        features: ['비밀번호', '인터폰연동', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'J20-DM',
        name: 'J20-DM',
        category: 'rim',
        type: 'rim',
        series: 'J Series',
        price: '320,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-j20-ih.png',
        description: '림형 도어맨',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'A20-CH',
        name: 'A20-CH',
        category: 'rim',
        type: 'rim',
        series: 'A Series',
        price: '300,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb5.png',
        description: '림형 카드형',
        features: ['비밀번호', '카드', '림형'],
        specs: {
            auth: '비밀번호, 카드, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'A20-SH',
        name: 'A20-SH',
        category: 'rim',
        type: 'rim',
        series: 'A Series',
        price: '280,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb6.png',
        description: '림형 심플',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },

    // WIDE Series
    {
        id: 'WIDE-DANDY',
        name: 'WIDE DANDY',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '280,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-dandy.png',
        description: '2중 체결로 5배 강력해진 Interlock Hook 메커니즘. 기존 도어록과 차원이 다른 핸들분리형 스마트도어락',
        features: ['이중 잠금 Interlock Hook (5배 강력)', '내화기술 (1000℃)', '충격 무력화 기술', 'IoT 서비스 통합 (Gateman Access, DOT, Smart Living)', '카드 (4개 포함)', '배터리 4개 포함'],
        specs: {
            auth: '카드, 기계식열쇠',
            color: '실버',
            battery: 'AA 4개',
            iot: '지원 (Gateman Access/DOT/Smart Living)'
        },
        popular: true
    },
    {
        id: 'WIDE-CRUZ2',
        name: 'WIDE CRUZ2',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '260,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-cruz2.png',
        description: '크루즈 2세대',
        features: ['지문인식', '비밀번호', '림형'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WIDE-RINO',
        name: 'WIDE RINO',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '250,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-rino.png',
        description: '리노 스타일',
        features: ['지문인식', '비밀번호', '림형'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WIDE-VELA2',
        name: 'WIDE VELA2',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '240,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-vela2.png',
        description: '벨라 2세대',
        features: ['비밀번호', '카드', '림형'],
        specs: {
            auth: '비밀번호, 카드, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WIDE-SPLIT',
        name: 'WIDE SPLIT',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '230,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-split.png',
        description: '분리형 디자인',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WIDE-FINGUS',
        name: 'WIDE FINGUS',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '220,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-fingus.png',
        description: '핑거스 모델',
        features: ['지문인식', '비밀번호', '림형'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WIDE-VIENA',
        name: 'WIDE VIENA',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '210,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-viena.png',
        description: '비에나 스타일',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WIDE-PLATO',
        name: 'WIDE PLATO',
        category: 'wide',
        type: 'rim',
        series: 'WIDE',
        price: '200,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-plato.png',
        description: '플라토 기본형',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },

    // W Series
    {
        id: 'WF-20',
        name: 'WF-20',
        category: 'wide',
        type: 'rim',
        series: 'W Series',
        price: '280,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-clasik.png',
        description: 'W 시리즈 지문형',
        features: ['지문인식', '비밀번호', '림형'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WV-40',
        name: 'WV-40',
        category: 'wide',
        type: 'rim',
        series: 'W Series',
        price: '250,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-wv-43.png',
        description: 'W 시리즈 밸류',
        features: ['지문인식', '비밀번호', '림형'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WK-40',
        name: 'WK-40',
        category: 'wide',
        type: 'rim',
        series: 'W Series',
        price: '240,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-wk-23.png',
        description: 'W 시리즈 카드형',
        features: ['비밀번호', '카드', '림형'],
        specs: {
            auth: '비밀번호, 카드, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WE-10',
        name: 'WE-10',
        category: 'wide',
        type: 'rim',
        series: 'W Series',
        price: '220,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-plato.png',
        description: 'W 시리즈 이지',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WG-5',
        name: 'WG-5',
        category: 'wide',
        type: 'rim',
        series: 'W Series',
        price: '200,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-viena.png',
        description: 'W 시리즈 기본형',
        features: ['비밀번호', '림형'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },

    // Glass Door
    {
        id: 'SHINE',
        name: 'SHINE',
        category: 'glass',
        type: 'glass',
        series: 'Glass Door',
        price: '680,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-shine.png',
        description: '유리문 전용 도어락',
        features: ['지문인식', '비밀번호', '카드', '유리문용', '자동잠금'],
        specs: {
            auth: '지문, 비밀번호, 카드, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'CURVY100-FH',
        name: 'CURVY100-FH',
        category: 'glass',
        type: 'glass',
        series: 'Glass Door',
        price: '580,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-curvy100-fh.png',
        description: '유리문 커비 모델',
        features: ['지문인식', '비밀번호', '유리문용'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'E100',
        name: 'E100',
        category: 'glass',
        type: 'glass',
        series: 'Glass Door',
        price: '480,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-e100.png',
        description: '유리문 이지 모델',
        features: ['비밀번호', '유리문용'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'GNP-YG120',
        name: 'GNP-YG120',
        category: 'glass',
        type: 'glass',
        series: 'Glass Door',
        price: '520,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gatemanwide/prod-thumb-gnp-yg120-.png',
        description: '유리문 프리미엄',
        features: ['지문인식', '비밀번호', '유리문용'],
        specs: {
            auth: '지문, 비밀번호, 기계식열쇠',
            color: '블랙, 실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    },
    {
        id: 'WB-200',
        name: 'WB-200',
        category: 'glass',
        type: 'glass',
        series: 'Glass Door',
        price: '380,000원',
        image: 'https://gateman.kr/common/img/smartdoorlock/gateman/prod-thumb-e100.png',
        description: '유리문 실용형',
        features: ['비밀번호', '유리문용'],
        specs: {
            auth: '비밀번호, 기계식열쇠',
            color: '실버',
            battery: 'AA 8개 (약 1년)',
            iot: '미지원'
        },
        popular: false
    }
];

// Total: 70+ products
console.log(`Total products loaded: ${productsData.length}`);
