import React from "react"

class WordBox extends React.Component{
	constructor(props){
		super(props)
		this.state = {
			letters: "",
			words : []
		}
	}
	componentWillReceiveProps(nextProps) {//Sets a hook that updates the words state when Forms.js updates its own words state
		this.setState({ words: nextProps.wordList,
			letters : nextProps.prevLetters
		});  
	}

	//Render all words that have been passed by parent class
	render(){
		return(
			<div class = "WordBox">
				<h3 id = "currentLetters"> {this.state.letters? "Current Letters " + this.state.letters:""} </h3>
				{this.state.words.map((arr) =>
					<div>
					<h5 class = "wordLength" key = {"arr" + arr[0].length.toString(10)}>{arr[0].length} letter words</h5>
					<p key = {arr[0].length}>{arr.join(" ")}</p>
					</div>
					)}
			</div>
		)
	}

}


export default WordBox