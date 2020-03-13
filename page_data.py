learn_pages = {
    'account' : {
        'title' : 'Account',
        'body' : '''An account is a group of subaddresses of a wallet.<br><br>

A wallet has a seed. From this seed, the primary address private spend and view keys are derived. From these private keys, subaddresses are derived. Subaddresses are grouped into accounts. This primary address is the first address in the first account in the wallet. Each account has its own balance, and can have multiple subaddresses associated with it. Since accounts are only groupings of subaddresses, there is no such thing as an account address (unless you count the first subaddress in the account as the 'account address'). So a wallet can have multiple accounts, and each account can have multiple subaddresses. Since accounts and subaddresses are deterministically derived from the seed, you only need to know the seed in order to restore the account/subaddress structure when restoring a wallet (although any labels you assign to the accounts/subaddresses will need to be noted separately).[1]''',
        'related-topics' : [{
            'url' : 'address',
            'title' : 'Address'
            } , {
            'url' : 'subaddress',
            'title' : 'Subaddress'
            } , {
            'url' : 'wallet',
            'title' : 'Wallet'
            } , {
            'url' : 'seed',
            'title' : 'Seed'
        }],
        'references' : [{
            'title': 'Difference between “Wallet” and “Account”',
            'author' : 'knacc',
            'url' : 'https://monero.stackexchange.com/questions/10111/difference-between-wallet-and-account',
            'source' : 'StackExchange',
            'year' : 2018
            } , {
            'title': 'Account',
            'author' : 'Monero Core Team',
            'url' : 'https://web.getmonero.org/resources/moneropedia/account.html',
            'source' : 'getmonero.org',
            'year' : 2020
            } , {
            'title': 'How Monero’s accounts and subaddresses work in Monerujo',
            'author' : 'Andres',
            'url' : 'https://medium.com/@anhdres/how-moneros-accounts-and-subaddresses-work-in-monerujo-4fa7df0a58e4',
            'source' : 'Medium',
            'year' : 2018
        }]
    } ,
    'airdrop' : {
        'title' : 'Airdrop',
        'body' : 'Distributing a cryptocurrency token or coin, usually for free, to numerous wallet addresses. [1] In a typical ICO, participants contribute capital to buy tokens whereas, in an airdrop (or hard fork), tokens are allocated to existing holders of a particular chain—typically Bitcoin or Ethereum. Instead of buying tokens, they’re simply given away to the holders of another coin. [2]',
        'related-topics' : [{
            'url' : 'fair-distribution',
            'title' : 'Fair Distribution'
            } , {
            'url' : 'ico',
            'title' : 'ICO'
        }],
        'references' : [{
            'title': 'Airdrop (cryptocurrency)',
            'author' : 'Wikipedia Editors',
            'url' : 'https://en.wikipedia.org/wiki/Airdrop_(cryptocurrency)',
            'source' : 'Wikipedia',
            'year' : 2020
            } , {
            'title': 'The Trend That Is Increasing The Urgency Of Owning Bitcoin And Ethereum',
            'author' : 'Spencer Bogart',
            'url' : 'https://www.forbes.com/sites/spencerbogart/2017/10/08/the-trend-that-is-increasing-the-urgency-of-owning-bitcoin-and-ethereum/#27ec56df116b',
            'source' : 'Forbes',
            'year' : 2017
        }]
    } ,
    'altcoin' : {
        'title' : 'Altcoin',
        'body' : '''Aside from bitcoin, there are hundreds of other digital currencies out there. These are known as “altcoins,” or alternatives to bitcoin; for example, ether, ripple, zcash, monero and dash, to name just a few. <br><br>

Altcoins can differ from Bitcoin in a range of ways. Some have a different economic model or a different coin-distribution method, like altcoins that were given away to all citizens of a country. Others employ different proof-of-work mining algorithms, perhaps to resist specialized mining hardware — or maybe they don’t even rely on proof of work at all. Several altcoins offer a more versatile programming language to build applications on top of, while yet others offer more privacy compared to Bitcoin. And there are also altcoins that serve very specific, non-monetary use cases, like domain name registry or data storage pointers. [1]''',
        'related-topics' : [{
            'url' : 'hard-fork',
            'title' : 'Hard fork'
            } , {
            'url' : 'ico',
            'title' : 'ICO'
        }],
        'references' : [{
            'title': 'What is an Altcoin?',
            'author' : 'Bitcoin Magazine',
            'url' : 'https://bitcoinmagazine.com/guides/what-altcoin',
            'source' : 'CRYPTO',
            'year' : 2017
        }]
    } ,
    'anti-money-laundering' : {
        'title' : 'Anti-money laundering',
        'body' : '''Money laundering is the illegal process of concealing the origins of money obtained illegally by passing it through a complex sequence of banking transfers or commercial transactions. The overall scheme of this process returns the money to the launderer in an obscure and indirect way.[1]
<br><br>
In late June 2019, one of the most authoritative regulatory organizations worldwide, the Financial Action Task Force (FATF), issued new guidelines on how digital assets should be regulated. While FATF recommendations are not legally binding, the G-20 stated that it uses them to regulate cryptocurrencies for Anti-Money Laundering (AML). For businesses that fail to make the grade, this could mean being shut out of lucrative international markets. No punitive measures have yet been imposed, but companies and crypto exchanges alike are acting fast.  [2]''',
        'related-topics' : [{
            'url' : 'fatf',
            'title' : 'FATF'
            } , {
            'url' : 'travel-rule',
            'title' : 'Travel rule'
        }],
        'references' : [{
            'title': 'Money Laundering',
            'author' : 'Wikipedia Editors',
            'url' : 'https://en.wikipedia.org/wiki/Money_laundering',
            'source' : 'Wikipedia',
            'year' : 2020
        }, {
            'title': 'FATF AML Regulation',
            'author' : 'Joseph Birch',
            'url' : 'https://cointelegraph.com/news/fatf-aml-regulation-can-the-crypto-industry-adapt-to-the-travel-rule',
            'source' : 'CoinTelegraph',
            'year' : 2017
        }]
    } ,
    'asic' : {
        'title' : 'ASIC',
        'body' : '''An application-specific integrated circuit (abbreviated as ASIC) is an integrated circuit (IC) customized for a particular use, rather than intended for general-purpose use. In mining hardware, ASICs were the next step of development after CPUs, GPUs and FPGAs. [1] <br><br>
The Monero team believes that ASIC machines have a centralizing effect as there are only a few companies in the world that are able to manufacture them. [2]
The Monero network successfully conducted a scheduled upgrade on Nov. 30. Among other features, the RandomX mining algorithm was introduced to cripple ASIC machines and improve the efficiency of CPUs. The Proof-of-Work algorithm uses random code execution and memory-intensive techniques to discourage the development of ASICs. Its introduction renders all existing CryptoNight ASICs obsolete, while the added complexity aims to make the development of new machines both expensive and ineffective.  [3]''',
        'related-topics' : [{
            'url' : 'randomx',
            'title' : 'RandomX'
            } , {
            'url' : 'proof-of-work',
            'title' : 'Proof-of-work'
        }],
        'references' : [{
            'title': 'ASIC',
            'author' : 'Bitcoin Wiki Editors',
            'url' : 'https://en.bitcoin.it/wiki/ASIC',
            'source' : 'Bitcoin Wiki',
            'year' : 2020
        } , {
            'title': 'Monero Implements Hard Fork Including New ASIC-Resistant Mining Algorithm',
            'author' : 'Joeri Cant',
            'url' : 'https://cointelegraph.com/news/monero-implements-hard-fork-including-new-asic-resistant-mining-algorithm',
            'source' : 'CoinTelegraph',
            'year' : 2019
        } , {
            'title': 'Monero Penalizes GPU and ASIC Mining with RandomX Upgrade',
            'author' : 'Andrey Schevchenko',
            'url' : 'https://cryptobriefing.com/monero-penalizes-gpu-mining-randomx/',
            'source' : 'Crypto Briefing',
            'year' : 2019
        }]
    } ,
    'atomic-swap' : {
        'title' : 'Atomic Swap',
        'body' : '''
An atomic swap allows the exchange across two different blockchains. This allows two people to exchange different currencies without a third party. While there are currently no possible atomic swaps available for monero, there do exist cross-chain transactions for litecoin, bitcoin, and ethereum.''',
        'related-topics' : [{
            'url' : 'fatf',
            'title' : 'FATF'
            } , {
            'url' : 'travel-rule',
            'title' : 'Travel rule'
        }],
        'references' : [{
            'title': 'Alt chains and atomic transfers',
            'author' : 'TierNolan',
            'url' : 'https://bitcointalk.org/index.php?topic=193281.msg2003765#msg2003765',
            'source' : 'BitcoinTalk Forum',
            'year' : 2013
        }]
    } ,
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
    } ,
    'sound-money' : {
        'title' : 'Sound Money',
        'body' : """There have been many forms of money in history, but some forms have worked better than others because they have characteristics that make them more useful. The characteristics of money are durability, portability, divisibility, uniformity, limited supply, and acceptability [1]. Let's compare two examples of possible forms of money:
<ul>
    <li>A cow. Cattle have been used as money at different points in history.</li>
    <li>ℳonero equal to the value of one cow.</li>
</ul>
Let's run down our list of characteristics to see how they stack up.
<ol>
    <li><b>Durability</b> A cow is fairly durable, but a long trip to market runs the risk of sickness or death for the cow and can severely reduce its value. Units of ℳonero cannot deteroriate or become broken in any way. It exists digitally within the decentralized peer-to-peer network which has no central point of failure.</li>
    <li><b>Portability.</b> While the cow is difficult to transport to the store, the currency can be easily be transferred wherever an internet connection is available.</li>
    <li><b>Divisibility.</b> A unit of ℳonero is practically infinitely divisble, up to 12 decimal places. A cow, on the other hand, is not very divisible.</li>
    <li><b>Uniformity.</b> Cows come in many sizes and shapes and each has a different value; cows are not a very uniform form of money. Every unit of ℳonero is indistinguishable. Because accounts and transactions are encrypted, every unit of ℳonero is essentially freshly minted currency. That is why every ℳonero is treated equally</li>
    <li><b>Limited supply.</b> In order to maintain its value, money must have a limited supply. While the supply of cows is fairly limited, if they were used as money, you can bet ranchers would do their best to increase the supply of cows, which would decrease their value. The supply, and therefore the value, of ℳonero is established by code agreed upon by the network participants so that the amount of money created is known and controlled.</li>
    <li><b>Acceptability.</b> Even though cows have intrinsic value, some people may not accept cattle as money. In contrast, as ℳonero adoption grows, people will be more than willing to accept your ℳonero. ℳonero can also be exchanged on numerous currency exchanges for any major currency in the world.</li>
</ol>
Well, it seems "udderly" clear at this point that ℳonero is a much better form of money than cattle. Apply these same proporties to other currencies like gold, USD, or Bitcoin and see how they stand up against ℳonero. Is gold portable? Is there a limited supply of US Dollars? Is every Bitcoin uniform? You will come to realize why ℳonero is sound money.""",
        'related-topics' : [{
            'url' : 'supply-properties',
            'title' : 'Supply properties'
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
            'title': 'Functions of Money',
            'author' : 'The Federal Reserve Bank',
            'url' : 'https://www.stlouisfed.org/education/economic-lowdown-podcast-series/episode-9-functions-of-money',
            'source' : 'The Economic Lowdon Podcast',
            'year' : 2020
        }]
    }
}
