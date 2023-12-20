# Universe of cinematography

## Database
- Country
  - Name
- Genres
  - Name
- Movies
  - Movie title original
  - Movie title cz
  - Movie title sk
  - Country of otigin -> list FK(Country)
  - Genre -> list FK(Genre)
  - Directors -> list FK(Persons)
  - Actors -> list FK(Persons)
  - Year of premiere
  - Rating -> FK(Rating)
  - Comment -> FK(Rating)
  - Image -> FK(Images)
  - Trailer -> url trailer
  - Description
- Rating
  - id movie
  - id user
  - Rating (0 - 100%)
- Images
  - id movie
  - image (image)
  - description
- Person
  - First name
  - Last name
  - Birthday
  - Date of death
  - Image
  - Biography

## Finction (views + templates)

- Show recommendation (homepage)
- Show list of all movies
  - Filter movies (list)
    - Genre
    - Rating
    - Actor
    - Director
    - Country
- Show detail of movie
- The logged in user can:
   - rate movies
   - comment on movies
- Admin can:
   - add new movie/actor/director/genre/country/comments
   - Can delete or edit a movie/actor/director