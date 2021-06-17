const express = require("express");
const router = express.Router();
const Post = require('../models/Post');

// gets all posts
router.get("/", async (req, res) => {

    // returns all posts
    try {
        const posts = await Post.find();
        res.json(posts);
    } catch (err) {
        res.json({ message: err });
    }
});

// submits posts
router.post("/", async (req, res) => {
    const post = new Post({
        title: req.body.title,
        description: req.body.description
    });

    // save to db
    try {
        const savedPost = await post.save()
        res.json(savedPost);
    } catch (err) {
        res.json({ message: err })
    }
});

// retrieve specific posts
router.get('/:postID', async (req, res) => {
    try {
        const post = await Post.findById(req.params.postID);
        res.json(post);
    } catch (err) {
        res.json({ message: err });
    }

});

// delete a specific post
router.delete("/:postID", async (req, res) => {
    try {
        const removedPost = await Post.remove({ _id: req.params.postID })
        res.json(removedPost);
    } catch (err) {
        res.json({ message: err });
    }

});

//update a post, patch
router.patch("/:postID", async (req, res) => {
    try {
        const updatedPost = await Post.updateOne(
            { _id: req.params.postID }, 
            { $set: { title: req.body.title } }
        );
        res.json(updatedPost);
    } catch (err) {
        res.json({ message: err });
    }

});

module.exports = router;