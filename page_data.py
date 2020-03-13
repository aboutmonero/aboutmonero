learn_pages = {
    'privacy' : {
        'title' : 'Privacy',
        'body' : 'Privacy and anonymity are the most important aspects of electronic cash.  Peer-to-peer payments seek to be concealed from third party’s view, a distinct difference when compared with traditional banking.  In particular, T. Okamoto and K. Ohta described six criteria of ideal electronic cash, which included “privacy:  relationship between the user and his purchases must be untraceable by anyone” [1].  From their description,  the CryptoNote protocol developers derived two properties which a fully anonymous electronic cash model must satisfy in order to comply with the requirements outlined by Okamoto and Ohta: Untraceability: for each incoming transaction all possible senders are equiprobable. Unlinkability: for any two outgoing transactions it is impossible to prove they were sent to the same person. [2] Monero meets these requirements through the utilization of the three encryption technologies: Ring Signatures, Stealth Addresses, and Ring Confidential Transactions. [3]',
        'related-topics' : [{
            'url' : 'ring-signature',
            'title' : 'Ring signature'
            } , {
            'url' : 'ringct',
            'title' : 'RingCT'
            } , {
            'url' : 'stealth-address',
            'title' : 'Stealth Address'
            } , {
            'url' : 'cryptonote',
            'title' : 'Cryptonote'
            }],
        'references' : [{
            'title': 'Universal electronic cash',
            'author' : 'Tatsuaki Okamoto and Kazuo Ohta',
            'url' : 'https://link.springer.com/chapter/10.1007/3-540-46766-1_27',
            'source' : 'CRYPTO',
            'year' : 1991
            } , {
            'title': 'CryptoNote v 2.0',
            'author' : 'Nicolas van Saberhagen',
            'url' : '../static/cryptonote-whitepaper.pdf',
            'source' : 'CryptoNote Whitepaper',
            'year' : 2013
            } , {
            'title': 'What advantages does Monero offer that are not provided by other cryptocurrencies?',
            'author' : 'JollyMort',
            'url' : 'https://monero.stackexchange.com/questions/2254/what-advantages-does-monero-offer-that-are-not-provided-by-other-cryptocurrencie/',
            'source' : 'StackExchange',
            'year' : 2017
            }]
    } ,
    'supply-properties' : {
        'title' : 'Supply Properties',
        'body' : """The economic properties of monero can be discussed in two eras. The first era is the 'fair-distribution' era which will last from the Genesis block in April 2014 until May 2022. During this era, monero is distributed to miners at an exponentially decreasing rate. The first block reward was ℳ17.59218, the millionth block had a reward of ℳ6.796686, and the two-millionth block ℳ2.040028. This block reward will decrease until it reaches ℳ0.6 per block in May 2022. At this point, the circulating supply will be ℳ18.132 million. [1] This is the end of the fair-distribution era.
<br><br>
After this, there is the 'tail-emission' era. Once the miner's block reward reaches ℳ0.6 per block, it will stay constant forever. The implication of this is that the circulating supply of monero will increase by (ℳ0.6 per block)*(365*24*60/2 blocks) = ℳ157,680 each year. [1] As the circulating supply increases and the amount of newly minted monero stays constant, there is a decreasing rate of inflation. In fact, this rate of inflation will forever stay below 1% per year in the tail emission era.""",
        'related-topics' : [{
            'url' : 'sound-money',
            'title' : 'Sound money'
            } , {
            'url' : 'controlled-supply',
            'title' : 'Controlled supply'
            } , {
            'url' : 'controlled-inflation',
            'title' : 'Controlled inflation'
            }, {
            'url' : 'fair-distribution',
            'title' : 'Fair distribution'
            }, {
            'url' : 'block-reward',
            'title' : 'Block reward'
            }, {
            'url' : 'emission-curve',
            'title' : 'Emission curve'
            }],
        'references' : [{
            'title': 'Useful For Learning About Monero: Coin Emission And Block Reward Schedules',
            'author' : 'Amichateur',
            'url' : 'https://www.reddit.com/r/Monero/comments/512kwh/useful_for_learning_about_monero_coin_emission/',
            'source' : 'Reddit',
            'year' : 2017
            }]
    } ,
    'history' : {
        'title' : 'History',
        'body' : """The Monero project begins with the introduction of the CryptoNote protocol in early 2014. A group of people (possibly a single person) created the protocol using a wide variety of pseudonyms. In the source code of the protocol, there are many copyright references to Andrey N. Sabelnikov who is associated with the botnet Kelihos. It is suspected that he played a role in the development of the CryptoNote Protocol. The first cryptocurrency to make use of the CryptoNote protocol was Bytecoin [1]. Many members of the cryptocurrency community were concerned about the lack of transparency from the Bytecoin development team. As a result, numerous copies of the CryptoNote protocol were made and many teams attemped to launch their own version of the CryptoNote protocol. Bitmonero was one of these copies [2]. Within the Bitmonero team, there was still major disagreement about the distribution and branding of the project [3]. A group of community members again copied the source code of Bitmonero and created Monero [4]. This all happened over the course of a month between March and April 2014. Much of the discussion that took place amongst the earliest developers of monero can still be found in the BitcoinTalk threads listed below.""",
        'related-topics' : [{
            'url' : 'cryptonote',
            'title' : 'CryptoNote'
            } , {
            'url' : 'bytecoin',
            'title' : 'Bytecoin'
            } , {
            'url' : 'bitmonero',
            'title' : 'Bitmonero'
            }],
        'references' : [{
            'title': 'Bytecoin. Secure, private, untraceable since 2012',
            'author' : 'DStrange',
            'url' : 'https://bitcointalk.org/index.php?topic=512747',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': 'Bitmonero - a new coin based on CryptoNote technology - LAUNCHED',
            'author' : 'thankful_for_today',
            'url' : 'https://bitcointalk.org/index.php?topic=563821',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': 'Monero - an anonymous coin based on CryptoNote technology',
            'author' : 'monero',
            'url' : 'https://bitcointalk.org/index.php?topic=582080',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': 'Monero - A secure, private, untraceable cryptocurrency',
            'author' : 'monero',
            'url' : 'https://bitcointalk.org/index.php?topic=583449',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            }]
    }
}
