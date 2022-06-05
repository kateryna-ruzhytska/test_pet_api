from PetManager import PetManager

if __name__ == "__main__":

    PetManager().find_pets_by_status("available")
    PetManager().find_pets_by_status("sold")
    PetManager().add_new_pet()
    PetManager().find_pet_by_id(16)
    PetManager().delete_pet(16)
