#### 01219114 & 01219115 Project
# **Last turtle**
A shooting game which you play as the last turtle(green turtle) in the turtleland shooting a zombie turtle(red turtle) to survive as long as you can
by the enemy is come from 4 direction north, east, west and south. The enemy will chase player until they died or player shoot them(count score when enemy died).
When they hit player a player's HP will decrease .When player score reach defined score player will level up.
after level up hp will increase max hp and reset to max hp  

press w,a,s,d for control
press enter for shoot bullet

## require libraries
* turtle 
* random
* python 3.10

## program design

#### 1.class Player 
attribute
* level : int 
* hp : int 
* atk : int

method
* setter
* getter
* cal_stat - calculate player stat when level up
* move_right
* move_left
* move_up
* move_down
* get_coordinate - return x,y coordinate
* enemy_hit - decrease player hp when hit enemy and return if player.hp = 0

#### 2.class Bullet
attribute
* player : player class
* state : boolean
* all_enemy : list of enemy object
* score : Score class
* uidisplay : UIdisplay class 

method
* getter
* setter
* move - move bullet 
* bullet_hit - return if bullet hit enemy

#### 3.class Enemy
attribute
* start_point : list
* atk : int
* hp : int
* player : Player class

method
* getter 
* setter
* move_to_player - move enemy to player

#### 4.class Score
attribute
* score : int
* score_player_cal : int

method 
* getter
* setter

#### 5.class Static_score
attribute
* score : Score class 
* uidisplay : UIdisplay class
* player : Player class 

method
* write - write player's statistic
* read - read data 

#### 6.class UIdisplay
attribute
* player : Player class
* all_enemy : list of Enemy object
* score : score class
* show_score_list : list
* show_hp_list : list
* show_level_list : list
* name : str

method
* getter
* setter
* show_score
* show_hp
* show_level
* name_showing


## Code structure
this game contain 7 file is 
* main.py
* player.py
* bullet.py
* enemy.py
* scores.py
* static_score.py
* data.txt

### git hub url
https://github.com/tnnpp/last-turtle




