module Main exposing (..)

import Html exposing (Html)


type alias Model =
    { nothing : String
    }


type Msg
    = NoOp



-- init


init : ( Model, Cmd Msg )
init =
    ( Model "", Cmd.none )



-- update


noCmd model =
    ( model, Cmd.none )


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        NoOp ->
            noCmd model



-- view


view : Model -> Html Msg
view model =
    Html.text "meh"



-- subs


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none



-- program


main =
    Html.program
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }
