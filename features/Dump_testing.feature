@tags @Dump
Feature: Dump data from socket

  Scenario Outline: Connect to socket with valid arguments
    Given Server Address <SERV>
     And Server port <PORT>
     And Output file <OUTPUT>
     When CLI is started with args
     Then Output file is created and should contain some text

     Examples: Several output
     | SERV   | PORT | OUTPUT |
     | localhost | 4444 | 1.txt |
     | localhost | 4444 | 3.txt |


  Scenario Outline: Connect to socket with invalid port
    Given Server Address <SERV>
     And Server port <PORT>
     And Output file 1.txt
     When CLI is started with args
     Then [WinError 10061]

     Examples: Invalid port
     | SERV   | PORT |
     | localhost | 4000444 |
     | localhost | 3306 |

  Scenario Outline: Connect to socket with invalid address
    Given Server Address <SERV>
     And Server port <PORT>
     And Output file 1.txt
     When CLI is started with args
     Then [WinError <ERRCODE>]

     Examples: Invalid Address
     | SERV   | PORT | ERRCODE |
     | ping.host | 4444 | 11001 |
     | 123.456.789 | 4444 | 11001 |
     | 123.123.123.123 | 4444 | 10060 |


  Scenario: Run without arguments
    Given arguments not exist
     When CLI is started without args
     Then Help appears

