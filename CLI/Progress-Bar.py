import os, sys, shutil, argparse, requests, time, inspect, zipfile 
from PIL import Image

def progress_bar(iteration, total, prefix='', suffix='', length=30, fill='-'):
    """Create a progress bar with ANSI escape codes for colored text.

    Args:
        iteration (int): Current iteration.
        total (int): Total iterations.
        prefix (str): Text to display before the progress bar.
        suffix (str): Text to display after the progress bar. Defaults to a newline character.
        length (int): Length of the progress bar.
        fill (str): Character to use to fill the progress bar.

    Returns:
        None: Displays the progress bar in the terminal.
    """
    percent = "{:.1f}".format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar_color = '\033[32m'  # ANSI escape code for green text
    # Check if progress bar is fully filled and adjust bar_fill accordingly
    if filled_length == length:
        bar_fill = bar_color + fill * filled_length + '\033[0m'
    else:
        bar_fill = bar_color + fill * (filled_length - 1) + ':' + '\033[0m' if filled_length > 0 else ''
    # ANSI escape codes for red text and reset to default color
    bar_remaining = '\033[31m' + '-' * (length - filled_length) + '\033[0m'
    print(f'\r{prefix} [{bar_fill}{bar_remaining}] {percent}% {suffix}', end='', flush=True)

def convert_items(zip_file_name):
    """A sample function to link to the progress bar."""
    # create tmp folder if it doesn't exist
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
        
    # unzip the zip file into the tmp folder
    with zipfile.ZipFile(zip_file_name, 'r') as zip:
        zip.extractall('tmp')

    # create output folder if it doesn't exist
    if not os.path.exists('output'):
        os.mkdir('output')

    # create a new transparent image with size 256x272
    items = Image.new('RGBA', (256, 272), (0, 0, 0, 0))

    # list of image filenames to paste onto the new image
    items_filenames = ["leather_helmet","chainmail_helmet","iron_helmet","diamond_helmet","gold_helmet","flint_and_steel","flint","coal","string","seeds_wheat","apple","apple_golden","egg","sugar","snowball","elytra","leather_chestplate","chainmail_chestplate","iron_chestplate","diamond_chestplate","gold_chestplate","bow_standby","brick","iron_ingot","feather","wheat","painting","sugarcane","bone","cake","slimeball","broken_elytra","leather_leggings","chainmail_leggings","iron_leggings","diamond_leggings","gold_leggings","arrow","end_crystal","gold_ingot","gunpowder","bread","sign","door_wood","door_iron","blank","fireball","chorus_fruit","leather_boots","chainmail_boots","iron_boots","diamond_boots","gold_boots","stick","compass_00","diamond","redstone_dust","clay_ball","paper","book_normal","map_empty","seeds_pumpkin","seeds_melon","popped_chorus_fruit","wood_sword","stone_sword","iron_sword","diamond_sword","gold_sword","fishing_rod_uncast","clock_00","bowl","mushroom_stew","glowstone_dust","bucket_empty","bucket_water","bucket_lava","bucket_milk","dye_powder_black","dye_powder_gray","wood_shovel","stone_shovel","iron_shovel","diamond_shovel","gold_shovel","fishing_rod_cast","repeater","porkchop_raw","porkchop_cooked","fish_cod_raw","fish_cod_cooked","rotten_flesh","cookie","shears","dye_powder_red","dye_powder_pink","wood_pickaxe","stone_pickaxe","iron_pickaxe","diamond_pickaxe","gold_pickaxe","bow_pulling_0","carrot_on_a_stick","leather","saddle","beef_raw","beef_cooked","ender_pearl","blaze_rod","melon","dye_powder_green","dye_powder_lime","wood_axe","stone_axe","iron_axe","diamond_axe","gold_axe","bow_pulling_1","potato_baked","potato","carrot","chicken_raw","chicken_cooked","ghast_tear","gold_nugget","nether_wart","dye_powder_brown","dye_powder_yellow","wood_hoe","stone_hoe","iron_hoe","diamond_hoe","gold_hoe","bow_pulling_2","potato_poisonous","minecart_normal","boat","melon_speckled","spider_eye_fermented","spider_eye","potion_bottle_drinkable","potion_overlay","dye_powder_blue","dye_powder_light_blue","leather_helmet_overlay","spectral_arrow","iron_horse_armor","diamond_horse_armor","gold_horse_armor","comparator","carrot_golden","minecart_chest","pumpkin_pie","spawn_egg","potion_bottle_splash","ender_eye","cauldron","blaze_powder","dye_powder_purple","dye_powder_magenta","blank","tipped_arrow_base","dragon_breath","name_tag","lead","netherbrick","fish_clownfish_raw","minecart_furnace","charcoal","spawn_egg_overlay","blank","experience_bottle","brewing_stand","magma_cream","dye_powder_cyan","dye_powder_orange","leather_leggings_overlay","tipped_arrow_head","lingering_potion","barrier","mutton_raw","rabbit_raw","fish_pufferfish_raw","minecart_hopper","hopper","nether_star","emerald","book_writable","book_written","flower_pot","dye_powder_silver","dye_powder_white","leather_boots_overlay","beetroot","beetroot_seeds","beetroot_soup","mutton_cooked","rabbit_cooked","fish_salmon_raw","minecart_tnt","armor_stand","fireworks","fireworks_charge","fireworks_charge_overlay","quartz","map","item_frame","book_enchanted","door_acacia","door_birch","door_dark_oak","door_jungle","door_spruce","rabbit_stew","fish_salmon_cooked","minecart_command_block","acacia_boat","birch_boat","dark_oak_boat","jungle_boat","spruce_boat","prismarine_shard","prismarine_crystals","leather_horse_armor","structure_void","blank","totem_of_undying","shulker_shell","iron_nugget","rabbit_foot","rabbit_hide","blank","blank","blank","blank","blank","blank","blank","blank","dragon_charge","13","cat","blocks","chirp","far","mall","mellohi","stal","strad","ward","11","wait","cod_bucket","salmon_bucket","pufferfish_bucket","tropical_fish_bucket","leather_horse_overlay","blank","blank","blank","blank","blank","blank","kelp","dried_kelp","sea_pickle","nautilus_shell","heart_of_the_sea","turtle_helmet","scute","trident","phantom_membrane"]

    # iterate through the list of image filenames and paste them onto the new image
    for i, filename in enumerate(items_filenames):
        x = (i % 16) * 16
        y = (i // 16) * 16
        try:
            img = Image.open(f'tmp/assets/minecraft/textures/items/{filename}.png')
            items.paste(img, (x, y))
        except FileNotFoundError:
            try:
                img = Image.open(f'fallback/items/{filename}.png')
                items.paste(img, (x, y))
                continue
            except FileNotFoundError:
                continue
        
        time.sleep(0.01)
        progress_bar(i + 1, len(items_filenames), prefix='Progress:', suffix='Completed')
    
    # save the new image to the output folder
    items.save('output/items.png')
    print("\nProcess Completed!")
    shutil.rmtree('tmp')

if __name__ == '__main__':
    convert_items("your_zip_file.zip")
