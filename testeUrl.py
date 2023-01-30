condominio = [
    "Aldenir Luiz",
    [  # casa_01
        "N-1322",
        [  # carro_01
            "VW Golf GTI 2012",  # Modelo carro_01
            "AMM3F45"
        ],
        [  # carro_02
            "GM Corsa Classic 2010",  # Modelo carro_02
            "HGM6H22"
        ]
    ],
    [  # casa_02
        "N-1344",
        [  # carro_01
            "BMW M3 GT3 2017",  # Modelo carro_01
            "MAB7C32"
        ],
        [  # carro_02
            "FIAT 500 2011",  # Modelo carro_02
            "MAB7C32"
        ]
    ]
]


def imprimir_nome():
    nome: str = input('Digite seu Nome: ')
    sobrenome: str = input('Digite seu Sobrenome: ')
    print(f"{nome} {sobrenome}")


imprimir_nome()


