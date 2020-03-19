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
    'address' : {
        'title' : 'Address',
        'body' : '''A monero address is where monero is sent to. If you want to send monero to someone, you need their address. This address can be your primary wallet address or a subaddress of a wallet. Every Monero address is 95 characters and begins with a 4. The Monero Core Team donation address, for instance, is 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A. [1] <br><br>Because monero addresses can be so long and difficult to remember, the Core team has introduced OpenAlias to create memorable personalized monero addresses. For example, monero donations can be sent to donate@getmonero.org or donate.getmonero.org. [2]''',
        'related-topics' : [{
            'url' : 'open-alias',
            'title' : 'OpenAlias'
            } , {
            'url' : 'subaddress',
            'title' : 'Subaddress'
            } , {
            'url' : 'stealth-address',
            'title' : 'Stealth address'
            } , {
            'url' : 'wallet',
            'title' : 'Wallet'
        }],
        'references' : [{
            'title': 'Address',
            'author' : 'Monero Core',
            'url' : 'https://web.getmonero.org/resources/moneropedia/address.html',
            'source' : 'getmonero.org',
            'year' : 2020
            } , {
            'title': 'OpenAlias Homepage',
            'author' : 'Monero Core Team',
            'url' : 'https://openalias.org/',
            'source' : 'openalias.org',
            'year' : 2020
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
    'atomic-units' : {
        'title' : 'Atomic Units',
        'body' : '''
ℳ1 = 1 000 000 000 000 atomic units. This is often the unit of measurement used in code to avoid using decimal numbers. This makes computation easier and quicker for computers. For humans, it is difficult to comprehend and discuss such large numbers, thus the unit conversion. [1]
''',
        'related-topics' : [{
            'url' : 'transaction-ouput',
            'title' : 'Transaction output'
            } , {
            'url' : 'supply-auditing',
            'title' : 'Supply auditing'
            } , {
            'url' : 'coinbase-transaction',
            'title' : 'Coinbase transaction'
        }],
        'references' : [{
            'title': 'Why does Monero seem to only use the first six decimal places (and not the full 12)?',
            'author' : 'bigreddmachine',
            'url' : 'https://monero.stackexchange.com/questions/1824/why-does-monero-seem-to-only-use-the-first-six-decimal-places-and-not-the-full',
            'source' : 'StackExchange',
            'year' : 2016
        }]
    } ,
    'balance' : {
        'title' : 'Balance',
        'body' : '''"Balance" refers to the total number of coins owned by a wallet. "Unlocked Balance" refers to the total number of coins that have been owned by the wallet long enough in order for them to be spent. Basically, the monero wallet (like Bitcoin's wallet and others) requires 10 blocks to be mined after your transaction is received and mined into the blockchain so that your monero is deep enough in the chain that it can't be doubled spent as part of a reorganization of the chain. Reorgs get exponentially harder with each subsequent block added on top of the one your transaction is in thanks to proof of work. [1]''',
        'related-topics' : [{
            'url' : 'reorganization-of-the-blockchain',
            'title' : 'Reorganization of the blockchain'
            } , {
            'url' : 'blockchain',
            'title' : 'Blockchain'
            } , {
            'url' : 'transaction-ouput',
            'title' : 'Transaction output'
            } , {
            'url' : 'wallet',
            'title' : 'Wallet'
        }],
        'references' : [{
            'title': '''What's the difference between “balance” and “unlocked balance”?''',
            'author' : 'bigreddmachine',
            'url' : 'https://monero.stackexchange.com/questions/3262/whats-the-difference-between-balance-and-unlocked-balance',
            'source' : 'StackExchange',
            'year' : 2017
        }]
    } ,
    'bisq' : {
        'title' : 'Bisq',
        'body' : '''Cryptocurrency was created to solve the problems of centralized payment systems yet the main method of purchasing cryptocurrency is through trusted centralized excahnges. Bisq is one solution built on pure P2P infrastructure: desktop software, Tor, local wallets, and no central accounts. While the transfer of national currency requires traditional payment channels like banks and payment processors, Bisq is not dependent on any particular one. [1]''',
        'related-topics' : [{
            'url' : 'decentralized-exchange',
            'title' : 'Decentralized exchange'
            } , {
            'url' : 'tor',
            'title' : 'Tor'
        }],
        'references' : [{
            'title': '''Bisq Vision''',
            'author' : 'Bisq Developers',
            'url' : 'https://bisq.network/vision/',
            'source' : 'bisq.network',
            'year' : 2020
        }]
    } ,
    'bitcoin' : {
        'title' : 'Bitcoin',
        'body' : '''Bitcoin is a cryptocurrency. It is a decentralized digital currency without a central bank or single administrator that can be sent from user to user on the peer-to-peer bitcoin network without the need for intermediaries. ''',
        'related-topics' : [{
            'url' : 'satoshi-nakamoto',
            'title' : 'Satoshi Nakamoto'
            } , {
            'url' : 'bitcoin-talk',
            'title' : 'BitcoinTalk'
            } , {
            'url' : 'b-money',
            'title' : 'B-money'
        }],
        'references' : [{
            'title': '''Bitcoin''',
            'author' : 'Bitcoin Core',
            'url' : 'https://bitcoin.org/en/',
            'source' : 'bitcoin.org',
            'year' : 2020
        }]
    } ,
    'bitcoin-talk' : {
        'title' : 'BitcoinTalk',
        'body' : '''
BitcoinTalk is the largest and one of the oldest message boards dedicated to blockchain and cryptocurrencies on the Internet. It was founded by Satoshi Nakamoto on November 22, 2009, and is a direct successor to his first SourceForge forum, which is now lost. 
<br><br>
The site contains a lot of information about the bitcoin sphere, presented in different languages. The digital currency is permanently connected with difficulties, but in this forum it is easy to find the answer strongly to any question. If the user of the forum could not find the necessary information, he can create a topic for discussion on his own and get data from practitioners – experienced members of the crypto-currency community. A team of resource managers are also able to help users to find relevant information and publish it on Bitcointalk. [1]
<br><br>
Much of the discussion that took place amongst the earliest developers of monero can still be found in the BitcoinTalk threads listed below.[2][3][4]''',
        'related-topics' : [{
            'url' : 'history',
            'title' : 'History'
            } , {
            'url' : 'satoshi-nakamoto',
            'title' : 'Satoshi Nakamoto'
            } , {
            'url' : 'bitcoin',
            'title' : 'Bitcoin'
            } , {
            'url' : 'altcoin',
            'title' : 'Altcoin'
        }],
        'references' : [{
            'title': '''BitcoinTalk''',
            'author' : 'Bitcoin Wiki Editors',
            'url' : 'https://en.bitcoinwiki.org/wiki/BitcoinTalk',
            'source' : 'Bitcoin Wiki',
            'year' : 2020
            } , {
            'title': '''Bytecoin. Secure, private, untraceable since 2012''',
            'author' : 'DStrange',
            'url' : 'https://bitcointalk.org/index.php?topic=512747',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': '''Bitmonero - a new coin based on CryptoNote technology - LAUNCHED''',
            'author' : 'thankful_for_today',
            'url' : 'https://bitcointalk.org/index.php?topic=563821.0',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': '''Monero - an anonymous coin based on CryptoNote technology''',
            'author' : 'monero',
            'url' : 'https://bitcointalk.org/index.php?topic=582080.0',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': '''Monero - A secure, private, untraceable cryptocurrency''',
            'author' : 'monero',
            'url' : 'https://bitcointalk.org/index.php?topic=583449.0',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014            
        }]
    } ,
    'block' : {
        'title' : 'Block',
        'body' : '''
<p>A block is a container of transactions, with a new block being added to the blockchain once every 2 minutes (see constant DIFFICULTY_TARGET_V2 defined as 120 seconds), on average. Blocks also contain a special type of transaction, the coinbase transaction, which add newly created Monero to the network. Blocks are created through the process of mining, and the node that successfully mines the block then broadcasts it to each of the nodes connected to it, who subsequently re-broadcast the block until the entire Monero network has received it. Fake or bad blocks generally cannot be created, as nodes that receive blocks always verify the transactions they contain against a set of consensus rules that all nodes adhere to, including validating the cryptographic signatures on each transaction. [1] </p>

<p>As an example, here is a query to the Monero Daemon: <code>monerod print_block 1300000</code> </p>

<pre><code>timestamp: 1493568547
previous hash: 217b2757da92bc6369fc22d79ef16911fc0716bcea106450c94619e905f3c796
nonce: 25166505
is orphan: 0
height: 1300000
depth: 139416
hash: 31b34272343a44a9f4ac7de7a8fcf3b7d8a3124d7d6870affd510d2f37e74cd0
difficulty: 7877790006
reward: 7883911503742
{
  "major_version": 5, 
  "minor_version": 5, 
  "timestamp": 1493568547, 
  "prev_id": "217b2757da92bc6369fc22d79ef16911fc0716bcea106450c94619e905f3c796", 
  "nonce": 25166505, 
  "miner_tx": {
    "version": 2, 
    "unlock_time": 1300060, 
    "vin": [ {
        "gen": {
          "height": 1300000
        }
      }
    ], 
    "vout": [ {
        "amount": 7883911503742, 
        "target": {
          "key": "7c54ec2fad8c41bb40cde9b78c002572ba777b05bb3bc80d0055c0d3489fdb17"
        }
      }
    ], 
    "extra": [ 1, 116, 174, 179, 44, 181, 153, 245, 119, 27, 105, 192, 244, 181, 175,
     62, 47, 244, 15, 129, 8, 223, 115, 234, 203, 131, 15, 62, 152, 103, 136, 144, 134,
      2, 8, 0, 0, 0, 10, 174, 4, 8, 0
    ], 
    "rct_signatures": {
      "type": 0
    }
  }, 
  "tx_hashes": [ "140564273396a16135ba0867ded6b7981fdc28bda45c62f993dc51ff26cfb2e5",
   "a32087d20f25e45097da9c899d8ec17df1d7563abe19047b3d115fe894bbf383",
    "4d2996d78485bd41980c79a7573e91fb06960a96884eda6b47877be8bc0e4eb4"
  ]
}
</code></pre>[2] ''',
        'related-topics' : [{
            'url' : 'blockchain',
            'title' : 'Blockchain'
            } , {
            'url' : 'mining',
            'title' : 'Mining'
            } , {
            'url' : 'coinbase-transaction',
            'title' : 'Coinbase transaction'
            } , {
            'url' : 'node',
            'title' : 'Node'
        }],
        'references' : [{
            'title': '''Block''',
            'author' : 'Monero Core',
            'url' : 'https://web.getmonero.org/resources/moneropedia/block.html',
            'source' : 'getmonero.org',
            'year' : 2020
            } , {
            'title': '''What is the format of a block in the monero blockchain?''',
            'author' : 'Jolly Mort',
            'url' : 'https://monero.stackexchange.com/questions/3958/what-is-the-format-of-a-block-in-the-monero-blockchain',
            'source' : 'StackExchange',
            'year' : 2017
            } , {
            'title': 'CRYPTONOTE STANDARD 003 - CryptoNote Blockchain ',
            'author' : 'Antonio M. Juarez',
            'url' : '../../static/cryptonote_standards/cns003.txt',
            'source' : 'CryptoNote Standards',
            'year' : 2012
        }]
    } ,
    'block-explorer' : {
        'title' : 'Block explorer',
        'body' : '''
A block explorer can be used to query transactions and blocks to analyze what data they may contain. Some block explorers can also provide analysis of the monero network with statistics such as transactions per day or network hashrate. Many block explorers exist for the Monero network. Use your favorite search engine to search 'monero block explorer' to find one.''',
        'related-topics' : [{
            'url' : 'blockchain',
            'title' : 'Blockchain'
            } , {
            'url' : 'block',
            'title' : 'Block'
            } , {
            'url' : 'daemon',
            'title' : 'Daemon'
            } , {
            'url' : 'node',
            'title' : 'Node'
        }],
        'references' : [{
        }]
    } ,
    'block-height' : {
        'title' : 'Block height',
        'body' : '''The number of blocks in the longest blockchain.''',
        'related-topics' : [{
            'url' : 'blockchain',
            'title' : 'Blockchain'
            } , {
            'url' : 'block',
            'title' : 'Block'
            } , {
            'url' : 'daemon',
            'title' : 'Daemon'
            } , {
            'url' : 'node',
            'title' : 'Node'
        }],
        'references' : [{
        }]
    } ,
    'block-interval' : {
        'title' : 'Block interval',
        'body' : '''
The average duration of time between confirming blocks in the blockchain. For the Monero blockchain, there was initially a one minute block interval then later changed to two minutes. If there is in increase in the network hashrate, then blocks are produced faster. That is why there is a difficulty adjustment. As the network hashrate increases, the difficulty of confirming blocks also increases to try to maintain a two minute block interval.''',
        'related-topics' : [{
            'url' : 'difficulty',
            'title' : 'Difficulty'
            } , {
            'url' : 'hashrate',
            'title' : 'Hashrate'
            } , {
            'url' : 'dynamic-block-size-limit',
            'title' : 'Dynamic block size limit'
            } , {
            'url' : 'block',
            'title' : 'Block'
        }],
        'references' : [{
        }]
    } ,
    'block-reward' : {
        'title' : 'Block reward',
        'body' : '''
For solving blocks and confirming transactions, miners are rewarded with newly minted monero and all of the fees paid by people sending monero. This is the only way that new monero is created. What follows is the function used to verify that the miner is requesting the correct block reward [1].
<pre><code>
}
//-----------------------------------------------------------------------------------------------
bool get_block_reward(size_t median_weight, size_t current_block_weight, uint64_t already_generated_coins, uint64_t &reward, uint8_t version) {
    static_assert(DIFFICULTY_TARGET_V2%60==0&&DIFFICULTY_TARGET_V1%60==0,"difficulty targets must be a multiple of 60");
    const int target = version < 2 ? DIFFICULTY_TARGET_V1 : DIFFICULTY_TARGET_V2;
    const int target_minutes = target / 60;
    const int emission_speed_factor = EMISSION_SPEED_FACTOR_PER_MINUTE - (target_minutes-1);

    uint64_t base_reward = (MONEY_SUPPLY - already_generated_coins) >> emission_speed_factor;
    if (base_reward < FINAL_SUBSIDY_PER_MINUTE*target_minutes)
    {
      base_reward = FINAL_SUBSIDY_PER_MINUTE*target_minutes;
    }

    uint64_t full_reward_zone = get_min_block_weight(version);

    //make it soft
    if (median_weight < full_reward_zone) {
      median_weight = full_reward_zone;
    }

    if (current_block_weight <= median_weight) {
      reward = base_reward;
      return true;
    }

    if(current_block_weight > 2 * median_weight) {
      MERROR("Block cumulative weight is too big: " << current_block_weight << ", expected less than " << 2 * median_weight);
      return false;
    }

    uint64_t product_hi;
    // BUGFIX: 32-bit saturation bug (e.g. ARM7), the result was being
    // treated as 32-bit by default.
    uint64_t multiplicand = 2 * median_weight - current_block_weight;
    multiplicand *= current_block_weight;
    uint64_t product_lo = mul128(base_reward, multiplicand, &product_hi);

    uint64_t reward_hi;
    uint64_t reward_lo;
    div128_64(product_hi, product_lo, median_weight, &reward_hi, &reward_lo, NULL, NULL);
    div128_64(reward_hi, reward_lo, median_weight, &reward_hi, &reward_lo, NULL, NULL);
    assert(0 == reward_hi);
    assert(reward_lo < base_reward);

    reward = reward_lo;
    return true;
}
</code></pre>''',
        'related-topics' : [{
            'url' : 'proof-of-work',
            'title' : 'Proof-of-work'
            } , {
            'url' : 'emission-curve',
            'title' : 'Emission Curve'
            } , {
            'url' : 'coinbase-transaction',
            'title' : 'Coinbase transaction'
            } , {
            'url' : 'supply-properties',
            'title' : 'Supply properties'
            } , {
            'url' : 'block',
            'title' : 'Block'
        }],
        'references' : [{
            'title': 'cryptonote_basic_impl.cpp',
            'author' : 'Monero Core',
            'url' : 'https://github.com/monero-project/monero/blob/master/src/cryptonote_basic/cryptonote_basic_impl.cpp',
            'source' : 'Monero Source Code',
            'year' : 2020
        }]
    } ,
    'block-height' : {
        'title' : 'Block interval',
        'body' : '''
The average duration of time between confirming blocks in the blockchain. For the Monero blockchain, there was initially a one minute block interval then later changed to two minutes. If there is in increase in the network hashrate, then blocks are produced faster. That is why there is a difficulty adjustment. As the network hashrate increases, the difficulty of confirming blocks also increases to try to maintain a two minute block interval.''',
        'related-topics' : [{
            'url' : 'difficulty',
            'title' : 'Difficulty'
            } , {
            'url' : 'hashrate',
            'title' : 'Hashrate'
            } , {
            'url' : 'dynamic-block-size-limit',
            'title' : 'Dynamic block size limit'
            } , {
            'url' : 'block',
            'title' : 'Block'
        }],
        'references' : [{
        }]
    } ,
    'b-money' : {
        'title' : 'B-money',
        'body' : '''B-money was an early proposal created by Wei Dai for an "anonymous, distributed electronic cash system". Satoshi Nakamoto referenced b-money when creating Bitcoin. In his essay, published on the cypherpunks mailing-list in November 1998, Dai proposed two protocols. The first protocol is impractical as it requires a broadcast channel that is unjammable as well being synchronous.
<br><br>
In the first protocol in the essay, the use of a proof of work function is proposed as a means of creating money. Dai's B-Money was proposed in the context of cypherpunks mailing-list discussions relating to possible applications of Hashcash, the first symmetric proof-of-work function, which was itself also published on the same mailing-list, the previous year - May 1997. (Like the B-money proposal, bitcoin itself also uses the hashcash cost-function as the proof-of-work during coin minting). In B-Money, money is transferred by broadcasting the transaction to all participants, all of whom keep accounts of all others. Contracts can be made with possible reparation in case of default, with a third party agreeing to be the arbitrator. If there is no agreement, each party broadcasts arguments or evidence in its favor and each of the participants determines the reparations/fines in his accounts for himself.
<br><br>
The second protocol has only a subset of the participants (the "servers") keeping accounts, which they have to publish, and the participants who do transactions verifying their balances by asking many of them. The participants also verify that the money supply is not being inflated. An amount of money as bail is required to become a server, which is lost if the server is found to be dishonest.
<br><br>
An alternate method of creating money is proposed, via an auction where participants bid on the solution of computational problems of known complexity. [1]''',
        'related-topics' : [{
            'url' : 'hashcash',
            'title' : 'Hashcash'
            } , {
            'url' : 'proof-of-work',
            'title' : 'Proof-of-work'
            } , {
            'url' : 'satoshi-nakamoto',
            'title' : 'Satoshi Nakamoto'
            } , {
            'url' : 'history',
            'title' : 'History'
        }],
        'references' : [{
            'title': 'B-money',
            'author' : 'Bitcoin Wiki Editors',
            'url' : 'https://en.bitcoin.it/wiki/B-money',
            'source' : 'Bitcoin Wiki',
            'year' : 2020
            } , {
            'title': 'b-money.txt',
            'author' : 'Wei Dai',
            'url' : 'http://www.weidai.com/bmoney.txt',
            'source' : 'weidai.com',
            'year' : 2020
            } , {
            'title': 'B-money',
            'author' : 'Satoshi Nakamoto Institute',
            'url' : 'https://nakamotoinstitute.org/b-money/',
            'source' : 'Satoshi Nakamoto Institute',
            'year' : 2020
        }]
    } ,
    'blockchain' : {
        'title' : 'Blockchain',
        'body' : '''At its core, Monero is built on the same technology that Bitcoin operates on. Unlike Bitcoin, Monero is built on the CryptoNote protocol. This protocol is an entirely new implementation of the blockchain technology with some key differences in database type, block size, privacy features, and fees for transactions. For more information please see the references below.''',
        'related-topics' : [{
            'url' : 'block',
            'title' : 'Block'
            } , {
            'url' : 'cryptonote',
            'title' : 'CryptoNote'
            } , {
            'url' : 'proof-of-work',
            'title' : 'Proof-of-work'
            } , {
            'url' : 'history',
            'title' : 'History'
        }],
        'references' : [{
            'title': 'Block chain',
            'author' : 'Bitcoin Wiki Editors',
            'url' : 'https://en.bitcoin.it/wiki/Block_chain',
            'source' : 'Bitcoin Wiki',
            'year' : 2020
            } , {
            'title': 'CRYPTONOTE STANDARD 003 - CryptoNote Blockchain ',
            'author' : 'Antonio M. Juarez',
            'url' : '../../static/cryptonote_standards/cns003.txt',
            'source' : 'CryptoNote Standards',
            'year' : 2012
            } , {
            'title': 'Why did Monero choose LMDB over alternative database types?',
            'author' : 'hyc',
            'url' : 'https://monero.stackexchange.com/questions/702/why-did-monero-choose-lmdb-over-alternative-database-types',
            'source' : 'StackExchange',
            'year' : 2016
        }]
    } ,
    'block-size-debate' : {
        'title' : 'Block size debate',
        'body' : '''The size of blocks bottleneck the number of transactions that can be included. If there are no blocksize limits, competition amongst miners will force blocks to include transactions at the lowest fee possible. When there is no additional block reward, there is little incentive for miners to compete. This could potentially centralize the mining power to a single miner compromising the security of the network. When blocks have a fixed size, there is a limit to the number of transactions requested to be included into a block. This could potentially cause fees to be unreasonably high for normal users.[1] The monero supply has a constant tail emission which provides a stable anchor to incentivize miners while also allowing block size to adapt to the current network demands.[2]''',
        'related-topics' : [{
            'url' : 'block',
            'title' : 'Block'
            } , {
            'url' : 'dynamic-block-size-limit',
            'title' : 'Dynamic block size limit'
            } , {
            'url' : 'proof-of-work',
            'title' : 'Proof-of-work'
        }],
        'references' : [{
            'title': 'Monero Speculation',
            'author' : 'ArcticMine',
            'url' : 'https://bitcointalk.org/index.php?topic=753252.msg12440450#msg12440450',
            'source' : 'BitcoinTalk',
            'year' : 2015
            } , {
            'title': 'Block reward penalties and dynamic block size',
            'author' : 'user36303',
            'url' : 'https://monero.stackexchange.com/questions/1067/block-reward-penalties-and-dynamic-block-size',
            'source' : 'StackExchange',
            'year' : 2016
        }]
    } ,
    'boolberry' : {
        'title' : 'Boolberry',
        'body' : '''At its core, Monero is built on the CryptoNote protocol. The origin of CryptoNote is largely unknown and disputed. In the original implementation there are many references to Andrey N. Sabelnikov. It is suspected that he played a role in the development of the CryptoNote Protocol. The first cryptocurrency to make use of the CryptoNote protocol was Bytecoin [1]. Many members of the cryptocurrency community were concerned about the lack of transparency from the Bytecoin development team. As a result, numerous copies of the CryptoNote protocol were made and many teams attemped to launch their own version of the CryptoNote protocol. Boolberry was one of these copies which was led by Andrey N. Sabelnikov. Since 2020, the development team has largely disbanded the project to focus work on a project named Zano.''',
        'related-topics' : [{
            'url' : 'cryptonote',
            'title' : 'CryptoNote'
            } , {
            'url' : 'history',
            'title' : 'History'
        }],
        'references' : [{
            'title': 'Bytecoin. Secure, private, untraceable since 2012',
            'author' : 'DStrange',
            'url' : 'https://bitcointalk.org/index.php?topic=512747',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': '[BBR] Boolberry: Privacy and Security - Guaranteed Since 2014',
            'author' : 'crypto_zoidberg',
            'url' : 'https://bitcointalk.org/index.php?topic=577267.0',
            'source' : 'BitcoinTalk Forum',
            'year' : 2014
            } , {
            'title': 'A brief history of Boolberry',
            'author' : 'Boolberry',
            'url' : 'https://medium.com/@BoolberryBBR/a-brief-history-of-boolberry-c4048d692272',
            'source' : 'BitcoinTalk Forum',
            'year' : 2019
            } , {
        }]
    } ,
    'cryptonote-standards' : {
        'title' : 'CryptoNote standards',
        'body' : '''
The Monero network is built on the CryptoNote Protocol. Since 2014, the core team has worked to make improvements and adjustments to the protocol. These are the original standards of the CryptoNote protocol as of 2012.
<div style="line-height:1.5">
<ul>
<li><a href="../../static/cryptonote_standards/cns001.txt">Signatures (outdated) (CNS001)</a>; <a href="../static/cryptonote_standards/cns002.txt">Signatures (revised) (CNS002)</a>: The exact method of zero-knowledge proof.</li>
<li><a href="../../static/cryptonote_standards/cns003.txt">Blockchain (CNS003)</a>: Describes how data is stored
   within blocks and the blockhain.</li>
<li><a href="../../static/cryptonote_standards/cns004.txt">Transactions (CNS004)</a>: The transfer of assets between users through transactions.</li>
<li><a href="../../static/cryptonote_standards/cns005.txt">Transaction Field Extra (CNS005)</a>:  This document defines the way extra data can be added to a CryptoNote transaction.</li>
<li><a href="../../static/cryptonote_standards/cns006.txt">One-Time Keys (CNS006)</a>: Describes how unlinkability of transactions is achieved.</li>
<li><a href="../../static/cryptonote_standards/cns007.txt">Keys and Addresses (CNS007)</a>: Various types of user keys used in CryptoNote and the way the addresses are encoded.
</li>
<li><a href="../../static/cryptonote_standards/cns008.txt">Hash Function (CNS008)</a>: The CryptoNote's default proof-of-work hash function, CryptoNight. </li>
<li><a href="../../static/cryptonote_standards/cns009.txt">Technology (CNS009)</a>: The core concepts of the
   CryptoNote technology and surveys the whole system's workflow.</li>
<li><a href="../../static/cryptonote_standards/cns010.txt">Difficulty Adjustment (CNS010)</a>: The method for
   maintaining the rate at which blocks are generated.</li>
</ul>''',
        'related-topics' : [{
            'url' : 'cryptonote',
            'title' : 'CryptoNote'
            } , {
            'url' : 'history',
            'title' : 'History'
        }],
        'references' : [{
            'title': 'CryptoNote Standards',
            'author' : 'CryptoNote',
            'url' : '',
            'source' : '',
            'year' : 2012
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
